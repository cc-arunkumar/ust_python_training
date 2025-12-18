from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from services.database import SessionLocal
from services.task_service import (
    create_task,
    get_tasks,
    get_task,
    update_task,
    delete_task,
    get_tasks_by_assignee
)
from schemas.task import TaskSchema
from utils.authorization import require_permission, get_current_user, ROLE_PERMISSIONS

task_router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


# ---------------- DB Dependency ----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- CREATE TASK (MANAGER ONLY) ----------------
@task_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission("task:create"))]
)
def create_new_task(task: TaskSchema, db: Session = Depends(get_db)):
    existing = get_task(db, task.task_id)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task already exists"
        )
    return create_task(db, task)


# ---------------- GET TASKS (ROLE AWARE) ----------------
@task_router.get("/", status_code=status.HTTP_200_OK)
def read_tasks(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    permissions = ROLE_PERMISSIONS.get(current_user["role"], set())

    if "task:read_all" in permissions:
        return get_tasks(db)

    if "task:read_own" in permissions:
        return get_tasks_by_assignee(db, current_user["emp_id"])

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Permission denied"
    )


# ---------------- GET TASK BY ID ----------------
@task_router.get(
    "/{task_id}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(require_permission("task:read_one"))]
)
def get_task_by_id(task_id: str, db: Session = Depends(get_db)):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return task


# ---------------- UPDATE TASK ----------------
@task_router.put(
    "/{task_id}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(require_permission("task:update"))]
)
def update_existing_task(
    task_id: str,
    task: TaskSchema,
    db: Session = Depends(get_db)
):
    updated = update_task(db, task_id, task)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return updated


# ---------------- PARTIAL UPDATE ----------------
@task_router.patch(
    "/{task_id}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(require_permission("task:update"))]
)
def patch_task(
    task_id: str,
    status_: str | None = None,
    priority: str | None = None,
    remarks: str | None = None,
    db: Session = Depends(get_db)
):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    if status_:
        task.status = status_
    if priority:
        task.priority = priority
    if remarks:
        task.remarks = remarks

    db.commit()
    db.refresh(task)
    return task


# ---------------- REVIEW TASK ----------------
@task_router.patch(
    "/{task_id}/review",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(require_permission("task:review"))]
)
def review_task(
    task_id: str,
    remarks: str,
    db: Session = Depends(get_db)
):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.status = "REVIEW"
    task.remarks = remarks

    db.commit()
    db.refresh(task)
    return task


# ---------------- DELETE TASK (DISABLED) ----------------
@task_router.delete(
    "/{task_id}",
    status_code=status.HTTP_403_FORBIDDEN
)
def delete_existing_task():
    raise HTTPException(
        status_code=403,
        detail="Delete task is not allowed"
    )
