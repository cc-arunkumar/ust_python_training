from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
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
@router.put("/{task_id}/status")
def update_task_status(
    task_id: int,
    status: TaskStatusEnum,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Only assignee or privileged roles can update
    if current_user.emp_id != task.assigned_to and current_user.role not in [RoleEnum.ADMIN, RoleEnum.MANAGER]:
        raise HTTPException(status_code=403, detail="Not authorized to update this task")

    task.status = status
    db.commit()
    db.refresh(task)
    return task
