# Import FastAPI components for building API routes and handling exceptions
from fastapi import APIRouter, HTTPException, status

# Import CRUD operations and data model for Employee
from ..crud.employee_crud import EmployeeCrud
from ..model.employee_model import EmployeeModel

# Initialize API Router with a prefix for all employee-related endpoints
employee_api = APIRouter(prefix="/employee")

# Instantiate the EmployeeCrud class to interact with the database layer
employee_crud = EmployeeCrud()


@employee_api.get("/list_all")
def get_all_employees():
    """
    Retrieve all employees from the system.

    Returns:
        List of employees retrieved from the database.
    Raises:
        HTTPException: If any error occurs during retrieval, returns 502 Bad Gateway.
    """
    try:
        return employee_crud.get_all_employee()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(e)
        )


@employee_api.post("/create")
def create_employee(employee: EmployeeModel):
    """
    Create a new employee record.

    Args:
        employee (EmployeeModel): Employee data to be created.

    Returns:
        Newly created employee record.
    Raises:
        HTTPException: If any error occurs during creation, returns 502 Bad Gateway.
    """
    try:
        return employee_crud.create_employee(employee)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(e)
        )


@employee_api.get("/get_by_id/{emp_id}")
def get_employee_by_id(emp_id: int):
    """
    Retrieve a single employee by their unique ID.

    Args:
        emp_id (int): Unique identifier of the employee.

    Returns:
        Employee record if found.
    Raises:
        HTTPException: If any error occurs during retrieval, returns 502 Bad Gateway.
    """
    try:
        return employee_crud.get_employee_by_id(emp_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(e)
        )


@employee_api.put("/update/{emp_id}")
def update_employee(emp_id: int, employee: EmployeeModel):
    """
    Update an existing employee record.

    Args:
        emp_id (int): Unique identifier of the employee to update.
        employee (EmployeeModel): Updated employee data.

    Returns:
        Updated employee record.
    Raises:
        HTTPException: If any error occurs during update, returns 502 Bad Gateway.
    """
    try:
        return employee_crud.update_employee(emp_id, employee)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(e)
        )


@employee_api.delete("/delete/{emp_id}")
def delete_employee_by_id(emp_id: int):
    """
    Delete an employee record by their unique ID.

    Args:
        emp_id (int): Unique identifier of the employee to delete.

    Returns:
        Confirmation of deletion.
    Raises:
        HTTPException: If any error occurs during deletion, returns 502 Bad Gateway.
    """
    try:
        return employee_crud.delete_employee(emp_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(e)
        )