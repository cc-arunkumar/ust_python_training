from fastapi import FastAPI, HTTPException, Depends
from datetime import timedelta
from typing import List

from models import LoginRequest, TokenResponse, Task, CreateTask, UpdateTask
from auth import create_access_token, get_current_user, ACCESS_TOKEN_EXPIRE_MINUTES, users
from utils import next_id

# Initialize FastAPI app
app = FastAPI(title="UST Task Manager")

# In-memory storage for tasks
tasks: List[Task] = []
current_id: int = 0   # Tracks the latest task ID


# Authentication Endpoints

@app.post("/login", response_model=TokenResponse)
def login(credentials: LoginRequest):
    """
    Login endpoint:
    - Validates username and password against hardcoded users.
    - Returns a JWT token if credentials are correct.
    """
    user = users.get(credentials.username)
    if not user or user["password"] != credentials.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    # Create JWT token with expiration
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=credentials.username, expires_delta=expires)
    return TokenResponse(access_token=token)



# Task CRUD Endpoints

@app.post("/tasks", response_model=Task)
def create_task(task: CreateTask, current_user=Depends(get_current_user)):
    """
    Create a new task:
    - Requires valid JWT authentication.
    - Auto-increments task ID.
    - Stores task in memory.
    """
    global current_id, tasks
    current_id = next_id(current_id)
    new_task = Task(
        id=current_id,
        title=task.title,
        description=task.description,
        completed=False
    )
    tasks.append(new_task)
    return new_task


@app.get("/tasks", response_model=List[Task])
def get_all_tasks(current_user=Depends(get_current_user)):
    """
    Get all tasks:
    - Requires valid JWT authentication.
    - Returns the full list of tasks.
    """
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int, current_user=Depends(get_current_user)):
    """
    Get a single task by ID:
    - Requires valid JWT authentication.
    - Returns the task if found, else raises 404.
    """
    task = next((t for t in tasks if t.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, update: UpdateTask, current_user=Depends(get_current_user)):
    """
    Update an existing task:
    - Requires valid JWT authentication.
    - Finds task by ID and updates its fields.
    - Returns updated task or raises 404 if not found.
    """
    for idx, t in enumerate(tasks):
        if t.id == task_id:
            updated = Task(
                id=t.id,
                title=update.title,
                description=update.description,
                completed=update.completed
            )
            tasks[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, current_user=Depends(get_current_user)):
    """
    Delete a task by ID:
    - Requires valid JWT authentication.
    - Removes task from memory if found.
    - Returns success message or raises 404 if not found.
    """
    global tasks
    for idx, t in enumerate(tasks):
        if t.id == task_id:
            tasks.pop(idx)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
