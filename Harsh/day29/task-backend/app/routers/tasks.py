from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.deps import get_db, get_current_user

router = APIRouter(prefix="/api/tasks", tags=["Tasks"])


# ---------------- CREATE TASK ----------------
@router.post("/", response_model=schemas.TaskOut)
def create_task(
    task: schemas.TaskCreate,
    current=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    role = current["role"]
    emp_id = int(current["emp_id"])

    if role not in ["Admin", "Manager"]:
        raise HTTPException(status_code=403, detail="Not allowed")

    # Manager can assign tasks only to employees under him
    if role == "Manager":
        employee = (
            db.query(models.Employee)
            .filter(models.Employee.id == task.assigned_to)
            .first()
        )

        if not employee or employee.manager_id != emp_id:
            raise HTTPException(
                status_code=403,
                detail="Employee not under this manager",
            )

        task.assigned_by = emp_id

    new_task = models.Task(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


# ---------------- LIST TASKS ----------------
@router.get("/", response_model=List[schemas.TaskOut])
def list_tasks(
    current=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    role = current["role"]
    emp_id = int(current["emp_id"])

    if role == "Admin":
        return db.query(models.Task).all()

    if role == "Manager":
        return db.query(models.Task).filter(
            models.Task.assigned_by == emp_id
        ).all()

    if role == "Employee":
        return db.query(models.Task).filter(
            models.Task.assigned_to == emp_id
        ).all()

    raise HTTPException(status_code=403, detail="Not allowed")


# ---------------- UPDATE TASK ----------------
@router.put("/{task_id}", response_model=schemas.TaskOut)
def update_task(
    task_id: int,
    data: schemas.TaskUpdate,
    current=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    role = current["role"]
    emp_id = int(current["emp_id"])

    task = db.query(models.Task).filter(models.Task.task_id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Manager can update only tasks he created
    if role == "Manager" and task.assigned_by != emp_id:
        raise HTTPException(status_code=403, detail="Not allowed")

    # Employee can update only status of tasks assigned to him
    if role == "Employee":
        if task.assigned_to != emp_id:
            raise HTTPException(status_code=403, detail="Not allowed")

        if data.status is None:
            raise HTTPException(
                status_code=400,
                detail="Employee can update only status",
            )

        task.status = data.status
        db.commit()
        db.refresh(task)
        return task

    # Admin can update anything
    for field, value in data.dict(exclude_unset=True).items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)
    return task


# ---------------- DELETE TASK ----------------
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    current=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    role = current["role"]
    emp_id = int(current["emp_id"])

    task = db.query(models.Task).filter(models.Task.task_id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Manager can delete only tasks he created
    if role == "Manager" and task.assigned_by != emp_id:
        raise HTTPException(status_code=403, detail="Not allowed")

    # Employees cannot delete tasks
    if role == "Employee":
        raise HTTPException(status_code=403, detail="Not allowed")

    db.delete(task)
    db.commit()
    return
