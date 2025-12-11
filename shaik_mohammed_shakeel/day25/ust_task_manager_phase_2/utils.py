from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session
import models
from mongodb_logger import log_activity  # Import MongoDB logging function
 
 
# Helper: resolve username -> User object (or None)
def _get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()
 
 
# Create a task with user_id fetched by username
def create_task(db: Session, task_in: models.TaskCreate, username: str) -> models.TaskResponse:
    # Get the user based on the username
    user = _get_user_by_username(db, username)
 
    if not user:
        raise HTTPException(status_code=404, detail=f"User with username {username} not found")
 
    # Create a new task and associate it with the correct user_id
    db_task = models.Task(
        title=task_in.title,
        description=task_in.description,
        completed=False,
        user_id=user.id,
    )
 
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
 
    # Log the task creation in MongoDB
    log_activity(username, "CREATE", db_task.id)
 
    return models.TaskResponse.from_orm(db_task)
 
 
# Get all tasks for a user (username provided)
def get_all_tasks(db: Session, username: str) -> List[models.TaskResponse]:
    user = _get_user_by_username(db, username)
    if not user:
        return []
 
    db_tasks = db.query(models.Task).filter(models.Task.user_id == user.id).all()
    return [models.TaskResponse.from_orm(task) for task in db_tasks]
 
 
# Get task by ID
def get_task_by_id(db: Session, task_id: int, username: str) -> Optional[models.TaskResponse]:
    user = _get_user_by_username(db, username)
    if not user:
        return None
 
    db_task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.user_id == user.id).first()
    if db_task:
        return models.TaskResponse.from_orm(db_task)
    return None
 
 
# Update task
def update_task(db: Session, task_id: int, task_in: models.TaskUpdate, username: str) -> Optional[models.TaskResponse]:
    user = _get_user_by_username(db, username)
    if not user:
        return None
 
    db_task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.user_id == user.id).first()
    if db_task:
        db_task.title = task_in.title
        db_task.description = task_in.description
        db_task.completed = task_in.completed
        db.commit()
        db.refresh(db_task)
 
        # Log the task update in MongoDB
        log_activity(username, "UPDATE", db_task.id)
 
        return models.TaskResponse.from_orm(db_task)
    return None
 
 
# Delete task
def delete_task(db: Session, task_id: int, username: str) -> bool:
    user = _get_user_by_username(db, username)
    if not user:
        return False
 
    db_task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.user_id == user.id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
 
        # Log the task deletion in MongoDB
        log_activity(username, "DELETE", db_task.id)
 
        return True
    return False
 
 