from database.sql_db import get_connection
from models.employee import EmployeeReqRes  # Pydantic Model
from models.user import UserReqRes
from crud.users_crud import add_user
from schema.employee_schema import EmployeeSchema
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException


def add_employee(new_emp: EmployeeReqRes, role: str, user):
    try:
        # Only Admin can create employees
        if role != "Admin":
            raise HTTPException(status_code=403, detail="Only Admin can add employees.")
        
        session = get_connection()
        new_employee = EmployeeSchema(
            name=new_emp.name,
            email=new_emp.email,
            designation=new_emp.designation,
            mgr_id=new_emp.mgr_id
        )
        session.add(new_employee)
        session.commit()
        session.refresh(new_employee)
        user_data = UserReqRes(
            e_id=new_employee.e_id,
            password="defaultPass123",
            role=[],  # Empty roles list
            status="active"
        )
        add_user(user_data)  # Create the user

        return EmployeeReqRes.from_orm(new_employee)  # Convert to Pydantic model
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()


def get_all_employees(role: str, user):
    try:
        session = get_connection()

        # If Manager, show only employees who report to them
        if role == "Manager":
            if "Manager" not in user.role:
                raise HTTPException(status_code=403, detail="Only managers can access their team members.")
            employees = session.query(EmployeeSchema).filter(EmployeeSchema.mgr_id == user.e_id).all()
        elif role == "Admin":
            if "Admin" not in user.role:
                raise HTTPException(status_code=403, detail="Only Admin can access all employees.")
            employees = session.query(EmployeeSchema).all()
        else:
            raise HTTPException(status_code=403, detail="Unauthorized access.")
        
        return [EmployeeReqRes.from_orm(emp) for emp in employees]  # Convert to list of Pydantic models
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()


def get_by_employee_id(id: int, role: str, user):
    try:
        session = get_connection()
        emp = session.query(EmployeeSchema).filter(EmployeeSchema.e_id == id).first()
        
        if not emp:
            raise HTTPException(status_code=404, detail="Employee Not Found")
        
        # Admin can view all employees; Manager can only view their team
        if role == "Manager":
            if emp.mgr_id != user.e_id:
                raise HTTPException(status_code=403, detail="Manager can only view their own team.")
        
        return EmployeeReqRes.from_orm(emp)  # Convert to Pydantic model
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()


def update_employee(id: int, updated: EmployeeReqRes, role: str, user):
    try:
        # Only Admin can update employee details
        if role != "Admin":
            raise HTTPException(status_code=403, detail="Only Admin can update employee details.")
        
        session = get_connection()
        emp = session.query(EmployeeSchema).filter(EmployeeSchema.e_id == id).first()
        
        if not emp:
            raise HTTPException(status_code=404, detail="Employee Not Found")
        emp.name=updated.name
        emp.email=updated.email
        emp.designation=updated.designation
        emp.mgr_id=updated.mgr_id
        for key, value in updated.items():
            setattr(emp, key, value)
        
        session.commit()
        session.refresh(emp)
        return EmployeeReqRes.from_orm(emp)  # Convert to Pydantic model
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()


def delete_employee(id: int, role: str, user):
    try:
        # Only Admin can delete employees
        if role != "Admin":
            raise HTTPException(status_code=403, detail="Only Admin can delete employees.")
        
        session = get_connection()
        emp = session.query(EmployeeSchema).filter(EmployeeSchema.e_id == id).first()
        
        if not emp:
            raise HTTPException(status_code=404, detail="Employee Not Found")
        
        session.delete(emp)
        session.commit()
        return {"detail": "Employee Deleted Successfully"}
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()
