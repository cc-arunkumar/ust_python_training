from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import List
from models import LoginRequest, Token, TaskCreate, TaskUpdate, Task, users
from auth import create_access_token, decode_token
from utils import get_next_task_id
from jose import JWTError

app = FastAPI(title="UST Task Manager")

tasks: List[Task] = []
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    token = credentials.credentials
    try:
        payload = decode_token(token)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
    username = payload.get("sub")
    if not username or username not in users:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
    return username


@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    user = users.get(data.username)
    if not user or user["password"] != data.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    token = create_access_token(subject=data.username)
    return Token(access_token=token, token_type="bearer")

@app.post("/tasks", response_model=Task)
def create_task(payload: TaskCreate, current_user: str = Depends(get_current_user)):
    print(f"User {current_user} is creating a task")
    new_task = Task(
        id=get_next_task_id(tasks),
        title=payload.title,
        description=payload.description,
        completed=False
    )
    tasks.append(new_task)
    return new_task

@app.get("/tasks", response_model=List[Task])
def get_all_tasks(current_user: str = Depends(get_current_user)):
    print(f"User {current_user} accessed /tasks")
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int, current_user: str = Depends(get_current_user)):
    for t in tasks:
        if t.id == task_id:
            return t
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, payload: TaskUpdate, current_user: str = Depends(get_current_user)):
    print(f"User {current_user} is updating task {task_id}")
    for id, t in enumerate(tasks):
        if t.id == task_id:
            updated = Task(id=t.id, title=payload.title, description=payload.description, completed=payload.completed)
            tasks[id] = updated
            return updated
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, current_user: str = Depends(get_current_user)):
    print(f"User {current_user} is deleting task {task_id}")
    for t in tasks:
        if t.id == task_id:
            tasks = [x for x in tasks if x.id != task_id]
            return {"message": "Task deleted successfully"}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")