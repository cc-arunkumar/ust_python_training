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
