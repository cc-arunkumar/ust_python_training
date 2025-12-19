"""# app/services/task_service.py

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.task import Task, TaskStatus
from app.models.user import User
from app.models.employee import Employee
from datetime import datetime

STATUS_FLOW = {
    "TO_DO": ["IN_PROGRESS"],
    "IN_PROGRESS": ["REVIEW"],
    "REVIEW": ["COMPLETED"],
    "COMPLETED": []
}

def _ensure_employee(db: Session, emp_id: int):
    if not db.query(Employee).filter(Employee.emp_id == emp_id).first():
        raise HTTPException(400, "Assigned employee not found")

def _ensure_manager_or_admin_user(db: Session, emp_id: int):
    u = db.query(User).filter(
        User.emp_id == emp_id,
        User.role.in_(["admin", "manager"]),
        User.status == "active"
    ).first()
    if not u:
        raise HTTPException(400, "Reviewer must be an active admin/manager")

# ==================== CREATE TASK ====================
def create_task(db: Session, data, current_user: User):
    # Ensuring only admins or managers can create tasks
    if current_user.role.value not in ["admin", "manager"]:
        raise HTTPException(
            status_code=403,
            detail="Only admin or manager can create tasks"
        )

    _ensure_employee(db, data.assigned_to)  # Ensure the assigned employee exists
    _ensure_manager_or_admin_user(db, data.reviewer)  # Ensure the reviewer is an active admin or manager

    task = Task(
        title=data.title,
        remarks=data.remarks,
        priority=data.priority,
        assigned_to=data.assigned_to,
        reviewer=data.reviewer,
        assigned_by=current_user.emp_id,
        created_by=current_user.emp_id,
        expected_closure=data.expected_closure
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

# ==================== GET TASKS ====================
def get_all_tasks(db: Session):
    return db.query(Task).all()

def get_task_by_id(db: Session, task_id: int):
    task = db.query(Task).filter(Task.task_id == task_id).first()
    if not task:
        raise HTTPException(404, "Task not found")
    return task

# ==================== UPDATE TASK ====================
def update_task(db: Session, task_id: int, data, current_user: User):
    task = get_task_by_id(db, task_id)

    if current_user.role.value == "employee" and task.assigned_to != current_user.emp_id:
        raise HTTPException(403, "You can update only your tasks")

    if current_user.role.value == "manager" and task.assigned_by != current_user.emp_id:
        raise HTTPException(403, "Managers can update only tasks they created")

    if data.title is not None:
        task.title = data.title
    if data.remarks is not None:
        task.remarks = data.remarks
    if data.priority is not None:
        task.priority = data.priority
    if data.assigned_to is not None:
        _ensure_employee(db, data.assigned_to)
        task.assigned_to = data.assigned_to
    if data.reviewer is not None:
        _ensure_manager_or_admin_user(db, data.reviewer)
        task.reviewer = data.reviewer
    if data.expected_closure is not None:
        task.expected_closure = data.expected_closure
    if data.actual_closure is not None:
        task.actual_closure = data.actual_closure

    task.updated_by = current_user.emp_id  # Store the person who updated the task

    db.commit()
    db.refresh(task)
    return task

# ==================== UPDATE STATUS ====================
def update_task_status(db: Session, task_id: int, new_status: str, current_user: User):
    task = db.query(Task).filter(Task.task_id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if current_user.role.value == "employee":
        if task.assigned_to != current_user.emp_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Employees can only update their own assigned tasks"
            )

    task.status = new_status
    task.updated_by = current_user.emp_id
    task.updated_at = datetime.utcnow()

    if new_status.lower() == "completed":
        task.actual_closure = datetime.utcnow()

    db.commit()
    db.refresh(task)
    return task

# ==================== DELETE TASK ====================
def delete_task(db: Session, task_id: int, current_user: User):
    task = get_task_by_id(db, task_id)

    if current_user.role.value == "employee":
        raise HTTPException(403, "Employees cannot delete tasks")

    if current_user.role.value == "manager" and task.assigned_by != current_user.emp_id:
        raise HTTPException(403, "Managers can delete only tasks they created")

    db.delete(task)
    db.commit()
    return {"message": "Task deleted"}
"""

from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.models.task import Task, TaskStatus, TaskPriority
from app.models.user import User

def create_task(db: Session, data, current_user: User):
    task = Task(
        title=data.title,
        remarks=data.remarks,
        priority=data.priority,
        status=TaskStatus.TO_DO,
        assigned_to=data.assigned_to,
        reviewer=data.reviewer,
        assigned_by=current_user.emp_id,
        created_by=current_user.emp_id,
        expected_closure=data.expected_closure
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_task_by_id(db: Session, task_id: int):
    task = db.query(Task).filter(Task.task_id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

def update_task(db: Session, task_id: int, data, current_user: User):
    task = get_task_by_id(db, task_id)

    # Permission checks:
    # - Employees may only update their own assigned tasks
    # - Managers may update only tasks they created
    if current_user.role.value == "employee" and task.assigned_to != current_user.emp_id:
        raise HTTPException(status_code=403, detail="You can update only your tasks")

    if current_user.role.value == "manager" and task.assigned_by != current_user.emp_id:
        raise HTTPException(status_code=403, detail="Managers can update only tasks they created")

    if data.title is not None:
        task.title = data.title
    if data.remarks is not None:
        task.remarks = data.remarks
    if data.priority is not None:
        task.priority = data.priority
    if data.assigned_to is not None:
        task.assigned_to = data.assigned_to
    if data.reviewer is not None:
        task.reviewer = data.reviewer
    if data.expected_closure is not None:
        task.expected_closure = data.expected_closure
    if data.actual_closure is not None:
        task.actual_closure = data.actual_closure
    task.updated_by = current_user.emp_id
    task.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(task)
    return task

def update_task_status(db: Session, task_id: int, data, current_user: User):
    task = get_task_by_id(db, task_id)
    task.status = data.status
    task.priority = data.priority
    task.updated_by = current_user.emp_id
    task.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(task)
    return task

def update_task_remarks(db: Session, task_id: int, data, current_user: User):
    task = get_task_by_id(db, task_id)
    task.remarks = data.remarks
    task.updated_by = current_user.emp_id
    task.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int, current_user: User):
    task = get_task_by_id(db, task_id)
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}