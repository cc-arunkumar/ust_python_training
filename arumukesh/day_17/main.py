# main.py
from fastapi import FastAPI, HTTPException, Depends
from models import TaskModel
from auth import get_current_user, create_access_token, LoginRequest, Token, User ,users,ACCESS_TOKEN_EXPIRE_MINS
from typing import List
from datetime import datetime, timedelta, timezone


app = FastAPI(title="Task Manager API")

tasks = []
task_id_counter = 1


@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    if data.username not in users or data.password != users[data.username]["password"]:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINS)
    token = create_access_token(subject=data.username, expires_delta=expires)

    return Token(access_token=token)



# ---------------- CREATE TASK ----------------
@app.post("/tasks")
def create_task(task: TaskModel, current_user: User = Depends(get_current_user)):
    global task_id_counter

    new_task = {
        "id": task_id_counter,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }

    tasks.append(new_task)
    task_id_counter += 1

    return new_task


# ---------------- GET ALL TASKS ----------------
@app.get("/tasks")
def get_tasks(current_user: User = Depends(get_current_user)):
    return tasks


# ---------------- GET TASK BY ID ----------------
@app.get("/tasks/{task_id}")
def get_by_id(task_id: int, current_user: User = Depends(get_current_user)):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


# ---------------- UPDATE TASK ----------------
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskModel, current_user: User = Depends(get_current_user)):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["description"] = updated_task.description
            task["completed"] = updated_task.completed
            return task

    raise HTTPException(status_code=404, detail="Task not found")


# ---------------- DELETE TASK ----------------
@app.delete("/tasks/{task_id}")
def del_task(task_id: int, current_user: User = Depends(get_current_user)):
    for i in range(len(tasks)):
        if tasks[i]["id"] == task_id:
            tasks.pop(i)
            return {"message": "Task deleted successfully"}

    raise HTTPException(status_code=404, detail="Task not found")
