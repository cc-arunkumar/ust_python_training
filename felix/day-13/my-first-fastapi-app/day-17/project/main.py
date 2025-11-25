from fastapi import FastAPI, HTTPException, status, Depends
from typing import Optional
from pydantic import BaseModel, Field
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI(title="UST Task Manager")

# -----------------------------
# JWT CONFIGURATION
# -----------------------------
SECRET_KEY = "UST-TaskTracker-Secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token validity duration


# -----------------------------
# REQUEST/RESPONSE MODELS
# -----------------------------
class LoginRequest(BaseModel):
    """Schema for user login"""
    username: str = Field(..., description="username is missing")
    password: str = Field(..., description="password is missing")


class Token(BaseModel):
    """Response model for generated JWT token"""
    access_token: str
    token_type: str


class User(BaseModel):
    """Represents authenticated user"""
    username: str


class TaskModel(BaseModel):
    """Full Task model for storing tasks"""
    id: int
    title: str
    description: str
    completed: bool


class TaskModelCreate(BaseModel):
    """Model for creating a new task"""
    title: str = Field(..., description="Field is required")
    description: str = Field(..., description="Field is required")


class TaskModelUpdate(BaseModel):
    """Model for updating an existing task"""
    title: str = Field(..., description="Field is required")
    description: str = Field(..., description="Field is required")
    completed: bool = Field(..., description="Field is required")


# -----------------------------
# IN-MEMORY STORAGE
# -----------------------------
tasks = []  # Stores all tasks
task_id_counter = 1  # Auto-incrementing task ID

# Hardcoded user for demo purposes
users = {
    "felix": {
        "username": "felix",
        "password": "password123"
    }
}


# -----------------------------
# TOKEN CREATION FUNCTION
# -----------------------------
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None) -> str:
    """
    Generates a JWT access token.
    :param subject: Username or user identifier
    :param expires_delta: Optional token expiry duration
    """
    to_encode = {"sub": subject}

    # Set expiration time
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})

    # Encode JWT token
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded


# Security scheme for authorization headers
security = HTTPBearer()


# -----------------------------
# AUTHENTICATION DEPENDENCY
# -----------------------------
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    """
    Validates the JWT token and returns the authenticated user.
    Raises 401 errors for invalid/expired tokens.
    """
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    username = payload.get("sub")

    # Validate user exists
    if username != users["felix"]["username"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    return User(username=username)


# -----------------------------
# AUTH ROUTES
# -----------------------------
@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    """
    Authenticates user and returns JWT token.
    """
    if data.username != users["felix"]["username"] or data.password != users["felix"]["password"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )

    # Generate access token
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)

    return Token(access_token=token, token_type="bearer")


# -----------------------------
# TASK MANAGEMENT ROUTES
# -----------------------------
@app.post("/task")
def create_task(task: TaskModelCreate, current_user: User = Depends(get_current_user)):
    """
    Creates a new task and stores it in memory.
    """
    global task_id_counter

    task_item = TaskModel(
        id=task_id_counter,
        title=task.title,
        description=task.description,
        completed=False
    )

    task_id_counter += 1
    tasks.append(task_item.__dict__)

    return task_item


@app.get("/tasks")
def list_all_tasks(current_user: User = Depends(get_current_user)):
    """
    Returns a list of all tasks.
    """
    return tasks


@app.get("/tasks/{task_id}")
def get_task_by_id(task_id: int, current_user: User = Depends(get_current_user)):
    """
    Fetch a single task by its ID.
    """
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskModelUpdate, current_user: User = Depends(get_current_user)):
    """
    Updates an existing task by its ID.
    """
    for index in range(len(tasks)):
        if tasks[index]["id"] == task_id:
            task_item = TaskModel(
                id=task_id,
                title=task.title,
                description=task.description,
                completed=task.completed
            )
            tasks[index] = task_item.__dict__
            return task_item

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, current_user: User = Depends(get_current_user)):
    """
    Deletes a task by its ID.
    """
    for index in range(len(tasks)):
        if tasks[index]["id"] == task_id:
            tasks.pop(index)
            return {"message": "Task deleted successfully"}

    raise HTTPException(status_code=404, detail="Task not found")
