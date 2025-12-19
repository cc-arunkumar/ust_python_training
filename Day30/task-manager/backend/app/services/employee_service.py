from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.employee import Employee
from app.models.user import User, User as UserModel, UserRole, UserStatus
from app.services.user_service import create_user




def create_employee(db: Session, data):
    if db.query(Employee).filter(Employee.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")
    # create employee row using only Employee fields
    emp_data = data.dict()
    password = emp_data.pop("password", None)
    role = emp_data.pop("role", None)

    employee = Employee(**emp_data)
    db.add(employee)
    db.commit()
    db.refresh(employee)

    # If admin provided account details, create a User record for this employee
    if password and role:
        # create_user will validate employee exists and that user doesn't exist
        try:
            create_user(db, employee.emp_id, password, role)
        except HTTPException as e:
            # If user creation fails, we won't roll back employee creation.
            # Log and surface a 400 error to the API consumer.
            raise HTTPException(status_code=e.status_code, detail=f"Employee created but user account failed: {e.detail}")

    return employee

def get_all_employees(db: Session):
    return db.query(Employee).all()

def get_employee(db: Session, emp_id: int):
    employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

def update_employee(db: Session, emp_id: int, data):
    employee = get_employee(db, emp_id)
    if data.name is not None:
        employee.name = data.name
    if data.designation is not None:
        employee.designation = data.designation
    if data.manager_id is not None:
        if data.manager_id == emp_id:
            raise HTTPException(400, "Employee cannot report to themselves")
        manager = db.query(User).filter(
            User.emp_id == data.manager_id,
            User.role == "manager",
            User.status == "active"
        ).first()
        if not manager:
            raise HTTPException(
                status_code=400,
                detail="Manager must be an active manager user"
            )
        employee.manager_id = data.manager_id

    # Handle user account updates (password, role, status)
    try:
        user = db.query(UserModel).filter(UserModel.emp_id == emp_id).first()
        # If admin provided password, update or create user
        if getattr(data, "password", None) is not None:
            if user:
                user.password = data.password
            else:
                # If role is provided use it, otherwise default to employee
                role_to_use = getattr(data, "role", None) or "employee"
                create_user(db, emp_id, data.password, role_to_use)

        # Update role if provided
        if getattr(data, "role", None) is not None and user:
            try:
                user.role = UserRole(getattr(data, "role"))
            except Exception:
                # ignore invalid enum values and surface a clear error
                raise HTTPException(status_code=400, detail="Invalid role value")

        # Update status if provided
        if getattr(data, "status", None) is not None:
            if not user:
                # If there's no existing user, require a password to create one
                if getattr(data, "password", None) is None:
                    raise HTTPException(status_code=400, detail="Cannot set status for non-existent user without providing a password to create an account")
                # create_user will have been called above when password was present
                user = db.query(UserModel).filter(UserModel.emp_id == emp_id).first()
            try:
                user.status = UserStatus(getattr(data, "status"))
            except Exception:
                raise HTTPException(status_code=400, detail="Invalid status value")
    except HTTPException:
        # re-raise HTTPExceptions as-is
        raise
    except Exception as e:
        # convert unexpected exceptions to HTTP errors for API consumers
        raise HTTPException(status_code=500, detail=str(e))
    db.commit()
    db.refresh(employee)
    return employee

def delete_employee(db: Session, emp_id: int):
    employee = get_employee(db, emp_id)
    db.delete(employee)
    db.commit()
    return {"message": "Employee deleted successfully"}