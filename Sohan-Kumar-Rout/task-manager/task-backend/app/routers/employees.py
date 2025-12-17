from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.deps import get_db, get_current_user

router = APIRouter(prefix="/api/employees", tags=["Employees"])


# ---------------- CREATE EMPLOYEE ----------------
@router.post("/", response_model=schemas.EmployeeOut)
def create_employee(
    employee: schemas.EmployeeCreate,
    current=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    role = current["role"]
    emp_id = int(current["emp_id"])

    # Only Admin or Manager can create employees
    if role not in ["Admin", "Manager"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed")

    # If Manager creates employee → force manager_id = manager.emp_id
    if role == "Manager":
        employee.manager_id = emp_id

    existing = (
        db.query(models.Employee)
        .filter(models.Employee.email == employee.email)
        .first()
    )
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_emp = models.Employee(**employee.dict())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp


# ---------------- LIST EMPLOYEES ----------------
@router.get("/", response_model=List[schemas.EmployeeOut])
def list_employees(
    current=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    role = current["role"]
    emp_id = int(current["emp_id"])

    # Manager sees only employees under him
    if role == "Manager":
        return db.query(models.Employee).filter(
            models.Employee.manager_id == emp_id
        ).all()

    # Admin sees all
    if role == "Admin":
        return db.query(models.Employee).all()

    # Employees cannot see employee list
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed")


# ---------------- UPDATE EMPLOYEE ----------------
@router.put("/{emp_id}", response_model=schemas.EmployeeOut)
def update_employee(
    emp_id: int,
    data: schemas.EmployeeUpdate,
    current=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    role = current["role"]
    current_id = int(current["emp_id"])

    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    # Manager can update only his employees
    if role == "Manager" and emp.manager_id != current_id:
        raise HTTPException(status_code=403, detail="Not allowed")

    # Employees cannot update employees
    if role == "Employee":
        raise HTTPException(status_code=403, detail="Not allowed")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(emp, field, value)

    db.commit()
    db.refresh(emp)
    return emp


# ---------------- DELETE EMPLOYEE ----------------
@router.delete("/{emp_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(
    emp_id: int,
    current=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    role = current["role"]
    current_id = int(current["emp_id"])

    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    # Manager can delete only his employees
    if role == "Manager" and emp.manager_id != current_id:
        raise HTTPException(status_code=403, detail="Not allowed")

    # Employees cannot delete employees
    if role == "Employee":
        raise HTTPException(status_code=403, detail="Not allowed")

    db.delete(emp)
    db.commit()
    return
