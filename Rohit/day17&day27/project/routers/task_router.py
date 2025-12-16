from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models import Task, TaskDB, UserDB
from auth import get_current_user
from database import get_db
from mongodb_logger import log_activity

router = APIRouter(tags=["Tasks"])

@router.post("/tasks")
def create_task(task: Task, username: str = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.username == username).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    new_task = TaskDB(title=task.title, description=task.description, completed=task.completed, user_id=user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    log_activity(username, "CREATE", new_task.id)
    return Task(id=new_task.id, title=new_task.title, description=new_task.description, completed=new_task.completed)

@router.get("/tasks", response_model=list[Task])
def get_tasks(username: str = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.username == username).first()
    tasks = db.query(TaskDB).filter(TaskDB.user_id == user.id).all()
    return [Task(id=t.id, title=t.title, description=t.description, completed=t.completed) for t in tasks]

@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int, username: str = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.username == username).first()
    task = db.query(TaskDB).filter(TaskDB.id == task_id, TaskDB.user_id == user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return Task(id=task.id, title=task.title, description=task.description, completed=task.completed)

@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task, username: str = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.username == username).first()
    task = db.query(TaskDB).filter(TaskDB.id == task_id, TaskDB.user_id == user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = updated_task.title
    task.description = updated_task.description
    task.completed = updated_task.completed
    db.commit()
    db.refresh(task)

    log_activity(username, "UPDATE", task.id)
    return Task(id=task.id, title=task.title, description=task.description, completed=task.completed)

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, username: str = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.username == username).first()
    task = db.query(TaskDB).filter(TaskDB.id == task_id, TaskDB.user_id == user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    log_activity(username, "DELETE", task.id)
    return {"message": "Task deleted successfully"}
