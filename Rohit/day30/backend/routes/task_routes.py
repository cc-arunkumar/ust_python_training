from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.models import Task, Employee, TaskStatusEnum, PriorityEnum, User, RoleEnum
from deps import get_current_user

from pydantic import BaseModel
router = APIRouter(tags=["Tasks"])
# Create a new task (only MANAGER/ADMIN)
@router.post("/")
def create_task(
    title: str,
    description: str,
    assigned_to: int,
    priority: PriorityEnum,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # Role check
    if current_user.role not in [RoleEnum.MANAGER, RoleEnum.ADMIN]:
        raise HTTPException(status_code=403, detail="Only MANAGER or ADMIN can create tasks")

    # Validate employees
    assignee = db.query(Employee).filter(Employee.emp_id == assigned_to).first()
    creator = db.query(Employee).filter(Employee.emp_id == current_user.emp_id).first()
    if not assignee or not creator:
        raise HTTPException(status_code=404, detail="Employee not found")

    # Create task
    task = Task(
        title=title,
        description=description,
        assigned_to=assigned_to,
        assigned_by=current_user.emp_id,
        priority=priority,
        status=TaskStatusEnum.TO_DO,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

# List all tasks (any authenticated user)
@router.get("/")
def list_tasks(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Task).all()

# Update task status (assignee or ADMIN/MANAGER)
class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    priority: PriorityEnum | None = None
    status: TaskStatusEnum | None = None
    remark: str | None = None
    assigned_to: int | None = None
@router.put("/{task_id}")
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if current_user.emp_id != task.assigned_to and current_user.role not in [RoleEnum.ADMIN, RoleEnum.MANAGER]:
        raise HTTPException(status_code=403, detail="Not authorized to update this task")

    # Apply updates
    if task_update.title is not None:
        task.title = task_update.title
    if task_update.description is not None:
        task.description = task_update.description
    if task_update.priority is not None:
        task.priority = task_update.priority
    if task_update.status is not None:
        task.status = task_update.status
    if task_update.remark is not None:
        task.remark = task_update.remark
    if task_update.assigned_to is not None:
        task.assigned_to = task_update.assigned_to

    db.commit()
    db.refresh(task)
    return task



# Delete a task (only ADMIN/MANAGER)
@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Only ADMIN or MANAGER can delete tasks
    if current_user.role not in [RoleEnum.ADMIN, RoleEnum.MANAGER]:
        raise HTTPException(status_code=403, detail="Not authorized to delete this task")

    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully", "task_id": task_id}