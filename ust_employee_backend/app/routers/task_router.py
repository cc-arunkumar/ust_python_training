from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import asyncio
import json
from fastapi import File, UploadFile, Response
import re
import os
from database.connection import get_db
from database.mongodb import log_activity,get_file_by_id
from utils.auth import role_guard
from models.users import UserDB
from bson import ObjectId
from schemas.task import (
    TaskBase,
    TaskAssign,
    TaskStatusUpdate,
    TaskPriorityUpdate,
    TaskReviewDecision,
    TaskCreate,
    TaskResponse,
)
from services.task_service import (
    create_task,
    get_tasks,
    get_task_by_id,
    update_task,
    patch_status
)
from database.mongodb import save_task_file_bytes, save_remark, get_remarks_for_task
from utils.notifications import notify_task_created

router = APIRouter(prefix="/api/tasks", tags=["Tasks"])

ALLOWED_IMAGE_MIME_TYPES = {
    "image/jpeg",
    "image/png",
    "image/webp",
}

ALLOWED_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}

# ---------- Get ----------
@router.get("/", response_model=list[TaskResponse])
def get_all(
    db: Session = Depends(get_db),
    current=Depends(role_guard(["Admin", "Manager", "Employee"]))
):
    """Return tasks according to role:
    - Admin: all tasks (no limit)
    - Manager: paginated/default tasks
    - Employee: only tasks assigned to the current employee
    """
    roles = current.get("roles", []) or []
    try:
        roles_lower = [str(r).lower() for r in roles]
    except Exception:
        roles_lower = []

    if "admin" in roles_lower:
        return get_tasks(db, skip=0, limit=None)

    # For managers and employees: show all TO_DO tasks (global), plus any tasks
    # that reference the current user's id (assigned_to_id, created_by_id,
    # assigned_by_id, or reviewer). This lets everyone see new TO_DO items but
    # otherwise only see tasks that involve them.
    from models.task import TaskDB

    # current['emp_id'] may be provided directly or under current['user']
    emp_id_raw = current.get("emp_id") or current.get("user", {}).get("emp_id")
    try:
        emp_digits = re.sub(r"\D", "", str(emp_id_raw))
        emp_id = int(emp_digits) if emp_digits else None
    except Exception:
        emp_id = None

    # Base query: all TO_DO tasks
    todo_q = db.query(TaskDB).filter(TaskDB.status == "TO_DO")

    if emp_id is None:
        # If we couldn't determine the user's emp_id, return only TO_DO tasks
        return todo_q.all()

    # Union: TO_DO OR tasks that reference this emp_id
    related_q = db.query(TaskDB).filter(
        (TaskDB.assigned_to_id == emp_id)
        | (TaskDB.created_by_id == emp_id)
        | (TaskDB.assigned_by_id == emp_id)
        | (TaskDB.reviewer == emp_id)
    )

    # Combine results: use SQLAlchemy `union` via `from_self` + filter OR, or simply
    # perform a single query with OR conditions including the TO_DO condition.
    combined = db.query(TaskDB).filter(
        (TaskDB.status == "TO_DO")
        | (TaskDB.assigned_to_id == emp_id)
        | (TaskDB.created_by_id == emp_id)
        | (TaskDB.assigned_by_id == emp_id)
        | (TaskDB.reviewer == emp_id)
    ).all()

    return combined

    # Default fallback: no tasks
    return []


@router.get("/{task_id}", response_model=TaskBase)
def get_by_id(
    task_id: int,
    db: Session = Depends(get_db),
    current=Depends(role_guard(["Admin", "Manager"]))
):
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(404, "Task not found")
    return task

@router.post("/", response_model=TaskBase)
def create(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current=Depends(role_guard(["Admin", "Manager"]))
):
    task_data = TaskBase(
        **task.dict(),
        created_by_id=current["user"].emp_id,
        status="TO_DO"
    )

    created = create_task(db, task_data)
    log_activity(current["user"].emp_id, "create_task", created.id)
    # Fire a websocket notification (non-blocking)
    try:
        payload = {
            "type": "task_created",
            "task": {
                "id": created.id,
                "title": created.title,
                "description": created.description,
                "status": created.status,
                "created_by_id": created.created_by_id,
                "assigned_to_id": created.assigned_to_id,
            }
        }
        notify_task_created(payload)
    except Exception:
        # best-effort, do not fail the request
        pass

    return created
@router.put("/{task_id}/assign", response_model=TaskBase)
def assign_task(
    task_id: int,
    task: TaskAssign,        # only assigned_to_id is required
    db: Session = Depends(get_db),
    current=Depends(role_guard(["Admin", "Manager"]))
):
    db_task = get_task_by_id(db, task_id)
    if not db_task:
        raise HTTPException(404, "Task not found")
    
    # Do not allow assigning a task that is already completed
    if getattr(db_task, "status", None) == "DONE":
        raise HTTPException(400, "Cannot assign a completed task")

    # Allow assignment and reassignment by Admin/Manager.
    # Normalize assigned_to_id and assigned_by_id to integers where possible
    try:
        assigned_to_id = int(task.assigned_to_id)
    except Exception:
        raise HTTPException(400, "Invalid assigned_to_id")

    # optional reviewer field from payload
    reviewer_id = None
    try:
        if getattr(task, "reviewer", None) is not None:
            reviewer_id = int(task.reviewer)
    except Exception:
        reviewer_id = None

    assigned_by_raw = current["user"].emp_id
    try:
        # current user emp_id may be string or numeric; strip non-digits then int
        import re

        assigned_by_str = str(assigned_by_raw)
        assigned_by_digits = re.sub(r"\D", "", assigned_by_str)
        assigned_by_id = int(assigned_by_digits) if assigned_by_digits else None
    except Exception:
        assigned_by_id = None

    # If the assigned employee doesn't have a User account, create one with default creds
    try:
        # UserDB.emp_id is stored as string in DB, so compare as string
        user_record = db.query(UserDB).filter(UserDB.emp_id == str(assigned_to_id)).first()
        if not user_record:
            new_user = UserDB(
                emp_id=str(assigned_to_id),
                password="password",
                roles=["Employee"],
                status="ACTIVE",
            )
            db.add(new_user)
            # commit now so user exists for downstream operations
            db.commit()
    except Exception:
        # best-effort: if user creation fails, continue with assignment but log
        pass

    db_task.assigned_to_id = assigned_to_id
    if reviewer_id is not None:
        db_task.reviewer = reviewer_id
    if assigned_by_id is not None:
        db_task.assigned_by_id = assigned_by_id
    db_task.assigned_at = datetime.now()
    # Keep task in TO_DO when assigned. Only the assigned employee may
    # transition the task to IN_PROGRESS. We still record assigned_at/assigned_by
    # and optional reviewer, but do not change the status here.

    db.commit()
    db.refresh(db_task)

    log_activity(current["user"].emp_id, "assign_task", task_id)

    return db_task





# ---------- Status ----------
@router.patch("/{task_id}")
def update_status(
    task_id: int,
    data: TaskStatusUpdate,
    db: Session = Depends(get_db),
    current=Depends(role_guard(["Manager", "Employee"]))
):
    try:
        # patch_status expects a role string (or None). role_guard returns
        # current with a `roles` list, so pass the primary role if present.
        roles = current.get("roles", []) or []
        role_str = None
        if isinstance(roles, list) and len(roles) > 0:
            role_str = str(roles[0])

        task = patch_status(db, task_id, data.status, role_str)
    except ValueError as e:
        raise HTTPException(400, str(e))

    if not task:
        raise HTTPException(404, "Task not found")

    log_activity(current["user"].emp_id, "update_status", task_id)

    return {
        "task_id": task.id,
        "status": task.status
    }


# ---------- File upload for task (GridFS) ----------
@router.post("/{task_id}/upload")
async def upload_task_file(
    task_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current=Depends(role_guard(["Admin", "Manager", "Employee"]))
):
    # Verify task exists
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # ---- Validate file type ----
    ext = os.path.splitext(file.filename)[1].lower()

    if file.content_type not in ALLOWED_IMAGE_MIME_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only image files (JPG, PNG, WEBP) are allowed"
        )

    if ext not in ALLOWED_IMAGE_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Invalid image file extension"
        )

    try:
        content = await file.read()

        if not content:
            raise HTTPException(400, "Empty file")

        file_id = save_task_file_bytes(
            task_id=task_id,
            filename=file.filename,
            content=content,
            content_type=file.content_type
        )

        if not file_id:
            raise HTTPException(500, "Failed to save image")

        log_activity(current["user"].emp_id, "upload_image", task_id)

        return {
            "file_id": str(file_id),
            "filename": file.filename,
            "content_type": file.content_type
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")
    
# ---------- Get task file (GridFS) ----------
@router.get("/tasks/file/{file_id}")
async def get_task_file(
    file_id: str,
    current=Depends(role_guard(["Admin", "Manager", "Employee"]))
):
    if not ObjectId.is_valid(file_id):
        raise HTTPException(status_code=400, detail="Invalid file id")

    file_data = get_file_by_id(file_id)

    if not file_data:
        raise HTTPException(status_code=404, detail="Image not found")

    grid_out = file_data["stream"]

    return Response(
        content=grid_out.read(),
        media_type=file_data["content_type"] or "image/jpeg",
        headers={
            # inline = show in browser (NOT download)
            "Content-Disposition": f'inline; filename="{file_data["filename"]}"',
            "Content-Length": str(file_data["length"]),
        }
    )


# ---------- Remarks: create / list (stored in MongoDB) ----------
@router.post("/{task_id}/remarks")
async def post_task_remark(
    task_id: int,
    payload: dict,
    current=Depends(role_guard(["Admin", "Manager", "Employee"]))
):
    comment = payload.get("comment") or payload.get("remarks") or ""
    if not comment:
        raise HTTPException(status_code=400, detail="Missing comment")

    # determine creator id where possible
    try:
        created_by_digits = re.sub(r"\D", "", str(current.get("user").emp_id))
        created_by = int(created_by_digits) if created_by_digits else None
    except Exception:
        created_by = None

    try:
        inserted = save_remark(task_id, comment, created_by)
        if not inserted:
            raise Exception("save failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save remark: {e}")

    return {"id": str(inserted), "task_id": task_id, "comment": comment, "created_by": created_by}


@router.get("/{task_id}/remarks")
async def list_task_remarks(
    task_id: int,
    current=Depends(role_guard(["Admin", "Manager", "Employee"]))
):
    try:
        docs = get_remarks_for_task(task_id)
        return docs
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch remarks: {e}")

# ---------- Send to Review ----------
@router.patch("/{task_id}/send-to-review")
def send_to_review(
    task_id: int,
    db: Session = Depends(get_db),
    current=Depends(role_guard(["Admin","Employee"]))
):
    task = get_task_by_id(db, task_id)

    if not task:
        raise HTTPException(404, "Task not found")

    if task.status != "IN_PROGRESS":
        raise HTTPException(400, "Only IN_PROGRESS tasks can be sent for review")

    # Allow sending to REVIEW even if a reviewer is not yet assigned.
    # Admins or Managers can assign a reviewer afterwards using the reviewer endpoint.
    task.status = "REVIEW"
    db.commit()
    db.refresh(task)

    log_activity(current["user"].emp_id, "send_to_review", task_id)

    return {
        "task_id": task.id,
        "status": task.status
    }



@router.put("/{task_id}/reviewer", response_model=TaskBase)
def assign_reviewer(
    task_id: int,
    payload: dict,
    db: Session = Depends(get_db),
    current=Depends(role_guard(["Admin", "Manager"]))
):
    """Assign a reviewer to a task (Admin or Manager).

    Admins may assign any reviewer. Managers may assign a reviewer only for
    tasks they created (i.e., they are the task owner/creator).

    Expects JSON {"reviewer_id": <int>}.

    When a reviewer is assigned we also set the task's assigned_to_id so the
    reviewer will receive the task.
    """
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(404, "Task not found")

    reviewer_id = payload.get("reviewer_id")
    try:
        reviewer_id = int(reviewer_id)
    except Exception:
        raise HTTPException(400, "Invalid reviewer_id")

    if getattr(task, "status", None) == "DONE":
        raise HTTPException(400, "Cannot assign reviewer to a completed task")

    # If caller is a Manager, verify they are the creator of the task
    roles = current.get("roles", []) or []
    try:
        roles_lower = [str(r).lower() for r in roles]
    except Exception:
        roles_lower = []

    if "manager" in roles_lower:
        try:
            emp_raw = current.get("user").emp_id if current.get("user") else current.get("emp_id")
            emp_digits = re.sub(r"\D", "", str(emp_raw))
            emp_id = int(emp_digits) if emp_digits else None
        except Exception:
            emp_id = None

        if emp_id is None or getattr(task, "created_by_id", None) is None or int(task.created_by_id) != int(emp_id):
            raise HTTPException(403, "Managers may only assign reviewer for tasks they created")

    # set reviewer and assign task to reviewer
    task.reviewer = reviewer_id
    task.assigned_to_id = reviewer_id
    # update assigned_at to reflect reassignment to reviewer
    task.assigned_at = datetime.now()
    db.commit()
    db.refresh(task)

    log_activity(current["user"].emp_id, "assign_reviewer", task_id)

    return task



@router.patch("/{task_id}/priority")
def update_priority(
    task_id: int,
    data: TaskPriorityUpdate,
    db: Session = Depends(get_db),
    current=Depends(role_guard(["Admin", "Manager", "Employee"]))
):
    """Allow the creator of the task to update its priority. Admin/Manager/Employee
    may be authenticated, but only the original creator (created_by_id) may change
    the priority value."""
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(404, "Task not found")

    # Normalize current user's emp_id to integer digits for comparison
    import re

    try:
        cur_emp_raw = current.get("user").emp_id if current.get("user") else current.get("emp_id")
        cur_digits = re.sub(r"\D", "", str(cur_emp_raw))
        cur_emp_id = int(cur_digits) if cur_digits else None
    except Exception:
        cur_emp_id = None

    # created_by_id on the task is stored as integer emp_id
    creator_id = getattr(task, "created_by_id", None)

    if creator_id is None or cur_emp_id is None or int(creator_id) != int(cur_emp_id):
        raise HTTPException(403, "Only the task creator may update priority")

    # Basic validation: allow low/medium/high (case-insensitive)
    new_priority = (data.priority or "").strip().lower()
    if new_priority not in ("low", "medium", "high"):
        raise HTTPException(400, "Invalid priority. Allowed: low, medium, high")

    task.priority = new_priority
    db.commit()
    db.refresh(task)

    log_activity(current["user"].emp_id, "update_priority", task_id)

    return {"task_id": task.id, "priority": task.priority}


# ---------- Review Decision ----------
@router.patch("/{task_id}/review-decision")
def review_decision(
    task_id: int,
    data: TaskReviewDecision,
    db: Session = Depends(get_db),
    current=Depends(role_guard(["Admin","Manager"]))
):
    task = get_task_by_id(db, task_id)

    if not task:
        raise HTTPException(404, "Task not found")

    if task.status != "REVIEW":
        raise HTTPException(400, "Only REVIEW tasks can be reviewed")

    task.reviewer = current["user"].emp_id
    task.remarks = data.remarks

    if data.action == "REJECT":
        task.status = "IN_PROGRESS"

    elif data.action == "APPROVE":
        task.status = "DONE"
        task.actual_closure = datetime.now()

    else:
        raise HTTPException(400, "Invalid action")

    db.commit()
    db.refresh(task)

    log_activity(current["user"].emp_id, f"review_{data.action.lower()}", task_id)

    # Save remark to MongoDB (best-effort)
    try:
        if data.remarks:
            # created_by stored as integer emp id where possible
            try:
                created_by_digits = re.sub(r"\D", "", str(current.get("user").emp_id))
                created_by = int(created_by_digits) if created_by_digits else None
            except Exception:
                created_by = None

            try:
                save_remark(task_id, data.remarks, created_by)
            except Exception:
                # best-effort: do not fail the request
                pass
    except Exception:
        pass

    return {
        "task_id": task.id,
        "status": task.status,
        "reviewer": task.reviewer,
        "actual_closure": task.actual_closure
    }
