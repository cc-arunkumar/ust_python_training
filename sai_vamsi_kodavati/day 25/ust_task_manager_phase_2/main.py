from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session
from database import get_db,User,Task
from models import  TaskInResponse, TaskCreate, TaskUpdate, LoginRequest

from auth import create_access_token
from mongodb_logger import log_activity
from utils import get_current_user
from datetime import timedelta

app = FastAPI()

# POST /login: User login and JWT token generation
@app.post("/login")
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()
    if not user or user.password != request.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    access_token = create_access_token(subject=request.username)
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/tasks", response_model=TaskInResponse)
async def create_task(task: TaskCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    new_task = Task(title=task.title, description=task.description, completed=False, user_id=current_user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    # Log the activity in MongoDB
    log_activity(username=current_user.username, action="CREATE", task_id=new_task.id)
    
    return new_task




@app.get("/tasks")
def get_tasks(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    tasks = db.query(Task).filter(Task.user_id == current_user.id).all()
    return tasks

# GET /tasks/{task_id}: Get a specific task
@app.get("/tasks/{task_id}", response_model=TaskInResponse)
async def get_task(task_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# PUT /tasks/{task_id}: Update an existing task
@app.put("/tasks/{task_id}", response_model=TaskInResponse)
async def update_task(task_id: int, task: TaskUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    task_to_update = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    if not task_to_update:
        raise HTTPException(status_code=404, detail="Task not found")
    
    for key, value in task.dict(exclude_unset=True).items():
        setattr(task_to_update, key, value)
    
    db.commit()
    db.refresh(task_to_update)
    
    # Log the activity in MongoDB
    log_activity(username=current_user.username, action="UPDATE", task_id=task_to_update.id)
    
    return task_to_update

# DELETE /tasks/{task_id}: Delete a task
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    task_to_delete = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    if not task_to_delete:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task_to_delete)
    db.commit()
    
    # Log the activity in MongoDB
    log_activity(username=current_user.username, action="DELETE", task_id=task_to_delete.id)
    
    return {"message": "Task deleted successfully"}
