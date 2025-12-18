from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.core.constants import TASK_STATUSES, TASK_STATUS_FLOW
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.task import Task
from app.models.employee import Employee
from app.schemas.task import (
    TaskCreate,
    TaskUpdate,
    TaskResponse,
    TaskStatusUpdate
)
from app.utils.logger import log_action

router = APIRouter(prefix="/tasks", tags=["Tasks"])


# -------------------------------------------------
# CREATE TASK (ADMIN / MANAGER ONLY)
# -------------------------------------------------
@router.post("/", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    if user["active_role"] not in ["ADMIN", "MANAGER"]:
        raise HTTPException(
            status_code=403,
            detail="Only Admin or Manager can create tasks"
        )

    # Validate assigned employee
    emp = db.query(Employee).filter(Employee.e_id == task.assigned_to).first()
    if not emp:
        raise HTTPException(
            status_code=400,
            detail="Assigned employee does not exist"
        )

    db_task = Task(
        title=task.title,
        description=task.description,
        assigned_to=task.assigned_to,
        created_by=user["emp_id"],
        assigned_by=user["emp_id"],
        priority=task.priority,
        status="TO_DO",
        assigned_at=datetime.utcnow(),
        expected_closure=task.expected_closure
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    log_action(
        user["emp_id"],
        "CREATE_TASK",
        f"Task {db_task.t_id} created"
    )

    return db_task


# -------------------------------------------------
# GET ALL TASKS (ROLE CONTEXT BASED)
# -------------------------------------------------
@router.get("/", response_model=list[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    # ADMIN → all tasks
    if user["active_role"] == "ADMIN":
        return db.query(Task).all()

    # MANAGER → only team tasks (NOT own tasks)
    if user["active_role"] == "MANAGER":
        return (
            db.query(Task)
            .join(Employee, Task.assigned_to == Employee.e_id)
            .filter(Employee.manager_id == user["emp_id"])
            .all()
        )

    # DEVELOPER → only own tasks
    if user["active_role"] == "DEVELOPER":
        return (
            db.query(Task)
            .filter(Task.assigned_to == user["emp_id"])
            .all()
        )

    return []


# -------------------------------------------------
# GET TASK BY ID (ROLE CONTEXT BASED)
# -------------------------------------------------
@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    task = db.query(Task).filter(Task.t_id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    # ADMIN → full access
    if user["active_role"] == "ADMIN":
        return task

    # DEVELOPER → own task only
    if (
        user["active_role"] == "DEVELOPER"
        and task.assigned_to == user["emp_id"]
    ):
        return task

    # MANAGER → team task only
    if user["active_role"] == "MANAGER":
        emp = db.query(Employee).filter(Employee.e_id == task.assigned_to).first()
        if emp and emp.manager_id == user["emp_id"]:
            return task

    raise HTTPException(
        status_code=403,
        detail="Not authorized to view this task"
    )


# -------------------------------------------------
# UPDATE TASK (ADMIN / MANAGER ONLY)
# -------------------------------------------------
@router.put("/{task_id}")
def update_task(
    task_id: int,
    data: TaskUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    if user["active_role"] not in ["ADMIN", "MANAGER"]:
        raise HTTPException(
            status_code=403,
            detail="Only Admin or Manager can update tasks"
        )

    task = db.query(Task).filter(Task.t_id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    for key, value in data.dict(exclude_unset=True).items():
        setattr(task, key, value)

    task.updated_at = datetime.utcnow()
    db.commit()

    log_action(
        user["emp_id"],
        "UPDATE_TASK",
        f"Task {task_id} updated"
    )

    return {"message": "Task updated successfully"}


# -------------------------------------------------
# UPDATE TASK STATUS (MANAGER / DEVELOPER ONLY)
# -------------------------------------------------
@router.patch("/{task_id}/status")
def update_task_status(
    task_id: int,
    payload: TaskStatusUpdate,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    role = user["active_role"]
    emp_id = user["emp_id"]
    new_status = payload.status

    # 🔹 Validate status
    if new_status not in TASK_STATUSES:
        raise HTTPException(400, "Invalid status")

    task = db.query(Task).filter(Task.t_id == task_id).first()
    if not task:
        raise HTTPException(404, "Task not found")

    current_status = task.status

    # ❌ Admin never updates status
    if role == "ADMIN":
        raise HTTPException(403, "Admin cannot update task status")

    # 🔒 Developer restrictions
    if role == "DEVELOPER":
        if task.assigned_to != emp_id:
            raise HTTPException(403, "Not your task")

    # 🔒 Validate workflow transition
    allowed = TASK_STATUS_FLOW.get(role, {}).get(current_status, [])
    if new_status not in allowed:
        raise HTTPException(
            403,
            f"{role} cannot change {current_status} → {new_status}",
        )

    # ✅ Common updates
    task.status = new_status
    task.updated_by = emp_id
    task.updated_at = datetime.utcnow()

    # 🔍 MANAGER REVIEW LOGIC
    if role == "MANAGER" and current_status == "REVIEW":
        task.reviewer = emp_id
        task.remarks = payload.remarks  # may be None

        # ✅ If approved
        if new_status == "DONE":
            task.actual_closure = datetime.utcnow()

    db.commit()

    return {
        "message": "Status updated",
        "from": current_status,
        "to": new_status,
        "reviewer": task.reviewer,
        "actual_closure": task.actual_closure,
    }


# -------------------------------------------------
# DELETE TASK (ADMIN ONLY)
# -------------------------------------------------
@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    if user["active_role"] not in ["ADMIN", "MANAGER"]:
        raise HTTPException(
            status_code=403,
            detail="Only Admin or Manager can delete tasks"
        )

    task = db.query(Task).filter(Task.t_id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(task)
    db.commit()

    log_action(
        user["emp_id"],
        "DELETE_TASK",
        f"Task {task_id} deleted"
    )

    return {"message": "Task deleted successfully"}

# -------------------------------------------------
# UPDATE TASK PRIORITY (MANAGER / DEVELOPER ONLY)
# -------------------------------------------------
@router.patch("/{task_id}/priority")
def update_task_priority(
    task_id: int,
    priority: str,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    if user["active_role"] not in ["ADMIN", "MANAGER"]:
        raise HTTPException(status_code=403, detail="Not allowed")

    task = db.query(Task).filter(Task.t_id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if priority not in ["LOW", "MEDIUM", "HIGH"]:
        raise HTTPException(status_code=400, detail="Invalid priority")

    task.priority = priority
    task.updated_at = datetime.utcnow()
    db.commit()

    log_action(
        user["emp_id"],
        "UPDATE_PRIORITY",
        f"TASK-{task_id} → {priority}"
    )

    return {"message": "Priority updated"}
