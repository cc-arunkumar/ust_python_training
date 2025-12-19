"""from fastapi import APIRouter, Depends, Query,HTTPException
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.task import Task, TaskStatus
from app.database.connection import get_db
from app.schemas.task import (
    TaskCreate, TaskUpdate, TaskStatusUpdate, TaskResponse,
)
from app.services.task_service import (
    create_task, get_all_tasks, get_task_by_id,
    update_task, update_task_status, delete_task
)
from app.utils.auth_dependency import get_current_user, require_role
from app.utils.pagination import paginate
from typing import List  
from app.models.user import User 
from app.models.PaginatedTaskResponse import PaginatedTaskResponse

router = APIRouter(prefix="/api/tasks", tags=["Tasks"])


@router.post(
    "/",
    response_model=TaskResponse,
    dependencies=[Depends(require_role("admin"))]
)
def add_task(
    data: TaskCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return create_task(db, data, current_user)


@router.get("/", response_model=PaginatedTaskResponse)
def get_all_task(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1)
):
    role = current_user.role.value
    emp_id = current_user.emp_id

    query = db.query(Task)

    # Role-based filtering
    if role == "employee":
        # Employees see only tasks assigned to them
        query = query.filter(Task.assigned_to == emp_id)
    elif role == "manager":
        # Managers should see tasks they created, tasks assigned to them,
        # and tasks where they are the reviewer (they may act as employee & reviewer)
        query = query.filter(
            or_(Task.assigned_by == emp_id, Task.assigned_to == emp_id, Task.reviewer == emp_id)
        )
    # admin sees everything - no filter

    # Pagination
    total = query.count()
    tasks = query.offset((page - 1) * limit).limit(limit).all()

    # Convert SQLAlchemy Task objects to Pydantic models
    tasks = [TaskResponse.from_orm(task) for task in tasks]

    return {
        "tasks": tasks,
        "total": total,
        "page": page,
        "limit": limit
    }

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return get_task_by_id(db, task_id)


@router.put("/{task_id}", response_model=TaskResponse)
def update_task_api(
    task_id: int,
    data: TaskUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return update_task(db, task_id, data, current_user)

@router.patch("/{task_id}/status", response_model=TaskResponse)
def change_status(
    task_id: int,
    data: TaskStatusUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    task = db.query(Task).filter(Task.task_id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Prevent changes to a completed task
    # Normalize current and new statuses to string values for comparison
    current_status = getattr(task.status, "value", str(task.status))
    new_status = getattr(data.status, "value", data.status)
    if current_status == TaskStatus.COMPLETED.value and new_status != TaskStatus.COMPLETED.value:
        raise HTTPException(status_code=403, detail="Completed tasks cannot be changed")

    # Update the status and priority
    task.status = data.status
    task.priority = data.priority
    task.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(task)

    return task


@router.delete("/{task_id}")
def remove_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return delete_task(db, task_id, current_user)
"""

from fastapi import APIRouter, Depends, Query, HTTPException
from datetime import datetime
from sqlalchemy.orm import Session
from typing import List
from app.database.connection import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskStatusUpdate, TaskResponse, PaginatedTaskResponse, TaskRemarksUpdate
from app.services.task_service import create_task, get_task_by_id, update_task, update_task_status, delete_task, update_task_remarks
from app.utils.auth import get_current_user, require_roles
from app.utils.pagination import paginate
from app.models.task import Task, TaskStatus
from app.models.user import User

router = APIRouter(prefix="/api/tasks", tags=["Tasks"])


@router.get("/my")
def get_my_tasks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Return tasks grouped for the current user: created, assigned, reviewer"""
    role = current_user.role.value
    emp_id = current_user.emp_id

    query_created = db.query(Task).filter(Task.assigned_by == emp_id)
    query_assigned = db.query(Task).filter(Task.assigned_to == emp_id)
    query_reviewer = db.query(Task).filter(Task.reviewer == emp_id)

    created = [TaskResponse.from_orm(t) for t in query_created.all()]
    assigned = [TaskResponse.from_orm(t) for t in query_assigned.all()]
    reviewer = [TaskResponse.from_orm(t) for t in query_reviewer.all()]

    return {"created": created, "assigned": assigned, "reviewer": reviewer}

@router.post("/", response_model=TaskResponse, dependencies=[Depends(require_roles(["admin", "manager"]))])
def add_task(data: TaskCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return create_task(db, data, current_user)

@router.get("/", response_model=PaginatedTaskResponse)
def get_all_task(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1)
):
    role = current_user.role.value
    emp_id = current_user.emp_id
    query = db.query(Task)
    # Role-based filtering
    if role == "employee":
        query = query.filter(Task.assigned_to == emp_id)
    elif role == "manager":
        query = query.filter(Task.assigned_by == emp_id)
    # admin sees everything - no filter
    paginated = paginate(query, page, limit)
    paginated["tasks"] = paginated.pop("data")  # Rename for response model
    return paginated

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return get_task_by_id(db, task_id)

@router.put("/{task_id}", response_model=TaskResponse)
def update_task_api(task_id: int, data: TaskUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """Allow admin/manager OR an employee updating their own assigned task.
    Permission checks are handled inside the service layer.
    """
    return update_task(db, task_id, data, current_user)

@router.patch("/{task_id}/remarks", response_model=TaskResponse)
def update_task_remarks_api(
    task_id: int,
    data: TaskRemarksUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    task = db.query(Task).filter(Task.task_id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Permission check - same logic
    if current_user.role.value not in ["admin", "manager"]:
        if current_user.role.value != "employee" or task.assigned_to != current_user.emp_id:
            raise HTTPException(status_code=403, detail="Not authorized to update this task")

    task.remarks = data.remarks
    task.updated_by = current_user.emp_id
    task.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(task)
    return task

@router.patch("/{task_id}/status", response_model=TaskResponse)
def change_status(
    task_id: int,
    data: TaskStatusUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    task = db.query(Task).filter(Task.task_id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    # Permission check
    if current_user.role.value not in ["admin", "manager"]:
        if current_user.role.value != "employee" or task.assigned_to != current_user.emp_id:
            raise HTTPException(status_code=403, detail="Not authorized to update this task status")

    # Prevent changes to a completed task
    current_status = getattr(task.status, "value", str(task.status))
    new_status = getattr(data.status, "value", data.status)
    if current_status == TaskStatus.COMPLETED.value and new_status != TaskStatus.COMPLETED.value:
        raise HTTPException(status_code=403, detail="Completed tasks cannot be changed")

    # Enforce adjacent-only status transitions server-side
    STATUS_FLOW = ["TO_DO", "IN_PROGRESS", "REVIEW", "COMPLETED"]
    try:
        from_idx = STATUS_FLOW.index(current_status)
        to_idx = STATUS_FLOW.index(new_status)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid status value")

    if abs(from_idx - to_idx) != 1:
        # Not an adjacent transition
        raise HTTPException(status_code=400, detail="Invalid status transition. Must move one step at a time")

    # Update the status and optional priority
    task.status = data.status
    if data.priority:
        task.priority = data.priority
    task.updated_by = current_user.emp_id
    task.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(task)
    return task

@router.delete("/{task_id}", dependencies=[Depends(require_roles(["admin", "manager"]))])
def remove_task(task_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return delete_task(db, task_id, current_user)