from fastapi import FastAPI, HTTPException, APIRouter,Depends
from src.models.login_model import User
from src.auth.jwt_auth import get_current_user
from src.models import employee_model
from src.crud import employee_crud
from typing import List, Optional

# Router for employee-related endpoints, all prefixed with "/employees"
employee_router = APIRouter(prefix="/employees")


# -------------------------------
# Endpoint: Search employees by field
# -------------------------------
@employee_router.get("/search", response_model=List[employee_model.Employee])
def search(field: str, val: str,current_user: User = Depends(get_current_user)):
    """
    Search employees by a given field and value.
    Example: /employees/search?field=name&val=John
    """
    if employee_crud.search_by_tag_employee(field, val):
        return employee_crud.search_by_tag_employee(field, val)
    raise HTTPException(status_code=404, detail="Not found")


# -------------------------------
# Endpoint: Create a new employee
# -------------------------------
@employee_router.post("/create", response_model=employee_model.Employee)
def create_employee(new_employee: employee_model.Employee,current_user: User = Depends(get_current_user)):
    """
    Create a new employee record.
    Validates employee data before inserting into DB.
    """
    if employee_model.validate_employee(new_employee):
        pass
    else:
        raise HTTPException(status_code=409, detail="Validation failed")
    if not employee_crud.create_employee(new_employee):
        raise HTTPException(status_code=400, detail="Failed to create the Employee")
    return new_employee


# -------------------------------
# Endpoint: List all employees / List all By Status
# -------------------------------
@employee_router.get("/list", response_model=List[employee_model.Employee])
def get_all(status: Optional[str] = "",current_user: User = Depends(get_current_user)):
    """
    Retrieve all employees, optionally filtered by status.
    Example: /employees/list?status=active
    """
    data = employee_crud.get_all_employees(status)
    new_li = []
    for row in list(data):
        x = employee_model.Employee(**row)  # Convert dict to Employee model
        new_li.append(x)
    return new_li


# -------------------------------
# Endpoint: Count all employees
# -------------------------------
@employee_router.get("/count")
def count_all(current_user: User = Depends(get_current_user)):
    """
    Return the total count of employees in the system.
    """
    data = employee_crud.get_all_employees()
    return {"detail": f"Count of records: {len(data)}"}


# -------------------------------
# Endpoint: Get employee by ID
# -------------------------------
@employee_router.get("/{id}", response_model=employee_model.Employee)
def get_by_id(id: int,current_user: User = Depends(get_current_user)):
    """
    Retrieve a single employee by their ID.
    """
    data = employee_crud.get_employee_by_id(id)
    if data:
        return employee_model.Employee(**data)
    raise HTTPException(status_code=404, detail="Employee id not found")


# -------------------------------
# Endpoint: Update employee by ID
# -------------------------------
@employee_router.put("/{id}", response_model=employee_model.Employee)
def update_by_id(id: int, new_employee: employee_model.Employee,current_user: User = Depends(get_current_user)):
    """
    Update an existing employee by ID.
    Validates employee data before updating.
    """
    if employee_model.validate_employee(new_employee):
        pass
    else:
        raise HTTPException(status_code=409, detail="Validation failed")
    if employee_crud.update_employee_by_id(id, new_employee):
        return new_employee
    raise HTTPException(status_code=400, detail="Unable to update Employee")


# -------------------------------
# Endpoint: Patch employee status
# -------------------------------
@employee_router.patch("/{id}/status", response_model=employee_model.Employee)
def patch_by_id(id: int, status: str,current_user: User = Depends(get_current_user)):
    """
    Update only the status field of an employee by ID.
    """
    data = get_by_id(id)
    if data:
        data.status = status
        return update_by_id(id, data)
    raise HTTPException(status_code=404, detail="ID not found")


# -------------------------------
# Endpoint: Delete employee by ID
# -------------------------------
@employee_router.delete("/{id}")
def delete_asset_id(id: int,current_user: User = Depends(get_current_user)):
    """
    Delete an employee record by ID.
    """
    if employee_crud.delete_employee_by_id(id):
        return {"detail": "Record deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee Id Doesnt Exist")
