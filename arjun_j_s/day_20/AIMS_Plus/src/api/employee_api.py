from fastapi import APIRouter, HTTPException, Depends
from ..models.employee_model import EmployeeDirectory
from ..models.user_model import User
from ..crud.employee_crud import Employee
from typing import List, Optional
from ..auth.authentication import get_current_user

emp_service = Employee()  # Service instance for employee CRUD
emp_router = APIRouter(prefix="/employees")  # Router with /employees prefix


@emp_router.get("/list")
def get_all(status: Optional[str] = "all",current_user : User =Depends(get_current_user)):  # Get all employees (optionally filter by status)
    try:
        return emp_service.get_all_emp(status)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@emp_router.get("/{emp_id}")
def get_by_id(emp_id: int,current_user : User =Depends(get_current_user)):  # Get employee by ID
    try:
        return emp_service.get_emp_by_id(emp_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@emp_router.put("/{emp_id}")
def update_emp(emp_id: int, emp: EmployeeDirectory,current_user : User =Depends(get_current_user)):  # Update full employee record
    try:
        if emp_service.update_emp(emp_id, emp):
            return {"message": "Update Successful"}
        else:
            return {"message": "Employee Not Found"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@emp_router.patch("/{emp_id}/")
def update_emp(emp_id: int, status: str,current_user : User =Depends(get_current_user)):  # Update only employee status
    try:
        if emp_service.update_emp_status(emp_id, status):
            return {"message": "Update Successful"}
        else:
            return {"message": "Employee Not Found"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@emp_router.post("/create")
def create_emp(emp: EmployeeDirectory,current_user : User =Depends(get_current_user)):  # Create new employee
    try:
        if emp_service.create_emp(emp):
            return {"message": "Added Successful"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@emp_router.delete("/{emp_id}")
def delete_emp(emp_id: int,current_user : User =Depends(get_current_user)):  # Delete employee by ID
    try:
        if emp_service.delete_emp(emp_id):
            return {"message": "Deleted Successful"}
        else:
            return {"message": "Employee Not Found"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@emp_router.get("/search/keyword/")
def get_by_keyword(keyword: str, value: str,current_user : User =Depends(get_current_user)):  # Search employee by keyword/value
    try:
        return emp_service.get_employee_keyword(keyword, value)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@emp_router.get("/all/count/")
def get_count(current_user : User =Depends(get_current_user)):  # Get total employee count
    try:
        return emp_service.get_emp_count()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))