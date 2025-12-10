from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from models import Task, User, TaskCreate, TaskUpdate, TaskResponse, LoginRequest, Token
from auth import create_access_token, get_user
from database import get_db
from sqlalchemy.exc import SQLAlchemyError
from mongo_logger import log_activity

app = FastAPI(title="Talent Management System")

# Login route (returns token for authenticated user)
@app.post("/login", response_model=Token)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()
    if not user or user.password != data.password:  
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_access_token(subject=data.username)
    return Token(access_token=token, token_type="bearer")


# Create a new task for the authenticated user
@app.post("/tasks", response_model=TaskResponse)
def add_task(task: TaskCreate, db: Session = Depends(get_db), current_user: str = Depends(get_user)):
    if not isinstance(current_user, str):
        raise HTTPException(status_code=400, detail="Invalid user data")
    
    # Query user based on the username string (current_user)
    user = db.query(User).filter(User.username == current_user).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    new_task = Task(**task.dict(), user_id=user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    log_activity(current_user, "CREATE", new_task.id)
    
    return new_task  

# Get all tasks for the authenticated user
@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db), current_user: str = Depends(get_user)):
    user = db.query(User).filter(User.username == current_user).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    tasks = db.query(Task).filter(Task.user_id == user.id).all()
    return tasks


# Get a specific task by task_id for the authenticated user
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_user)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task and task.user_id == db.query(User).filter(User.username == current_user).first().id:
        return task  
    
    raise HTTPException(status_code=404, detail="Task not found or unauthorized")

# Update an existing task
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db), current_user: str = Depends(get_user)):
    # Query the task and ensure it belongs to the user
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task or db_task.user_id != db.query(User).filter(User.username == current_user).first().id:
        raise HTTPException(status_code=404, detail="Task not found or unauthorized")
    
    db_task.title = task.title
    db_task.description = task.description
    db_task.completed = task.completed
    db.commit()
    db.refresh(db_task)
    
    log_activity(current_user, "UPDATE", db_task.id)
    
    return db_task  

# Delete a task for the authenticated user
@app.delete("/tasks/{task_id}", status_code=200)
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_user)):
    # Query the task and ensure it belongs to the user
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task or db_task.user_id != db.query(User).filter(User.username == current_user).first().id:
        raise HTTPException(status_code=404, detail="Task not found or unauthorized")
    
    db.delete(db_task)
    db.commit()
    
    log_activity(current_user, "DELETE", task_id)
    
    return {"detail": "Task deleted successfully"}
