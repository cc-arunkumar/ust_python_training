from typing import List, Optional
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer

from models import AddTask, GetTask, LoginRequest, TokenResponse
from auth import create_access_token, verify_token
from utils import users

app = FastAPI(title="Task Tracker API")

# In-memory storage
tasks: List[GetTask] = []
current_id: int = 1

# OAuth2 bearer with token URL /login
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def find_task(task_id: int) -> Optional[GetTask]:
    for t in tasks:
        if t.id == task_id:
            return t
    return None


def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    payload = verify_token(token)
    return payload.get("sub")


@app.post("/login", response_model=TokenResponse)
def login(credentials: LoginRequest):
    user = users.get(credentials.username)
    if not user or user["password"] != credentials.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_access_token({"sub": credentials.username})
    return {"access_token": token, "token_type": "bearer"}



@app.post("/tasks", response_model=GetTask)
def create_task(task: AddTask, user: str = Depends(get_current_user)):
    global current_id
    new_task = GetTask(
        id=current_id,
        title=task.title,
        description=task.description,
        completed=task.completed
    )
    tasks.append(new_task)
    current_id += 1
    return new_task


@app.get("/tasks", response_model=List[GetTask])
def get_all_tasks(user: str = Depends(get_current_user)):
    return tasks


@app.get("/tasks/{task_id}", response_model=GetTask)
def get_task(task_id: int, user: str = Depends(get_current_user)):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=GetTask)
def update_task(task_id: int, updated: AddTask, user: str = Depends(get_current_user)):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    task.title = updated.title
    task.description = updated.description
    task.completed = updated.completed
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, user: str = Depends(get_current_user)):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    for i, t in enumerate(tasks):
        if t.id == task_id:
            tasks.pop(i)
            break
    return {"message": "Task deleted successfully"}
