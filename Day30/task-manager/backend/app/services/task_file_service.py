"""from sqlalchemy.orm import Session
from fastapi import HTTPException, UploadFile
from app.models.task_file import TaskFile
from app.models.task import Task


def upload_task_file(
    db: Session,
    task_id: int,
    file: UploadFile
):
    task = db.query(Task).filter(Task.task_id == task_id).first()
    if not task:
        raise HTTPException(404, "Task not found")

    data = file.file.read()

    if len(data) > 5 * 1024 * 1024:  # 5MB limit
        raise HTTPException(400, "File too large")

    task_file = TaskFile(
        task_id=task_id,
        filename=file.filename,
        content_type=file.content_type,
        file_data=data
    )

    db.add(task_file)
    db.commit()
    db.refresh(task_file)
    return task_file


def get_task_file(db: Session, file_id: int):
    file = db.query(TaskFile).filter(TaskFile.file_id == file_id).first()
    if not file:
        raise HTTPException(404, "File not found")
    return file
"""

from sqlalchemy.orm import Session
from fastapi import HTTPException, UploadFile
from app.models.task_file import TaskFile
from app.models.task import Task

def upload_task_file(db: Session, task_id: int, file: UploadFile):
    task = db.query(Task).filter(Task.task_id == task_id).first()
    if not task:
        raise HTTPException(404, "Task not found")
    data = file.file.read()
    if len(data) > 5 * 1024 * 1024:  # 5MB limit
        raise HTTPException(400, "File too large")
    task_file = TaskFile(
        task_id=task_id,
        filename=file.filename,
        content_type=file.content_type,
        file_data=data
    )
    db.add(task_file)
    db.commit()
    db.refresh(task_file)
    return task_file

def get_task_file(db: Session, file_id: int):
    file = db.query(TaskFile).filter(TaskFile.file_id == file_id).first()
    if not file:
        raise HTTPException(404, "File not found")
    return file