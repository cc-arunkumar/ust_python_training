from fastapi import Depends, APIRouter, HTTPException
from src.model.model_employees import Employee
from src.auth.jwt_authentication import get_current_user, User
from src.crud.employee_crud import (
    create_employee,
    get_all,
    get_by_id,
    update,
    delete,
    update_emp_status,
    get_count,
    get_emp_by_status,
    find
)

# Router configuration for Employee module
router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post("/")
def create(data: Employee, current_user: User = Depends(get_current_user)):
    """
    Create a new employee record.
    Requires authentication via JWT.
    """
    return create_employee(data)


@router.get("/")
def list_all(current_user: User = Depends(get_current_user)):
    """
    Retrieve all employee records.
    Protected route requiring authentication.
    """
    return get_all()


@router.get("/status/{status}")
def filter_by_status(status: str, current_user: User = Depends(get_current_user)):
    """
    Fetch employee records filtered by status (Active/Inactive).
    """
    return get_emp_by_status(status)


@router.get("/search/{column}/{value}")
def search(column: str, value: str, current_user: User = Depends(get_current_user)):
    """
    Search employees by a specific column and value.
    Example: /employees/search/name/John
    """
    return find(column, value)


@router.get("/count")
def count_data(current_user: User = Depends(get_current_user)):
    """
    Get total employee count.
    Useful for dashboard summaries.
    """
    return get_count()


@router.get("/{emp_id}")
def get(emp_id: int, current_user: User = Depends(get_current_user)):
    """
    Retrieve a single employee by ID.
    Raises 404 if employee does not exist.
    """
    result = get_by_id(emp_id)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result


@router.put("/{emp_id}")
def modify(emp_id: int, data: Employee, current_user: User = Depends(get_current_user)):
    """
    Update employee details by ID.
    Uses full update (PUT).
    """
    return update(emp_id, data)


@router.patch("/{status}")
def update_status(status: str, current_user: User = Depends(get_current_user)):
    """
    Update employee status (Active/Inactive).
    Uses partial update (PATCH).
    """
    return update_emp_status(status)


@router.delete("/{emp_id}")
def remove(emp_id: int, current_user: User = Depends(get_current_user)):
    """
    Delete an employee record by ID.
    """
    return delete(emp_id)
