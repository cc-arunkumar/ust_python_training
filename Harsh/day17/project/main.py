from fastapi import FastAPI, HTTPException, Depends
from datetime import timedelta
from models import LoginRequest, Token, Task
from auth import DEMO_USER, DEMO_PASSWORD, create_access_token, get_current_user, ACCESS_TOKEN_EXPIRE_MINUTES
from utils import tasks, next_id

app = FastAPI(title="Task Tracker")

@app.post("/login")
def login(data: LoginRequest):
    if data.username != DEMO_USER or data.password != DEMO_PASSWORD:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)
    return Token(access_token=token, token_type="bearer")

@app.post("/tasks")
def create_task(task: Task, user: str = Depends(get_current_user)):
    global next_id
    task.id = next_id
    tasks.append(task)
    next_id += 1
    return task

@app.get("/tasks")
def get_tasks(user: str = Depends(get_current_user)):
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int, user: str = Depends(get_current_user)):
    for t in tasks:
        if t.id == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task, user: str = Depends(get_current_user)):
    for t in tasks:
        if t.id == task_id:
            t.title = updated_task.title
            t.description = updated_task.description
            t.completed = updated_task.completed
            return t
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, user: str = Depends(get_current_user)):
    for t in tasks:
        if t.id == task_id:
            tasks.remove(t)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
