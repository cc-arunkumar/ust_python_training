"""from fastapi import APIRouter, Depends,Query
from sqlalchemy.orm import Session
from app.models.employee import Employee
from app.database.connection import get_db
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeResponse
)
from app.services.employee_service import (
    create_employee,
    get_all_employees,
    get_employee,
    update_employee,
    delete_employee
)
from app.utils.pagination import paginate

from app.utils.auth_dependency import require_role, get_current_user
# app/routers/employee_router.py

router = APIRouter(
    prefix="/api/employees",
    tags=["Employees"]
)

# -----------------------------
# CREATE EMPLOYEE (ADMIN ONLY)
# -----------------------------
@router.post(
    "/",
    response_model=EmployeeResponse,
    dependencies=[Depends(require_role("admin"))]
)
def add_employee(
    data: EmployeeCreate,
    db: Session = Depends(get_db)
):
    return create_employee(db, data)


# -----------------------------
# GET ALL EMPLOYEES
# -----------------------------
@router.get("/")
def get_all_employees(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    query = db.query(Employee).order_by(Employee.emp_id.desc())
    return paginate(query, page, limit)

# -----------------------------
# GET EMPLOYEE BY ID
# -----------------------------
@router.get(
    "/{emp_id}",
    response_model=EmployeeResponse
)
def get_employee_by_id(
    emp_id: int,
    db: Session = Depends(get_db)
):
    return get_employee(db, emp_id)


# -----------------------------
# UPDATE EMPLOYEE (ADMIN ONLY)
# -----------------------------
@router.put(
    "/{emp_id}",
    response_model=EmployeeResponse,
    dependencies=[Depends(require_role("admin"))]
)
def update_emp(
    emp_id: int,
    data: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    return update_employee(db, emp_id, data)


# -----------------------------
# DELETE EMPLOYEE (ADMIN ONLY)
# -----------------------------
@router.delete(
    "/{emp_id}",
    dependencies=[Depends(require_role("admin"))]
)
def remove_employee(
    emp_id: int,
    db: Session = Depends(get_db)
):
    return delete_employee(db, emp_id)
"""


from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from app.services.employee_service import create_employee, get_employee, update_employee, delete_employee
from app.utils.pagination import paginate
from app.utils.auth import require_roles, get_current_user
from app.models.employee import Employee

router = APIRouter(prefix="/api/employees", tags=["Employees"])

@router.post("/", response_model=EmployeeResponse, dependencies=[Depends(require_roles("admin"))])
def add_employee(data: EmployeeCreate, db: Session = Depends(get_db)):
    return create_employee(db, data)

@router.get("/")
def get_all_employees(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    query = db.query(Employee).order_by(Employee.emp_id.desc())
    return paginate(query, page, limit)

@router.get("/{emp_id}", response_model=EmployeeResponse)
def get_employee_by_id(emp_id: int, db: Session = Depends(get_db)):
    return get_employee(db, emp_id)

@router.put("/{emp_id}", response_model=EmployeeResponse, dependencies=[Depends(require_roles("admin"))])
def update_emp(emp_id: int, data: EmployeeUpdate, db: Session = Depends(get_db)):
    return update_employee(db, emp_id, data)

@router.delete("/{emp_id}", dependencies=[Depends(require_roles("admin"))])
def remove_employee(emp_id: int, db: Session = Depends(get_db)):
    return delete_employee(db, emp_id)