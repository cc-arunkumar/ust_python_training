from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import models
from utils import create_task, get_all_tasks, get_task_by_id, update_task, delete_task
from db_connection_sql import get_db
import auth
from mongodb_logger import log_activity  # Import MongoDB logging function


app = FastAPI(title="UST Task Manager - Task Tracker API")


# ---------------- LOGIN ----------------

@app.post("/login")
def login(user_credentials: models.UserLogin, db: Session = Depends(get_db)):
    user = auth.authenticate_user(
        user_credentials.username,
        user_credentials.password,
        db  # Pass the DB session to the authentication function
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

@app.post("/tasks", response_model=models.TaskResponse)
def create_task_endpoint(
    task_in: models.TaskCreate,
    current_user: dict = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    new_task = create_task(db, task_in, current_user["username"])  # Pass username to get user_id

    # Log the task creation in MongoDB
    log_activity(current_user["username"], "CREATE", new_task.id)

    return new_task


# ---------------- GET ALL TASKS ----------------

@app.get("/tasks", response_model=List[models.TaskResponse])
def get_all_tasks_endpoint(
    current_user: dict = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    tasks = get_all_tasks(db, current_user["username"])

    return tasks


# ---------------- GET ONE TASK ----------------

@app.get("/tasks/{task_id}", response_model=models.TaskResponse)
def get_single_task_endpoint(
    task_id: int,
    current_user: dict = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    task = get_task_by_id(db, task_id, current_user["username"])

    if not task:
        raise HTTPException(404, "Task not found")

    return task


# ---------------- UPDATE TASK ----------------

@app.put("/tasks/{task_id}", response_model=models.TaskResponse)
def update_task_endpoint(
    task_id: int,
    task_data: models.TaskUpdate,
    current_user: dict = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    updated = update_task(db, task_id, task_data, current_user["username"])

    if not updated:
        raise HTTPException(404, "Task not found")

    # Log the task update in MongoDB
    log_activity(current_user["username"], "UPDATE", updated.id)

    return updated


# ---------------- DELETE TASK ----------------

@app.delete("/tasks/{task_id}")
def delete_task_endpoint(
    task_id: int,
    current_user: dict = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    ok = delete_task(db, task_id, current_user["username"])

    if not ok:
        raise HTTPException(404, "Task not found")

    # Log the task deletion in MongoDB
    log_activity(current_user["username"], "DELETE", task_id)

    return {"message": "Task deleted successfully"}
