from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import TaskModel, UserModel, get_db
from auth import get_current_user, create_access_token, LoginRequest, Token, User, ACCESS_TOKEN_EXPIRE_MINS
from datetime import timedelta
from pymongo import MongoClient
from datetime import datetime

app = FastAPI(title="Task Manager API")

# MongoDB Setup for Activity Logging
client = MongoClient("mongodb://localhost:27017/")
mongo_db = client["ust_mongo_db"]
log_collection = mongo_db["activity_log"]

# MySQL Login Endpoint
@app.post("/login", response_model=Token)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.username == data.username).first()
    if not user or user.password != data.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINS)
    token = create_access_token(subject=data.username, expires_delta=expires)
    return Token(access_token=token)

# Task Creation Endpoint
@app.post("/tasks")
def create_task(task: TaskModel, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_task = TaskModel(
        title=task.title,
        description=task.description,
        completed=task.completed,
        user_id=current_user.id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    # Log Activity to MongoDB
    log_collection.insert_one({
        "username": current_user.username,
        "action": "CREATE",
        "task_id": new_task.id,
        "timestamp": datetime.utcnow()
    })

    return new_task

# Get All Tasks for a User
@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    tasks = db.query(TaskModel).filter(TaskModel.user_id == current_user.id).all()
    return tasks

# Get Task by ID
@app.get("/tasks/{task_id}")
def get_by_id(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id, TaskModel.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Update Task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskModel, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id, TaskModel.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = updated_task.title
    task.description = updated_task.description
    task.completed = updated_task.completed

    db.commit()
    db.refresh(task)

    # Log Activity to MongoDB
    log_collection.insert_one({
        "username": current_user.username,
        "action": "UPDATE",
        "task_id": task.id,
        "timestamp": datetime.utcnow()
    })

    return task

# Delete Task
@app.delete("/tasks/{task_id}")
def del_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id, TaskModel.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    # Log Activity to MongoDB
    log_collection.insert_one({
        "username": current_user.username,
        "action": "DELETE",
        "task_id": task.id,
        "timestamp": datetime.utcnow()
    })

    return {"message": "Task deleted successfully"}
