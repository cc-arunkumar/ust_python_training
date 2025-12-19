from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import or_
from pydantic import BaseModel
# from src.database.db_connection import get_db
from src.database.db_creation import Tasks, Employee, User
from src.services.auth import get_current_user,get_db
from src.models.models import TaskCreate, TaskUpdate, TaskResponse
from datetime import datetime
router = APIRouter(
    prefix="/api/v1/tasks",
    tags=["Tasks"]
)

# ==================== HELPERS ====================

def is_admin(user: User):
    # Support both legacy `role` string and token-provided `roles` list
    roles = []
    if hasattr(user, "roles") and isinstance(user.roles, (list, tuple)):
        roles = [r.lower() for r in user.roles if isinstance(r, str)]
    elif hasattr(user, "role") and isinstance(user.role, str):
        roles = [r.strip().lower() for r in user.role.split(",") if r.strip()]

    return "admin" in roles

def is_manager(user: User):
    roles = []
    if hasattr(user, "roles") and isinstance(user.roles, (list, tuple)):
        roles = [r.lower() for r in user.roles if isinstance(r, str)]
    elif hasattr(user, "role") and isinstance(user.role, str):
        roles = [r.strip().lower() for r in user.role.split(",") if r.strip()]

    return "manager" in roles

def is_developer(user: User):
    roles = []
    if hasattr(user, "roles") and isinstance(user.roles, (list, tuple)):
        roles = [r.lower() for r in user.roles if isinstance(r, str)]
    elif hasattr(user, "role") and isinstance(user.role, str):
        roles = [r.strip().lower() for r in user.role.split(",") if r.strip()]

    return "developer" in roles


def get_manager_team_ids(db: Session, manager_id: str):
    """Return list of employee IDs reporting to this manager"""
    # manager_id may be int (from users table) or str (from employee table).
    # Normalize to string for comparison with Employee.mgr_id (which is a string column).
    mid = str(manager_id)
    return [
        emp.emp_id
        for emp in db.query(Employee).filter(Employee.mgr_id == mid).all()
    ]


def get_task_or_404(db: Session, t_id: int):
    task = db.query(Tasks).filter(Tasks.t_id == t_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# ==================== CREATE TASK ====================
# In your tasks router file
from sqlalchemy import exists

@router.post(
    "",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_task(
    task: TaskCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Create a new task (Admin and Manager only)
    """
    # Allow both admin and manager to create tasks
    if not (is_admin(current_user) or is_manager(current_user)):
        raise HTTPException(
            status_code=403, 
            detail="Only Admin and Manager can create tasks"
        )
    
    try:
        new_task = Tasks(
            title=task.title,
            description=task.description,
            created_by=str(current_user.emp_id),
            assigned_to=task.assigned_to,
            assigned_by=str(current_user.emp_id),
            assigned_at=datetime.now(),
            priority=task.priority,
            status=task.status,
            reviewer=task.reviewer,
            expected_closure=task.expected_closure,
            remarks=task.remarks
        )
        
        db.add(new_task)
        db.commit()
        
        # Query back instead of refresh
        created_task = db.query(Tasks).filter(Tasks.t_id == new_task.t_id).first()
        
        return created_task
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Error creating task: {str(e)}"
        )
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

    # Developers should be able to see tasks assigned to them
    if is_developer(current_user):
        # normalize comparison by casting to string
        my_id = str(current_user.emp_id)
        return db.query(Tasks).filter(Tasks.assigned_to == my_id).all()

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

    # Allow developer if they are the assignee or the reviewer
    if is_developer(current_user):
        my_id = str(current_user.emp_id)
        if task.assigned_to == my_id or task.reviewer == my_id:
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

class StatusPayload(BaseModel):
    status: str


@router.patch(
    "/{t_id}/status",
    response_model=TaskResponse,
    status_code=status.HTTP_200_OK
)
async def update_task_status(
    t_id: int,
    status_payload: StatusPayload,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Use t_id from path for clarity; body contains only the new status
    task = get_task_or_404(db, t_id)

    if status_payload.status is None:
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

    task.status = status_payload.status
    task.updated_by = str(current_user.emp_id)

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
