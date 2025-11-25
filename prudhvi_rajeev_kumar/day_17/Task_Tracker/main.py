from fastapi import FastAPI, HTTPException, Depends
from datetime import timedelta
from typing import List

from models import LoginRequest, Token, User, TaskModel
from utils import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from auth import get_current_user, DEMO_USERNAME, DEMO_PASSWORD

app = FastAPI(title="Task Tracker API")

next_id = 1
tasks: List[TaskModel] = []

@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(status_code=401, detail="Incorrect username or password.")
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)
    return Token(access_token=token, token_type="bearer")

@app.post("/tasks")
def create_task(task: TaskModel, current_user: User = Depends(get_current_user)):
    global next_id
    task.id = next_id
    tasks.append(task)
    next_id += 1
    return task

@app.get("/tasks")
def get_tasks(current_user: User = Depends(get_current_user)):
    return tasks

@app.get("/tasks/{task_id}")
def get_task_by_id(task_id: int, current_user: User = Depends(get_current_user)):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}")
def update_task(task_id: int, new_data: TaskModel, current_user: User = Depends(get_current_user)):
    for task in tasks:
        if task.id == task_id:
            task.title = new_data.title
            task.description = new_data.description
            task.completed = new_data.completed
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, current_user: User = Depends(get_current_user)):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
