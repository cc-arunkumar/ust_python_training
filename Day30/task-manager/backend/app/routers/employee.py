from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.employee import EmployeeCreate, EmployeeResponse
from app.services.employee_service import create_employee
from app.database import get_db 
from typing import List
from app.core.security import get_current_user



from app.schemas.employee import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeResponse
)
from app.services.employee_service import (
    create_employee,
    get_all_employees,
    get_employee_by_id,
    update_employee,
    delete_employee
)
from app.database import get_db
from app.core.security import get_current_user


router = APIRouter(prefix="/employees", tags=["Employees"])



# ----additional----

from fastapi import HTTPException

def admin_only(current_user: dict):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin only")
# ----additional----


# @router.post("/", response_model=EmployeeResponse)
# def create_employee_api(employee: EmployeeCreate, db: Session = Depends(get_db)):
#     return create_employee(db, employee)


# # GET ALL
# @router.get("/", response_model=List[EmployeeResponse])
# def get_all_employees_api(
#     db: Session = Depends(get_db),
#     current_user: dict = Depends(get_current_user)
# ):
#     return get_all_employees(db)


# # GET BY ID
# @router.get("/{emp_id}", response_model=EmployeeResponse)
# def get_employee_api(
#     emp_id: int,
#     db: Session = Depends(get_db),
#     current_user: dict = Depends(get_current_user)
# ):
#     return get_employee_by_id(db, emp_id)


# # UPDATE
# @router.put("/{emp_id}", response_model=EmployeeResponse)
# def update_employee_api(
#     emp_id: int,
#     employee: EmployeeUpdate,
#     db: Session = Depends(get_db),
#     current_user: dict = Depends(get_current_user)
# ):
#     return update_employee(db, emp_id, employee)


# # DELETE
# @router.delete("/{emp_id}")
# def delete_employee_api(
#     emp_id: int,
#     db: Session = Depends(get_db),
#     current_user: dict = Depends(get_current_user)
# ):
#     return delete_employee(db, emp_id)



@router.post("/", response_model=EmployeeResponse)
def create_employee_api(
    employee: EmployeeCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    admin_only(current_user)
    return create_employee(db, employee)


@router.get("/", response_model=List[EmployeeResponse])
def get_all_employees_api(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] not in ["admin"] and "manager" not in current_user["role"]:
        raise HTTPException(403, "Access denied")
    return get_all_employees(db)


@router.get("/{emp_id}", response_model=EmployeeResponse)
def get_employee_api(
    emp_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] not in ["admin"] and "manager" not in current_user["role"]:
        raise HTTPException(403, "Access denied")
    return get_employee_by_id(db, emp_id)


@router.put("/{emp_id}", response_model=EmployeeResponse)
def update_employee_api(
    emp_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    admin_only(current_user)
    return update_employee(db, emp_id, employee)


@router.delete("/{emp_id}")
def delete_employee_api(
    emp_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    admin_only(current_user)
    return delete_employee(db, emp_id)


