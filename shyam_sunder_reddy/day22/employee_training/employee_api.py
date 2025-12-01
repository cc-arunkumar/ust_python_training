from fastapi import FastAPI,HTTPException,APIRouter,Depends
from typing import List
from employee_model import Employee
import employee_crud 
from jwt_auth import get_current_user,User

emp_router=APIRouter(prefix="/employees")

@emp_router.get("/",response_model=List[Employee])
def get_all(current_user: User = Depends(get_current_user)):
    data=employee_crud.get_all_employees()
    return data

@emp_router.get("/{id}",response_model=Employee)
def get_by_id(id:int,current_user: User = Depends(get_current_user)):
    x=employee_crud.get_employee_by_id(id)
    if x:
        return x
    raise HTTPException(status_code=404,detail="Employee not found")

@emp_router.post("/",response_model=Employee)
def create_employee(emp:Employee,current_user: User = Depends(get_current_user)):
    employee_crud.create_employee(emp)
    return emp

@emp_router.put("/{id}",response_model=Employee)
def update_employee(id:int,emp:Employee,current_user: User = Depends(get_current_user)):
    x=employee_crud.update_employee_by_Id(id,emp)
    if x:
        return x
    raise HTTPException(status_code=404,detail="Employee Not Found")

@emp_router.patch("/{id}")
def patch(id,field,value,current_user: User = Depends(get_current_user)):
    x=employee_crud.patch_by_id(id,field,value)
    if x:
        return {"detail":"employee field updated"}
    raise HTTPException(status_code=404,detail="Employee Not Found")
 
@emp_router.delete("/{id}")
def delete(id:int,current_user: User = Depends(get_current_user)):
    x=employee_crud.delete_by_id(id)
    if x:
        return {"detail":"Employee Deleted Successfully"}
    raise HTTPException(status_code=404,detail="Employee Not Found")
 