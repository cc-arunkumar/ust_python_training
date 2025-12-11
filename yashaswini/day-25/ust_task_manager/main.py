# main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from logger import log_action
from auth import (
    login, 
    LoginRequest, 
    get_current_user, 
    get_db
)
from database import Tasks, Employee
from pydantic import BaseModel

app = FastAPI(title="Task Manager API")


# ---------------- TASK MODEL ----------------
class TaskModel(BaseModel):
    title: str
    description: str

class TaskUpdateModel(BaseModel):
    title: str | None = None
    description: str | None = None


# ---------------- LOGIN ROUTE ----------------
@app.post("/login")
def login_user(request: LoginRequest, db: Session = Depends(get_db)):
    return login(request, db)


# ---------------- CREATE TASK ----------------
@app.post("/tasks")
def create_task(task: TaskModel, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    new_task = Tasks(
        title=task.title,
        description=task.description,
        user_id=current_user["id"]
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    log_action(current_user["id"], "CREATE_TASK", {"task_id": new_task.id})
    return new_task


# ---------------- GET MY TASKS ----------------
@app.get("/tasks/my")
def get_my_tasks(current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    tasks = db.query(Tasks).filter(Tasks.user_id == current_user["id"]).all()
    return tasks



# ---------------- GET SINGLE TASK ----------------
@app.get("/tasks/{task_id}")
def get_single_task(task_id: int, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    task = db.query(Tasks).filter(
        Tasks.id == task_id,
        Tasks.user_id == current_user["id"]
    ).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


# ---------------- UPDATE TASK ----------------
@app.put("/tasks/{task_id}")
def update_task(task_id: int, update_data: TaskUpdateModel, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    task = db.query(Tasks).filter(
        Tasks.id == task_id,
        Tasks.user_id == current_user["id"]
    ).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if update_data.title is not None:
        task.title = update_data.title

    if update_data.description is not None:
        task.description = update_data.description

    db.commit()
    db.refresh(task)
    log_action(current_user["id"], "UPDATE_TASK", {"task_id": task_id})
    
    return {"message": "Task updated successfully", "task": task}


# ---------------- DELETE TASK ----------------
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    task = db.query(Tasks).filter(
        Tasks.id == task_id,
        Tasks.user_id == current_user["id"]
    ).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    log_action(current_user["id"], "DELETE_TASK", {"task_id": task_id})
    
    return {"message": "Task deleted successfully"}