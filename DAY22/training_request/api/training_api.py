from fastapi import APIRouter,Depends
from crud.training_crud import *
from models.model import TrainingModel
from auth.training_auth import get_curr_user,User

router=APIRouter()

@router.post("/training")
def add_train(train:TrainingModel,current_user: User = Depends(get_curr_user)):
    create=create_training(train.training_id,train.training_name,train.training_title,train.training_description,train.requested_date,train.status,train.manager_id)
    return create

@router.get("/training")
def get_train(current_user: User = Depends(get_curr_user)):
    return get_all_training()

@router.get("/training/{id}")
def get_train_by_id(id:int,current_user: User = Depends(get_curr_user)):
    return get_training_by_id(id)
    
@router.put("/training/{id}")
def update_train(id:int, train:TrainingModel,current_user: User = Depends(get_curr_user)):
    return update_training_by_id(id,train.training_id,train.training_name,train.training_title,train.training_description,train.requested_date,train.status,train.manager_id)

@router.patch("/training/{id}")
def update_status(id:int, train:TrainingModel,current_user: User = Depends(get_curr_user)):
    return update_training_status(id,train.status)
    
@router.delete("/training/{id}")
def delete_train(id:int,current_user: User = Depends(get_curr_user)):
    return delete_training_by_id(id)