from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.employee import Employee
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeOut
)

router = APIRouter(prefix="/employees", tags=["Employees"])


# 🔹 GET ALL EMPLOYEES (ADMIN ONLY)
@router.get("/", response_model=List[EmployeeOut])
def get_all_employees(
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    if user.get("active_role") != "ADMIN":
        raise HTTPException(status_code=403, detail="Admin only")

    return db.query(Employee).all()


# 🔹 GET EMPLOYEE BY ID
@router.get("/{emp_id}", response_model=EmployeeOut)
def get_employee(
    emp_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    if user.get("active_role") != "ADMIN":
        raise HTTPException(status_code=403)

    emp = db.query(Employee).filter(Employee.e_id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404)

    return emp


# 🔹 CREATE EMPLOYEE
@router.post("/", response_model=EmployeeOut)
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    if user.get("active_role") != "ADMIN":
        raise HTTPException(status_code=403)

    db_emp = Employee(**employee.dict())
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)

    return db_emp


# 🔹 UPDATE EMPLOYEE
@router.put("/{emp_id}", response_model=EmployeeOut)
def update_employee(
    emp_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    if user.get("active_role") != "ADMIN":
        raise HTTPException(status_code=403)

    emp = db.query(Employee).filter(Employee.e_id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404)

    for key, value in employee.dict(exclude_unset=True).items():
        setattr(emp, key, value)

    db.commit()
    db.refresh(emp)
    return emp


# 🔹 DELETE EMPLOYEE
@router.delete("/{emp_id}")
def delete_employee(
    emp_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    if user.get("active_role") != "ADMIN":
        raise HTTPException(status_code=403)

    emp = db.query(Employee).filter(Employee.e_id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404)

    db.delete(emp)
    db.commit()
    return {"message": "Employee deleted"}
