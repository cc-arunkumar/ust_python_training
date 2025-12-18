from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from services.database import SessionLocal
from services.employee_service import *
from schemas.employee import EmployeeSchema
from utils.authorization import require_permission

emp_router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


# ---------------- DB Dependency ----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- GET ALL (ADMIN,MANAGER) ----------------
@emp_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(require_permission("employee:read_all"))]
)
def get_all_employees(db: Session = Depends(get_db)):
    return get_employees(db)



# ---------------- GET BY ID (ADMIN,MANAGER,EMPLOYEE) ----------------
@emp_router.get(
    "/{emp_id}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(require_permission("employee:read_one"))]
)
def get_single_employee(emp_id: str, db: Session = Depends(get_db)):
    emp = get_employee(db, emp_id)
    if not emp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )
    return emp



# ---------------- CREATE (ADMIN ONLY) ----------------
@emp_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission("employee:create"))]
)
def create_new_employee(emp: EmployeeSchema, db: Session = Depends(get_db)):
    existing = get_employee(db, emp.emp_id)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Employee already exists"
        )
    return create_employee(db, emp)


# ---------------- UPDATE (ADMIN ONLY) ----------------
@emp_router.put(
    "/{emp_id}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(require_permission("employee:update"))]
)
def update_existing_employee(
    emp_id: str,
    emp: EmployeeSchema,
    db: Session = Depends(get_db)
):
    updated = update_employee(db, emp_id, emp)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )
    return updated


# ---------------- DELETE (ADMIN ONLY) ----------------
@emp_router.delete(
    "/{emp_id}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(require_permission("employee:delete"))]
)
def delete_existing_employee(emp_id: str, db: Session = Depends(get_db)):
    deleted = delete_employee(db, emp_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )
    return {"message": "Employee deleted successfully"}


# ---------------- ASSIGN EMPLOYEE (ADMIN ONLY) ----------------
@emp_router.patch(
    "/{emp_id}/assign",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(require_permission("employee:assign"))]
)
def assign_employee(
    emp_id: str,
    mgr_id: str,
    db: Session = Depends(get_db)
):
    emp = get_employee(db, emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    emp.mgr_id = mgr_id
    db.commit()
    db.refresh(emp)
    return emp
