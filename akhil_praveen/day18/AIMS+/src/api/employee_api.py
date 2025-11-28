from fastapi import FastAPI, HTTPException, APIRouter
from typing import Optional
from ..models.employeedirectory import EmployeeDirectory, StatusValidate
from ..crud.employee_crud import EmployeeCrud

# Initialize the EmployeeCrud instance to interact with the employee database
employee_reader = EmployeeCrud()

# Create the APIRouter instance for employee-related routes with a prefix "/employee"
employee_router = APIRouter(prefix="/employee")

# Route to create a new employee record in the database
@employee_router.post("/create")
def create_employee(employee: EmployeeDirectory):
    try:
        # Call the create_employee method from EmployeeCrud to insert the employee record
        return employee_reader.create_employee(employee)
    except Exception as e:
        # Log the error and raise a 404 HTTPException if something goes wrong
        print(e)
        raise HTTPException(status_code=404, detail="Not Found")

# Route to retrieve a list of all employees, or filter by status
@employee_router.get("/list")
def get_all_employee(status: Optional[str] = "ALL"):
    try:
        # Call the get_all_employee method from EmployeeCrud to fetch employees based on status
        return employee_reader.get_all_employee(status)
    except Exception:
        # If an error occurs, raise a 404 HTTPException with a message
        raise HTTPException(status_code=404, detail="Not Found")

# Route to retrieve a specific employee by their ID
@employee_router.get("/{id}")
def get_employee_by_id(id: int):
    try:
        # Call the get_employee_by_id method from EmployeeCrud to fetch employee by ID
        return employee_reader.get_employee_by_id(id)
    except Exception:
        # If an error occurs, raise a 404 HTTPException with a message
        raise HTTPException(status_code=404, detail="Not Found")

# Route to update an employee's record by their ID
@employee_router.put("/{id}")
def update_employee(id: int, data: EmployeeDirectory):
    try:
        # Call the update_employee method from EmployeeCrud to update the employee's data
        return employee_reader.update_employee(id, data)
    except Exception as e:
        # Log the error and raise a 404 HTTPException if something goes wrong
        print(str(e))
        raise HTTPException(status_code=404, detail="Not Found")

# Route to update the status of an employee by their ID
@employee_router.patch("/{id}/status")
def update_employee_status(id: int, status: StatusValidate):
    try:
        # Print the status for debugging purposes
        print(status)
        # Call the update_employee_status method from EmployeeCrud to update the employee's status
        return employee_reader.update_employee_status(id, status.status)
    except Exception:
        # If an error occurs, raise a 404 HTTPException with a message
        raise HTTPException(status_code=404, detail="Not Found")

# Route to delete an employee record by their ID
@employee_router.delete("/{id}")
def delete_employee(id: int):
    try:
        # Call the delete_employee method from EmployeeCrud to delete the employee by ID
        return employee_reader.delete_employee(id)
    except Exception:
        # If an error occurs, raise a 404 HTTPException with a message
        raise HTTPException(status_code=404, detail="Not Found")

# Route to search for an employee by a specific keyword (e.g., 'emp_code') and value
@employee_router.get("/search/keyword")
def get_employee_by_keyword(keyword: str, value: str):
    try:
        # Call the get_employee_by_keyword method from EmployeeCrud to search employees
        return employee_reader.get_employee_by_keyword(keyword, value)
    except Exception as e:
        # Log the error and raise a 404 HTTPException if something goes wrong
        print(e)
        raise HTTPException(status_code=404, detail="Not Found")

# Route to retrieve the count of all employees
@employee_router.get("/list/count")
def get_count():
    try:
        # Call the get_all_employee_count method from EmployeeCrud to get the employee count
        return employee_reader.get_all_employee_count()
    except Exception as e:
        # Log the error and raise a 404 HTTPException if something goes wrong
        print(e)
        raise HTTPException(status_code=404, detail="Not Found")
