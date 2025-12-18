# routes/employee_routes.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from pydantic import BaseModel
from database import get_db
from models.models import Employee, User, RoleEnum
from deps import get_current_user
from mongo import log_activity  # optional audit logging

router = APIRouter(tags=["Employees"])

def require_admin(current_user: User):
    role = current_user.role if isinstance(current_user.role, RoleEnum) else RoleEnum(current_user.role)
    if role != RoleEnum.ADMIN:
        raise HTTPException(status_code=403, detail="Only ADMIN can perform this action")
    return role

# ---------- Schemas ----------
class EmployeeCreate(BaseModel):
    name: str
    designation: Optional[str] = None
    manager_id: Optional[int] = None

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    designation: Optional[str] = None
    manager_id: Optional[int] = None

# ---------- Routes ----------

# Create employee (ADMIN only)
@router.post("/", response_model=dict)
def create_employee(
    payload: EmployeeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    require_admin(current_user)

    emp = Employee(
        name=payload.name,
        designation=payload.designation,
        manager_id=payload.manager_id,
    )
    db.add(emp)
    db.commit()
    db.refresh(emp)

    log_activity(current_user.user_id, "employee_created", {"emp_id": emp.emp_id})

    return {
        "message": "Employee created",
        "employee": {
            "emp_id": emp.emp_id,
            "name": emp.name,
            "designation": emp.designation,
            "manager_id": emp.manager_id,
        },
    }

# Get all employees (ADMIN only)
@router.get("/", response_model=dict)
def get_all_employees(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    q: Optional[str] = Query(None, description="Search by name"),
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
):
    require_admin(current_user)

    query = db.query(Employee)
    if q:
        query = query.filter(Employee.name.ilike(f"%{q}%"))
    total = query.count()
    employees = query.order_by(Employee.emp_id).offset(offset).limit(limit).all()

    log_activity(current_user.user_id, "employee_list", {"count": len(employees), "total": total, "q": q})

    def serialize(e: Employee):
        return {
            "emp_id": e.emp_id,
            "name": e.name,
            "designation": e.designation,
            "manager_id": e.manager_id,
        }

    return {"total": total, "items": [serialize(e) for e in employees]}

# Get employee by id (ADMIN only)
@router.get("/{emp_id}", response_model=dict)
def get_employee_by_id(
    emp_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    require_admin(current_user)

    emp = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    log_activity(current_user.user_id, "employee_get", {"emp_id": emp_id})

    return {
        "emp_id": emp.emp_id,
        "name": emp.name,
        "designation": emp.designation,
        "manager_id": emp.manager_id,
    }

# Update employee (ADMIN only)
@router.patch("/{emp_id}", response_model=dict)
def update_employee(
    emp_id: int,
    payload: EmployeeUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    require_admin(current_user)

    emp = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    if payload.name is not None:
        emp.name = payload.name
    if payload.designation is not None:
        emp.designation = payload.designation
    if payload.manager_id is not None:
        emp.manager_id = payload.manager_id

    db.commit()
    db.refresh(emp)

    log_activity(current_user.user_id, "employee_updated", {"emp_id": emp.emp_id})

    return {
        "message": "Employee updated",
        "employee": {
            "emp_id": emp.emp_id,
            "name": emp.name,
            "designation": emp.designation,
            "manager_id": emp.manager_id,
        },
    }

# Delete employee (ADMIN only)
@router.delete("/{emp_id}", response_model=dict)
def delete_employee(
    emp_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    require_admin(current_user)

    emp = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(emp)
    db.commit()

    log_activity(current_user.user_id, "employee_deleted", {"emp_id": emp_id})

    return {"message": "Employee deleted", "emp_id": emp_id}
