import sys
import os

# Add the 'src' directory to sys.path dynamically
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))


from fastapi import FastAPI, HTTPException,APIRouter,Depends
from pydantic import BaseModel
from typing import List
from src.crud.employee_crud import (create_employee,get_all_employees,get_employees_by_status,get_employee_by_id,update_employee,update_employee_status,delete_employee,search_employees_by_keyword,get_employee_count)
from models.employee_model import Employee
# from src.auth.login_function import get_current_user,User
from src.auth.login_function import get_current_user,User

employee_router = APIRouter(prefix="/employee")

# 1. POST /employees/create - Create a new employee
@employee_router.post("/employees/create", response_model=Employee)
def create_employee_api(employee: Employee,current_user: User = Depends(get_current_user)):
    create_employee(employee)
    return employee


# 2. GET /employees/list - Get all employees
@employee_router.get("/employees/list",response_model=Employee)
def get_employees(current_user: User = Depends(get_current_user)):
    employees = get_all_employees()
    return employees


# 3. GET /employees/list?status= - Get employees by status
@employee_router.get("/employees/list", response_model=List[Employee])
def get_employees_by_status(status: str,current_user: User = Depends(get_current_user)):
    employees = get_employees_by_status(status)
    return employees


# 4. GET /employees/{id} - Get employee by ID
@employee_router.get("/employees/{id}", response_model=Employee)
def get_employee_by_id_api(id: int,current_user: User = Depends(get_current_user)):
    employee = get_employee_by_id(id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


# 5. PUT /employees/{id} - Update employee by ID
@employee_router.put("/employees/{id}", response_model=Employee)
def update_employee_api(id: int, employee: Employee,current_user: User = Depends(get_current_user)):
    update_employee(id, employee)
    return employee


# 6. PATCH /employees/{id}/status - Update only the status of an employee
@employee_router.patch("/employees/{id}/status")
def update_employee_status_api(id: int, status: str,current_user: User = Depends(get_current_user)):
    update_employee_status(id, status)
    return {"message": f"Employee {id} status updated to {status}"}


# 7. DELETE /employees/{id} - Delete an employee by ID
@employee_router.delete("/employees/{id}")
def delete_employee_api(id: int,current_user: User = Depends(get_current_user)):
    delete_employee(id)
    return {"message": f"Employee {id} deleted successfully"}


# 8. GET /employees/search?keyword= - Search employees by keyword
@employee_router.get("/employees/search", response_model=List[Employee])
def search_employees_api(keyword: str,current_user: User = Depends(get_current_user)):
    employees = search_employees_by_keyword(keyword)
    return employees


# 9. GET /employees/count - Get the count of employees in the database
@employee_router.get("/employees/count")
def count_employees_api(current_user: User = Depends(get_current_user)):
    count = get_employee_count()
    return {"count": count}
