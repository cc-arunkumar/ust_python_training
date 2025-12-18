from typing import Optional, Dict, Any, Union
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.params import Query
from sqlalchemy.orm import Session
from database.connection import get_db
from schemas.employee import EmployeeCreate, EmployeeResponse
from services.employee_service import (
    get_employees, get_employee_by_id, create_employee,
    update_employee, delete_employee
)
from database.mongodb import log_activity
from utils.auth import role_guard

router = APIRouter(prefix="/api", tags=["Employees"])




# --- Endpoints ---
@router.get("/employees", response_model=list[EmployeeResponse])
def get_all(
    db: Session = Depends(get_db),
    skip: Optional[int] = Query(None, ge=0, description="Number of records to skip"),
    limit: Optional[int] = Query(None, gt=0, description="Maximum number of records to return"),
    current=Depends(role_guard("Admin"))
):
    """Get all employees with optional pagination."""
    if skip is not None or limit is not None:
        return get_employees(db, skip=skip or 0, limit=limit or 100)
    return get_employees(db, skip=0, limit=None)

@router.get("/employees/{emp_id}", response_model=EmployeeResponse)
def get_by_id(
    emp_id: int,
    db: Session = Depends(get_db),
    current=Depends(role_guard(["Manager", "Employee"]))
):
    emp = get_employee_by_id(db, emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@router.post("/employees", response_model=EmployeeResponse)
def create(
    emp: EmployeeCreate,
    db: Session = Depends(get_db),
    current=Depends(role_guard("Admin"))
):
    created = create_employee(db, emp)
    log_activity(current["user"].emp_id, "create_employee", created.emp_id)
    return created

@router.put("/employees/{emp_id}", response_model=EmployeeResponse)
def update(
    emp_id: int,
    emp: EmployeeCreate,
    db: Session = Depends(get_db),
    current=Depends(role_guard("Admin"))
):
    updated = update_employee(db, emp_id, emp)
    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found")
    log_activity(current["user"].emp_id, "update_employee", emp_id)
    return updated

@router.delete("/employees/{emp_id}")
def delete(
    emp_id: int,
    db: Session = Depends(get_db),
    current=Depends(role_guard("Admin"))
):
    if not delete_employee(db, emp_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    log_activity(current["user"].emp_id, "delete_employee", emp_id)
    return {"message": "Employee deleted"}
