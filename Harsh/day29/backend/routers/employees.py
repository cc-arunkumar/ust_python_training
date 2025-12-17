from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from database.mysql import get_db
from schemas.employees import *
from services.employees import EmployeeService
from auth.auth import get_current_user
from models.employees import Employee

emp_router = APIRouter(prefix="/employees", tags=["Employees"])


@emp_router.post("/", response_model=EmployeeResponse, status_code=201)
def create_employee(payload: EmployeeCreate,
                    db: Session = Depends(get_db),
                    user=Depends(get_current_user)):
    try:
        if "ADMIN" not in user.role:
            raise HTTPException(403, "Admin only")
        
        # Validate manager exists if manager_id is provided
        if payload.manager_id:
            manager = EmployeeService.get_by_id(db, payload.manager_id)
            if not manager:
                raise HTTPException(404, f"Manager with ID {payload.manager_id} not found")
        
        return EmployeeService.create(db, payload.dict())
    
    except HTTPException:
        raise
    except IntegrityError as e:
        db.rollback()
        if "Duplicate entry" in str(e.orig):
            raise HTTPException(409, "Employee with this email or ID already exists")
        raise HTTPException(400, f"Database integrity error: {str(e.orig)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(500, f"Database error: {str(e)}")
    except Exception as e:
        db.rollback()
        raise HTTPException(500, f"Internal server error: {str(e)}")


@emp_router.get("/", response_model=list[EmployeeResponse])
def list_employees(db: Session = Depends(get_db),
                   user=Depends(get_current_user)):
    try:
        # ADMIN can see all employees
        if "ADMIN" in user.role:
            return EmployeeService.get_all(db)
        
        # MANAGER can see employees under them
        elif "MANAGER" in user.role:
            return EmployeeService.get_employees_under_manager(db, user.emp_id)
        
        # DEVELOPER can only see themselves
        elif "DEVELOPER" in user.role:
            employee = EmployeeService.get_by_id(db, user.emp_id)
            if not employee:
                raise HTTPException(404, "Employee not found")
            return [employee]
        
        else:
            raise HTTPException(403, "Insufficient permissions")
    
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        raise HTTPException(500, f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(500, f"Internal server error: {str(e)}")


@emp_router.get("/{emp_id}", response_model=EmployeeResponse)
def get_employee(emp_id: int, 
                 db: Session = Depends(get_db),
                 user=Depends(get_current_user)):
    try:
        emp = EmployeeService.get_by_id(db, emp_id)
        if not emp:
            raise HTTPException(404, "Employee not found")
        
        # ADMIN can view any employee
        if "ADMIN" in user.role:
            return emp
        
        # MANAGER can view employees under them
        elif "MANAGER" in user.role:
            if EmployeeService.is_employee_under_manager(db, emp_id, user.emp_id):
                return emp
            raise HTTPException(403, "You can only view employees under you")
        
        # DEVELOPER can only view themselves
        elif "DEVELOPER" in user.role:
            if emp_id == user.emp_id:
                return emp
            raise HTTPException(403, "You can only view your own profile")
        
        else:
            raise HTTPException(403, "Insufficient permissions")
    
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        raise HTTPException(500, f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(500, f"Internal server error: {str(e)}")


@emp_router.put("/{emp_id}", response_model=EmployeeResponse)
def update_employee(emp_id: int, payload: EmployeeUpdate,
                    db: Session = Depends(get_db),
                    user=Depends(get_current_user)):
    try:
        emp = EmployeeService.get_by_id(db, emp_id)
        if not emp:
            raise HTTPException(404, "Employee not found")
        
        # Only ADMIN can update employees
        if "ADMIN" not in user.role:
            raise HTTPException(403, "Admin only")
        
        update_data = payload.dict(exclude_unset=True)
        
        # Validate emp_id and manager_id are not the same
        if "manager_id" in update_data and update_data["manager_id"]:
            if emp_id == update_data["manager_id"]:
                raise HTTPException(400, "Employee ID and Manager ID cannot be the same")
            
            # Validate manager exists
            manager = EmployeeService.get_by_id(db, update_data["manager_id"])
            if not manager:
                raise HTTPException(404, f"Manager with ID {update_data['manager_id']} not found")

        return EmployeeService.update(db, emp, update_data)
    
    except HTTPException:
        raise
    except IntegrityError as e:
        db.rollback()
        if "Duplicate entry" in str(e.orig):
            raise HTTPException(409, "Email already exists for another employee")
        raise HTTPException(400, f"Database integrity error: {str(e.orig)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(500, f"Database error: {str(e)}")
    except Exception as e:
        db.rollback()
        raise HTTPException(500, f"Internal server error: {str(e)}")


@emp_router.delete("/{emp_id}", status_code=204)
def delete_employee(emp_id: int,
                    db: Session = Depends(get_db),
                    user=Depends(get_current_user)):
    try:
        # Only ADMIN can delete employees
        if "ADMIN" not in user.role:
            raise HTTPException(403, "Admin only")

        emp = EmployeeService.get_by_id(db, emp_id)
        if not emp:
            raise HTTPException(404, "Employee not found")

        EmployeeService.delete(db, emp)
    
    except HTTPException:
        raise
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(400, "Cannot delete employee. They may have associated records (tasks, users, etc.)")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(500, f"Database error: {str(e)}")
    except Exception as e:
        db.rollback()
        raise HTTPException(500, f"Internal server error: {str(e)}")