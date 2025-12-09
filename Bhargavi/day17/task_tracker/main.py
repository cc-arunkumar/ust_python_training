# UST Task Manager
# Project: Task Tracker API(Phase 1)
# Tech Stack: FastAPI + Python
# Security: JWT authentication (HS256)
# Data Storage: In-Memory Lists Only (No DB)
# Goal: Build a secure backend API that manages tasks.
# 1.Project Overview
# You will build a JWT-secured Task Tracker API with the following modules:
# 1. User Login API → Returns JWT token
# 2. Task CRUD API (Create, Read, Update, Delete) → Requires JWT
# 3. In-memory data storage → No database
# 4. Input validation using Pydantic models
# This API will be used later as the backend for a frontend app.
# This is Phase 1, so we focus only on backend basics.
# 2.Mandatory Rules
# All participants must follow these exact instructions:
# ✔ Same endpoints
# ✔ Same request & response format
# UST Task Manager 1
# ✔ Same field names
# ✔ Same in-memory storage structure
# ✔ Same sample Indian context data
# ✔ No advanced features
# ✔ No additional libraries except fastapi , uvicorn , python-jose
# ✔ Code must run with uvicorn main:app --reload
# 3.Directory Structure
# project/
# │── main.py
# │── models.py
# │── auth.py
# │── utils.py
# 4.API Requirements
# 4.1 User Authentication
# We will hardcode one user.
# Hardcoded User
# users = {
#  "rahul": {
#  "username": "rahul",
#  "password": "password123" # store as plain text for this assignment onl
# y
# UST Task Manager 2
#  }
# }
# Login Endpoint
# POST /login
# Request Body
# {
#  "username": "rahul",
#  "password": "password123"
# }
# Response (JWT Token)
# {
#  "access_token": "<jwt_token_here>",
#  "token_type": "bearer"
# }
# Login is the only endpoint that does not need JWT.
# 4.2 Task Model
# Each task will contain:
# Field Type Example
# id int auto-increment (1,2,3…)
# title str "Pay Electricity Bill"
# description str "Pay BESCOM bill before due date"
# completed bool False
# UST Task Manager 3
# 4.3 Store Tasks in Memory
# Use a Python list:
# tasks = []
# 5.CRUD Endpoints
# 5.1 Create Task
# POST /tasks
# Request Body
# {
#  "title": "Buy groceries",
#  "description": "Buy rice and dal from D-Mart"
# }
# Response
# {
#  "id": 1,
#  "title": "Buy groceries",
#  "description": "Buy rice and dal from D-Mart",
#  "completed": false
# }
# 5.2 Get All Tasks
# GET /tasks
# UST Task Manager 4
# Response Example
# [
#  {
#  "id": 1,
#  "title": "Buy groceries",
#  "description": "Buy rice and dal from D-Mart",
#  "completed": false
#  },
#  {
#  "id": 2,
#  "title": "Pay Electricity Bill",
#  "description": "Pay BESCOM bill before 15th",
#  "completed": true
#  }
# ]
# 5.3 Get Single Task
# GET /tasks/{task_id}
# Response Example
# {
#  "id": 1,
#  "title": "Buy groceries",
#  "description": "Buy rice and dal from D-Mart",
#  "completed": false
# }
# If task doesn't exist → return:
# {"detail": "Task not found"}
# UST Task Manager 5
# 5.4 Update Task
# PUT /tasks/{task_id}
# Request Body (full update)
# {
#  "title": "Buy vegetables",
#  "description": "Buy tomatoes from Reliance Fresh",
#  "completed": true
# }
# Response
# {
#  "id": 1,
#  "title": "Buy vegetables",
#  "description": "Buy tomatoes from Reliance Fresh",
#  "completed": true
# }
# 5.5 Delete Task
# DELETE /tasks/{task_id}
# Response
# {"message": "Task deleted successfully"}
# 6.JWT Requirements
# UST Task Manager 6
# Algorithm: HS256
# Secret Key:
# SECRET_KEY = "UST-TaskTracker-Secret"
# Expiry: 30 minutes
# 7.Authentication Rule
# Every endpoint except POST /login must include:
# Authorization: Bearer <token>
# If missing or invalid → return:
# {"detail": "Could not validate credentials"}
# 8.Sample Inputs & Outputs (Cover all
# scenarios)
# ✅ Scenario 1: Successful Login
# Input
# {
#  "username": "rahul",
#  "password": "password123"
# }
# Output
# UST Task Manager 7
# {
#  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
#  "token_type": "bearer"
# }
# ❌ Scenario 2: Login Failure
# Input
# {
#  "username": "rahul",
#  "password": "wrongpass"
# }
# Output
# {"detail": "Invalid username or password"}
# ✅ Scenario 3: Create Task
# Input
# {
#  "title": "Book train tickets",
#  "description": "Book IRCTC tickets to Chennai"
# }
# Output
# {
#  "id": 1,
#  "title": "Book train tickets",
# UST Task Manager 8
#  "description": "Book IRCTC tickets to Chennai",
#  "completed": false
# }
# ❌ Scenario 4: Create Task with Missing Title
# Input
# {
#  "description": "Something"
# }
# Output
# {
#  "detail": [
#  {
#  "loc": ["body", "title"],
#  "msg": "field required",
#  "type": "value_error.missing"
#  }
#  ]
# }
# ✅ Scenario 5: Update Task
# Input
# {
#  "title": "Pay Water Bill",
#  "description": "Pay BWSSB bill",
# UST Task Manager 9
#  "completed": true
# }
# Output
# {
#  "id": 1,
#  "title": "Pay Water Bill",
#  "description": "Pay BWSSB bill",
#  "completed": true
# }
# ❌ Scenario 6: Get Non-Existing Task
# Response
# {"detail": "Task not found"}
# ❌ Scenario 7: Delete Non-Existing Task
# Response
# {"detail": "Task not found"}
# 9.What Your Final Submission Must
# Contain
# ✔ main.py
# ✔ models.py
# ✔ auth.py
# UST Task Manager 10
# ✔ utils.py
# ✔ A word document containing screenshots of all REQ/RESP from Swagger Docs
# ✔ Should run using:
# uvicorn main:app --reload
# 10.TEST CASESWITH INPUT + EXPECTED
# OUTPUT
# SECTION 1 — LOGIN API TEST CASES
# 1.1 Successful Login
# Input
# POST /login
# {
#  "username": "rahul",
#  "password": "password123"
# }
# Expected Output
# {
#  "access_token": "<valid_jwt_token>",
#  "token_type": "bearer"
# }
# 1.2 Login –Wrong Password
# UST Task Manager 11
# Input
# POST /login
# {
#  "username": "rahul",
#  "password": "wrongpass"
# }
# Expected Output
# {"detail": "Invalid username or password"}
# 1.3 Login –Wrong Username
# Input
# POST /login
# {
#  "username": "suresh",
#  "password": "password123"
# }
# Expected Output
# {"detail": "Invalid username or password"}
# 1.4 Login – Missing Username
# Input
# POST /login
# {
# UST Task Manager 12
#  "password": "password123"
# }
# Expected Output
# {
#  "detail": [
#  {
#  "loc": ["body", "username"],
#  "msg": "field required",
#  "type": "value_error.missing"
#  }
#  ]
# }


from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from models import Task, TaskInResponse, TaskCreate, TaskUpdate, LoginRequest
from auth import create_access_token
from utils import get_current_user, get_task_by_id
from datetime import timedelta
 
app = FastAPI()
 
# In-memory storage for tasks and hardcoded users
tasks = []
next_task_id = 1
 
users = {
    "rahul": {
        "username": "rahul",
        "password": "password123"
    }
}
 
# POST /login: User login and JWT token generation
@app.post("/login")
async def login(request: LoginRequest):
    user = users.get(request.username)
    if not user or user['password'] != request.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
   
    access_token = create_access_token(subject=request.username)
    return {"access_token": access_token, "token_type": "bearer"}
 
# POST /tasks: Create a new task
@app.post("/tasks", response_model=TaskInResponse)
async def create_task(task: TaskCreate, current_user: str = Depends(get_current_user)):
    global next_task_id
    task_data = task.dict()
    task_data["id"] = next_task_id
    tasks.append(task_data)
    next_task_id += 1
    return task_data
 
# GET /tasks: Get all tasks
@app.get("/tasks", response_model=List[TaskInResponse])
async def get_all_tasks(current_user: str = Depends(get_current_user)):
    return tasks
 
# GET /tasks/{task_id}: Get a specific task
@app.get("/tasks/{task_id}", response_model=TaskInResponse)
async def get_task(task_id: int, current_user: str = Depends(get_current_user)):
    task = get_task_by_id(task_id, tasks)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
 
# PUT /tasks/{task_id}: Update an existing task
@app.put("/tasks/{task_id}", response_model=TaskInResponse)
async def update_task(task_id: int, task: TaskUpdate, current_user: str = Depends(get_current_user)):
    task_to_update = get_task_by_id(task_id, tasks)
    if not task_to_update:
        raise HTTPException(status_code=404, detail="Task not found")
   
    updated_task = task_to_update.copy()
    updated_task.update(task.dict(exclude_unset=True))
    tasks[tasks.index(task_to_update)] = updated_task
    return updated_task
 
# DELETE /tasks/{task_id}: Delete a task
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int, current_user: str = Depends(get_current_user)):
    task_to_delete = get_task_by_id(task_id, tasks)
    if not task_to_delete:
        raise HTTPException(status_code=404, detail="Task not found")
   
    tasks.remove(task_to_delete)
    return {"message": "Task deleted successfully"}
 
 