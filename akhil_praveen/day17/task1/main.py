from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel
from jose import JWTError, jwt
from model import CreateTask, TaskModel, tasks, id_list, UpdateTask, LoginRequest, User, Token
from auth import ALGORITHM, SECRET_KEY, create_access_token, get_current_user, DEMO_PASSWORD, DEMO_USERNAME, ACCESS_TOKEN_EXPIRE_MINUTES

# Initialize FastAPI app
app = FastAPI(title="UST Task Manager")

next_id = 1  # Variable to keep track of the next task ID

# Login endpoint to authenticate and return a JWT token
@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    # Check if the provided username and password match the demo credentials
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Username or Password")
    
    # Generate the access token with expiration time
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)
    
    # Return the JWT token
    return Token(access_token=token, token_type="bearer")


# Endpoint to add a new task (requires a valid JWT token)
@app.post("/task")
def add_task(task: CreateTask, current_user: User = Depends(get_current_user)):
    global next_id
    new_task = TaskModel(
        id=next_id,
        title=task.title,
        description=task.description
    )
    tasks.append(new_task)  # Append new task to the list of tasks
    id_list.append(next_id)  # Add task ID to the ID list
    next_id += 1  # Increment the task ID for the next task
    return new_task


# Get all tasks (requires a valid JWT token)
@app.get("/task")
def get_all_tasks(current_user: User = Depends(get_current_user)):
    return tasks  # Return the list of all tasks


# Get a task by its ID (requires a valid JWT token)
@app.get("/task/{id}")
def get_task_by_id(id: int, current_user: User = Depends(get_current_user)):
    if id not in id_list:
        raise HTTPException(status_code=404, detail="Task doesn't exist!")  # Task not found
    for data in tasks:
        if data.id == id:
            return data  # Return the task if found


# Update a task by its ID (requires a valid JWT token)
@app.put("/task/{id}")
def update_task(id: int, task: UpdateTask, current_user: User = Depends(get_current_user)):
    if id not in id_list:
        raise HTTPException(status_code=404, detail="Task doesn't exist!")  # Task not found
    for i in range(len(tasks)):
        if tasks[i].id == id:
            updated_task = TaskModel(id=id,
                                     title=task.title,
                                     description=task.description,
                                     completed=task.completed)
            tasks[i] = updated_task  # Update the task
            return updated_task  # Return the updated task


# Delete a task by its ID (requires a valid JWT token)
@app.delete("/task/{id}")
def delete_profile(id: int, current_user: User = Depends(get_current_user)):
    if id not in id_list:
        raise HTTPException(status_code=404, detail="Task Not Found")  # Task not found
    for i in range(len(tasks)):
        if tasks[i].id == id:
            removed = tasks.pop(i)  # Remove the task from the list
            id_list.remove(id)  # Remove the ID from the ID list
            return removed  # Return the removed task


# Sample Output

"""
Sample Output for /login (POST):
Input:
{
    "username": "demo_user",
    "password": "demo_password"
}
Output:
{
    "access_token": "some_jwt_token",
    "token_type": "bearer"
}

Sample Output for /task (POST):
Input:
{
    "title": "Task 1",
    "description": "Description of Task 1"
}
Output:
{
    "id": 1,
    "title": "Task 1",
    "description": "Description of Task 1",
    "completed": false
}

Sample Output for /task (GET):
Input:
Authorization: Bearer <some_jwt_token>
Output:
[
    {
        "id": 1,
        "title": "Task 1",
        "description": "Description of Task 1",
        "completed": false
    },
    {
        "id": 2,
        "title": "Task 2",
        "description": "Description of Task 2",
        "completed": false
    }
]

Sample Output for /task/{id} (GET):
Input:
Authorization: Bearer <some_jwt_token>
Output:
{
    "id": 1,
    "title": "Task 1",
    "description": "Description of Task 1",
    "completed": false
}

Sample Output for /task/{id} (GET) with invalid ID:
Input:
Authorization: Bearer <some_jwt_token>
Output:
{
    "detail": "Task doesn't exist!"
}

Sample Output for /task/{id} (PUT):
Input:
{
    "title": "Updated Task 1",
    "description": "Updated Description of Task 1",
    "completed": true
}
Output:
{
    "id": 1,
    "title": "Updated Task 1",
    "description": "Updated Description of Task 1",
    "completed": true
}

Sample Output for /task/{id} (DELETE):
Input:
Authorization: Bearer <some_jwt_token>
Output:
{
    "id": 1,
    "title": "Task 1",
    "description": "Description of Task 1",
    "completed": false
}
"""
