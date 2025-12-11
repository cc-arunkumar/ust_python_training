# main.py
from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from models import Task, CreateTask, LoginRequest, Token, User, UserDB, TaskDB,Base
from auth import create_access_token, get_current_user, ACCESS_TOKEN_EXPIRE_MINUTES
from database import get_db,engine
from mongodb_logger import log_action
from datetime import timedelta

Base.metadata.create_all(bind=engine)
app = FastAPI(title="UST Task Tracker")


# ------------------ LOGIN ------------------
@app.post("/login", response_model=Token)
def login(data: LoginRequest, db: Session = Depends(get_db)):

    user = db.query(UserDB).filter(UserDB.username == data.username).first()

    if not user or user.password != data.password:
        raise HTTPException(401, "Invalid username or password")

    token = create_access_token(
        subject=user.username,
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return Token(access_token=token, token_type="bearer")


# ------------------ GET ALL TASKS ------------------
@app.get("/task", response_model=list[Task])
def get_all_tasks(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user = db.query(UserDB).filter(UserDB.username == current_user.username).first()
    tasks = db.query(TaskDB).filter(TaskDB.user_id == user.id).all()
    return tasks


# ------------------ GET TASK BY ID ------------------
@app.get("/task/{task_id}", response_model=Task)
def get_task_by_id(
    task_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user = db.query(UserDB).filter(UserDB.username == current_user.username).first()

    task = db.query(TaskDB).filter(TaskDB.id == task_id, TaskDB.user_id == user.id).first()

    if not task:
        raise HTTPException(404, "Task not found")

    return task


# ------------------ CREATE TASK ------------------
@app.post("/task", response_model=Task)
def create_task(
    task: CreateTask,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = db.query(UserDB).filter(UserDB.username == current_user.username).first()

    new_task = TaskDB(
        title=task.title,
        description=task.description,
        completed=task.completed,
        user_id=user.id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    log_action(user.username, "CREATE", new_task.id)

    return new_task


# ------------------ UPDATE TASK ------------------
@app.put("/task/{task_id}", response_model=Task)
def update_task(
    task_id: int,
    task: CreateTask,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user = db.query(UserDB).filter(UserDB.username == current_user.username).first()

    existing = db.query(TaskDB).filter(TaskDB.id == task_id, TaskDB.user_id == user.id).first()
    if not existing:
        raise HTTPException(404, "Task not found")

    existing.title = task.title
    existing.description = task.description
    existing.completed = task.completed

    db.commit()
    db.refresh(existing)

    log_action(user.username, "UPDATE", task_id)

    return existing


# ------------------ DELETE TASK ------------------
@app.delete("/task/{task_id}")
def delete_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user = db.query(UserDB).filter(UserDB.username == current_user.username).first()

    existing = db.query(TaskDB).filter(TaskDB.id == task_id, TaskDB.user_id == user.id).first()

    if not existing:
        raise HTTPException(404, "Task not found")

    db.delete(existing)
    db.commit()

    log_action(user.username, "DELETE", task_id)

    return {"message": "Task Deleted Successfully"}
