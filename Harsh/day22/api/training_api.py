from fastapi import Depends, HTTPException, APIRouter
from auth.jwt_auth import User, get_current_user
from models.training_model import TrainingRequest
from crud.training_crud import (
    get_all_training,
    get_by_id,
    create_training,
    delete_training,
    update_trainig,
    partial_update
)

router = APIRouter(
    prefix="/api/v1/training-requests"
)

@router.get("/")
def list_training_requests(user: User = Depends(get_current_user)):
    try:
        return get_all_training()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching training requests: {str(e)}")

@router.get("/{id}")
def get_training_request(id: int, user: User = Depends(get_current_user)):
    try:
        trn = get_by_id(id)
        if not trn:
            raise HTTPException(status_code=404, detail="Training request not found")
        return trn
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching training request: {str(e)}")

@router.post("/")
def create_training_request(trn: TrainingRequest, user: User = Depends(get_current_user)):
    try:
        return create_training(trn)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating training request: {str(e)}")

@router.put("/{id}")
def update_training_request(id: int, trn: TrainingRequest, user: User = Depends(get_current_user)):
    try:
        return update_trainig(id, trn)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating training request: {str(e)}")

@router.patch("/{id}")
def patch_training_request(id: int, trng_title: str, user: User = Depends(get_current_user)):
    try:
        return partial_update(id, trng_title)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error partially updating training request: {str(e)}")

@router.delete("/{id}")
def delete_training_request(id: int, user: User = Depends(get_current_user)):
    try:
        result = delete_training(id)
        if not result:
            raise HTTPException(status_code=404, detail="Training request not found")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting training request: {str(e)}")
