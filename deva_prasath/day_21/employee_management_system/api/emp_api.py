from fastapi import APIRouter, HTTPException,Depends
from typing import List, Optional  
from models.emp_models import Employee
from crud.emp_crud import ( 
    fetch_employee_by_id,
    create_emp,
    modify_employee,
    remove_employee,
)

# Router for handling all /employees related API endpoints
employee_router = APIRouter(prefix="/employees")

# Endpoint: Get a single employee by ID
@employee_router.get("/{employee_id}")
def get_employee(employee_id: int):
    try:
        employee = fetch_employee_by_id(employee_id)  # Fetch employee by ID from database
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")  # If no record found
        return employee  # Return employee data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Handle unexpected errors


# Endpoint: Create a new employee
@employee_router.post("/create")
def create_employee_endpoint(employee: Employee):
    try:
        create_emp(employee)  # Insert employee into database
        return employee  # Return the created employee data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Handle errors (ex: email already exists)
    

# Endpoint: Update an existing employee by ID
@employee_router.put("/{employee_id}")
async def update_employee_endpoint(employee_id: int, employee :Employee):
    try:
        modify_employee(employee_id, employee)  # Update employee data
        return employee  # Return updated data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Handle update errors


# Endpoint: Delete an employee by ID
@employee_router.delete("/{employee_id}")
async def delete_employee_endpoint(employee_id: int):
    try:
        remove_employee(employee_id)  # Delete employee from database
        return {"message": "Employee deleted successfully"}  # Success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Handle deletion errors
