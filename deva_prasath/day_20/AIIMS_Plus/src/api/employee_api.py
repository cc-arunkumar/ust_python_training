from fastapi import APIRouter, HTTPException,Depends # Import FastAPI components
from typing import List, Optional  # Import typing components for type hinting
from ..models.employee_model import EmployeeCreate  # Import EmployeeCreate model from employee_model
from ..crud.employee_crud import (
    get_employees,  # Import CRUD operations for employees
    get_employee_by_id,
    create_employee,
    update_employee,
    update_employee_status,
    delete_employee,
    search_employees,
    count_employees
)
from ..auth.auth_jwt_token import get_current_user
employee_router = APIRouter(prefix="/employees",tags=["Employee"])  # Create a new router for employee-related endpoints


# Endpoint to list employees, optionally filtered by status
@employee_router.get("/list")
def list_employees(status: Optional[str] = None,current_user: dict = Depends(get_current_user)):
    try:
        employees = get_employees(status)  # Fetch employees based on status
        return employees
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure



# Endpoint to search for employees based on a keyword
@employee_router.get("/search")
async def search_employees_endpoint(keyword: str,current_user: dict = Depends(get_current_user)):
    try:
        employees = search_employees(keyword)  # Search for employees by keyword
        return employees
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure


# Endpoint to get the count of total employees
@employee_router.get("/count")
async def count_employees_endpoint(current_user: dict = Depends(get_current_user)):
    try:
        count = count_employees()  # Get total employee count
        return {"total_employees": count}  # Return employee count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure


# Endpoint to fetch a specific employee by ID
@employee_router.get("/{employee_id}")
def get_employee(employee_id: int,current_user: dict = Depends(get_current_user)):
    try:
        employee = get_employee_by_id(employee_id)  # Fetch employee by ID
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")  # Return error if not found
        return employee
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure


# Endpoint to create a new employee
@employee_router.post("/create")
def create_employee_endpoint(employee: EmployeeCreate,current_user: dict = Depends(get_current_user)):
    try:
        create_employee(employee)  # Call CRUD function to create employee
        return employee  # Return created employee
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure


# Endpoint to update an existing employee by ID
@employee_router.put("/{employee_id}")
async def update_employee_endpoint(employee_id: int, employee: EmployeeCreate,current_user: dict = Depends(get_current_user)):
    try:
        update_employee(employee_id, employee)  # Update employee using the provided ID and data
        return employee  # Return updated employee
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure



# Endpoint to update the status of an employee
@employee_router.patch("/{employee_id}/status")
async def update_employee_status_endpoint(employee_id: int, status: str,current_user: dict = Depends(get_current_user)):
    try:
        update_employee_status(employee_id, status)  # Update employee status
        return {"message": "Employee status updated successfully"}  # Return success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure


# Endpoint to delete an employee by ID
@employee_router.delete("/{employee_id}")
async def delete_employee_endpoint(employee_id: int,current_user: dict = Depends(get_current_user)):
    try:
        delete_employee(employee_id)  # Delete employee using the provided ID
        return {"message": "Employee deleted successfully"}  # Return success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure


