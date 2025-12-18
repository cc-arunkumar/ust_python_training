# app/api/v1/routes/employees.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.mysql import get_db
from app.models.sql_models import Employee
from app.schemas.employee_schema import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from app.api.deps import get_current_user

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

# ---------------- GET All Employees ----------------
@router.get("/", response_model=List[EmployeeResponse])
def get_all_employees(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    if "admin" not in current_user["roles"]:
        raise HTTPException(status_code=403, detail="Only admin can view employees")
    return db.query(Employee).all()

# ---------------- GET Employee by ID ----------------
@router.get("/{emp_id}", response_model=EmployeeResponse)
def get_employee(emp_id: str, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

# ---------------- CREATE Employee ----------------
@router.post("/", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    if "admin" not in current_user["roles"]:
        raise HTTPException(status_code=403, detail="Only admin can create employee")

    existing = db.query(Employee).filter(Employee.email == employee.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    last_employee = db.query(Employee).order_by(Employee.id.desc()).first()
    new_emp_id = f"E{int(last_employee.emp_id[1:]) + 1:04d}" if last_employee else "E1001"

    if employee.manager_id:
        manager = db.query(Employee).filter(Employee.emp_id == employee.manager_id).first()
        if not manager:
            raise HTTPException(status_code=400, detail="Manager does not exist")

    new_employee = Employee(
        emp_id=new_emp_id,
        name=employee.name,
        email=employee.email,
        designation=employee.designation,
        manager_id=employee.manager_id
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

# ---------------- UPDATE Employee by ID ----------------
@router.put("/{emp_id}", response_model=EmployeeResponse)
def update_employee(emp_id: str, employee: EmployeeUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    if "admin" not in current_user["roles"]:
        raise HTTPException(status_code=403, detail="Only admin can update employee")

    db_employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    # Update fields if provided
    if employee.name is not None:
        db_employee.name = employee.name
    if employee.email is not None:
        # Check if email already exists
        existing = db.query(Employee).filter(Employee.email == employee.email, Employee.emp_id != emp_id).first()
        if existing:
            raise HTTPException(status_code=400, detail="Email already exists")
        db_employee.email = employee.email
    if employee.designation is not None:
        db_employee.designation = employee.designation
    if employee.manager_id is not None:
        manager = db.query(Employee).filter(Employee.emp_id == employee.manager_id).first()
        if not manager:
            raise HTTPException(status_code=400, detail="Manager does not exist")
        db_employee.manager_id = employee.manager_id

    db.commit()
    db.refresh(db_employee)
    return db_employee

# ---------------- DELETE Employee by ID ----------------
@router.delete("/{emp_id}", response_model=dict)
def delete_employee(emp_id: str, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    if "admin" not in current_user["roles"]:
        raise HTTPException(status_code=403, detail="Only admin can delete employee")

    db_employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(db_employee)
    db.commit()
    return {"message": f"Employee {emp_id} deleted successfully"}
