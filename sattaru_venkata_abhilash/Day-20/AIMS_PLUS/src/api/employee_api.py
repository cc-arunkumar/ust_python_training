from fastapi import FastAPI, HTTPException, status, APIRouter, Depends
from typing import List, Optional
from src.models.employee_model import EmployeeDirectory  # Importing Employee model
from src.config.db_connection import get_connection  # Importing database connection
from src.crud.employee_crud import get_all, get_by_id, insert_emp, update_emp_by_id, delete_emp, search_emp  # Importing CRUD functions for employees
from src.auth.auth_jwt_token import User, get_curr_user  # Importing JWT authentication logic

# Initialize the FastAPI app and router for employee-related routes
employee_router = APIRouter(prefix="/employees")

# Create Employee endpoint (No authentication needed for this one)
@employee_router.post('/create', response_model=EmployeeDirectory)
def create_employee(new_emp: EmployeeDirectory):
    """
    Endpoint to create a new employee. This route doesn't require authentication.
    It takes a new employee as input and inserts it into the database.
    """
    try:
        insert_emp(new_emp)  # Insert employee into the database
        return new_emp  # Return the newly created employee
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error: {e}")  # If error occurs, raise HTTP exception

# Get all employees endpoint (Secured with JWT)
@employee_router.get("/", response_model=List[EmployeeDirectory])
def get_employees(status_filter: Optional[str] = "", current_user: User = Depends(get_curr_user)):  # Secure with JWT authentication
    """
    Endpoint to get a list of all employees. Only accessible by authenticated users.
    You can also filter employees by their status (optional).
    """
    try:
        rows = get_all(status_filter)  # Fetch all employees from the database (with an optional status filter)
        if not rows:
            return []  # Return empty list if no employees found
        emp_li = [EmployeeDirectory(**row) for row in rows]  # Convert rows to Pydantic models
        return emp_li  # Return the list of employees
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{e}")  # Raise error if something goes wrong

# Search employees by field and keyword (Secured with JWT)
@employee_router.get("/search")
def search_by_word(field_type: str, keyword: str, current_user: User = Depends(get_curr_user)):  # Secure with JWT authentication
    """
    Endpoint to search employees by a specific field and keyword. Only accessible by authenticated users.
    """
    try:
        data = search_emp(field_type, keyword)  # Perform search operation in DB based on field and keyword
        return data  # Return search results
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to fetch data: {e}")  # Handle errors in search operation

# Get employees with optional status filter (Secured with JWT)
@employee_router.get("/lists", response_model=List[EmployeeDirectory])
def get_employees_by_status(status_filter: Optional[str] = "", current_user: User = Depends(get_curr_user)):  # Secure with JWT authentication
    """
    Endpoint to get a list of employees filtered by their status. Only accessible by authenticated users.
    """
    try:
        rows = get_all(status_filter)  # Fetch employees from DB with optional status filter
        if not rows:
            return []  # Return empty list if no employees found
        emp_li = [EmployeeDirectory(**row) for row in rows]  # Convert rows to Pydantic models
        return emp_li  # Return the list of employees
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{e}")  # Handle errors during employee retrieval

# Get employee count (Secured with JWT)
@employee_router.get("/count")
def count_employees(current_user: User = Depends(get_curr_user)):  # Secure with JWT authentication
    """
    Endpoint to get the count of employees. Only accessible by authenticated users.
    """
    try:
        data = get_all()  # Get all employees from DB
        count = len(data) if data else 0  # Return count of employees, or 0 if none are found
        return {"count": count}  # Return count in a dictionary
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error counting employees: {str(e)}")  # Handle errors during counting

# Get employee by ID (Secured with JWT)
@employee_router.get("/{emp_id}", response_model=EmployeeDirectory)
def get_employee_by_id(emp_id: int, current_user: User = Depends(get_curr_user)):  # Secure with JWT authentication
    """
    Endpoint to get a single employee by their ID. Only accessible by authenticated users.
    """
    try:
        row = get_by_id(emp_id)  # Fetch employee by ID from DB
        if not row:
            raise HTTPException(status_code=404, detail="Employee not found")  # Raise error if employee is not found
        return EmployeeDirectory(**row)  # Convert to Pydantic model and return
    except Exception as e:
        raise HTTPException(status_code=400, detail="ID not found")  # Handle invalid ID error

# Update employee details (Secured with JWT)
@employee_router.put("/{emp_id}", response_model=EmployeeDirectory)
def update_employee(emp_id: int, update_emp: EmployeeDirectory, current_user: User = Depends(get_curr_user)):  # Secure with JWT authentication
    """
    Endpoint to update an employee's details by their ID. Only accessible by authenticated users.
    """
    try:
        update_emp_by_id(emp_id, update_emp)  # Update employee in the database
        return update_emp  # Return the updated employee
    except HTTPException as e:
        raise e  # Raise the exception if it's HTTP-related
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Update failed: {str(e)}")  # Handle any errors during update

# Delete employee by ID (Secured with JWT)
@employee_router.delete("/{emp_id}")
def delete_employee_by_id(emp_id: int, current_user: User = Depends(get_curr_user)):  # Secure with JWT authentication
    """
    Endpoint to delete an employee by their ID. Only accessible by authenticated users.
    """
    try:
        if delete_emp(emp_id):  # Try deleting the employee
            return {"detail": "Employee deleted successfully"}  # Return success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting employee: {str(e)}")  # Handle errors during deletion

# Update employee status (Secured with JWT)
@employee_router.patch("/{emp_id}/status")
def update_employee_status(emp_id: int, status: str, current_user: User = Depends(get_curr_user)):  # Secure with JWT authentication
    """
    Endpoint to update an employee's status by their ID. Only accessible by authenticated users.
    """
    try:
        data = get_by_id(emp_id)  # Fetch employee by ID from DB
        if not data:
            raise HTTPException(status_code=404, detail="Employee not found")  # Raise error if employee not found
        
        data['status'] = status  # Update employee's status
        update_emp_by_id(emp_id, EmployeeDirectory(**data))  # Update the employee in DB
        
        return {"message": "Employee status updated successfully", "employee_id": emp_id, "new_status": status}  # Return success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating employee status: {str(e)}")  # Handle errors during status update
