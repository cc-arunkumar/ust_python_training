from fastapi import FastAPI, APIRouter
from crud import create_training_request, get_training_request_by_id, update_training_request_by_id, delete_training_request_by_id,patch_by_employee,get_all_employee
from model import TrainingRequestModel

router = APIRouter()

@router.post("/employee")
def create(emp: TrainingRequestModel):

    return create_training_request(emp.employee_id, emp.employee_name, emp.training_title, emp.training_description, emp.requested_date, emp.status, emp.manager_id)

@router.get("/employee")
def get_all_employee(employee_id: int):
    return get_all_employee()
    

@router.get("/employee/{employee_id}")
def get_employee(employee_id: int):
    return get_training_request_by_id(employee_id)

@router.put("/employee/{employee_id}")
def update_employee(employee_id: int, emp: TrainingRequestModel):
    return update_training_request_by_id(employee_id, emp.employee_id, emp.employee_name, emp.training_title, emp.training_description, emp.requested_date, emp.status, emp.manager_id)

@router.patch("/employee/{employee_id}")
def patch_employee(employee_id:int,emp:TrainingRequestModel):
    return patch_by_employee(employee_id,emp.status)

@router.delete("/employee/{employee_id}")
def del_employee(employee_id: int):
    return delete_training_request_by_id(employee_id)
