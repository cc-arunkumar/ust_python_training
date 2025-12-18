from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import asyncio
import json
from fastapi import File, UploadFile

from database.connection import get_db
from database.mongodb import log_activity
from utils.auth import role_guard

from schemas.task import (
    TaskBase,
    TaskAssign,
    TaskStatusUpdate,
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
from database.mongodb import save_task_file_bytes
from utils.notifications import notify_task_created

router = APIRouter(prefix="/api/tasks", tags=["Tasks"])


# ---------- Get ----------
@router.get("/", response_model=list[TaskResponse])
def get_all(
    db: Session = Depends(get_db),
    current=Depends(role_guard(["Admin", "Manager"]))
):
    return get_tasks(db)


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


# ---------- Assign ----------
@router.put("/{task_id}", response_model=TaskBase)
def assign(
    task_id: int,
    task: TaskAssign,
    db: Session = Depends(get_db),
    current=Depends(role_guard(["Manager"]))
):
    task.assigned_by_id = current["user"].emp_id
    updated = update_task(db, task_id, task)
    if not updated:
        raise HTTPException(404, "Task not found")

    log_activity(current["user"].emp_id, "assign_task", task_id)
    return updated


# ---------- Status ----------
@router.patch("/{task_id}")
def update_status(
    task_id: int,
    data: TaskStatusUpdate,
    db: Session = Depends(get_db),
    current=Depends(role_guard(["Manager", "Employee"]))
):
    try:
        task = patch_status(db, task_id, data.status, current["role"])
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
    # verify task exists
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(404, "Task not found")

    try:
        content = await file.read()
        file_id = save_task_file_bytes(task_id, file.filename, content, file.content_type)
        if not file_id:
            raise HTTPException(500, "Failed to save file")

        # log and return file id
        log_activity(current["user"].emp_id, "upload_file", task_id)
        return {"file_id": str(file_id), "filename": file.filename}
    except Exception as e:
        raise HTTPException(500, f"Upload failed: {str(e)}")


# ---------- Send to Review ----------
@router.patch("/{task_id}/send-to-review")
def send_to_review(
    task_id: int,
    db: Session = Depends(get_db),
    current=Depends(role_guard(["Employee"]))
):
    task = get_task_by_id(db, task_id)

    if not task:
        raise HTTPException(404, "Task not found")

    if task.status != "IN_PROGRESS":
        raise HTTPException(400, "Only IN_PROGRESS tasks can be sent for review")

    task.status = "REVIEW"
    db.commit()
    db.refresh(task)

    log_activity(current["user"].emp_id, "send_to_review", task_id)

    return {
        "task_id": task.id,
        "status": task.status
    }


# ---------- Review Decision ----------
@router.patch("/{task_id}/review-decision")
def review_decision(
    task_id: int,
    data: TaskReviewDecision,
    db: Session = Depends(get_db),
    current=Depends(role_guard(["Manager"]))
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

    return {
        "task_id": task.id,
        "status": task.status,
        "reviewer": task.reviewer,
        "actual_closure": task.actual_closure
    }
