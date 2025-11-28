from fastapi import FastAPI, HTTPException, status, APIRouter, Depends
from src.crud import employee_crud
from src.models import employee_model
from typing import List, Optional
from src.auth.auth_jwt_token import get_current_user
from src.models.login_model import User

# Router for employee endpoints
employee_router = APIRouter(prefix="/employees")

# Search employees by field and keyword
@employee_router.get('/search', response_model=List[employee_model.EmployeeDirectory])
def search_by_word(field_type: str, keyword: str, curr_user: User = Depends(get_current_user)):
    try:
        data = employee_crud.search_employee(field_type, keyword)
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to fetch data: {e}")


# Get all employees (optionally filter by status)
@employee_router.get('/list', response_model=List[employee_model.EmployeeDirectory])
def get_all(status_filter: Optional[str] = "", curr_user: User = Depends(get_current_user)):
    try:
        data = employee_crud.get_all_employees(status_filter)
        new_li = []
        for row in data:
            new_li.append(employee_model.EmployeeDirectory(**row))
        return new_li
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Failed to Fetch All the Records: {e}")


# Get count of employees
@employee_router.get("/count")
def count_all(curr_user: User = Depends(get_current_user)):
    data = employee_crud.get_all_employees()
    return {"detail": f"Count of records: {len(data)}"}


# Get employee by ID
@employee_router.get('/{id}', response_model=employee_model.EmployeeDirectory)
def get_by_id(id: int,curr_user: User = Depends(get_current_user)):
    try:
        data = employee_crud.get_employee_by_id(id)
        if not data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not Found")
        return employee_model.EmployeeDirectory(**data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"ID not Found or Unable to fetch the Record : {e}")


# Create a new employee
@employee_router.post('/create', response_model=employee_model.EmployeeDirectory)
def create_asset(new_asset: employee_model.EmployeeDirectory,curr_user: User = Depends(get_current_user)):
    try:
        employee_crud.create_employee(new_asset)
        return new_asset
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error: {e}")


# Delete employee by ID
@employee_router.delete("/{id}")
def delete_asset_id(id: int,curr_user: User = Depends(get_current_user)):
    try:
        if employee_crud.delete_employee_by_id(id):
            return {"detail": "Record deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Asset Id Doesnt Exist: {e}")


# Update employee by ID
@employee_router.put("/{id}", response_model=employee_model.EmployeeDirectory)
def update_by_id(id: int, new_asset: employee_model.EmployeeDirectory,curr_user: User = Depends(get_current_user)):
    try:
        employee_crud.update_asset_by_id(id, new_asset)
        data = employee_crud.get_employee_by_id(id)
        return employee_model.EmployeeDirectory(**data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to update asset: {e}")


# Patch employee status by ID
@employee_router.patch("/{id}/status", response_model=employee_model.EmployeeDirectory)
def patch_by_id(id: int, status: str):
    data = get_by_id(id)
    try:
        if data:
            data.status = status
            return update_by_id(id, data)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error: {e}")
