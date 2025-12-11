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
# Requirements:
# Create a users table in MySQL
# Store one default user:
# username: rahul
# password: password123 (plain text allowed for assignment)
# Login endpoint must now validate credentials against this database
# No new fields should be added to the API response
# To the outside world → login works exactly the same
# Internally → switch from dictionary → SQLAlchemy MySQL query
# 3.2 Persist Tasks in MySQL Instead of InMemory List
# Replace:
# UST Task Manager – Phase 2 6
# tasks = []
# with a SQLAlchemy ORM table named tasks.
# Requirements:
# All Create, Read, Update, Delete operations must use MySQL
# IDs must remain auto-incremented integers
# Each task must belong to a user ( user_id foreign key)
# Only the authenticated user's tasks should be visible
# Behavior to preserve:
# Error messages identical
# Returned fields identical
# Success messages identical
# 3.3 Enforce User-Specific Task Ownership
# Phase 1 allowed multiple users in theory, but no DB existed.
# Phase 2 introduces real user scoping:
# Rule:
# A logged-in user can only create, read, update, or delete their own tasks.
# This means:
# GET /tasks → returns only this user’s tasks
# GET /tasks/{task_id} → must check user matches
# PUT /tasks/{task_id} → must check user matches
# DELETE /tasks/{task_id} → must check user matches
# If task belongs to another user → return:
# UST Task Manager – Phase 2 7
# {"detail": "Task not found"}
# (Do not reveal existence of others’ tasks.)
# 3.4 Additional: Log User Activity in
# MongoDB
# Each activity log document should include:
# username
# action (CREATE, UPDATE, DELETE)
# task_id
# timestamp
# Log the following:
# When user creates a task
# When user updates a task
# When user deletes a task
# Do NOT log:
# GET requests
# Login requests
# Important rule:
# Logging failures in MongoDB must NEVER break the API
# (This simulates real enterprise non-critical logging systems.)
# 4. New Responsibilities for participants
# UST Task Manager – Phase 2 8
# 4.1 Install MySQL + create database
# participants must create:
# ust_task_manager_db
# 4.2 Add SQLAlchemy ORM with MySQL connection
# Create new file database.py
# Set up engine + session
# Create Base ORM model
# 4.3 Implement User ORM model
# 4.4 Implement Task ORM model
# 4.5 Replace all in-memory logic with DB operations
# 4.6 Implement MongoDB logging
# 4.7 Test all Phase 1 test cases again
# All response formats MUST match Phase 1.
# 5. What Must Be Delivered
# participants must submit:
# Word/PDF with Swagger screenshots of ALL test cases
# MySQL database export
# Project folder containing:
# main.py
# models.py
# auth.py
# utils.py
# UST Task Manager – Phase 2 9
# database.py (NEW)
# mongodb_logger.py
# API must run with:
# uvicorn main:app --reload
# All Phase 1 tests must pass unchange
from datetime import timedelta
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from jose import JWTError, jwt
from auth import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, get_current_user
from models import LoginRequest, Token, User, Taskmodelcreate, TaskModel
from my_sqldb_conn import (
    get_all_users,
    create_tasks,
    get_all_tasks,
    get_task_by_id,
    delete_task_by_id,
    update_task_by_id
)
from mongo_connection import log, Logger

# Initialize FastAPI app
app = FastAPI(title="UST TASK MANAGER PHASE 2")

# Fetch all user details from SQL database
user_details = get_all_users()

@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    """
    Authenticate user and generate JWT token.
    """
    for row in user_details:
        if data.username != row.username or data.password != row.password:
            # Invalid credentials
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password"
            )
    # Set token expiry time
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # Generate JWT token
    token = create_access_token(subject=data.username, expires_delta=expires)
    return Token(access_token=token, token_type="bearer")


@app.post("/tasks")
def create_task(task: Taskmodelcreate, current_user: User = Depends(get_current_user)):
    """
    Create a new task for the authenticated user.
    """
    try:
        tasks = TaskModel(
            title=task.title,
            description=task.description,
            completed=False
        )
        new_task = create_tasks(tasks, current_user.username)

        # Log the action in MongoDB
        log.insert_one(Logger(
            username=current_user.username,
            action="CREATE",
            task_id=new_task.id
        ).__dict__)

        return new_task
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating task: {str(e)}"
        )


@app.get("/tasks")
def get_tasks(current_user: User = Depends(get_current_user)):
    """
    Retrieve all tasks for the authenticated user.
    """
    try:
        return get_all_tasks(current_user.username)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching tasks: {str(e)}"
        )


@app.get("/tasks/{task_id}")
def get_task(task_id: int, current_user: User = Depends(get_current_user)):
    """
    Retrieve a specific task by ID.
    """
    try:
        task = get_task_by_id(task_id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )
        return task
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching task: {str(e)}"
        )


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Taskmodelcreate, current_user: User = Depends(get_current_user)):
    """
    Update a specific task by ID.
    """
    try:
        updated_task = update_task_by_id(task_id, task, current_user.username)
        if not updated_task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        # Log the update action
        log.insert_one(Logger(
            username=current_user.username,
            action="UPDATE",
            task_id=task_id
        ).__dict__)

        return updated_task
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating task: {str(e)}"
        )


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, current_user: User = Depends(get_current_user)):
    """
    Delete a specific task by ID.
    """
    try:
        deleted = delete_task_by_id(task_id, current_user.username)
        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        # Log the delete action
        log.insert_one(Logger(
            username=current_user.username,
            action="DELETE",
            task_id=task_id
        ).__dict__)

        return {"message": "Deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting task: {str(e)}"
        )
