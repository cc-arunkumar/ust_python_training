from fastapi import FastAPI, HTTPException, APIRouter,Depends
from typing import Optional
from ..models.employee_directory import EmployeeDirectory, StatusValidate
from ..crud.employee_crud import EmployeeCrud
from ..auth.jwt_auth import get_current_user,User

# Initialize CRUD handler for employee operations
employee_reader = EmployeeCrud()

# Create a router instance with a prefix for all employee-related endpoints
employee_router = APIRouter(prefix="/employee")


@employee_router.post("/create")
def create_employee(employee: EmployeeDirectory,current_user: User = Depends(get_current_user)):
    """
    Endpoint to create a new employee record.
    Accepts an EmployeeDirectory model as input.
    """
    try:
        return employee_reader.create_employee(employee)
    except Exception as e:
        # Log the error for debugging purposes
        print(e)
        raise HTTPException(status_code=404, detail="Not Found")


@employee_router.get("/list")
def get_all_employee(status: Optional[str] = "ALL",current_user: User = Depends(get_current_user)):
    """
    Endpoint to retrieve all employees.
    Optional query parameter 'status' can filter employees by status.
    Defaults to 'ALL' to return every employee.
    """
    try:
        return employee_reader.get_all_employee(status)
    except Exception:
        raise HTTPException(status_code=404, detail="Not Found")


@employee_router.get("/{id}")
def get_employee_by_id(id: int,current_user: User = Depends(get_current_user)):
    """
    Endpoint to fetch a single employee by their unique ID.
    """
    try:
        return employee_reader.get_employee_by_id(id)
    except Exception:
        raise HTTPException(status_code=404, detail="Not Found")


@employee_router.put("/{id}")
def update_employee(id: int, data: EmployeeDirectory,current_user: User = Depends(get_current_user)):
    """
    Endpoint to update an existing employee record by ID.
    Accepts an EmployeeDirectory model with updated data.
    """
    try:
        return employee_reader.update_employee(id, data)
    except Exception as e:
        # Log the error for debugging purposes
        print(str(e))
        raise HTTPException(status_code=404, detail="Not Found")


@employee_router.patch("/{id}/status")
def update_employee_status(id: int, status: StatusValidate,current_user: User = Depends(get_current_user)):
    """
    Endpoint to update only the status of an employee.
    Accepts a StatusValidate model containing the new status.
    """
    try:
        print(status)  # Debug print, can be replaced with proper logging
        return employee_reader.update_employee_status(id, status.status)
    except Exception:
        raise HTTPException(status_code=404, detail="Not Found")


@employee_router.delete("/{id}")
def delete_employee(id: int,current_user: User = Depends(get_current_user)):
    """
    Endpoint to delete an employee record by ID.
    """
    try:
        return employee_reader.delete_employee(id)
    except Exception:
        raise HTTPException(status_code=404, detail="Not Found")


@employee_router.get("/search/keyword")
def get_employee_by_keyword(keyword: str, value: str,current_user: User = Depends(get_current_user)):
    """
    Endpoint to search employees dynamically by a given keyword and value.
    Example: /employee/search/keyword?keyword=name&value=John
    """
    try:
        return employee_reader.get_employee_by_keyword(keyword, value)
    except Exception as e:
        print(e)  # Debug print, can be replaced with proper logging
        raise HTTPException(status_code=404, detail="Not Found")


@employee_router.get("/list/count")
def get_count(current_user: User = Depends(get_current_user)):
    """
    Endpoint to return the total count of employees.
    Useful for dashboards or summary views.
    """
    try:
        return employee_reader.get_all_employee_count()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail="Not Found")