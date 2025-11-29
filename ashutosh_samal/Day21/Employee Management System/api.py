from fastapi import APIRouter, HTTPException,Depends
from typing import List, Optional  
from models import Employee
from crud import ( 
    fetch_employee_by_id,
    create_new_employee,
    modify_employee,
    remove_employee,
)

employee_router = APIRouter(prefix="/employees")

# Endpoint to fetch a specific employee by ID
@employee_router.get("/{employee_id}")
def get_employee(employee_id: int):
    try:
        employee = fetch_employee_by_id(employee_id)  # Fetch employee by ID
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")  # Return error if not found
        return employee
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure


# Endpoint to create a new employee
@employee_router.post("/create")
def create_employee_endpoint(employee: Employee):
    try:
        create_new_employee(employee)  # Call CRUD function to create employee
        return employee  # Return created employee
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure
    

# Endpoint to update an existing employee by ID
@employee_router.put("/{employee_id}")
async def update_employee_endpoint(employee_id: int, employee :Employee):
    try:
        modify_employee(employee_id, employee)  # Update employee using the provided ID and data
        return employee  # Return updated employee
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Endpoint to delete an employee by ID
@employee_router.delete("/{employee_id}")
async def delete_employee_endpoint(employee_id: int):
    try:
        remove_employee(employee_id)  # Delete employee using the provided ID
        return {"message": "Employee deleted successfully"}  # Return success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
