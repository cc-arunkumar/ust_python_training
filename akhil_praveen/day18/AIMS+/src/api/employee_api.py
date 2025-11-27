from fastapi import FastAPI,HTTPException,APIRouter
from typing import Optional
from ..models.employeedirectory import EmployeeDirectory,StatusValidate
from ..crud.employee_crud import EmployeeCrud

employee_reader = EmployeeCrud()
employee_router = APIRouter(prefix="/employee")

@employee_router.post("/create")
def create_employee(employee:EmployeeDirectory):
    try:
        return employee_reader.create_employee(employee)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404,detail="Not Found")

@employee_router.get("/list")
def get_all_employee(status:Optional[str] = "ALL"):
    try:
        return employee_reader.get_all_employee(status)
    except Exception:
        raise HTTPException(status_code=404,detail="Not Found")

@employee_router.get("/{id}")
def get_employee_by_id(id:int):
    try:
        return employee_reader.get_employee_by_id(id)
    except Exception:
        raise HTTPException(status_code=404,detail="Not Found")

@employee_router.put("/{id}")
def update_employee(id:int,data:EmployeeDirectory):
    try:
        return employee_reader.update_employee(id,data)
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404,detail="Not Found")

@employee_router.patch("/{id}/status")
def update_employee_status(id:int,status:StatusValidate):
    try:
        print(status)
        return employee_reader.update_employee_status(id,status.status)
    except Exception:
        raise HTTPException(status_code=404,detail="Not Found")

@employee_router.delete("/{id}")
def delete_employee(id:int):
    try:
        return employee_reader.delete_employee(id)
    except Exception:
        raise HTTPException(status_code=404,detail="Not Found")

@employee_router.get("/search/keyword")
def get_employee_by_keyword(keyword:str,value:str):
    try:
        return employee_reader.get_employee_by_keyword(keyword,value)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404,detail="Not Found")

@employee_router.get("/list/count")
def get_count():
    try:
        return employee_reader.get_all_employee_count()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404,detail="Not Found")
