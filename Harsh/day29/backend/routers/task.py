from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from database.mysql import get_db
from database.mongo import reviews_collection, audit_logs_collection
from schemas.task import TaskCreate, TaskUpdate, TaskStatusPatch, TaskResponse, TaskPriorityUpdate
from models.task import Task
from services.task import TaskService, ALLOWED_STATUSES
from services.employees import EmployeeService
from auth.auth import get_current_user

task_router = APIRouter(prefix="/tasks", tags=["Tasks"])

# -------------------- List Tasks --------------------
@task_router.get("/", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db), user=Depends(get_current_user)):
    if "ADMIN" in user.role:
        return db.query(Task).all()
    elif "MANAGER" in user.role:
        subordinate_ids = EmployeeService.get_subordinate_ids(db, user.emp_id)
        return db.query(Task).filter(
            (Task.assigned_to.in_(subordinate_ids)) |
            (Task.assigned_to == user.emp_id) |
            (Task.created_by == user.emp_id) |
            (Task.reviewer == user.emp_id)
        ).all()
    elif "DEVELOPER" in user.role:
        return db.query(Task).filter(
            (Task.assigned_to == user.emp_id) |
            (Task.reviewer == user.emp_id)
        ).all()
    else:
        raise HTTPException(403, "Insufficient permissions")

# -------------------- Get Task --------------------
@task_router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    task = db.query(Task).filter(Task.task_id == task_id).first()
    if not task:
        raise HTTPException(404, "Task not found")
    return task

# -------------------- Create Task --------------------
@task_router.post("/", response_model=TaskResponse, status_code=201)
def create_task(payload: TaskCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    if not any(r in user.role for r in ["ADMIN", "MANAGER"]):
        raise HTTPException(403, "Admin or Manager only")

    if "MANAGER" in user.role and "ADMIN" not in user.role:
        if payload.assigned_to:
            subordinate_ids = EmployeeService.get_subordinate_ids(db, user.emp_id)
            if payload.assigned_to not in subordinate_ids and payload.assigned_to != user.emp_id:
                raise HTTPException(403, "You can only assign tasks to employees under you")

    task = TaskService.create(db, payload.dict(), user)

    try:
        audit_logs_collection.insert_one({
            "action": "TASK_CREATED",
            "task_id": task.task_id,
            "emp_id": user.emp_id,
            "timestamp": datetime.utcnow()
        })
    except Exception:
        pass

    return task

# -------------------- Update Task --------------------
@task_router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, payload: TaskUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    task = db.query(Task).filter(Task.task_id == task_id).first()
    if not task:
        raise HTTPException(404, "Task not found")
    data = payload.dict(exclude_unset=True)
    return TaskService.update(db, task, data, user)

# -------------------- Update Status --------------------
@task_router.patch("/{task_id}/status", response_model=TaskResponse)
def patch_status(task_id: int, payload: TaskStatusPatch, db: Session = Depends(get_db), user=Depends(get_current_user)):
    task = db.query(Task).filter(Task.task_id == task_id).first()
    if not task:
        raise HTTPException(404, "Task not found")

    if "DEVELOPER" in user.role and task.status == "REVIEW" and payload.status == "DONE":
        raise HTTPException(403, "Employee cannot move task to DONE")

    updated_task = TaskService.update_status(db, task, payload.status, user)

    if payload.review:
        try:
            reviews_collection.insert_one({
                "task_id": task.task_id,
                "review": payload.review,
                "reviewed_by": user.emp_id,
                "created_at": datetime.utcnow()
            })
        except Exception:
            pass

    try:
        audit_logs_collection.insert_one({
            "action": "STATUS_UPDATED",
            "task_id": task.task_id,
            "user_id": user.emp_id,
            "timestamp": datetime.utcnow()
        })
    except Exception:
        pass

    return updated_task

# -------------------- Update Priority --------------------
@task_router.patch("/{task_id}/priority", response_model=TaskResponse)
def update_task_priority(task_id: int, payload: TaskPriorityUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    task = db.query(Task).filter(Task.task_id == task_id).first()
    if not task:
        raise HTTPException(404, "Task not found")
    return TaskService.update_priority(db, task, payload.priority, user)

# -------------------- Delete Task --------------------
@task_router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    task = db.query(Task).filter(Task.task_id == task_id).first()
    if not task:
        raise HTTPException(404, "Task not found")
    db.delete(task)
    db.commit()
