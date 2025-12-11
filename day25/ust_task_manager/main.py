from fastapi import FastAPI, HTTPException, Depends, status  # Import FastAPI, HTTPException for error handling, Depends for dependency injection
from sqlalchemy.orm import Session  # Import SQLAlchemy session for database interaction
from models import Task, CreateTask, LoginRequest, Token, User, UserDB, TaskDB, Base  # Import models and database base class
from auth import create_access_token, get_current_user, ACCESS_TOKEN_EXPIRE_MINUTES  # Import authentication utilities
from database import get_db, engine  # Import database connection and engine
from mongodb_logger import log_action  # Import logging utility for MongoDB
from datetime import timedelta  # Import timedelta for setting expiration time of tokens

# Create the tables in the database using SQLAlchemy
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="UST Task Tracker")

# Endpoint for user login, returns an access token for authenticated users
@app.post("/login", response_model=Token)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    # Query user from database based on provided username
    user = db.query(UserDB).filter(UserDB.username == data.username).first()

    # Check if the user exists and if the password matches
    if not user or user.password != data.password:
        raise HTTPException(401, "Invalid username or password")  # Unauthorized if invalid

    # Generate JWT access token for the user
    token = create_access_token(
        subject=user.username,
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    # Return the token in a response
    return Token(access_token=token, token_type="bearer")

# Endpoint to get all tasks for the logged-in user
@app.get("/task", response_model=list[Task])
def get_all_tasks(
    current_user: User = Depends(get_current_user),  # Dependency to get the current logged-in user
    db: Session = Depends(get_db)  # Dependency to get a database session
):
    # Query user by username
    user = db.query(UserDB).filter(UserDB.username == current_user.username).first()

    # Get all tasks for the user
    tasks = db.query(TaskDB).filter(TaskDB.user_id == user.id).all()

    return tasks

# Endpoint to get a specific task by its ID for the logged-in user
@app.get("/task/{task_id}", response_model=Task)
def get_task_by_id(
    task_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Query user by username
    user = db.query(UserDB).filter(UserDB.username == current_user.username).first()

    # Query task by task ID and ensure it belongs to the current user
    task = db.query(TaskDB).filter(TaskDB.id == task_id, TaskDB.user_id == user.id).first()

    if not task:
        raise HTTPException(404, "Task not found")  # If task doesn't exist, return 404

    return task

# Endpoint to create a new task for the logged-in user
@app.post("/task", response_model=Task)
def create_task(
    task: CreateTask,  # Pydantic model to receive task data
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Query user by username
    user = db.query(UserDB).filter(UserDB.username == current_user.username).first()

    # Check if a task with the same title already exists for the user
    existing_task = db.query(TaskDB).filter(TaskDB.title == task.title, TaskDB.user_id == user.id).first()

    if existing_task:
        raise HTTPException(status_code=400, detail="Task with this title already exists")  # Raise an error if the task exists

    # Create a new task and assign it to the user
    new_task = TaskDB(
        title=task.title,
        description=task.description,
        completed=task.completed,
        user_id=user.id
    )

    # Add the task to the database and commit the changes
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    # Log the action in MongoDB
    log_action(user.username, "CREATE", new_task.id)

    return new_task

# Endpoint to update an existing task
@app.put("/task/{task_id}", response_model=Task)
def update_task(
    task_id: int,
    task: CreateTask,  # Pydantic model for updating task details
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Query user by username
    user = db.query(UserDB).filter(UserDB.username == current_user.username).first()

    # Check if the task exists and belongs to the current user
    existing = db.query(TaskDB).filter(TaskDB.id == task_id, TaskDB.user_id == user.id).first()
    if not existing:
        raise HTTPException(404, "Task not found")  # Raise an error if the task is not found

    # Update the task's details
    existing.title = task.title
    existing.description = task.description
    existing.completed = task.completed

    # Commit the changes to the database
    db.commit()
    db.refresh(existing)

    # Log the update action
    log_action(user.username, "UPDATE", task_id)

    return existing

# Endpoint to delete a task by its ID
@app.delete("/task/{task_id}")
def delete_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Query user by username
    user = db.query(UserDB).filter(UserDB.username == current_user.username).first()

    # Check if the task exists and belongs to the current user
    existing = db.query(TaskDB).filter(TaskDB.id == task_id, TaskDB.user_id == user.id).first()

    if not existing:
        raise HTTPException(404, "Task not found")  # Raise an error if the task is not found

    # Delete the task from the database
    db.delete(existing)
    db.commit()

    # Log the delete action
    log_action(user.username, "DELETE", task_id)

    return {"message": "Task Deleted Successfully"}  # Return a success message
