from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy import or_, text
from models.employees import Employee
from fastapi import HTTPException
from typing import List
 
 
class EmployeeService:
 
    @staticmethod
    def create(db: Session, data: dict) -> Employee:
        try:
            # Validate emp_id and manager_id
            emp = Employee(**data)
            db.add(emp)
            db.commit()
            db.refresh(emp)
            # Now emp.emp_id exists
            if emp.manager_id == emp.emp_id:
                db.delete(emp)
                db.commit()
                raise HTTPException(400, "Employee cannot be their own manager")
            return emp
        except IntegrityError as e:
            db.rollback()
            raise
        except ValueError as e:
            db.rollback()
            raise HTTPException(400, str(e))
        except SQLAlchemyError as e:
            db.rollback()
            raise
 
    @staticmethod
    def get_all(db: Session) -> List[Employee]:
        try:
            return db.query(Employee).all()
        except SQLAlchemyError as e:
            # Fallback: maybe the `status` column is missing in DB schema
            # Do a raw select of known columns excluding status
            try:
                rows = db.execute(
                    text("SELECT emp_id, emp_name, email, designation, manager_id FROM employees")
                ).mappings().all()
                # Return list of dict-like objects compatible with Pydantic response
                return [dict(r) for r in rows]
            except Exception:
                raise
 
    @staticmethod
    def get_by_id(db: Session, emp_id: int) -> Employee:
        try:
            return db.query(Employee).filter(Employee.emp_id == emp_id).first()
        except SQLAlchemyError as e:
            # Fallback raw query without status
            try:
                row = db.execute(
                    text("SELECT emp_id, emp_name, email, designation, manager_id FROM employees WHERE emp_id = :id"),
                    {"id": emp_id},
                ).mappings().first()
                return dict(row) if row else None
            except Exception:
                raise
 
    @staticmethod
    def get_employees_under_manager(db: Session, manager_id: int) -> List[Employee]:
        """
        Get all employees directly under a manager and the manager themselves
        """
        try:
            # Get direct reports
            employees = db.query(Employee).filter(
                or_(
                    Employee.manager_id == manager_id,
                    Employee.emp_id == manager_id
                )
            ).all()
            return employees
        except SQLAlchemyError as e:
            # Fallback raw query excluding status
            rows = db.execute(
                text(
                    "SELECT emp_id, emp_name, email, designation, manager_id FROM employees "
                    "WHERE manager_id = :mid OR emp_id = :mid"
                ),
                {"mid": manager_id},
            ).mappings().all()
            return [dict(r) for r in rows]
 
    @staticmethod
    def get_all_employees_under_manager(db: Session, manager_id: int) -> List[Employee]:
        """
        Recursively get all employees under a manager (including nested hierarchy)
        """
        try:
            all_employees = []
            visited = set()
           
            def get_subordinates(mgr_id: int):
                if mgr_id in visited:
                    return
                visited.add(mgr_id)
               
                # Get direct reports
                direct_reports = db.query(Employee).filter(
                    Employee.manager_id == mgr_id
                ).all()

                for emp in direct_reports:
                    # append the ORM instance or dict as-is
                    all_employees.append(emp)
                    # determine emp id safely for recursion
                    try:
                        next_mgr_id = emp.emp_id
                    except Exception:
                        # emp may be a dict from fallback raw SQL
                        next_mgr_id = emp.get("emp_id") if isinstance(emp, dict) else None
                    if next_mgr_id is not None:
                        get_subordinates(next_mgr_id)
           
            # Start with the manager themselves
            manager = db.query(Employee).filter(Employee.emp_id == manager_id).first()
            if manager:
                all_employees.append(manager)
           
            # Get all subordinates
            get_subordinates(manager_id)
           
            return all_employees
        except SQLAlchemyError as e:
            # fallback: raw query for manager
            row = db.execute(
                text(
                    "SELECT emp_id, emp_name, email, designation, manager_id FROM employees WHERE emp_id = :id"
                ),
                {"id": manager_id},
            ).mappings().first()
            if row:
                all_employees.append(dict(row))
            # Ensure we always return the collected employees in fallback
            return all_employees
 
    @staticmethod
    def get_subordinate_ids(db: Session, manager_id: int) -> List[int]:
        """
        Get list of employee IDs under a manager (including the manager)
        """
        try:
            employees = EmployeeService.get_all_employees_under_manager(db, manager_id)
            ids = []
            for emp in employees:
                if hasattr(emp, "emp_id"):
                    ids.append(emp.emp_id)
                elif isinstance(emp, dict):
                    eid = emp.get("emp_id")
                    if eid is not None:
                        ids.append(eid)
            return ids
        except Exception as e:
            raise
 
    @staticmethod
    def is_employee_under_manager(db: Session, emp_id: int, manager_id: int) -> bool:
        """
        Check if an employee is under a specific manager (direct or indirect)
        """
        try:
            subordinate_ids = EmployeeService.get_subordinate_ids(db, manager_id)
            return emp_id in subordinate_ids
        except Exception as e:
            raise
 
    @staticmethod
    def update(db: Session, emp: Employee, data: dict) -> Employee:
        try:
            # Validate if manager_id is being updated
            if "manager_id" in data and data["manager_id"]:
                if emp.emp_id == data["manager_id"]:
                    raise ValueError("Employee ID and Manager ID cannot be the same")
           
            for k, v in data.items():
                setattr(emp, k, v)
            db.commit()
            db.refresh(emp)
            return emp
        except IntegrityError as e:
            db.rollback()
            raise
        except ValueError as e:
            db.rollback()
            raise HTTPException(400, str(e))
        except SQLAlchemyError as e:
            db.rollback()
            raise
 
    @staticmethod
    def delete(db: Session, emp: Employee):
        try:
            # soft-delete: mark employee as INACTIVE
            try:
                emp.status = "INACTIVE"
                db.commit()
                db.refresh(emp)
            except Exception:
                # fallback to hard delete if status column not present or fails
                db.delete(emp)
                db.commit()
        except IntegrityError as e:
            db.rollback()
            raise
        except SQLAlchemyError as e:
            db.rollback()
            raise
 