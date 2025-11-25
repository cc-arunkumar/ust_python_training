from fastapi import FastAPI, Depends, HTTPException, status  # FastAPI and exception handling
from pydantic import BaseModel  # For data validation
from typing import List, Optional  # For type hints like List, Optional
from models import Task, TaskInResponse, TaskCreate, TaskUpdate, LoginRequest  # Import Pydantic models
from auth import create_access_token  # Token creation helper
from utils import get_current_user, get_task_by_id  # Helper functions
from datetime import timedelta

# Create FastAPI app
app = FastAPI()

# In-memory storage for tasks (data is lost when server restarts)
tasks = []
next_task_id = 1  # Auto-increment ID for tasks

# Hardcoded users for authentication
users = {
    "rahul": {
        "username": "rahul",
        "password": "password123"
    }
}

# POST /login → User login & JWT token generation
@app.post("/login")
async def login(request: LoginRequest):
    # Check if user exists
    user = users.get(request.username)

    # Check password correctness
    if not user or user['password'] != request.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    # Create JWT token
    access_token = create_access_token(subject=request.username)

    # Return token
    return {"access_token": access_token, "token_type": "bearer"}


# POST /tasks → Create a new task
@app.post("/tasks", response_model=TaskInResponse)
async def create_task(task: TaskCreate, current_user: str = Depends(get_current_user)):
    global next_task_id

    # Use model_dump() instead of dict()
    task_data = task.model_dump()

    # Assign unique ID to the task
    task_data["id"] = next_task_id

    # Add task to in-memory list
    tasks.append(task_data)

    # Increment next ID
    next_task_id += 1

    return task_data


# PUT /tasks/{task_id} → Update a task
@app.put("/tasks/{task_id}", response_model=TaskInResponse)
async def update_task(task_id: int, task: TaskUpdate, current_user: str = Depends(get_current_user)):
    # Find existing task
    task_to_update = get_task_by_id(task_id, tasks)

    # Handle not found
    if not task_to_update:
        raise HTTPException(status_code=404, detail="Task not found")

    # Create a copy and update fields that are provided
    updated_task = task_to_update.copy()

    # Use model_dump() instead of dict()
    updated_task.update(task.model_dump(exclude_unset=True))

    # Replace old record with updated one
    tasks[tasks.index(task_to_update)] = updated_task
    return updated_task


# DELETE /tasks/{task_id} → Delete a task
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int, current_user: str = Depends(get_current_user)):
    # Find existing task
    task_to_delete = get_task_by_id(task_id, tasks)

    # If task not found
    if not task_to_delete:
        raise HTTPException(status_code=404, detail="Task not found")

    # Remove from list
    tasks.remove(task_to_delete)

    return {"message": "Task deleted successfully"}
