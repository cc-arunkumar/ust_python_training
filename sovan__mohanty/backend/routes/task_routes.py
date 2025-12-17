from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.models import Task, Employee, TaskStatusEnum, PriorityEnum, User, RoleEnum
from deps import get_current_user
from mongo import log_activity   # <-- import logger

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
    role = current_user.role if isinstance(current_user.role, RoleEnum) else RoleEnum(current_user.role)

    if role not in [RoleEnum.MANAGER, RoleEnum.ADMIN]:
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
        priority=priority if isinstance(priority, PriorityEnum) else PriorityEnum(priority),
        status=TaskStatusEnum.TO_DO,
    )
    db.add(task)
    db.commit()
    db.refresh(task)

    # Log creation
    log_activity(
        performed_by=current_user.user_id,
        action="task_created",
        details={
            "task_id": task.id,
            "title": task.title,
            "assigned_to": assigned_to,
            "priority": task.priority.name,
            "status": task.status.name,
            "role": role.name,
        },
    )

    return task


# List all tasks (any authenticated user)
@router.get("/")
def list_tasks(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    log_activity(current_user.user_id, "list_tasks", {"count": len(tasks)})
    return tasks


def normalize_status(value) -> TaskStatusEnum:
    if isinstance(value, TaskStatusEnum):
        return value
    if isinstance(value, str):
        try:
            return TaskStatusEnum[value]
        except KeyError:
            try:
                return TaskStatusEnum(value)
            except ValueError:
                pass
    raise HTTPException(status_code=400, detail=f"Invalid status '{value}'")


def normalize_role(value) -> RoleEnum:
    if isinstance(value, RoleEnum):
        return value
    try:
        return RoleEnum[value]
    except (KeyError, TypeError):
        try:
            return RoleEnum(value)
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid role '{value}'")


def is_transition_allowed(role: RoleEnum, current: TaskStatusEnum, target: TaskStatusEnum) -> bool:
    if role == RoleEnum.EMPLOYEE:
        return (current == TaskStatusEnum.TO_DO and target == TaskStatusEnum.IN_PROGRESS) or \
               (current == TaskStatusEnum.IN_PROGRESS and target == TaskStatusEnum.REVIEW)
    if role in [RoleEnum.MANAGER, RoleEnum.ADMIN]:
        return (current == TaskStatusEnum.REVIEW and target in [TaskStatusEnum.IN_PROGRESS, TaskStatusEnum.DONE])
    return False


# Update task status with strict workflow rules
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

    role = normalize_role(current_user.role)
    new_status = normalize_status(status)
    current_status = task.status if isinstance(task.status, TaskStatusEnum) else normalize_status(task.status)

    if role == RoleEnum.EMPLOYEE:
        if current_user.emp_id != task.assigned_to:
            raise HTTPException(status_code=403, detail="Not authorized: only assignee can update their task")

    if not is_transition_allowed(role, current_status, new_status):
        raise HTTPException(
            status_code=403,
            detail=(
                f"Invalid transition for role {role.name}: "
                f"{current_status.name} → {new_status.name}. "
                "Allowed: EMPLOYEE: TO_DO→IN_PROGRESS, IN_PROGRESS→REVIEW; "
                "MANAGER/ADMIN: REVIEW→IN_PROGRESS or REVIEW→DONE"
            ),
        )

    task.status = new_status
    db.commit()
    db.refresh(task)

    # Log status update
    log_activity(
        performed_by=current_user.user_id,
        action="task_status_update",
        details={
            "task_id": task.id,
            "from": current_status.name,
            "to": task.status.name,
            "role": role.name,
            "assignee_emp_id": task.assigned_to,
        },
    )

    return task
