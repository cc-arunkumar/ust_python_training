from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.employee import Employee
from app.services.log_service import LogService
from app.db.mongo import get_mongo_db

class EmployeeService:
    def __init__(self, db_sql: Session, db_mongo=None):
        self.db = db_sql
        # ✅ Fix: explicit None check instead of truthiness
        if db_mongo is None:
            db_mongo = get_mongo_db()
        self.log_service = LogService(db_mongo)

    def list(self) -> list[Employee]:
        return list(self.db.execute(select(Employee)).scalars().all())

    def get(self, emp_id: int) -> Employee | None:
        return self.db.get(Employee, emp_id)

    def create(self, data: dict, actor_id: str | None = None) -> Employee:
        emp = Employee(**data)
        self.db.add(emp)
        self.db.commit()
        self.db.refresh(emp)
        self.log_service.log_event("INFO", f"Employee created {emp.emp_id}", actor_id, "employee_create")
        return emp

    def update(self, emp_id: int, data: dict, actor_id: str | None = None) -> Employee:
        emp = self.get(emp_id)
        if not emp:
            raise ValueError("Employee not found")
        for k, v in data.items():
            setattr(emp, k, v)
        self.db.commit()
        self.db.refresh(emp)
        self.log_service.log_event("INFO", f"Employee updated {emp.emp_id}", actor_id, "employee_update")
        return emp

    def delete(self, emp_id: int, actor_id: str | None = None) -> bool:
        emp = self.get(emp_id)
        if not emp:
            return False
        self.db.delete(emp)
        self.db.commit()
        self.log_service.log_event("WARNING", f"Employee deleted {emp_id}", actor_id, "employee_delete")
        return True
