from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy import or_
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
            raise
 
    @staticmethod
    def get_by_id(db: Session, emp_id: int) -> Employee:
        try:
            return db.query(Employee).filter(Employee.emp_id == emp_id).first()
        except SQLAlchemyError as e:
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
            raise HTTPException(500, f"Database error: {str(e)}")
 
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
                    all_employees.append(emp)
                    # Recursively get their subordinates
                    get_subordinates(emp.emp_id)
           
            # Start with the manager themselves
            manager = db.query(Employee).filter(Employee.emp_id == manager_id).first()
            if manager:
                all_employees.append(manager)
           
            # Get all subordinates
            get_subordinates(manager_id)
           
            return all_employees
        except SQLAlchemyError as e:
            raise HTTPException(500, f"Database error: {str(e)}")
 
    @staticmethod
    def get_subordinate_ids(db: Session, manager_id: int) -> List[int]:
        """
        Get list of employee IDs under a manager (including the manager)
        """
        try:
            employees = EmployeeService.get_all_employees_under_manager(db, manager_id)
            return [emp.emp_id for emp in employees]
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
            db.delete(emp)
            db.commit()
        except IntegrityError as e:
            db.rollback()
            raise
        except SQLAlchemyError as e:
            db.rollback()
            raise
 