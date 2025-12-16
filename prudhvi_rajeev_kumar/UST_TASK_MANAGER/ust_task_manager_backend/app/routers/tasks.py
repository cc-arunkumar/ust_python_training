from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.sql import get_sql_db
from app.db.mongo import get_mongo_db
from app.services.task_service import TaskService
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut
from app.core.dependencies import require_manager, require_employee, AuthUser

router = APIRouter(prefix="/api/tasks", tags=["tasks"])

@router.get("/", response_model=list[TaskOut])
def list_tasks(
    current_user: AuthUser = Depends(require_employee),
    db_sql: Session = Depends(get_sql_db),
    db_mongo=Depends(get_mongo_db)
):
    service = TaskService(db_sql, db_mongo)
    return service.list()

@router.get("/{task_id}", response_model=TaskOut)
def get_task(
    task_id: int,
    current_user: AuthUser = Depends(require_employee),
    db_sql: Session = Depends(get_sql_db),
    db_mongo=Depends(get_mongo_db)
):
    service = TaskService(db_sql, db_mongo)
    task = service.get(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

@router.post("/", response_model=TaskOut)
def create_task(
    body: TaskCreate,
    current_user: AuthUser = Depends(require_manager),
    db_sql: Session = Depends(get_sql_db),
    db_mongo=Depends(get_mongo_db)
):
    service = TaskService(db_sql, db_mongo)
    try:
        return service.create(body.dict(), actor_id=current_user["sub"])
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.put("/{task_id}", response_model=TaskOut)
def update_task(
    task_id: int,
    body: TaskUpdate,
    current_user: AuthUser = Depends(require_manager),
    db_sql: Session = Depends(get_sql_db),
    db_mongo=Depends(get_mongo_db)
):
    service = TaskService(db_sql, db_mongo)
    try:
        return service.update(task_id, body.dict(), actor_id=current_user["sub"])
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    current_user: AuthUser = Depends(require_manager),
    db_sql: Session = Depends(get_sql_db),
    db_mongo=Depends(get_mongo_db)
):
    service = TaskService(db_sql, db_mongo)
    ok = service.delete(task_id, actor_id=current_user["sub"])
    if not ok:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return {"deleted": True}

@router.patch("/{task_id}/status", response_model=TaskOut)
def set_task_status(
    task_id: int,
    status_value: dict,
    current_user: AuthUser = Depends(require_employee),
    db_sql: Session = Depends(get_sql_db),
    db_mongo=Depends(get_mongo_db)
):
    status_str = status_value.get("status")
    if not status_str:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing status")
    service = TaskService(db_sql, db_mongo)
    try:
        return service.set_status(task_id, status_str, actor_id=current_user["sub"])
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
