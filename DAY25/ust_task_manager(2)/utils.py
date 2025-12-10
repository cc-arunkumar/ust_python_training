from typing import List
from sqlalchemy.orm import Session
from models import Task

# Removed in-memory tasks and get_next_task_id() - not needed for DB

def get_tasks_from_db(db: Session, user_id: int) -> List[Task]:
    return db.query(Task).filter(Task.user_id == user_id).all()

def create_task_in_db(db: Session, task: Task) -> Task:
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

"""
tasks = []

def get_next_task_id():
    if not tasks:
        return 1
    return tasks[-1]["id"] + 1
"""