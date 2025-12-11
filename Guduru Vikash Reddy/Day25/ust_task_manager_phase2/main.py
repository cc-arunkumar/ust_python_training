# Main.py
from sqlalchemy.orm import Session
from database import SessionLocal, User, get_all_tasks, get_task_by_id, update_task, delete_task, create_task
from auth import create_access_token, get_curr_user
from fastapi import FastAPI, HTTPException, Depends, status
from models import TaskResponse, LoginRequest, Token, TaskModel, TaskPost
from datetime import timedelta
from typing import List
from mongo_db_loggers import mongodb_logs

# Initialize FastAPI app with a title
app = FastAPI(title="Task Tracker API")

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db  # Yield the session to the route function
    finally:
        db.close()  # Close the session after the operation

# Token expiration time (30 minutes)
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Login endpoint to authenticate user and return JWT token
@app.post("/login", response_model=Token)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    # Validate user credentials from the database
    user = db.query(User).filter(User.username == data.username).first()
    if not user or user.password != data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    if not data.username or not data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username and password are required"
        )

    # Set token expiration time
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # Create the access token
    token = create_access_token(subject=data.username, expires_delta=expires)

    return Token(access_token=token, token_type="bearer")  # Return the generated token

# Endpoint to fetch current authenticated user's details
@app.get("/me")
def read_me(current_user: User = Depends(get_curr_user)):
    return {
        "message": "This is a protected JWT token route.",
        "username": current_user.username,
    }

# Endpoint to create a new task for the authenticated user
@app.post("/tasks", response_model=TaskResponse)
def create_task_endpoint(new_task: TaskModel, current_user: User = Depends(get_curr_user)):
    # Create the task and associate it with the current user
    task = create_task(new_task.title, new_task.description, current_user.id, completed=False)
    if not task:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Task creation failed")

    # Log the task creation in MongoDB (logging system)
    mongodb_logs(current_user.username, "CREATE", task.id)
    return task  # Return the created task

# Endpoint to get all tasks assigned to the authenticated user
@app.get("/tasks", response_model=List[TaskResponse])
def get_all_tasks_endpoint(current_user: User = Depends(get_curr_user)):
    tasks = get_all_tasks(current_user.id)  # Fetch all tasks for the user
    return tasks or []  # Return an empty list if no tasks found

# Endpoint to fetch a specific task by its ID
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task_endpoint(task_id: int, current_user: User = Depends(get_curr_user)):
    task = get_task_by_id(task_id, current_user.id)  # Fetch the task by ID and user
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task  # Return the found task

# Endpoint to update a specific task by task ID
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task_endpoint(task_id: int, updated_task: TaskPost, current_user: User = Depends(get_curr_user)):
    # Update the task with new data
    task = update_task(task_id, updated_task.title, updated_task.description, updated_task.completed, current_user.id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found or update failed")

    # Log the task update action in MongoDB (logging system)
    mongodb_logs(current_user.username, "UPDATE", task.id)
    return task  # Return the updated task

# Endpoint to delete a task by its ID
@app.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id: int, current_user: User = Depends(get_curr_user)):
    # Delete the task by ID
    deleted_data = delete_task(task_id, current_user.id)
    if not deleted_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found or delete failed")

    # Log the task deletion action in MongoDB (logging system)
    mongodb_logs(current_user.username, "DELETE", task_id)
    return {"message": "Task deleted successfully"}  
