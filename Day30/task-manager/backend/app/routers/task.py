from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.core.security import get_current_user
from app.schemas.task import (
    TaskCreate,
    TaskUpdate,
    TaskStatusUpdate,
    TaskRemarksUpdate,
    TaskResponse
)
from app.services.task_service import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
    update_task_status,
    update_task_remarks,
    delete_task
)
from app.models.task import Task
from app.utils.enums import TASK_STATUS

router = APIRouter(prefix="/tasks", tags=["Tasks"])


# ---------------- CREATE TASK ----------------
@router.post("/", response_model=TaskResponse)
def create_task_api(
    data: TaskCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return create_task(db, data, current_user)


# ---------------- GET ALL TASKS ----------------
@router.get("/", response_model=List[TaskResponse])
def get_tasks_api(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return get_all_tasks(db, current_user)


# ---------------- GET TASK BY ID ----------------
@router.get("/{task_id}", response_model=TaskResponse)
def get_task_api(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return get_task_by_id(db, task_id, current_user)


# ---------------- GET MY TASKS ----------------
@router.get("/my/tasks", response_model=List[TaskResponse])
def get_my_tasks(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return db.query(Task).filter(
        Task.assign_to == current_user["employee_id"]
    ).all()


# ---------------- GET TASKS FOR REVIEW ----------------
@router.get("/review/tasks", response_model=List[TaskResponse])
def get_review_tasks(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if "admin" not in current_user["role"] and "manager" not in current_user["role"]:
        raise Exception("Access denied")

    return db.query(Task).filter(Task.status == "review").all()


# ---------------- FILTER BY EMPLOYEE ----------------
@router.get("/employee/{employee_id}", response_model=List[TaskResponse])
def get_tasks_by_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return db.query(Task).filter(Task.assign_to == employee_id).all()


# ---------------- FILTER BY STATUS ----------------
@router.get("/status/{status}", response_model=List[TaskResponse])
def get_tasks_by_status(
    status: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if status not in TASK_STATUS:
        raise Exception("Invalid status")

    return db.query(Task).filter(Task.status == status).all()


# ---------------- UPDATE TASK ----------------
@router.put("/{task_id}", response_model=TaskResponse)
def update_task_api(
    task_id: int,
    data: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return update_task(db, task_id, data, current_user)


# ---------------- UPDATE STATUS ----------------
@router.patch("/{task_id}/status", response_model=TaskResponse)
def update_status_api(
    task_id: int,
    data: TaskStatusUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return update_task_status(db, task_id, data.status, current_user)


# ---------------- UPDATE REMARKS ----------------
@router.patch("/{task_id}/remarks", response_model=TaskResponse)
def update_remarks_api(
    task_id: int,
    data: TaskRemarksUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return update_task_remarks(db, task_id, data.remarks, current_user)


# ---------------- COMPLETE TASK ----------------
@router.patch("/{task_id}/complete", response_model=TaskResponse)
def complete_task_api(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return update_task_status(db, task_id, "completed", current_user)


# ---------------- DELETE TASK ----------------
@router.delete("/{task_id}")
def delete_task_api(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return delete_task(db, task_id, current_user)
