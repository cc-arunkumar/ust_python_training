from datetime import datetime, timedelta, timezone
from typing import List, Optional

from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from jose import JWTError, jwt

# FastAPI app
app = FastAPI(title="Minimal JWT Auth Demo")

# Configuration
SECRET_KEY = "UST-TaskTracker-Secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Demo user (hardcoded to avoid interactive input)
DEMO_USERNAME = "rahul"
DEMO_PASSWORD = "password123"

# Pydantic Models
class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str

# Separate models for input vs output
class TaskCreate(BaseModel):
    title: str
    description: str

class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False

# Helper to create JWT
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode = {"sub": subject, "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# HTTPBearer for Authorization: Bearer <token>
security = HTTPBearer()

# Decode + verify token
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    username = payload.get("sub")
    if username != DEMO_USERNAME:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    return User(username=username)

# /login endpoint → returns JWT token
@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    token = create_access_token(subject=data.username)
    return Token(access_token=token, token_type="bearer")

# In-memory task storage
tasks: List[Task] = []
_next_id = 1

# /tasks → Fetch all tasks (protected)
@app.get("/tasks", response_model=List[Task])
def get_tasks(current_user: User = Depends(get_current_user)):
    return tasks

# /tasks → Create a new task (protected)
@app.post("/tasks", response_model=Task)
def create_task(task_in: TaskCreate, current_user: User = Depends(get_current_user)):
    global _next_id
    task = Task(id=_next_id, title=task_in.title, description=task_in.description, completed=False)
    tasks.append(task)
    _next_id += 1
    return task

# /tasks/{task_id} → Get a single task by ID (protected)
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int, current_user: User = Depends(get_current_user)):
    for t in tasks:
        if t.id == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task not found")

# /tasks/{task_id} → Update a task by ID (full update, protected)
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_in: TaskUpdate, current_user: User = Depends(get_current_user)):
    for i, t in enumerate(tasks):
        if t.id == task_id:
            if task_in.title is None or task_in.description is None or task_in.completed is None:
                raise HTTPException(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    detail="title, description, and completed are required",
                )
            updated = Task(
                id=task_id,
                title=task_in.title,
                description=task_in.description,
                completed=task_in.completed,
            )
            tasks[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Task not found")

# /tasks/{task_id} → Delete a task by ID (protected)
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, current_user: User = Depends(get_current_user)):
    for i, t in enumerate(tasks):
        if t.id == task_id:
            tasks.pop(i)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
