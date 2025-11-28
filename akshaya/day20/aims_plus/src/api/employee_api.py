from fastapi import FastAPI, HTTPException, UploadFile, File, Query, APIRouter, Depends
import csv, io
from src.models.employee_model import EmployeeModel
from ..auth.jwt_auth import get_current_user
from ..models.user_model import User
from src.crud.employee_crud import (
    create_employee_db, get_all_employees_db, list_employees_by_status_db,
    get_employee_by_id_db, update_employee_db, update_employee_status_db,
    delete_employee_db, search_employees_db, count_employees_db
)

# Create an instance of APIRouter for employee-related routes
emp_router = APIRouter()

# 1. Create employee endpoint
@emp_router.post("/employees/create")
def create_employee(employee: EmployeeModel, current_user: User = Depends(get_current_user)):
    """
    Creates a new employee record in the database.
    The employee data is provided in the request body.
    The user must be authenticated via JWT (Depends on `get_current_user`).
    """
    # Attempt to create the employee in the database
    if not create_employee_db(employee):
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "message": "Employee created successfully"}

# 2. Search employees endpoint
@emp_router.get("/employees/search")
def search_employees(keyword: str = Query(...), value: str = Query(...), current_user: User = Depends(get_current_user)):
    """
    Searches employees based on a provided keyword and value.
    The user must be authenticated via JWT.
    """
    # Perform the search based on provided keyword and value
    result = search_employees_db(keyword, value)

    # Handle case where the database query fails
    if result is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "data": result}

# 3. Count total employees endpoint
@emp_router.get("/employees/count")
def count_employees(current_user: User = Depends(get_current_user)):
    """
    Returns the total count of employees in the database.
    The user must be authenticated via JWT.
    """
    # Fetch the total count of employees from the database
    total = count_employees_db()

    # Handle case where the database query fails
    if total is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "count": total}

# 4. Get all employees or filter by status endpoint
@emp_router.get("/employees/list")
def list_employees(status: str = None, current_user: User = Depends(get_current_user)):
    """
    Returns a list of all employees, optionally filtered by status.
    The user must be authenticated via JWT.
    """
    # If status is provided, filter employees by status
    if status:
        result = list_employees_by_status_db(status)
    else:
        # Otherwise, fetch all employees
        result = get_all_employees_db()

    # Handle case where database query fails
    if result is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "data": result}

# 5. Get employee by employee_id endpoint
@emp_router.get("/employees/{id}")
def get_employee(id: int, current_user: User = Depends(get_current_user)):
    """
    Fetches a specific employee by their ID.
    Returns employee data if found, otherwise raises a 404 error.
    The user must be authenticated via JWT.
    """
    # Fetch the employee by ID from the database
    employee = get_employee_by_id_db(id)

    # If no employee is found, raise a 404 HTTP exception
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"status": "success", "data": employee}

# 6. Update full employee record endpoint
@emp_router.put("/employees/{id}")
def update_employee(id: int, employee: EmployeeModel, current_user: User = Depends(get_current_user)):
    """
    Updates an existing employee record with the provided new data.
    The user must be authenticated via JWT.
    """
    # Attempt to update the employee record in the database
    if not update_employee_db(id, employee):
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "message": "Employee updated successfully"}

# 7. Update only employee status endpoint
@emp_router.patch("/employees/{id}/status")
def update_employee_status(id: int, status: str, current_user: User = Depends(get_current_user)):
    """
    Updates only the status of an existing employee.
    The user must be authenticated via JWT.
    """
    # Attempt to update the employee status in the database
    if not update_employee_status_db(id, status):
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "message": "Employee status updated"}

# 8. Delete employee endpoint
@emp_router.delete("/employees/{id}")
def delete_employee(id: int, current_user: User = Depends(get_current_user)):
    """
    Deletes an employee record by their ID.
    The user must be authenticated via JWT.
    """
    # Attempt to delete the employee from the database
    if not delete_employee_db(id):
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "message": f"Employee {id} deleted"}
