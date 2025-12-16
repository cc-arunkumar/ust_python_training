from sqlalchemy.orm import Session
from models import TaskORM, TaskCreate, TaskUpdate, Task
from logfile import log_activity


# ---------------- CREATE TASK ----------------
def create_task(db: Session, task_data: TaskCreate, user_id: int, username: str):
    new_task = TaskORM(
        title=task_data.title,
        description=task_data.description,
        completed=False,
        user_id=user_id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    log_activity("CREATE", new_task.id, username)
    return new_task


# ---------------- GET ALL TASKS FOR USER ----------------
def get_tasks(db: Session, user_id: int):
    tasks = db.query(TaskORM).filter(TaskORM.user_id == user_id).all()
    return tasks


# ---------------- GET SINGLE TASK ----------------
def get_task(db: Session, task_id: int, user_id: int):
    task = db.query(TaskORM).filter(
        TaskORM.id == task_id,
        TaskORM.user_id == user_id
    ).first()
    return task


# ---------------- UPDATE TASK ----------------
def update_task(db: Session, task_id: int, task_data: TaskUpdate, user_id: int, username: str):
    task = db.query(TaskORM).filter(
        TaskORM.id == task_id,
        TaskORM.user_id == user_id
    ).first()

    if not task:
        return None

    task.title = task_data.title
    task.description = task_data.description
    task.completed = task_data.completed

    db.commit()
    db.refresh(task)
    log_activity("UPDATE", task.id, username)
    return task


# ---------------- DELETE TASK ----------------
def delete_task(db: Session, task_id: int, user_id: int, username: str):
    task = db.query(TaskORM).filter(
        TaskORM.id == task_id,
        TaskORM.user_id == user_id
    ).first()

    if not task:
        return False

    db.delete(task)
    db.commit()
    log_activity("DELETE", task_id, username)
    return True
