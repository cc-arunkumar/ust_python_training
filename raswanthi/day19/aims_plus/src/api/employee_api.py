from fastapi import FastAPI, HTTPException, Query, APIRouter, Depends
from ..auth.auth_jwt_token import get_current_user   # Dependency to get the currently logged-in user
from ..models.user_model import User                 # User model for authentication
from src.models.employee_model import EmployeeModel  # Employee model definition
from src.crud.employee_crud import (
    create_employee_db, get_all_employees_db, list_employees_by_status_db,
    get_employee_by_id_db, update_employee_db, update_employee_status_db,
    delete_employee_db, search_employees_db, count_employees_db
)

# Create a router for employee-related endpoints with a common prefix
employee_router = APIRouter(prefix="/employees")


# ------------------- CREATE -------------------
@employee_router.post("/employees/create")
def create_employee(employee: EmployeeModel, current_user: User = Depends(get_current_user)):
    """
    Create a new employee record.
    - Requires authentication (current_user).
    - Accepts EmployeeModel object as input.
    - Returns success message if created, else raises HTTP 500.
    """
    if not create_employee_db(employee):
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "message": "Employee created successfully"}


# ------------------- SEARCH -------------------
@employee_router.get("/employees/search")
def search_employees(keyword: str = Query(...), value: str = Query(...), current_user: User = Depends(get_current_user)):
    """
    Search employees by keyword and value.
    - Example: /employees/search?keyword=name&value=John
    - Returns matching employees.
    - Raises HTTP 500 if database connection fails.
    """
    result = search_employees_db(keyword, value)
    if result is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "data": result}


# ------------------- COUNT -------------------
@employee_router.get("/employees/count")
def count_employees(current_user: User = Depends(get_current_user)):
    """
    Count total number of employees.
    - Returns integer count.
    - Raises HTTP 500 if database connection fails.
    """
    total = count_employees_db()
    if total is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "count": total}


# ------------------- LIST -------------------
@employee_router.get("/employees/list")
def list_employees(status: str = None, current_user: User = Depends(get_current_user)):
    """
    List all employees.
    - Optional query parameter 'status' to filter employees by status.
    - Returns all employees if no status is provided.
    - Raises HTTP 500 if database connection fails.
    """
    if status:
        result = list_employees_by_status_db(status)
    else:
        result = get_all_employees_db()
    if result is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "data": result}


# ------------------- GET BY ID -------------------
@employee_router.get("/employees/{id}")
def get_employee(id: int, current_user: User = Depends(get_current_user)):
    """
    Retrieve a single employee by ID.
    - Returns employee details if found.
    - Raises HTTP 404 if employee not found.
    """
    employee = get_employee_by_id_db(id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"status": "success", "data": employee}


# ------------------- UPDATE -------------------
@employee_router.put("/employees/{id}")
def update_employee(id: int, employee: EmployeeModel, current_user: User = Depends(get_current_user)):
    """
    Update an existing employee by ID.
    - Accepts EmployeeModel object with updated fields.
    - Returns success message if updated.
    - Raises HTTP 500 if database connection fails.
    """
    if not update_employee_db(id, employee):
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "message": "Employee updated successfully"}


# ------------------- UPDATE STATUS -------------------
@employee_router.patch("/employees/{id}/status")
def update_employee_status(id: int, status: str, current_user: User = Depends(get_current_user)):
    """
    Update only the status of an employee.
    - Example: PATCH /employees/1/status?status=inactive
    - Returns success message if updated.
    - Raises HTTP 500 if database connection fails.
    """
    if not update_employee_status_db(id, status):
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "message": "Employee status updated"}


# ------------------- DELETE -------------------
@employee_router.delete("/employees/{id}")
def delete_employee(id: int, current_user: User = Depends(get_current_user)):
    """
    Delete an employee by ID.
    - Returns success message if deleted.
    - Raises HTTP 500 if database connection fails.
    """
    if not delete_employee_db(id):
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "message": f"Employee {id} deleted"}
