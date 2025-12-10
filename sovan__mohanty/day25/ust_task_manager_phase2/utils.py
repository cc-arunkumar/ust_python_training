from sqlalchemy.orm import Session
from models import TaskORM, TaskCreate, TaskUpdate
from mongodb_logger import log_activity

def create_task(db: Session, task_data: TaskCreate, user_id: int, username: str):
    task = TaskORM(title=task_data.title, description=task_data.description, completed=False, user_id=user_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    log_activity(username, "CREATE", task.id)
    return task

def get_tasks(db: Session, user_id: int):
    return db.query(TaskORM).filter(TaskORM.user_id == user_id).all()

def get_task(db: Session, task_id: int, user_id: int):
    return db.query(TaskORM).filter(TaskORM.id == task_id, TaskORM.user_id == user_id).first()

def update_task(db: Session, task_id: int, task_data: TaskUpdate, user_id: int, username: str):
    task = get_task(db, task_id, user_id)
    if not task:
        return None
    if task_data.title is not None:
        task.title = task_data.title
    if task_data.description is not None:
        task.description = task_data.description
    if task_data.completed is not None:
        task.completed = task_data.completed
    db.commit()
    db.refresh(task)
    log_activity(username, "UPDATE", task.id)
    return task

def delete_task(db: Session, task_id: int, user_id: int, username: str):
    task = get_task(db, task_id, user_id)
    if not task:
        return False
    db.delete(task)
    db.commit()
    log_activity(username, "DELETE", task.id)
    return True
