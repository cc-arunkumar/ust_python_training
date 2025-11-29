from fastapi import APIRouter, Query,Depends
from typing import Optional
from models.employee_model import EmployeeCreate, EmployeeUpdate, EmployeeStatusUpdate
from auth.auth_jwt_token import get_current_user
from crud.employee_crud import (
    create_employee,
    list_employees,
    get_employee_by_id,
    update_employee,
    update_employee_status,
    delete_employee,
    search_employee,
    count_employees,
    bulk_upload_employees_from_csv,
)

router = APIRouter(prefix="/employees", tags=["Employees"])


def success(message: str, data=None):
    return {"status": "success", "message": message, "data": data}


@router.post("/create")
def create_employee_api(payload: EmployeeCreate,current_user: dict = Depends(get_current_user)):
    return success("Employee created successfully", create_employee(payload))


@router.get("/list")
def list_employees_api(status: Optional[str] = Query(default=None),current_user: dict = Depends(get_current_user)):
    return success("Employees fetched successfully", list_employees(status))


@router.get("/{emp_id}")
def get_employee_api(emp_id: int,current_user: dict = Depends(get_current_user)):
    return success("Employee fetched successfully", get_employee_by_id(emp_id))


@router.put("/{emp_id}")
def update_employee_api(emp_id: int, payload: EmployeeUpdate,current_user: dict = Depends(get_current_user)):
    return success("Employee updated successfully", update_employee(emp_id, payload))


@router.patch("/{emp_id}/status")
def update_employee_status_api(emp_id: int, payload: EmployeeStatusUpdate,current_user: dict = Depends(get_current_user)):
    return success("Employee status updated successfully", update_employee_status(emp_id, payload.status))


@router.delete("/{emp_id}")
def delete_employee_api(emp_id: int,current_user: dict = Depends(get_current_user)):
    delete_employee(emp_id)
    return success("Employee deleted successfully", None)


@router.get("/search/")
def search_employee_api(keyword: str = Query(...),current_user: dict = Depends(get_current_user)):
    return success("Employees search result", search_employee(keyword))


@router.get("/count")
def count_employees_api(current_user: dict = Depends(get_current_user)):
    return success("Total employees counted successfully", {"count": count_employees()})


@router.post("/bulk-upload")
def bulk_upload_employees_api(current_user: dict = Depends(get_current_user)):
    bulk_upload_employees_from_csv()
    return success("Employees bulk uploaded successfully", None)
