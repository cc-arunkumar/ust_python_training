# Import necessary libraries and modules
from fastapi import FastAPI, HTTPException, status, Depends
from models import Task, tasks, next_id   # Task model, in-memory task list, and auto-increment ID
from auth import (
    Token, LoginRequest, User, users,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token,
    get_current_user
)
from typing import List
import datetime

# Initialize FastAPI application
app = FastAPI(title="UST Task Tracker")

# ---------------- LOGIN ENDPOINT ----------------
@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    """
    Authenticate user by checking username and password.
    If valid, generate and return an access token.
    """
    for user in users:
        if data.username == user.username and data.password == user.password:
            # Token expiration time
            expires = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            # Create JWT token
            token = create_access_token(subject=data.username, expires_delta=expires)
            return Token(access_token=token, token_type="bearer")

    # Raise error if credentials are invalid
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
    )

# ✅ Example Output (Success):
# {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
#   "token_type": "bearer"
# }
#
# ❌ Example Output (Failure):
# {
#   "detail": "Incorrect username or password"
# }

# ---------------- CREATE TASK ENDPOINT ----------------
@app.post("/tasks", response_model=Task)
def create(task: Task, current_user: User = Depends(get_current_user)):
    """
    Create a new task and assign it a unique ID.
    """
    global next_id
    task.id = next_id
    next_id += 1
    tasks.append(task)
    return task

# ✅ Example Output:
# {
#   "id": 1,
#   "title": "Finish project",
#   "description": "Complete FastAPI module",
#   "completed": false
# }

# ---------------- DISPLAY ALL TASKS ENDPOINT ----------------
@app.get("/tasks", response_model=List[Task])
def display(current_user: User = Depends(get_current_user)):
    """
    Display all tasks created by the user.
    """
    return tasks

# ✅ Example Output:
# [
#   {
#     "id": 1,
#     "title": "Finish project",
#     "description": "Complete FastAPI module",
#     "completed": false
#   },
#   {
#     "id": 2,
#     "title": "Write documentation",
#     "description": "Add comments and outputs",
#     "completed": false
#   }
# ]

# ---------------- SEARCH TASK BY ID ENDPOINT ----------------
@app.get("/tasks/{task_id}", response_model=Task)
def search_byid(task_id: int, current_user: User = Depends(get_current_user)):
    """
    Search for a task by its ID.
    """
    for t in tasks:
        if t.id == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task Not Found")

# ✅ Example Output (Success):
# {
#   "id": 1,
#   "title": "Finish project",
#   "description": "Complete FastAPI module",
#   "completed": false
# }
#
# ❌ Example Output (Failure):
# {
#   "detail": "Task Not Found"
# }

# ---------------- UPDATE TASK ENDPOINT ----------------
@app.put("/tasks/{task_id}", response_model=Task)
def update(task_id: int, task: Task, current_user: User = Depends(get_current_user)):
    """
    Update an existing task by ID.
    """
    for t in tasks:
        if t.id == task_id:
            t.title = task.title
            t.description = task.description
            t.completed = task.completed
            return t
    raise HTTPException(status_code=404, detail="Task Not Found")

# ✅ Example Output (Success):
# {
#   "id": 1,
#   "title": "Finish project (Updated)",
#   "description": "Complete FastAPI module ASAP",
#   "completed": true
# }
#
# ❌ Example Output (Failure):
# {
#   "detail": "Task Not Found"
# }

# ---------------- DELETE TASK ENDPOINT ----------------
@app.delete("/tasks/{task_id}")
def delete(task_id: int, current_user: User = Depends(get_current_user)):
    """
    Delete a task by its ID.
    """
    for t in tasks:
        if t.id == task_id:
            tasks.remove(t)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task Not Found")

# ✅ Example Output (Success):
# {
#   "message": "Task deleted successfully"
# }
#
# ❌ Example Output (Failure):
# {
#   "detail": "Task Not Found"
# }
