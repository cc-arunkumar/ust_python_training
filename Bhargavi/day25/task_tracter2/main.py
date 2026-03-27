# UST Task Manager – Phase 2
# (Extended Project Requirement – Database Integration)
# Document Type: Requirement Specification
# Audience: UST Employees
# Prerequisites: Completed Phase 1 (In-Memory Task Tracker)

# 1. Objective of Phase 2
# Phase 1 introduced a basic Task Tracker API using:
# FastAPI
# JWT security
# In-memory storage ( tasks = [] )
# Hardcoded user authentication
# Phase 2 upgrades the backend to use persistent storage with MySQL and
# MongoDB for activity logging — but without changing ANY of the external API
# behavior.

# This simulates how real enterprise systems evolve:
# → First build functionality → then plug in databases while keeping the API stable.
# 2. What Must NOT Change (100% SAME as
# Phase 1)
# This is extremely important.
# In Phase 2, the internal implementation changes, but the API behavior must
# remain EXACTLY the same, so that the frontend (or automated tests) never break.
# Below is a detailed explanation of each item.
# UST Task Manager – Phase 2 1

# 2.1 Same Endpoints
# You must NOT add / remove / rename any API routes.
# Still required:
# Authentication
# POST /login
# Task Operations
# POST /tasks
# GET /tasks
# GET /tasks/{task_id}
# PUT /tasks/{task_id}
# DELETE /tasks/{task_id}

# Why:
# The frontend team or automated testers expect these exact endpoints. Backend
# internal changes must never break clients.
# 2.2 Same Request & Response Format
# All JSON inputs and outputs must match Phase 1 EXACTLY, including:
# Field names
# Field types
# Field presence
# Error messages
# Error structure
# Ordering (as much as possible)
# Example — Create Task response must still return:

# UST Task Manager – Phase 2 2
# {
#  "id": 1,
#  "title": "...",
#  "description": "...",
#  "completed": false
# }
# Why:

# In enterprise projects, API contracts must remain stable even when backend
# technology changes (in-memory → DB).
# 2.3 Same Directory Structure
# Your folder structure must NOT change.
# project/
# │── main.py
# │── models.py
# │── auth.py
# │── utils.py
# You may ADD new files (e.g., database.py), but existing file names must remain
# unchanged because:
# Trainers will evaluate based on this structure
# Auto-testing scripts may import these modules
# participants must follow consistent learning design
# 2.4 Same JWT Mechanism
# JWT token creation, verification, and error handling must remain:
# Algorithm: HS256
# Secret key: "UST-TaskTracker-Secret"
# UST Task Manager – Phase 2 3
# Expiry: 30 minutes
# Token returned as:
# {
#  "access_token": "xxxx",
#  "token_type": "bearer"
# }
# Why:
# Changing JWT logic would invalidate all Phase 1 tests.
# 2.5 Same Pydantic Models
# Your input validation using Pydantic must remain unchanged.
# Examples:
# Create Task Input Model
# Fields required:
# title : str
# description : str
# Update Task Input Model
# Same fields:
# title
# description
# completed
# Why:
# The API must validate data the same way as before.
# 2.6 Same Swagger Testing
# UST Task Manager – Phase 2 4
# When participants open:
# http://127.0.0.1:8000/docs
# They must see:
# Exact same endpoint list
# Exact same input body examples
# Exact same error messages
# Exact same responses
# JWT authorization option on each protected endpoint
# Why:
# The training assignment requires testing all scenarios from the existing
# document.
# 2.7 Same User Login Flow
# In Phase 1:
# The user "rahul" and password "password123" were hardcoded.
# In Phase 2, they will be stored in MySQL.
# But the login behavior must remain identical:
# Valid login
# Should return JWT.
# Invalid login
# Should return:
# {"detail": "Invalid username or password"}
# Why:
# UST Task Manager – Phase 2 5
# External behavior cannot change. Only backend implementation shifts to a
# database.
# 3. What MUST Change in Phase 2
# This is the actual new work participants must do.
# 3.1 Migrate Users to MySQL
# Instead of:
# users = {"rahul": {...}}
# You will now store users in MySQL.

from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from models import Task, User, TaskCreate, TaskUpdate, TaskResponse, LoginRequest, Token
from auth import create_access_token, get_user
from database import get_db
from sqlalchemy.exc import SQLAlchemyError
from mongodb_logger import log_activity

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