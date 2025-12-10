from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
from database import get_db, create_all_tables
from models import LoginRequest, Token, TaskModel, TaskCreate, TaskUpdate, UserORM, TaskORM
from utils import create_access_token
from auth import get_current_user
from models import User
from mongodb_logger import log_activity

app = FastAPI(title="UST Task Manager", version="2.0")

create_all_tables()

@app.on_event("startup")
def seed_default_user():
    db = next(get_db())
    try:
        existing = db.query(UserORM).filter(UserORM.username == "rahul").first()
        if not existing:
            db.add(UserORM(username="rahul", password="password123"))
            db.commit()
    finally:
        db.close()

@app.post("/login", response_model=Token)
def login(credentials: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(UserORM).filter(UserORM.username == credentials.username).first()
    if not user or user.password != credentials.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    token = create_access_token(subject=user.username)
    return {"access_token": token, "token_type": "bearer"}

@app.post("/tasks", response_model=TaskModel)
def create_task(
    task_in: TaskCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    user = db.query(UserORM).filter(UserORM.username == current_user.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    task = TaskORM(
        title=task_in.title,
        description=task_in.description,
        completed=False,
        user_id=user.id,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    log_activity(current_user.username, "CREATE", task.id)

    return TaskModel(id=task.id, title=task.title, description=task.description, completed=task.completed)

@app.get("/tasks", response_model=List[TaskModel])
def list_tasks(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    user = db.query(UserORM).filter(UserORM.username == current_user.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    tasks = (
        db.query(TaskORM)
        .filter(TaskORM.user_id == user.id)
        .order_by(TaskORM.id.asc())
        .all()
    )
    return [TaskModel(id=t.id, title=t.title, description=t.description, completed=t.completed) for t in tasks]

@app.get("/tasks/{task_id}", response_model=TaskModel)
def get_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    user = db.query(UserORM).filter(UserORM.username == current_user.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    task = db.query(TaskORM).filter(TaskORM.id == task_id, TaskORM.user_id == user.id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    return TaskModel(id=task.id, title=task.title, description=task.description, completed=task.completed)

@app.put("/tasks/{task_id}", response_model=TaskModel)
def update_task(
    task_id: int,
    task_in: TaskUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    user = db.query(UserORM).filter(UserORM.username == current_user.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    task = db.query(TaskORM).filter(TaskORM.id == task_id, TaskORM.user_id == user.id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    task.title = task_in.title
    task.description = task_in.description
    task.completed = task_in.completed
    db.commit()
    db.refresh(task)

    log_activity(current_user.username, "UPDATE", task.id)

    return TaskModel(id=task.id, title=task.title, description=task.description, completed=task.completed)

@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    user = db.query(UserORM).filter(UserORM.username == current_user.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    task = db.query(TaskORM).filter(TaskORM.id == task_id, TaskORM.user_id == user.id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    db.delete(task)
    db.commit()

    log_activity(current_user.username, "DELETE", task.id)
    return {"detail": "Task deleted successfully"}
