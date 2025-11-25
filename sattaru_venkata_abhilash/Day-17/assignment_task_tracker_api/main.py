from typing import List
from fastapi import FastAPI, Depends, HTTPException, status

from models import UserLogin, TaskCreate, TaskUpdate, Task
import auth
from utils import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
    delete_task,
)

app = FastAPI(title="UST Task Manager - Task Tracker API")


# ---------------- LOGIN ----------------

@app.post("/login")
def login(user_credentials: UserLogin):
    user = auth.authenticate_user(
        user_credentials.username,
        user_credentials.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    access_token = auth.create_access_token(
        data={"sub": user["username"]}
    )

    return {"access_token": access_token, "token_type": "bearer"}


# ---------------- CREATE TASK ----------------

@app.post("/tasks")
def create_task_endpoint(
    task_in: TaskCreate,
    current_user: dict = Depends(auth.get_current_user)
):
    new_task = create_task(task_in)

    # Return EXACT UST output order
    return {
        "id": new_task.id,
        "title": new_task.title,
        "description": new_task.description,
        "completed": new_task.completed
    }


# ---------------- GET ALL TASKS ----------------

@app.get("/tasks")
def get_all_tasks_endpoint(
    current_user: dict = Depends(auth.get_current_user)
):
    tasks = get_all_tasks()

    # Return tasks in required field order
    return [
        {
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "completed": t.completed
        }
        for t in tasks
    ]


# ---------------- GET ONE TASK ----------------

@app.get("/tasks/{task_id}")
def get_single_task_endpoint(
    task_id: int,
    current_user: dict = Depends(auth.get_current_user)
):
    task = get_task_by_id(task_id)

    if not task:
        raise HTTPException(404, "Task not found")

    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }


# ---------------- UPDATE TASK ----------------

@app.put("/tasks/{task_id}")
def update_task_endpoint(
    task_id: int,
    task_data: TaskUpdate,
    current_user: dict = Depends(auth.get_current_user)
):
    updated = update_task(task_id, task_data)

    if not updated:
        raise HTTPException(404, "Task not found")

    return {
        "id": updated.id,
        "title": updated.title,
        "description": updated.description,
        "completed": updated.completed
    }


# ---------------- DELETE TASK ----------------

@app.delete("/tasks/{task_id}")
def delete_task_endpoint(
    task_id: int,
    current_user: dict = Depends(auth.get_current_user)
):
    ok = delete_task(task_id)

    if not ok:
        raise HTTPException(404, "Task not found")

    return {"message": "Task deleted successfully"}

