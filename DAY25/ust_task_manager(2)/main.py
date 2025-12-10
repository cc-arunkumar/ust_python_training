from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List

from database import get_db, engine, Base
from models import Task, TaskCreate, TaskUpdate, TaskResponse, User
from auth import get_current_user, authenticate_user, create_access_token
from mongodb_logger import log_activity

app = FastAPI(title="UST Task Manager - Phase 2")

# Create tables + default user
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    db: Session = next(get_db())
    if not db.query(User).filter(User.username == "rahul").first():
        db.add(User(username="rahul", password="password123"))
        db.commit()
        print("Created default user: rahul / password123")

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_task = Task(**task.dict(), user_id=current_user.id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    log_activity(current_user.username, "CREATE", db_task.id)
    return db_task

@app.get("/tasks", response_model=List[TaskResponse])
def get_tasks(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Task).filter(Task.user_id == current_user.id).all()

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    update_data = task_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)
    
    db.commit()
    db.refresh(task)
    log_activity(current_user.username, "UPDATE", task.id)
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    log_activity(current_user.username, "DELETE", task.id)
    return {"message": "Task deleted successfully"}


"""from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import List
from auth import authenticate_user, create_access_token, verify_token
from models import TaskCreate, TaskUpdate, Task
from utils import tasks, get_next_task_id

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# ------------------- LOGIN -------------------
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_access_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}


# ------------------- AUTH DEPENDENCY -------------------
def get_current_user(token: str = Depends(oauth2_scheme)):
    return verify_token(token)


# ------------------- CREATE TASK -------------------
@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate, user: dict = Depends(get_current_user)):
    task_id = get_next_task_id()
    new_task = {
        "id": task_id,
        "title": task.title,
        "description": task.description,
        "completed": False
    }
    tasks.append(new_task)
    return new_task


# ------------------- GET ALL TASKS -------------------
@app.get("/tasks", response_model=List[Task])
def get_all_tasks(user: dict = Depends(get_current_user)):
    return tasks


# ------------------- GET SINGLE TASK -------------------
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int, user: dict = Depends(get_current_user)):
    for t in tasks:
        if t["id"] == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task not found")


# ------------------- UPDATE TASK -------------------
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: TaskUpdate, user: dict = Depends(get_current_user)):
    for t in tasks:
        if t["id"] == task_id:
            t["title"] = updated_task.title
            t["description"] = updated_task.description
            t["completed"] = updated_task.completed
            return t

    raise HTTPException(status_code=404, detail="Task not found")


# ------------------- DELETE TASK -------------------
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, user: dict = Depends(get_current_user)):
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            return {"message": "Task deleted successfully"}

    raise HTTPException(status_code=404, detail="Task not found")


"""