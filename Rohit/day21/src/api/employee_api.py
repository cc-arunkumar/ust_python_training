from fastapi import APIRouter,HTTPException,FastAPI
from src.models.employee_pydentic import Employee_pydentic
from src.config.db_connection import get_connection
from src.crud.employee_crud import get_all_employees,delete_employee,get_employee_by_id,create_emp,update_employee_by_id
employee_router = APIRouter(prefix="/employee")



@employee_router.post("/create")
def add_employee(emp:Employee_pydentic):
    try:
        return create_emp(emp)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
@employee_router.get("")
def get_all_employee():
    try:
       return get_all_employees()
    except Exception as e:
        pass
    finally:
        pass
    
    
@employee_router.get("/{id}")
def get_employee_id(id:int):
    try:
        return get_employee_by_id(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@employee_router.put("/update/{id}")
def update_employee(id:int,emp:Employee_pydentic):
    try:
        return update_employee_by_id(id,emp)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@employee_router.delete("/{id}")
def remove_employee(id:int):
    try:
        return delete_employee(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    