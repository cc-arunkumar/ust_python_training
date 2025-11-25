from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import List
from models import Task, TaskIn, User, LoginRequest, Token
from auth import create_jwt_token, verify_jwt_token
from utils import tasks, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta

app = FastAPI()

# HTTPBearer for Authorization: Bearer <token>
security = HTTPBearer()

# Hardcoded user credentials
users = {
    "rahul": {
        "username": "rahul",
        "password": "password123"  # store as plain text for this assignment only
    }
}

# /login endpoint -> returns JWT token
@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    user = users.get(data.username)
    if not user or user["password"] != data.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_jwt_token(subject=data.username, expires_delta=expires)
    return Token(access_token=token, token_type="bearer")


# Helper function to decode and verify token
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials  # Extract token only
    try:
        payload = verify_jwt_token(token)  # Decode and verify token
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    
    username = payload.get("sub")  # Extract the username from the token's 'sub' claim
    
    # Check if the username exists in the users dictionary
    if username not in users:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    
    return User(username=username)


# Create Task
@app.post("/tasks", response_model=Task)
def create_task(task: TaskIn, current_user: User = Depends(get_current_user)):
    task_id = len(tasks) + 1
    new_task = Task(id=task_id, **task.dict())
    tasks.append(new_task)
    return new_task


# Get All Tasks
@app.get("/tasks", response_model=List[Task])
def get_tasks(current_user: User = Depends(get_current_user)):
    return tasks


# Get a Single Task
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int, current_user: User = Depends(get_current_user)):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


# Update Task
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskIn, current_user: User = Depends(get_current_user)):
    for existing_task in tasks:
        if existing_task.id == task_id:
            existing_task.title = task.title
            existing_task.description = task.description
            existing_task.completed = task.completed
            return existing_task
    raise HTTPException(status_code=404, detail="Task not found")


# Delete Task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, current_user: User = Depends(get_current_user)):
    for existing_task in tasks:
        if existing_task.id == task_id:
            tasks.remove(existing_task)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")

#sample output:
# Scenario 1: Successful Login
# Input
# {
#   "username": "rahul",
#   "password": "password123"
# }
# output
# Response body
# {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJyYWh1bCIsImV4cCI6MTc2NDA0ODU2OX0.lzmHa0QF7S13Hxd_6f91n0XbBEBA9p3R1gKyQhT2XFg",
#   "token_type": "bearer"
# }

# 1.2 Login –Wrong Password
# Request body
# {
#   "username": "rahul",
#   "password": "wrongpass"
# }

# Response body

# {
#   "detail": "Incorrect username or password"
# }
# 1.3 Login –Wrong Username
# Request body
# {
#   "username": "suresh",
#   "password": "password123"
# }
# Response body
# {
#   "detail": "Incorrect username or password"
# }
# 1.4 Login – Missing Username
# Request body
# {
#   "password": "password123"
# }
	

# Error: Unprocessable Content
# Response body

# {
#   "detail": [
#     {
#       "type": "missing",
#       "loc": [
#         "body",
#         "username"
#       ],
#       "msg": "Field required",
#       "input": {
#         "password": "password123"
#       }
#     }
#   ]
# }
#  2.1 Create Task – Valid
# Request body
# {
#   "title": "Buy Milk",
#   "description": "Buy Nandini milk from nearby shop",
#   "completed": false
# }
	
# Response body

# {
#   "title": "Buy Milk",
#   "description": "Buy Nandini milk from nearby shop",
#   "completed": false,
#   "id": 1
# }
# 2.2 Create Task –With Long Description
# Request body
# {
#   "title": "Apply PAN Card",
#   "description": "Visit NSDL center in Bangalore and submit documents",
#   "completed": false
# }
	
# Response body

# {
#   "title": "Apply PAN Card",
#   "description": "Visit NSDL center in Bangalore and submit documents",
#   "completed": false,
#   "id": 2
# }
# 2.3 Create Task – Missing Title
# Request body
# POST /tasks
# {
#  "description": "Pay LIC premium"
# }
# Response body

# {
#   "detail": [
#     {
#       "type": "json_invalid",
#       "loc": [
#         "body",
#         0
#       ],
#       "msg": "JSON decode error",
#       "input": {},
#       "ctx": {
#         "error": "Expecting value"
#       }
#     }
#   ]
# }
# 2.4 Create Task – Missing Description
# Request body
# {
#  "title": "Pay Broadband Bill"
# }
# Response body

# {
#   "detail": [
#     {
#       "type": "missing",
#       "loc": [
#         "body",
#         "description"
#       ],
#       "msg": "Field required",
#       "input": {
#         "title": "Pay Broadband Bill"
#       }
#     }
#   ]
# }
# 2.5 Create Task – Empty Fields
# request body:
# {
#   "title": "",
#   "description": "",
#   "completed": false
# }
	
# Response body
# {
#   "title": "",
#   "description": "",
#   "completed": false,
#   "id": 3
# }
# GET ALL TASKS (GET /tasks)
	
# Response body

# [
#   {
#     "title": "Buy Milk",
#     "description": "Buy Nandini milk from nearby shop",
#     "completed": false,
#     "id": 1
#   },
#   {
#     "title": "Apply PAN Card",
#     "description": "Visit NSDL center in Bangalore and submit documents",
#     "completed": false,
#     "id": 2
#   },
#   {
#     "title": "",
#     "description": "",
#     "completed": false,
#     "id": 3
#   }
# ]
# 4.1 Valid — Get Task 1
# task_id *
# integer-1
	
# Response body

# {
#   "title": "Buy Milk",
#   "description": "Buy Nandini milk from nearby shop",
#   "completed": false,
#   "id": 1
# }
# 4.2 Valid — Get Task 2
# task_id *
# integer-2
	
# Response body

# {
#   "title": "Apply PAN Card",
#   "description": "Visit NSDL center in Bangalore and submit documents",
#   "completed": false,
#   "id": 2
# }

# 4.3 Non-Existing Task
# task_id *
# integer
# (path --10
	
# Response body

# {
#   "detail": "Task not found"
# }
# 5.1 Update Existing Task (Valid)
# task_id *
# integer
# (path)  1
	
# Request body

# {
#  "title": "Buy Vegetables",
#  "description": "Buy tomatoes and onions from Big Bazaar",
#  "completed": true
# }
	
# Response body

# {
#   "title": "Buy Vegetables",
#   "description": "Buy tomatoes and onions from Big Bazaar",
#   "completed": true,
#   "id": 1
# }
# 5.2 Update Task — Toggle Completion Only
# task_id *
# integer
# (path) 2
	
# Request body

# {
#  "title": "Apply PAN Card",
#  "description": "Visit NSDL center in Bangalore and submit documents",
#  "completed": true
# }
# Response body

# {
#   "title": "Apply PAN Card",
#   "description": "Visit NSDL center in Bangalore and submit documents",
#   "completed": true,
#   "id": 2
# }
# 5.3 Update Task — Empty Title Allowed
# task_id *
# integer
# (path)  3
	
# Request body

# {
#  "title": "",
#  "description": "This was an empty task earlier",
#  "completed": false
# }
	
# Response body

# {
#   "title": "",
#   "description": "This was an empty task earlier",
#   "completed": false,
#   "id": 3
# }
# 5.4 Update Non-Existing Task
# task_id *
# integer 99
# (path)
	
# Request body
# {
#  "title": "Ghost",
#  "description": "This task does not exist",
#  "completed": false
# }
# SECTION 6 — DELETE TASK (DELETE
# /tasks/{task_id})
# task_id *
# integer
# (path) 2	
# Response body

# {
#   "message": "Task deleted successfully"
# }
# 6.2 Try Getting Deleted Task
# task_id *
# integer
# (path) 2
# Response body

# {
#   "detail": "Task not found"
# }
# 6.3 Delete Non-Existing Task
# task_id *
# integer
# (path) 50
# Response body 
# {
#   "detail": "Task not found"
# }