from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Task, TaskCreate, TaskUpdate, LoginRequest, Token, User
from auth import create_access_token, get_user
from utils import create_task, get_tasks, get_task, update_task, delete_task
from database import get_db

app = FastAPI(title="UST Task Manager Phase 2")

@app.post("/login", response_model=Token)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()
    if not user or user.password != data.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_access_token(subject=user.username)
    return Token(access_token=token, token_type="bearer")

@app.post("/tasks", response_model=Task)
def create_task_endpoint(task_data: TaskCreate, current_user: User = Depends(get_user), db: Session = Depends(get_db)):
    return create_task(db, task_data, current_user.id, current_user.username)

@app.get("/tasks", response_model=list[Task])
def get_tasks_endpoint(current_user: User = Depends(get_user), db: Session = Depends(get_db)):
    return get_tasks(db, current_user.id)

@app.get("/tasks/{task_id}", response_model=Task)
def get_task_endpoint(task_id: int, current_user: User = Depends(get_user), db: Session = Depends(get_db)):
    task = get_task(db, task_id, current_user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task_endpoint(task_id: int, task_data: TaskUpdate, current_user: User = Depends(get_user), db: Session = Depends(get_db)):
    task = update_task(db, task_id, task_data, current_user.id, current_user.username)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id: int, current_user: User = Depends(get_user), db: Session = Depends(get_db)):
    success = delete_task(db, task_id, current_user.id, current_user.username)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}