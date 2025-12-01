from fastapi import APIRouter, HTTPException
from employee_inventory import Employee
from employee_crud import (
    create_employee,
    get_all_employees,
    get_employee_by_id,
    update_employee,
    delete_employee
)

# Create router instance
router = APIRouter(prefix="/employees", tags=["Employees"])

@router.post("/create")
def add_employee(emp: Employee):
    emp_id = create_employee(emp)
    return {"message": "Employee created successfully", "emp_id": emp_id}

@router.get("/list")
def list_employees():
    return get_all_employees()

@router.get("/{emp_id}")
def get_emp(emp_id: int):
    employee = get_employee_by_id(emp_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found.")
    return employee

@router.put("/{emp_id}")
def update_employee_record(emp_id: int, new_emp: Employee):
    updated = update_employee(emp_id, new_emp)
    if updated == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee updated successfully"}

@router.delete("/{emp_id}")
def remove_emp(emp_id: int):
    deleted = delete_employee(emp_id)
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted"}
