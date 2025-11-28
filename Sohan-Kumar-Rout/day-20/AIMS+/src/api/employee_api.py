from fastapi import APIRouter, Depends, HTTPException
from auth.jwt_auth import User, get_curr_user
from crud.employee_crud import (
    create_employee,
    get_all_employees,
    count_employees,
    search_employees,
    get_employee_by_id,
    update_employee_by_id,
    update_employee_status,
    delete_employee,
)
from models.employee_model import Employee

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.get("/count")
def count(current_user: User = Depends(get_curr_user)):
    return count_employees()

@router.post("/create")
def add_employee(emp: Employee, current_user: User = Depends(get_curr_user)):
    try:
        return create_employee(emp)
    except Exception as e:
        print(f"Error in create_employee: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/list")
def list_employees(status: str | None = None, current_user: User = Depends(get_curr_user)):
    return get_all_employees(status)



@router.get("/search")
def search(column_name: str, keyword: str, current_user: User = Depends(get_curr_user)):
    return search_employees(column_name, keyword)

@router.get("/{id}")
def read_employee(id: int, current_user: User = Depends(get_curr_user)):
    result = get_employee_by_id(id)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result

@router.put("/{id}")
def update_employee(id: int, emp: Employee, current_user: User = Depends(get_curr_user)):
    result = update_employee_by_id(id, emp)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result

@router.patch("/{id}/status")
def update_status(id: int, new_status: str, current_user: User = Depends(get_curr_user)):
    result = update_employee_status(id, new_status)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result

@router.delete("/{id}")
def remove_employee(id: int, current_user: User = Depends(get_curr_user)):
    result = delete_employee(id)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result
