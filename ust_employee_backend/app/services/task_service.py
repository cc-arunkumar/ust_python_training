from sqlalchemy.orm import Session
from models.task import TaskDB
from schemas.task import TaskCreate

def create_task(db: Session, task: TaskCreate):
    db_task = TaskDB(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    """Return a paginated list of tasks.

    Args:
        db: SQLAlchemy Session
        skip: number of records to skip (offset)
        limit: maximum number of records to return

    Returns:
        list[TaskDB]
    """
    query = db.query(TaskDB).offset(skip)
    if limit is not None and limit > 0:
        query = query.limit(limit)
    return query.all()

def get_task_by_id(db: Session, task_id: int):
    return db.query(TaskDB).filter(TaskDB.id == task_id).first()

def update_task(db: Session, task_id: int, task: TaskCreate):
    db_task = get_task_by_id(db, task_id)
    if not db_task:
        return None

    for key, value in task.model_dump().items():
        setattr(db_task, key, value)

    db.commit()
    db.refresh(db_task)
    return db_task

VALID_STATUSES = {"TO_DO", "IN_PROGRESS","DONE", "REVIEW" }

def patch_status(db: Session, task_id: int, status: str, role: str | None = None):
    # normalize input
    normalized_status = status.strip().upper()

    if normalized_status not in VALID_STATUSES:
        raise ValueError(
            f"Invalid task status. Allowed: {', '.join(VALID_STATUSES)}"
        )

    task = db.query(TaskDB).filter(TaskDB.id == task_id).first()
    if not task:
        return None

    task.status = normalized_status
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    db_task = get_task_by_id(db, task_id)
    if not db_task:
        return False

    db.delete(db_task)
    db.commit()
    return True

def patch_reviewer(db, task_id: int, reviewer_id: str):
    task = get_task_by_id(db, task_id)
    if not task:
        return None

    if task.status != "DONE":
        raise ValueError("Task must be completed before assigning reviewer")

    task.reviewer_id = reviewer_id
    task.assigned_to = reviewer_id  # task goes to reviewer
    db.commit()
    db.refresh(task)
    return task


def patch_review(db, task_id: int, reviewer_id: str, remarks: str):
    task = get_task_by_id(db, task_id)
    if not task:
        return None

    task.reviewer_id = reviewer_id
    task.remarks = remarks
    db.commit()
    db.refresh(task)
    return task