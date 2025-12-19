from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

# from src.database.db_connection import get_db
from src.database.db_creation import Employee
from src.services.auth import get_current_user,get_db
from src.database.db_creation import User  # ORM User model

from src.models.models import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeResponse
)

router = APIRouter(
    prefix="/api/v1/employees",
    tags=["Employees"]
)

# ==================== ADMIN DEPENDENCY ====================
def admin_only(current_user: User = Depends(get_current_user)):
    if current_user.role.lower() != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required"
        )
    return current_user


# ==================== CREATE EMPLOYEE ====================
@router.post(
    "",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_employee(
    employee: EmployeeCreate,
    _: User = Depends(admin_only),
    db: Session = Depends(get_db)
):
    existing_employee = db.query(Employee).filter(
        (Employee.emp_id == employee.emp_id) |
        (Employee.email == employee.email)
    ).first()

    if existing_employee:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Employee with this ID or email already exists"
        )

    db_employee = Employee(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee


# ==================== GET ALL EMPLOYEES ====================
@router.get(
    "",
    response_model=list[EmployeeResponse],
    status_code=status.HTTP_200_OK
)
async def get_all_employees(
    _: User = Depends(admin_only),
    db: Session = Depends(get_db)
):
    return db.query(Employee).all()


# ==================== GET EMPLOYEE BY ID ====================
@router.get(
    "/{emp_id}",
    response_model=EmployeeResponse,
    status_code=status.HTTP_200_OK
)
async def get_employee_by_id(
    emp_id: str,
    _: User = Depends(admin_only),
    db: Session = Depends(get_db)
):
    employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


# ==================== UPDATE EMPLOYEE ====================
@router.put(
    "/{emp_id}",
    response_model=EmployeeResponse,
    status_code=status.HTTP_200_OK
)
async def update_employee(
    emp_id: str,
    employee_update: EmployeeUpdate,
    _: User = Depends(admin_only),
    db: Session = Depends(get_db)
):
    employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    update_data = employee_update.model_dump(exclude_unset=True)

    # Optional: validate manager exists
    if "mgr_id" in update_data and update_data["mgr_id"]:
        manager = db.query(Employee).filter(
            Employee.emp_id == update_data["mgr_id"]
        ).first()
        if not manager:
            raise HTTPException(
                status_code=400,
                detail="Manager with given ID does not exist"
            )

    for field, value in update_data.items():
        setattr(employee, field, value)

    db.commit()
    db.refresh(employee)

    return employee


# ==================== DELETE EMPLOYEE ====================
@router.delete(
    "/{emp_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_employee(
    emp_id: str,
    _: User = Depends(admin_only),
    db: Session = Depends(get_db)
):
    employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(employee)
    db.commit()
    return None
