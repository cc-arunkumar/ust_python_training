from datetime import datetime, timedelta, timezone
from typing import List, Optional

from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from models import Task,TaskCreate,TaskUpdate,UserLogin,Token
from auth import create_access_token,get_current_user,DEMO_USERNAME,DEMO_PASSWORD


app = FastAPI(title="UST Task Manager")


# In-memory storage
tasks: List[dict] = []
next_task_id = 1


# Login (no JWT required)
@app.post("/login", response_model=Token)
def login(data: UserLogin):
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_access_token(username=data.username)
    return {"access_token": token, "token_type": "bearer"}

# Create Task
@app.post("/tasks", response_model=Task)
def create_task(data: TaskCreate, username: str = Depends(get_current_user)):
    global next_task_id
    for t in tasks:
        if t["title"].lower() == data.title.lower():
            raise HTTPException(status_code=400, detail="Title already exists")
    new_task = {"id": next_task_id, "title": data.title, "description": data.description, "completed": False}
    tasks.append(new_task)
    next_task_id += 1
    return new_task

# Get All Tasks
@app.get("/tasks", response_model=List[Task])
def get_tasks(username: str = Depends(get_current_user)):
    return tasks

# Get Single Task
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int, username: str = Depends(get_current_user)):
    for t in tasks:
        if t["id"] == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task not found")

# Update Task
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, data: TaskUpdate, username: str = Depends(get_current_user)):
    for t in tasks:
        if t["id"] == task_id:
            t.update({"title": data.title, "description": data.description, "completed": data.completed})
            return t
    raise HTTPException(status_code=404, detail="Task not found")

# Delete Task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, username: str = Depends(get_current_user)):
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
