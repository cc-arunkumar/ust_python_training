from fastapi import APIRouter,HTTPException
from ..models.employee_model import EmployeeDirectory
from ..crud.employee_crud import Employee
from typing import List,Optional

emp_service = Employee()

emp_router = APIRouter(prefix="/employees")


@emp_router.get("/list")
def get_all(status:Optional[str]="all"):
    try:
        return emp_service.get_all_emp(status)
    except Exception as e:
        raise HTTPException(status_code=404,detail =str(e))
    
@emp_router.get("/{emp_id}")
def get_by_id(emp_id:int):
    try:
        return emp_service.get_emp_by_id(emp_id)
    except Exception as e:
        raise HTTPException(status_code=404,detail =str(e))
    
@emp_router.put("/{emp_id}")
def update_emp(emp_id:int,emp:EmployeeDirectory):
    try:
        if emp_service.update_emp(emp_id,emp):
            return {"message" : "Update Successfull"}
        else:
            return {"message" : "Employee Not Found"}
    except Exception as e:
        raise HTTPException(status_code=404,detail =str(e))
    
@emp_router.patch("/{emp_id}/")
def update_emp(emp_id:int,status:str):
    try:
        if emp_service.update_emp_status(emp_id,status):
            return {"message" : "Update Successfull"}
        else:
            return {"message" : "Employee Not Found"}
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404,detail=str(e))
    
@emp_router.post("/create")
def create_emp(emp:EmployeeDirectory):
    try:
        if emp_service.create_emp(emp):
            return {"message" : "Added Successfull"}
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404,detail=str(e))
    
@emp_router.delete("/{emp_id}")
def delete_emp(emp_id:int):
    try:
        if emp_service.delete_emp(emp_id):
            return {"message" : "Deleted Successfull"}
        else:
            return {"message" : "Employee Not Found"}
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404,detail=str(e))
    
@emp_router.get("/search/keyword/")
def get_by_keyword(keyword:str,value:str):
    try:
        return emp_service.get_employee_keyword(keyword,value)
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404,detail =str(e))
    
@emp_router.get("/all/count/")
def get_count():
    try:
        return emp_service.get_emp_count()
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404,detail =str(e))