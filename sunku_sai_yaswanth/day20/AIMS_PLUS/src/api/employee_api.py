# Importing necessary modules for FastAPI app
from fastapi import FastAPI, HTTPException, status, APIRouter, Depends
from typing import List, Optional
from src.auth.auth_jwt_token import User, get_current_user  # JWT authentication utilities
from src.models.employee_model import EmployeeDirectory  # Employee model for validation
from src.config.db_connection import get_connection  # DB connection helper
from src.crud.employee_crud import get_all, get_by_id, insert_emp, update_emp_by_id, delete_emp, search_emp  # CRUD operations for employee data

# Create an APIRouter instance for employee-related endpoints with the "/employee" prefix
employee_router = APIRouter(prefix="/employee")

# Endpoint to get a list of employees, with an optional status filter
@employee_router.get("/list", response_model=List[EmployeeDirectory])
def get_emp(status_filter: Optional[str] = "", current_user: User = Depends(get_current_user)):
    try:
        # Retrieve all employees, applying the optional status filter if provided
        rows = get_all(status_filter)
        emp_li = []
        for row in rows:
            # Convert each row to EmployeeDirectory model
            emp_li.append(EmployeeDirectory(**row))
        return emp_li  # Return the list of employees
    except Exception as e:
        # In case of an error, raise an HTTP 400 error with the exception message
        raise HTTPException(status_code=400, detail=f"{e}")

# Endpoint to search employees by field and keyword (e.g., name, department)
@employee_router.get("/search")
def search_by_word(field_type: str, keyword: str, current_user: User = Depends(get_current_user)):
    try:
        # Perform the search based on the field type and keyword
        data = search_emp(field_type, keyword)
        return data  # Return the search result
    except Exception as e:
        # In case of an error, raise an HTTP 400 error
        raise HTTPException(status_code=400, detail=f"Unable to fetch data: {e}")

# Endpoint to count the total number of employees in the system
@employee_router.get("/count")
def count_data(current_user: User = Depends(get_current_user)):
    try:
        # Retrieve all employees to count them
        data = get_all()
        if data is None:
            # If no employees are found, raise a 404 error
            raise HTTPException(status_code=404, detail="No employee found.")
        return {"count": len(data)}  # Return the employee count
    except Exception as e:
        # In case of an error, raise a 500 error
        raise HTTPException(status_code=500, detail=f"Error counting employees: {str(e)}")

# Endpoint to get an employee by their ID
@employee_router.get("/{emp_id}", response_model=EmployeeDirectory)
def get_emp_by_id(emp_id: int, current_user: User = Depends(get_current_user)):
    try:
        # Fetch the employee by their ID
        rows = get_by_id(emp_id)
        if not rows:
            # If no employee is found, raise a 404 error
            raise HTTPException(status_code=404, detail="Employee not exists")
        return EmployeeDirectory(**rows)  # Return the employee details
    except Exception as e:
        # In case of an error, raise a 400 error
        raise HTTPException(status_code=400, detail="ID not found")

# Endpoint to create a new employee
@employee_router.post('/create', response_model=EmployeeDirectory)
def create_asset(new_emp: EmployeeDirectory, current_user: User = Depends(get_current_user)):
    try:
        # Insert the new employee into the database
        insert_emp(new_emp)
        return new_emp  # Return the newly created employee details
    except Exception as e:
        # In case of an error, raise an HTTP 404 error with the exception message
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error: {e}")

# Endpoint to update an employee's details by their ID
@employee_router.put("/{emp_id}", response_model=EmployeeDirectory)
def update_details(emp_id: int, update_emp: EmployeeDirectory, current_user: User = Depends(get_current_user)):
    try:
        # Update the employee details in the database
        update_emp_by_id(emp_id, update_emp)
        return update_emp  # Return the updated employee details
    except HTTPException as e:
        # If a specific HTTPException occurs, raise it directly
        raise e  
    except Exception as e:
        # In case of an error, raise an HTTP 400 error
        raise HTTPException(status_code=400, detail=f"Update failed: {str(e)}")

# Endpoint to delete an employee by their ID
@employee_router.delete("/{id}")
def delete_asset_by_id(id: int, current_user: User = Depends(get_current_user)):
    try:
        # Attempt to delete the employee from the database
        if delete_emp(id):
            return {"detail": "Employee deleted successfully"}  # Return success message
    except Exception as e:
        # In case of an error, raise a 400 error with the exception message
        raise HTTPException(status_code=400, detail=f"Error deleting employee: {str(e)}")

# Endpoint to update an employee's status by their ID
@employee_router.patch("/{emp_id}/status")
def update_vendor_status(emp_id: int, status: str, current_user: User = Depends(get_current_user)):
    try:
        # Fetch the existing employee by their ID
        data = get_by_id(emp_id)
        
        if not data:
            # If no employee is found, raise a 404 error
            raise HTTPException(status_code=404, detail="Employee not found")
        
        # Update the active_status field of the employee
        data['active_status'] = status
        
        # Save the updated employee record in the database
        update_emp_by_id(emp_id, EmployeeDirectory(**data))
        
        # Return success message with updated employee status
        return {"message": "Employee status updated successfully", "employee_id": emp_id, "new_status": status}
        
    except Exception as e:
        # In case of an error, raise a 400 error with the exception message
        raise HTTPException(status_code=400, detail=f"Error updating employee status: {str(e)}")
