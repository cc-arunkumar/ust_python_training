from src.models.employee_pydentic import EmployeeDirectory
from src.crud.employee_inventory import count_employees,get_all_employee,get_all_employees_status,create_employee,delete_employee,update_employee_by_id,update_employee_status,search_employees,get_employee_by_id
from src.auth.jwt_auth import get_current_user
from src.models.login_model import User
import pymysql
from fastapi import FastAPI, HTTPException,Depends,APIRouter



employee_router = APIRouter(prefix="/employees") 


@employee_router.post("/create")
def add_employee(emp: EmployeeDirectory,current_user: User = Depends(get_current_user)):
    try:
        return create_employee(emp)
    except Exception as e:
        print(f"Error in create_employee: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@employee_router.get("/list")
def list_employees(status: str | None = None,current_user: User = Depends(get_current_user)):
    return get_all_employees_status(status)

@employee_router.get("/list")
def list_employees(current_user: User = Depends(get_current_user)):
    return get_all_employee()

@employee_router.get("/count")
def count(current_user: User = Depends(get_current_user)):
    return count_employees()

@employee_router.get("/search")
def search(column_name: str, keyword: str,current_user: User = Depends(get_current_user)):
    return search_employees(column_name, keyword)

@employee_router.get("/{id}")
def read_employee(id: int,current_user: User = Depends(get_current_user)):
    result = get_employee_by_id(id)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result

@employee_router.put("/{id}")
def update_employee(id: int, emp: EmployeeDirectory,current_user: User = Depends(get_current_user)):
    result = update_employee_by_id(id, emp)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result

@employee_router.patch("/{id}/status")
def update_status(id: int, new_status: str,current_user: User = Depends(get_current_user)):
    result = update_employee_status(id, new_status)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result

@employee_router.delete("/{id}")
def remove_employee(id: int,current_user: User = Depends(get_current_user)):
    result = delete_employee(id)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result