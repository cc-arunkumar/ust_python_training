from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app import models, schemas
from app.deps import get_db, get_current_user
from app.mongo import log_activity

router = APIRouter(prefix="/api/tasks", tags=["Tasks"])

def is_transition_allowed(role: str, current: str, new: str) -> bool:
    if current == new:
        return True

    if current == "COMPLETED":
        return False

    employee_transitions = {
        ("TO_DO", "IN_PROGRESS"),
        ("IN_PROGRESS", "REVIEW"),
    }

    manager_transitions = employee_transitions.union(
        {
            ("REVIEW", "COMPLETED"),
            ("REVIEW", "IN_PROGRESS"),
        }
    )

    if role == "Employee":
        return (current, new) in employee_transitions

    if role in ["Manager", "Admin"]:
        return (current, new) in manager_transitions

    return False


def build_base_activity(current_user, action: str):
    """
    Common fields for every activity log entry.
    """
    return {
        "timestamp": datetime.utcnow(),
        "user_id": int(current_user["emp_id"]),
        "user_role": current_user["role"],
        "action": action,  # e.g. "CREATE_TASK", "UPDATE_TASK", "DELETE_TASK", "STATUS_CHANGE"
    }


# ---------------- CREATE TASK ----------------
@router.post("/", response_model=schemas.TaskOut)
def create_task(
    task: schemas.TaskCreate,
    current=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    role = current["role"]
    emp_id = int(current["emp_id"])

    if role not in ["Admin", "Manager"]:
        raise HTTPException(status_code=403, detail="Not allowed")

    if not task.status:
        task.status = "TO_DO"

    if role == "Manager":
        employee = (
            db.query(models.Employee)
            .filter(models.Employee.id == task.assigned_to)
            .first()
        )

        if not employee or employee.manager_id != emp_id:
            raise HTTPException(
                status_code=403,
                detail="Employee not under this manager",
            )

        task.assigned_by = emp_id

    new_task = models.Task(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    # ------- LOG ACTIVITY IN MONGODB -------
    activity = build_base_activity(current, "CREATE_TASK")
    activity.update(
        {
            "task_id": new_task.task_id,
            "title": new_task.title,
            "status": new_task.status,
            "assigned_to": new_task.assigned_to,
            "assigned_by": new_task.assigned_by,
            "details": "Task created",
        }
    )
    log_activity(activity)

    return new_task


# ---------------- LIST TASKS ----------------
@router.get("/", response_model=List[schemas.TaskOut])
def list_tasks(
    current=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    role = current["role"]
    emp_id = int(current["emp_id"])

    if role == "Admin":
        return db.query(models.Task).all()

    if role == "Manager":
        return db.query(models.Task).filter(
            models.Task.assigned_by == emp_id
        ).all()

    if role == "Employee":
        return db.query(models.Task).filter(
            models.Task.assigned_to == emp_id
        ).all()

    raise HTTPException(status_code=403, detail="Not allowed")


# ---------------- UPDATE TASK ----------------
@router.put("/{task_id}", response_model=schemas.TaskOut)
def update_task(
    task_id: int,
    data: schemas.TaskUpdate,
    current=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    role = current["role"]
    emp_id = int(current["emp_id"])

    task = db.query(models.Task).filter(models.Task.task_id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Snapshot old values for logging
    old_task_data = {
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "assigned_to": task.assigned_to,
        "assigned_by": task.assigned_by,
        "priority": task.priority,
        "remarks": task.remarks,  # Track the old remark
    }

    # Update remarks if provided
    if data.remarks is not None:
        task.remarks = data.remarks  # Update remarks field in database

    # Update other fields if necessary
    update_data = data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)

    # ------- LOG ACTIVITY -------
    # Log field-level changes: what changed from what to what
    changed_fields = {}
    if task.remarks != old_task_data["remarks"]:
        changed_fields["remarks"] = {
            "from": old_task_data["remarks"],
            "to": task.remarks,
        }

    # Log other field changes (if any)
    activity = build_base_activity(current, "UPDATE_TASK")
    activity.update(
        {
            "task_id": task.task_id,
            "changes": changed_fields,
        }
    )

    # Log activity in MongoDB
    log_activity(activity)

    return task


# ---------------- DELETE TASK ----------------
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    current=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    role = current["role"]
    emp_id = int(current["emp_id"])

    task = db.query(models.Task).filter(models.Task.task_id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if role == "Manager" and task.assigned_by != emp_id:
        raise HTTPException(status_code=403, detail="Not allowed")

    if role == "Employee":
        raise HTTPException(status_code=403, detail="Not allowed")

    db.delete(task)
    db.commit()

    # ------- LOG DELETE -------
    activity = build_base_activity(current, "DELETE_TASK")
    activity.update(
        {
            "task_id": task_id,
            "details": "Task deleted",
        }
    )
    log_activity(activity)

    return
