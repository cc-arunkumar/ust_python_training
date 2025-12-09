from fastapi import APIRouter
from src.models.training_pydentic import TrainingPydantic
from src.crud.training_service import (
    create_training_request,
    get_training_data,
    get_training_by_id,
    update_patch_by_training,
    update_put_by_training,
    delete_by_training
)

training_router = APIRouter(prefix="/training", tags=["Training Requests"])

@training_router.post("/create")
def create_request(training: TrainingPydantic):
    return create_training_request(training)

@training_router.get("")
def get_training():
    return get_training_data()

@training_router.get("/{id}")
def get_training_id(id: int):
    return get_training_by_id(id)

@training_router.patch("/{id}")
def update_patch_training(id: int, field: str, value: str):
    return update_patch_by_training(id, field, value)

@training_router.put("/{id}")
def update_put_training(id: int, training: TrainingPydantic):
    return update_put_by_training(id, training)

@training_router.delete("/{id}")
def delete_training(id: int):
    return delete_by_training(id)
