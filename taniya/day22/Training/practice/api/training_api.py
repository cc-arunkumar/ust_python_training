from fastapi import HTTPException,APIRouter,Depends
from practice.crud.training_crud import (
    Create_employee,
    get_employees,
    get_employees_by_id,
    update_employee,
    update_training_title,
    delete_training
)
from practice.auth.login import get_username
from practice.models.login_model import user
from practice.models.training_models import Training

employee_router = APIRouter(prefix="/employee")

@employee_router.post("/create")
def employee_create(request:Training,current_user: user = Depends(get_username)):
    try:
        return Create_employee(request)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@employee_router.get("")
def get_employee(current_user: user = Depends(get_username)):
    try:
        return get_employees()
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
@employee_router.get("/{id}")
def get_employee_by_id(id,current_user: user = Depends(get_username)):
    try:
        return get_employees_by_id(id)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
    
@employee_router.put("/{id}")
def update(id:int,request:Training,current_user: user = Depends(get_username)):
    try:
        return update_employee(id,request)
    # employee_id,
            # request.employee_name,
            # request.training_title,
            # request.training_description,
            # request.requested_date.strftime("%Y-%m-%d"),
            # request.status,
            # request.manager_id,
            # request.last_updated,)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@employee_router.patch("/{id}/training_title")
def update_training(id:int,training_title:str,current_user: user = Depends(get_username)):
    return update_training_title(id,training_title)