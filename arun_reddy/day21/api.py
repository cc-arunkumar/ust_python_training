from fastapi import APIRouter, HTTPException, status
from employee_model import Employee
from crud_op import insert_emp, get_by_id, get_all, update_employee, delete_by_id

# Create an API router with a prefix for all employee-related endpoints
emp_router = APIRouter(prefix="/employees")

# -------------------------------
# Endpoint: Create a new employee
# -------------------------------
@emp_router.post("")
def create_emp(emp: Employee):
    """
    Create a new employee record in the database.
    Input: Employee object (validated by Pydantic model).
    Output: Success message or error.
    """
    try:
        return insert_emp(emp)  # Call CRUD function to insert employee
    except Exception as e:
        # Raise HTTP 500 if something goes wrong
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# ---------------------------------
# Endpoint: Get employee by ID
# ---------------------------------
@emp_router.get("/{employee_id}")
def get_id(employee_id: int):
    """
    Retrieve a single employee record by its ID.
    Input: employee_id (integer).
    Output: Employee details as dictionary.
    """
    try:
        return get_by_id(employee_id)  # Call CRUD function to fetch employee
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# ---------------------------------
# Endpoint: Get all employees
# ---------------------------------
@emp_router.get("")
def get_emp():
    """
    Retrieve all employee records from the database.
    Output: List of employees as dictionaries.
    """
    try:
        return get_all()  # Call CRUD function to fetch all employees
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# ---------------------------------
# Endpoint: Update employee by ID
# ---------------------------------
@emp_router.put("/{employee_id}")
def update_emp(employee_id: int, emp: Employee):
    """
    Update an existing employee record by ID.
    Input: employee_id (integer), Employee object with updated data.
    Output: Updated employee object.
    """
    try:
        return update_employee(employee_id, emp)  # Call CRUD function to update employee
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# ---------------------------------
# Endpoint: Delete employee by ID
# ---------------------------------
@emp_router.delete("/{employee_id}")
def delete_emp(employee_id: int):
    """
    Delete an employee record by ID.
    Input: employee_id (integer).
    Output: Success message if deleted.
    """
    try:
        return delete_by_id(employee_id)  # Call CRUD function to delete employee
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
