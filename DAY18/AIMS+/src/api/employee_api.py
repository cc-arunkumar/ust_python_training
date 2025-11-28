from fastapi import APIRouter, Query, Depends
from src.models.employee_model import EmployeeCreate, EmployeeUpdate
from src.crud.employee_crud import *
from src.auth.auth import get_curr_user
from src.models.login_model import User

emp_router = APIRouter(prefix="/employees", tags=["Employees"])

@emp_router.post("/create")
def create(emp: EmployeeCreate, current_user: User = Depends(get_curr_user)):
    return create_employee(
        emp.emp_code, emp.full_name, emp.email, emp.phone,
        emp.department, emp.location, emp.join_date, emp.status
    )

@emp_router.get("/list")
def list_all(status: str = None, current_user: User = Depends(get_curr_user)):
    if status:
        return get_all_employees(status)
    else:
        return get_all_employees()

@emp_router.get("/count")
def count(current_user: User = Depends(get_curr_user)):
    return count_employees()

@emp_router.get("/search")
def search(keyword: str = Query(...), current_user: User = Depends(get_curr_user)):
    return search_employees(keyword)

@emp_router.patch("/{id}/status")
def patch_status(id: int, status: str = Query(...), current_user: User = Depends(get_curr_user)):
    return update_status_only(id, status)

@emp_router.get("/{id}")
def get_one(id: int, current_user: User = Depends(get_curr_user)):
    return get_employee_by_id(id)

@emp_router.put("/{id}")
def update(id: int, emp: EmployeeUpdate, current_user: User = Depends(get_curr_user)):
    return update_employee(
        id, emp.emp_code, emp.full_name, emp.email, emp.phone,
        emp.department, emp.location, emp.join_date, emp.status
    )

@emp_router.delete("/{id}")
def delete(id: int, current_user: User = Depends(get_curr_user)):
    return delete_employee(id)
