from fastapi import APIRouter, HTTPException, Depends
from models.employee_model import Employee
from crud.employee_crud import (
    create_employee,
    get_all_employee,
    get_employee_by_id,
    delete_employee,
    update_employee
)
from auth.employee_auth import get_current_user

router = APIRouter(
    prefix="/employee",
    tags=["Employee"]
)

@router.get("/")
def getemp(current_user: str = Depends(get_current_user)):
    try:
        return get_all_employee()
    except Exception:
        raise HTTPException(status_code=500, detail="Error fetching employees")

@router.get("/{employee_id}")
def getbyid(employee_id: int, current_user: str = Depends(get_current_user)):
    try:
        return get_employee_by_id(employee_id)
    except Exception:
        raise HTTPException(status_code=500, detail="Error fetching employee")

@router.post("/")
def create(emp: Employee, current_user: str = Depends(get_current_user)):
    try:
        return create_employee(emp)
    except Exception:
        raise HTTPException(status_code=500, detail="Error creating employee")

@router.put("/{employee_id}")
def update(employee_id: int, emp: Employee, current_user: str = Depends(get_current_user)):
    try:
        return update_employee(employee_id, emp)
    except Exception:
        raise HTTPException(status_code=500, detail="Error updating employee")

@router.delete("/{employee_id}")
def delete(employee_id: int, current_user: str = Depends(get_current_user)):
    try:
        return delete_employee(employee_id)
    except Exception:
        raise HTTPException(status_code=500, detail="Error deleting employee")
