from app.database.mysql_connection import get_connection
from app.models.models import EmployeeReqRes  # Pydantic Model
from app.schemas.schemas import EmployeeSchema
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from fastapi import HTTPException
from app.models.models import UserReqRes
from app.crud.users_crud import add_user, normalize_role_param
from app.crud.users_crud import get_user_by_id

def add_employee(new_emp: EmployeeReqRes, role: str, user, initial_role: str | None = None):
    session = None
    try:
        if role != "Admin":
            raise HTTPException(status_code=403, detail="Only Admin can add employees.")
        session = get_connection()
        # If no manager provided, default to the creating user's e_id (Admin creating employee)
        assigned_mgr = new_emp.mgr_id if getattr(new_emp, 'mgr_id', None) is not None else getattr(user, 'e_id', None)
        if assigned_mgr is None:
            # As a last resort, default to 0 (should not happen for proper auth flows)
            assigned_mgr = 0

        new_employee = EmployeeSchema(
            name=new_emp.name,
            email=new_emp.email,
            designation=new_emp.designation,
            mgr_id=assigned_mgr
        )
        session.add(new_employee)
        session.commit()
        session.refresh(new_employee)
        # Create an associated user in users table. Use initial_role if provided,
        # otherwise default to Developer.
        # Normalize incoming role (e.g. 'developer' -> 'Developer') so Pydantic/DB accept it.
        if initial_role:
            nr = normalize_role_param(initial_role)
            assigned_roles = [nr] if nr else ["Developer"]
        else:
            assigned_roles = ["Developer"]

        # Build UserReqRes with normalized roles
        user_data = UserReqRes(
            e_id=new_employee.e_id,
            password="password123",
            roles=assigned_roles,
            status="active"
        )
        add_user(user_data)
        return EmployeeReqRes.model_validate(new_employee)  # Convert to Pydantic model
    except IntegrityError as e:
        # Duplicate key (email) or other integrity constraints
        if session:
            session.rollback()
        # Provide a clear 409 Conflict for duplicate emails
        raise HTTPException(status_code=409, detail="Employee with this email already exists")
    except SQLAlchemyError as e:
        if session:
            session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        if session:
            session.close()


def get_all_employees(role: str, user):
    session = None
    try:
        session = get_connection()
        
        # If Manager, show only employees who report to them
        if role == "Manager":
            if "Manager" not in user.roles:
                raise HTTPException(status_code=403, detail="Only managers can access their team members.")
            employees = session.query(EmployeeSchema).filter(EmployeeSchema.mgr_id == user.e_id).all()
        elif role == "Admin":
            if "Admin" not in user.roles:
                raise HTTPException(status_code=403, detail="Only Admin can access all employees.")
            employees = session.query(EmployeeSchema).all()
        else:
            raise HTTPException(status_code=403, detail="Unauthorized access.")
        
        # employees = session.query(EmployeeSchema).all()
        return [EmployeeReqRes.model_validate(emp) for emp in employees]  # Convert to list of Pydantic models
    except SQLAlchemyError as e:
        if session:
            session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        if session:
            session.close()


def get_by_employee_id(id: int, role: str, user):
    session = None
    try:
        session = get_connection()
        emp = session.query(EmployeeSchema).filter(EmployeeSchema.e_id == id).first()
        if not emp:
            raise HTTPException(status_code=404, detail="Employee Not Found")
              
        # Admin can view all employees; Manager can only view their team
        # if role == "Manager":
        #     if emp.mgr_id != user.e_id:
        #         raise HTTPException(status_code=403, detail="Manager can only view their own team.")
            
        return EmployeeReqRes.model_validate(emp)  # Convert to Pydantic model
    except SQLAlchemyError as e:
        if session:
            session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        if session:
            session.close()


def get_assignable_employees(role: str, user):
    """Return all employees that can be assigned tasks (exclude users who have Admin role)."""
    session = None
    try:
        session = get_connection()
        # Permission: Manager or Admin may request this
        if role == "Manager":
            if "Manager" not in user.roles:
                raise HTTPException(status_code=403, detail="Only Manager can access assignable employees")
        elif role == "Admin":
            if "Admin" not in user.roles:
                raise HTTPException(status_code=403, detail="Only Admin can access assignable employees")
        else:
            raise HTTPException(status_code=403, detail="Unauthorized access.")

        all_emps = session.query(EmployeeSchema).all()
        assignable = []
        for emp in all_emps:
            try:
                u = get_user_by_id(emp.e_id)
                # get_user_by_id returns UserReqRes which has roles list
                if "Admin" in (u.roles or []):
                    continue
            except Exception:
                # If user record isn't found, treat as non-admin (assignable)
                pass
            assignable.append(emp)

        return [EmployeeReqRes.model_validate(emp) for emp in assignable]
    except SQLAlchemyError as e:
        if session:
            session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        if session:
            session.close()


def update_employee(id: int, updated: dict, role: str, user):
    session = None
    try:
         # Only Admin can update employee details
        if role != "Admin":
            raise HTTPException(status_code=403, detail="Only Admin can update employee details.")
        session = get_connection()
        emp = session.query(EmployeeSchema).filter(EmployeeSchema.e_id == id).first()
        if not emp:
            raise HTTPException(status_code=404, detail="Employee Not Found")
        for key, value in updated.items():
            setattr(emp, key, value)
        session.commit()
        session.refresh(emp)
        return EmployeeReqRes.model_validate(emp)  # Convert to Pydantic model
    except SQLAlchemyError as e:
        if session:
            session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        if session:
            session.close()


def delete_employee(id: int, role: str, user):
    session = None
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
        if session:
            session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        if session:
            session.close()