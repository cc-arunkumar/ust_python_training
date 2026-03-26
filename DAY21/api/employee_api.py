from fastapi import APIRouter
from crud.employee_crud import *
from model.employee_model import EmployeeModel

router=APIRouter()

@router.post("/employee")
def create(emp:EmployeeModel):
    return create_employee(
        emp.first_name,emp.last_name,emp.email,emp.position,emp.salary,emp.hire_date
    )
    
@router.get("/employee/{employee_id}")
def get_employee(employee_id:int):
    return get_employee_by_id(employee_id)

@router.put("/employee/{employee_id}")
def update_employee(employee_id:int,emp:EmployeeModel):
    return update_employee_by_id(employee_id,emp.first_name,emp.last_name,emp.email,emp.position,emp.salary,emp.hire_date)

@router.delete("/employee/{employee_id}")
def delete_employee(employee_id:int):
    return delete_employee_by_id(employee_id)
