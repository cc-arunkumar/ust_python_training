from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Optional
from database import get_db
from models.models import Task, Employee, TaskStatusEnum, PriorityEnum, User, RoleEnum
from deps import get_current_user

router = APIRouter(tags=["Tasks"])

# Create a new task (only MANAGER/ADMIN)
@router.post("/")
def create_task(
    title: str,
    description: str,
    assigned_to: int,
    priority: PriorityEnum,
    remark: Optional[str] = None,   # ✅ allow remark at creation
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if current_user.role not in [RoleEnum.MANAGER, RoleEnum.ADMIN]:
        raise HTTPException(status_code=403, detail="Only MANAGER or ADMIN can create tasks")

    assignee = db.query(Employee).filter(Employee.emp_id == assigned_to).first()
    creator = db.query(Employee).filter(Employee.emp_id == current_user.emp_id).first()
    if not assignee or not creator:
        raise HTTPException(status_code=404, detail="Employee not found")

    task = Task(
        title=title,
        description=description,
        assigned_to=assigned_to,
        assigned_by=current_user.emp_id,
        priority=priority,
        status=TaskStatusEnum.TO_DO,
        remark=remark,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

# List all tasks (any authenticated user, excluding deleted)
@router.get("/")
def list_tasks(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Task).filter(Task.is_deleted == False).all()

# Update task status (assignee or ADMIN/MANAGER)
@router.put("/{task_id}/status")
def update_task_status(
    task_id: int,
    status: TaskStatusEnum,
    remark: Optional[str] = None,   # ✅ managers can add/update remark
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    task = db.query(Task).filter(Task.id == task_id, Task.is_deleted == False).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if current_user.role == RoleEnum.EMPLOYEE:
        if current_user.emp_id != task.assigned_to:
            raise HTTPException(status_code=403, detail="Not authorized to update this task")

        if task.status == TaskStatusEnum.TO_DO and status == TaskStatusEnum.IN_PROGRESS:
            task.status = status
        elif task.status == TaskStatusEnum.IN_PROGRESS and status == TaskStatusEnum.REVIEW:
            task.status = status
        else:
            raise HTTPException(status_code=403, detail="Employees can only move TO_DO→IN_PROGRESS or IN_PROGRESS→REVIEW")

    elif current_user.role in [RoleEnum.MANAGER, RoleEnum.ADMIN]:
        if task.status == TaskStatusEnum.REVIEW and status in [TaskStatusEnum.IN_PROGRESS, TaskStatusEnum.DONE]:
            task.status = status
            if remark is not None:
                task.remark = remark   # ✅ update remark when moving out of REVIEW
        else:
            raise HTTPException(status_code=403, detail="Managers/Admins can only move REVIEW→IN_PROGRESS or REVIEW→DONE")

    else:
        raise HTTPException(status_code=403, detail="Not authorized to update task status")

    db.commit()
    db.refresh(task)
    return task

# Update task priority (only MANAGER/ADMIN)
@router.put("/{task_id}/priority")
def update_task_priority(
    task_id: int,
    priority: PriorityEnum,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    task = db.query(Task).filter(Task.id == task_id, Task.is_deleted == False).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if current_user.role not in [RoleEnum.MANAGER, RoleEnum.ADMIN]:
        raise HTTPException(status_code=403, detail="Only MANAGER or ADMIN can update priority")

    task.priority = priority
    db.commit()
    db.refresh(task)
    return task

# ✅ Soft delete task (only MANAGER/ADMIN)
@router.put("/{task_id}/delete")
def soft_delete_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    task = db.query(Task).filter(Task.id == task_id, Task.is_deleted == False).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if current_user.role not in [RoleEnum.MANAGER, RoleEnum.ADMIN]:
        raise HTTPException(status_code=403, detail="Only MANAGER or ADMIN can delete tasks")

    task.is_deleted = True
    task.deleted_at = datetime.utcnow()

    db.commit()
    db.refresh(task)
    return {"message": "Task soft deleted", "task_id": task.id}
