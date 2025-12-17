from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime
from app.models.task import Task
from app.models.employee import Employee
from app.services.log_service import LogService
from app.db.mongo import get_mongo_db

class TaskService:
    def __init__(self, db_sql: Session, db_mongo=None):
        self.db = db_sql
        # ✅ Fix: explicit None check instead of truthiness
        if db_mongo is None:
            db_mongo = get_mongo_db()
        self.log_service = LogService(db_mongo)

    def list(self) -> list[Task]:
        return list(self.db.execute(select(Task)).scalars().all())

    def get(self, task_id: int) -> Task | None:
        return self.db.get(Task, task_id)

    def create(self, data: dict, actor_id: str | None = None) -> Task:
    # Validate employees exist
        assigned_emp = self.db.get(Employee, data.get("assigned_to"))
        if not assigned_emp:
            raise ValueError("assigned_to employee not found")

        # ✅ Manager restriction: assigned_by must be the manager of assigned employee
        if actor_id:
            manager_emp = self.db.get(Employee, int(actor_id))
            if manager_emp and assigned_emp.manager_id != manager_emp.emp_id:
                raise ValueError("Manager can only assign tasks to their own employees")

        # Continue with existing validation
        for key in ["assigned_by", "created_by"]:
            if self.db.get(Employee, data.get(key)) is None:
                raise ValueError(f"{key} employee not found")

        task = Task(**data)
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        self.log_service.log_event("INFO", f"Task created {task.taskid}", actor_id, "task_create")
        return task


    def update(self, task_id: int, data: dict, actor_id: str | None = None) -> Task:
        task = self.get(task_id)
        if not task:
            raise ValueError("Task not found")
        # Validate employee IDs if present
        for key in ["assigned_to", "reviewer", "updated_by"]:
            if key in data and data[key] is not None:
                if self.db.get(Employee, data[key]) is None:
                    raise ValueError(f"{key} employee not found")
        for k, v in data.items():
            setattr(task, k, v)
        self.db.commit()
        self.db.refresh(task)
        self.log_service.log_event("INFO", f"Task updated {task.taskid}", actor_id, "task_update")
        return task

    def delete(self, task_id: int, actor_id: str | None = None) -> bool:
        task = self.get(task_id)
        if not task:
            return False
        self.db.delete(task)
        self.db.commit()
        self.log_service.log_event("WARNING", f"Task deleted {task_id}", actor_id, "task_delete")
        return True

    def set_status(self, task_id: int, status: str, actor_id: str | None = None) -> Task:
        task = self.get(task_id)
        if not task:
            raise ValueError("Task not found")
        task.status = status
        if status in {"done", "closed"} and task.actual_closure is None:
            task.actual_closure = datetime.utcnow()
        self.db.commit()
        self.db.refresh(task)
        self.log_service.log_event("INFO", f"Task status set {task.taskid} -> {status}", actor_id, "task_status")
        return task
