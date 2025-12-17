from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.mysql import get_db
from app.models.sql_models import Employee
from app.schemas.employee_schema import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeResponse
)
from app.api.deps import get_current_user

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

# ---------------------------------------------------
# GET ALL EMPLOYEES (ACTIVE ONLY)
# ---------------------------------------------------
@router.get("/", response_model=List[EmployeeResponse])
def get_all_employees(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if "admin" not in current_user["roles"]:
        raise HTTPException(status_code=403, detail="Only admin can view employees")

    employees = db.query(Employee).filter(Employee.is_active == True).all()
    return employees


# ---------------------------------------------------
# GET EMPLOYEE BY EMP_ID
# ---------------------------------------------------
@router.get("/{emp_id}", response_model=EmployeeResponse)
def get_employee(
    emp_id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    employee = db.query(Employee).filter(
        Employee.emp_id == emp_id,
        Employee.is_active == True
    ).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


# ---------------------------------------------------
# CREATE EMPLOYEE (ADMIN ONLY)
# ---------------------------------------------------
@router.post("/", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if "admin" not in current_user["roles"]:
        raise HTTPException(status_code=403, detail="Only admin can create employee")

    # check email uniqueness
    existing = db.query(Employee).filter(Employee.email == employee.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    # generate emp_id
    last_employee = db.query(Employee).order_by(Employee.emp_id.desc()).first()
    if last_employee:
        last_number = int(last_employee.emp_id[1:])
        new_emp_id = f"E{last_number + 1}"
    else:
        new_emp_id = "E1001"

    # employee cannot be own manager
    if employee.manager_id == new_emp_id:
        raise HTTPException(
            status_code=400,
            detail="Employee cannot be their own manager"
        )

    # manager must exist and be active
    if employee.manager_id:
        manager = db.query(Employee).filter(
            Employee.emp_id == employee.manager_id,
            Employee.is_active == True
        ).first()
        if not manager:
            raise HTTPException(status_code=400, detail="Manager does not exist")

    new_employee = Employee(
        emp_id=new_emp_id,
        name=employee.name,
        email=employee.email,
        designation=employee.designation,
        manager_id=employee.manager_id,
        is_active=True            
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee


# ---------------------------------------------------
# UPDATE EMPLOYEE (ADMIN ONLY)
# ---------------------------------------------------
@router.put("/{emp_id}", response_model=EmployeeResponse)
def update_employee(
    emp_id: str,
    employee_data: EmployeeUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if "admin" not in current_user["roles"]:
        raise HTTPException(status_code=403, detail="Only admin can update employee")

    employee = db.query(Employee).filter(
        Employee.emp_id == emp_id,
        Employee.is_active == True
    ).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    # employee cannot be own manager
    if employee_data.manager_id == emp_id:
        raise HTTPException(status_code=400, detail="Employee cannot be own manager")

    # manager must exist
    if employee_data.manager_id:
        manager = db.query(Employee).filter(
            Employee.emp_id == employee_data.manager_id,
            Employee.is_active == True
        ).first()
        if not manager:
            raise HTTPException(status_code=400, detail="Manager does not exist")

    if employee_data.name is not None:
        employee.name = employee_data.name

    if employee_data.email is not None:
        employee.email = employee_data.email

    if employee_data.designation is not None:
        employee.designation = employee_data.designation

    if employee_data.manager_id is not None:
        employee.manager_id = employee_data.manager_id

    db.commit()
    db.refresh(employee)

    return employee


# ---------------------------------------------------
# SOFT DELETE EMPLOYEE (ADMIN ONLY)
# ---------------------------------------------------
@router.delete("/{emp_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(
    emp_id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if "admin" not in current_user["roles"]:
        raise HTTPException(status_code=403, detail="Only admin can delete employee")

    employee = db.query(Employee).filter(
        Employee.emp_id == emp_id,
        Employee.is_active == True
    ).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    employee.is_active = False   
    db.commit()

    return None
