from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from models import Task, TaskInResponse, TaskCreate, TaskUpdate, LoginRequest
from auth import create_access_token
from utils import get_current_user, get_task_by_id
from datetime import timedelta
 
app = FastAPI()
 
# In-memory storage for tasks and hardcoded users
tasks = []
next_task_id = 1
 
users = {
    "rahul": {
        "username": "rahul",
        "password": "password123"
    }
}
 
# POST /login: User login and JWT token generation
@app.post("/login")
async def login(request: LoginRequest):
    user = users.get(request.username)
    if not user or user['password'] != request.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
   
    access_token = create_access_token(subject=request.username)
    return {"access_token": access_token, "token_type": "bearer"}
 
# POST /tasks: Create a new task
@app.post("/tasks", response_model=TaskInResponse)
async def create_task(task: TaskCreate, current_user: str = Depends(get_current_user)):
    global next_task_id
    task_data = task.dict()
    task_data["id"] = next_task_id
    tasks.append(task_data)
    next_task_id += 1
    return task_data
 
# GET /tasks: Get all tasks
@app.get("/tasks", response_model=List[TaskInResponse])
async def get_all_tasks(current_user: str = Depends(get_current_user)):
    return tasks
 
# GET /tasks/{task_id}: Get a specific task
@app.get("/tasks/{task_id}", response_model=TaskInResponse)
async def get_task(task_id: int, current_user: str = Depends(get_current_user)):
    task = get_task_by_id(task_id, tasks)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
 
# PUT /tasks/{task_id}: Update an existing task
@app.put("/tasks/{task_id}", response_model=TaskInResponse)
async def update_task(task_id: int, task: TaskUpdate, current_user: str = Depends(get_current_user)):
    task_to_update = get_task_by_id(task_id, tasks)
    if not task_to_update:
        raise HTTPException(status_code=404, detail="Task not found")
   
    updated_task = task_to_update.copy()
    updated_task.update(task.dict(exclude_unset=True))
    tasks[tasks.index(task_to_update)] = updated_task
    return updated_task
 
# DELETE /tasks/{task_id}: Delete a task
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int, current_user: str = Depends(get_current_user)):
    task_to_delete = get_task_by_id(task_id, tasks)
    if not task_to_delete:
        raise HTTPException(status_code=404, detail="Task not found")
   
    tasks.remove(task_to_delete)
    return {"message": "Task deleted successfully"}
 
 