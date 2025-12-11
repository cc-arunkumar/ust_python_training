# Import necessary modules from FastAPI and other dependencies
from fastapi import FastAPI, HTTPException, status, Depends
from typing import List
from auth import create_access_token, get_user  # Functions for token creation and user verification
from sqlalchemy.orm import Session  # Session for interacting with the database
from database import get_db, UserDB, TaskDB  # Database access and models
from models import TaskCreate, TaskUpdate, TaskResponse, Token, LoginRequest  # Request and response models
import mongodb_logger  # Logger for MongoDB activity

# Initialize FastAPI application with a title
app = FastAPI(title="Task Tracker API")

# Endpoint for user login, returns a token if credentials are valid
@app.post("/login", response_model=Token)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    # Fetch the user from the database based on the username
    user = db.query(UserDB).filter(UserDB.username == request.username).first()
    # Validate the user’s password
    if not user or user.password != request.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    # Create an access token for the user
    token = create_access_token(subject=request.username)
    # Return the token as a response
    return Token(access_token=token, token_type="bearer")

# Endpoint to create a new task
@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: UserDB = Depends(get_user)):
    # Create a new task in the database
    db_task = TaskDB(title=task.title, description=task.description, completed=False, user_id=current_user.id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    # Log the activity of task creation to MongoDB
    mongodb_logger.log_activity(current_user.username, "CREATE", db_task.id)
    # Return the created task as a response
    return db_task

# Endpoint to fetch all tasks for the current user
@app.get("/tasks", response_model=List[TaskResponse])
def get_all_tasks(db: Session = Depends(get_db), current_user: UserDB = Depends(get_user)):
    # Query the database for tasks assigned to the current user
    tasks = db.query(TaskDB).filter(TaskDB.user_id == current_user.id).all()
    # Return the list of tasks
    return tasks

# Endpoint to fetch a specific task by its ID
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task_by_id(task_id: int, db: Session = Depends(get_db), current_user: UserDB = Depends(get_user)):
    # Query the database for the task by ID and user
    task = db.query(TaskDB).filter(TaskDB.id == task_id, TaskDB.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    # Return the task if found
    return task

# Endpoint to update a task by its ID
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db), current_user: UserDB = Depends(get_user)):
    # Fetch the task to update
    db_task = db.query(TaskDB).filter(TaskDB.id == task_id, TaskDB.user_id == current_user.id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # Update task fields if provided
    if task.title is not None:
        db_task.title = task.title
    if task.description is not None:
        db_task.description = task.description
    if task.completed is not None:
        db_task.completed = task.completed
    
    # Commit the changes to the database
    db.commit()
    db.refresh(db_task)
    # Log the activity of task update to MongoDB
    mongodb_logger.log_activity(current_user.username, "UPDATE", db_task.id)
    # Return the updated task as a response
    return db_task

# Endpoint to delete a task by its ID
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: UserDB = Depends(get_user)):
    # Fetch the task to delete
    db_task = db.query(TaskDB).filter(TaskDB.id == task_id, TaskDB.user_id == current_user.id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # Delete the task from the database
    db.delete(db_task)
    db.commit()
    # Log the activity of task deletion to MongoDB
    mongodb_logger.log_activity(current_user.username, "DELETE", task_id)
    # Return a success message
    return {"detail": "Task deleted"}
