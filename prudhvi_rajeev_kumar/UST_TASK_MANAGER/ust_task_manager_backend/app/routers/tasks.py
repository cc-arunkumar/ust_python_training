from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.sql import get_sql_db
from app.db.mongo import get_mongo_db
from app.services.task_service import TaskService
from app.models.employee import Employee
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut
from app.core.dependencies import require_manager, require_employee, AuthUser

router = APIRouter(prefix="/api/tasks", tags=["tasks"])

# -------------------------
# LIST TASKS
# -------------------------
@router.get("/", response_model=list[TaskOut])
def list_tasks(
    current_user: AuthUser = Depends(require_employee),
    db_sql: Session = Depends(get_sql_db),
    db_mongo=Depends(get_mongo_db)
):
    service = TaskService(db_sql, db_mongo)
    tasks = service.list()
    # Employees only see their own tasks
    if current_user["role"] == "employee":
        tasks = [t for t in tasks if t.assigned_to == current_user["employee_id"]]
    return tasks

# -------------------------
# GET SINGLE TASK
# -------------------------
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
        raise HTTPException(status_code=404, detail="Task not found")

    # Employees can only view their own tasks
    if current_user["role"] == "employee" and task.assigned_to != current_user["employee_id"]:
        raise HTTPException(status_code=403, detail="Not authorized to view this task")

    return task

# -------------------------
# CREATE TASK (manager only)
# -------------------------
@router.post("/", response_model=TaskOut)
def create_task(
    body: TaskCreate,
    current_user: AuthUser = Depends(require_manager),
    db_sql: Session = Depends(get_sql_db),
    db_mongo=Depends(get_mongo_db)
):
    service = TaskService(db_sql, db_mongo)
    assigned_emp = db_sql.get(Employee, body.assigned_to)
    if not assigned_emp:
        raise HTTPException(status_code=400, detail="Assigned employee not found")

    # ✅ Manager can only assign tasks to their own employees
    manager_emp = db_sql.get(Employee, current_user["employee_id"])
    if not manager_emp or assigned_emp.manager_id != manager_emp.emp_id:
        raise HTTPException(status_code=403, detail="Not authorized to assign task to this employee")

    try:
        return service.create(body.dict(), actor_id=current_user["employee_id"])
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# -------------------------
# UPDATE TASK (manager only)
# -------------------------
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
        return service.update(task_id, body.dict(), actor_id=current_user["employee_id"])
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# -------------------------
# DELETE TASK (manager only)
# -------------------------
@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    current_user: AuthUser = Depends(require_manager),
    db_sql: Session = Depends(get_sql_db),
    db_mongo=Depends(get_mongo_db)
):
    service = TaskService(db_sql, db_mongo)
    ok = service.delete(task_id, actor_id=current_user["employee_id"])
    if not ok:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"deleted": True}

# -------------------------
# UPDATE TASK STATUS (employee only)
# -------------------------
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
        raise HTTPException(status_code=400, detail="Missing status")

    service = TaskService(db_sql, db_mongo)
    task = service.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # ✅ Employees can only update their own tasks
    if current_user["role"] == "employee" and task.assigned_to != current_user["employee_id"]:
        raise HTTPException(status_code=403, detail="Not authorized to update this task")

    return service.set_status(task_id, status_str, actor_id=current_user["employee_id"])

# -------------------------
# REVIEW TASK (manager only)
# -------------------------
@router.post("/{task_id}/review", response_model=TaskOut)
def review_task(
    task_id: int,
    current_user: AuthUser = Depends(require_manager),
    db_sql: Session = Depends(get_sql_db),
    db_mongo=Depends(get_mongo_db)
):
    service = TaskService(db_sql, db_mongo)
    task = service.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    assigned_emp = db_sql.get(Employee, task.assigned_to)
    if not assigned_emp or assigned_emp.manager_id != current_user["employee_id"]:
        raise HTTPException(status_code=403, detail="Not authorized to review this task")

    if task.status != "done":
        raise HTTPException(status_code=400, detail="Task must be marked done before review")

    task.status = "review"
    db_sql.commit()
    db_sql.refresh(task)
    service.log_service.log_event("INFO", f"Task {task.taskid} reviewed", current_user["employee_id"], "task_review")
    return task
