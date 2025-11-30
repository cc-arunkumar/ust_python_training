from fastapi import HTTPException, APIRouter
from src.crud.employee_crud import (
    create_employees,
    get_all_employees,
    get_employees_by_id,
    update_employees,
    delete_employee
)
from src.models.employee_management import Employee

employee_router = APIRouter(prefix="/employee")

@employee_router.post("/create")
def add_employee(emp: Employee):
    try:
        return create_employees(emp)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@employee_router.get("")
def get_employees():
    try:
        return get_all_employees()
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@employee_router.get("/{id}")
def get_employee_id(id: int):
    try:
        return get_employees_by_id(id)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@employee_router.put("/update/{id}")
def update_employee(id: int, emp: Employee):
    try:
        return update_employees(id, emp)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@employee_router.delete("/{id}")
def remove_employee(id: int):
    try:
        return delete_employee(id)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
