# routes/employee_routes.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
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

# Create employee (ADMIN only)
@router.post("/", response_model=dict)
def create_employee(
    name: str,
    email: str,
    department: Optional[str] = None,
    title: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    require_admin(current_user)

    # Unique email check
    exists = db.query(Employee).filter(Employee.email == email).first()
    if exists:
        raise HTTPException(status_code=409, detail="Employee with this email already exists")

    emp = Employee(
        name=name,
        email=email,
        department=department,
        title=title,
    )
    db.add(emp)
    db.commit()
    db.refresh(emp)

    log_activity(
        performed_by=current_user.user_id,
        action="employee_created",
        details={"emp_id": emp.emp_id, "name": emp.name, "email": emp.email},
    )

    return {"message": "Employee created", "employee": emp.to_dict() if hasattr(emp, "to_dict") else {
        "emp_id": emp.emp_id, "name": emp.name, "email": emp.email, "department": emp.department, "title": emp.title
    }}

# Get all employees (ADMIN only)
@router.get("/", response_model=dict)
def get_all_employees(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    q: Optional[str] = Query(None, description="Search by name or email"),
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
):
    require_admin(current_user)

    query = db.query(Employee)
    if q:
        query = query.filter((Employee.name.ilike(f"%{q}%")) | (Employee.email.ilike(f"%{q}%")))
    total = query.count()
    employees = query.order_by(Employee.emp_id).offset(offset).limit(limit).all()

    log_activity(current_user.user_id, "employee_list", {"count": len(employees), "total": total, "q": q})

    def serialize(e: Employee):
        return {
            "emp_id": e.emp_id,
            "name": e.name,
            "email": e.email,
            "department": e.department,
            "title": e.title,
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
        "email": emp.email,
        "department": emp.department,
        "title": emp.title,
    }

# Update employee (ADMIN only)
@router.patch("/{emp_id}", response_model=dict)
def update_employee(
    emp_id: int,
    name: Optional[str] = None,
    email: Optional[str] = None,
    department: Optional[str] = None,
    title: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    require_admin(current_user)

    emp = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    if email and email != emp.email:
        exists = db.query(Employee).filter(Employee.email == email).first()
        if exists:
            raise HTTPException(status_code=409, detail="Another employee with this email already exists")

    if name is not None:
        emp.name = name
    if email is not None:
        emp.email = email
    if department is not None:
        emp.department = department
    if title is not None:
        emp.title = title

    db.commit()
    db.refresh(emp)

    log_activity(
        performed_by=current_user.user_id,
        action="employee_updated",
        details={"emp_id": emp.emp_id, "name": emp.name, "email": emp.email, "department": emp.department, "title": emp.title},
    )

    return {"message": "Employee updated", "employee": {
        "emp_id": emp.emp_id,
        "name": emp.name,
        "email": emp.email,
        "department": emp.department,
        "title": emp.title,
    }}

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
