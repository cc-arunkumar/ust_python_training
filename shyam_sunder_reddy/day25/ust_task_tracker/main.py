from fastapi import FastAPI, HTTPException, status, Depends
from models import TaskSchema, UserSchema
from auth import (
    Token, LoginRequest,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token,
    get_current_user
)
from database import fetch_user, get_all_tasks, create_task, get_by_id, update_task, delete_task,create_u
from typing import List
import datetime

app = FastAPI(title="UST Task Tracker")

# ---------------- LOGIN ENDPOINT ----------------
# create user
@app.post("/createuser")
def create_user(user:UserSchema):
    return create_u(user)

#login with username password
@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    user = fetch_user(data)
    if user:
        expires = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        token = create_access_token(subject=str(user.user_id), expires_delta=expires)
        return Token(access_token=token, token_type="bearer")
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password"
    )


# ---------------- CREATE TASK ENDPOINT ----------------
@app.post("/tasks", response_model=TaskSchema)
def create(task: TaskSchema, current_user: UserSchema = Depends(get_current_user)):
    return create_task(task, current_user.user_id)

# ---------------- DISPLAY ALL TASKS ENDPOINT ----------------
@app.get("/tasks", response_model=List[TaskSchema])
def display(current_user: UserSchema = Depends(get_current_user)):
    return get_all_tasks(current_user.user_id)

# ---------------- SEARCH TASK BY ID ENDPOINT ----------------
@app.get("/tasks/{task_id}", response_model=TaskSchema)
def search_byid(task_id: int, current_user: UserSchema = Depends(get_current_user)):
    return get_by_id(task_id, current_user.user_id)

# ---------------- UPDATE TASK ENDPOINT ----------------
@app.put("/tasks/{task_id}", response_model=TaskSchema)
def update(task_id: int, task: TaskSchema, current_user: UserSchema = Depends(get_current_user)):
    return update_task(task_id, task, current_user.user_id)

# ---------------- DELETE TASK ENDPOINT ----------------
@app.delete("/tasks/{task_id}")
def delete(task_id: int, current_user: UserSchema = Depends(get_current_user)):
    return delete_task(task_id, current_user.user_id)
