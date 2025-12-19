from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import or_
from pydantic import BaseModel
# from src.database.db_connection import get_db
from src.database.db_creation import Tasks, Employee, User
from src.services.auth import get_current_user,get_db
from src.models.models import TaskCreate, TaskUpdate, TaskResponse

router = APIRouter(
    prefix="/api/v1/tasks",
    tags=["Tasks"]
)

# ==================== HELPERS ====================

def is_admin(user: User):
    return user.role.lower() == "admin"

def is_manager(user: User):
    return user.role.lower() == "manager"

def is_developer(user: User):
    return user.role.lower() == "developer"


def get_manager_team_ids(db: Session, manager_id: str):
    """Return list of employee IDs reporting to this manager"""
    return [
        emp.emp_id
        for emp in db.query(Employee).filter(Employee.mgr_id == manager_id).all()
    ]


def get_task_or_404(db: Session, t_id: int):
    task = db.query(Tasks).filter(Tasks.t_id == t_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# ==================== CREATE TASK ====================
# In your tasks router file
from sqlalchemy import exists

@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(
    task: TaskCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if not (is_admin(current_user) or is_manager(current_user)):
        raise HTTPException(status_code=403, detail="Not authorized to create tasks")

    # NEW: Check if reviewer has at least one subordinate (i.e., is a manager)
    is_manager_reviewer = db.query(
        exists().where(Employee.mgr_id == task.reviewer)
    ).scalar()

    reviewer_exists = db.query(Employee).filter(Employee.emp_id == task.reviewer).first() is not None

    if not reviewer_exists:
        raise HTTPException(status_code=400, detail="Reviewer does not exist")
    
    if not is_manager_reviewer:
        raise HTTPException(status_code=400, detail="Reviewer must be a manager (must have subordinates)")

    db_task = Tasks(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
# ==================== GET ALL TASKS ====================
@router.get(
    "",
    response_model=list[TaskResponse],
    status_code=status.HTTP_200_OK
)
async def get_all_tasks(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if is_admin(current_user):
        return db.query(Tasks).all()

    if is_manager(current_user):
        team_ids = get_manager_team_ids(db, current_user.emp_id)
        return db.query(Tasks).filter(
            Tasks.assigned_to.in_(team_ids)
        ).all()

    raise HTTPException(status_code=403, detail="Not authorized to view tasks")


# ==================== GET TASK BY ID ====================
@router.get(
    "/{t_id}",
    response_model=TaskResponse,
    status_code=status.HTTP_200_OK
)
async def get_task_by_id(
    t_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    task = get_task_or_404(db, t_id)

    if is_admin(current_user):
        return task

    if is_manager(current_user):
        team_ids = get_manager_team_ids(db, current_user.emp_id)
        if task.assigned_to not in team_ids:
            raise HTTPException(status_code=403, detail="Access denied")
        return task

    raise HTTPException(status_code=403, detail="Access denied")


# ==================== UPDATE TASK (NON-STATUS) ====================
@router.put(
    "/{t_id}",
    response_model=TaskResponse,
    status_code=status.HTTP_200_OK
)
async def update_task(
    t_id: int,
    task_update: TaskUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    task = get_task_or_404(db, t_id)

    if is_admin(current_user):
        pass

    elif is_manager(current_user):
        team_ids = get_manager_team_ids(db, current_user.emp_id)
        if task.assigned_to not in team_ids:
            raise HTTPException(status_code=403, detail="Not your team task")

    else:
        raise HTTPException(status_code=403, detail="Not authorized")

    update_data = task_update.model_dump(exclude_unset=True)

    # ❌ Status cannot be updated here
    update_data.pop("status", None)

    for field, value in update_data.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)

    return task


# ==================== UPDATE TASK STATUS ====================
@router.patch(
    "/{t_id}/status",
    response_model=TaskResponse,
    status_code=status.HTTP_200_OK
)

class StatusUpdate(BaseModel):
    t_id:int
    status:str
async def update_task_status(
    status_update:StatusUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    task = get_task_or_404(db,status_update.t_id)

    if status_update.status is None:
        raise HTTPException(status_code=400, detail="Status is required")

    # Admin cannot change status
    if is_admin(current_user):
        raise HTTPException(status_code=403, detail="Admin cannot change task status")

    # Reviewer OR Developer (assignee) only
    if not (
        str(current_user.emp_id) == task.reviewer or
        str(current_user.emp_id) == task.assigned_to
    ):
        raise HTTPException(status_code=403, detail="Not authorized to change status")

    task.status = status_update.status
    task.updated_by = current_user.emp_id

    db.commit()
    db.refresh(task)

    return task


# ==================== DELETE TASK ====================
@router.delete(
    "/{t_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_task(
    t_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if not is_admin(current_user):
        raise HTTPException(status_code=403, detail="Admin only")

    task = get_task_or_404(db, t_id)
    db.delete(task)
    db.commit()
    return None

# ==================== UPDATE TASK PRIORITY ====================
@router.patch(
    "/{t_id}/priority",
    response_model=TaskResponse,
    status_code=status.HTTP_200_OK
)
async def update_task_priority(
    t_id: int,
    priority_update: TaskUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    task = get_task_or_404(db, t_id)

    if priority_update.priority is None:
        raise HTTPException(status_code=400, detail="Priority is required")

    # ✅ Admin can update any task
    if is_admin(current_user):
        pass

    # ✅ Manager can update priority of team tasks
    elif is_manager(current_user):
        team_ids = get_manager_team_ids(db, current_user.emp_id)
        if task.assigned_to not in team_ids:
            raise HTTPException(status_code=403, detail="Not your team task")

    # ❌ Developers cannot update priority
    else:
        raise HTTPException(status_code=403, detail="Not authorized to update priority")

    task.priority = priority_update.priority
    task.updated_by = current_user.emp_id

    db.commit()
    db.refresh(task)

    return task
