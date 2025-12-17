from fastapi import APIRouter
from Models.user_model import UserSchema as User
from crud.user_crud import (
    create_user,
    get_user_by_id,
    get_users_by_emp_id,
    update_user_by_id,
    delete_user_by_id
)

user_router = APIRouter(prefix="/user")

@user_router.post("",tags=["Users"])
def create_user_endpoint(user: User):
    return create_user(user)

@user_router.get("/{user_id}",tags=["Users"])
def get_user(user_id: int):
    return get_user_by_id(user_id)

@user_router.get("/by-emp/{emp_id}",tags=["Users"])
def get_users_by_employee(emp_id: int):
    return get_users_by_emp_id(emp_id)

@user_router.put("/{user_id}",tags=["Users"])
def update_user(user_id: int, user: User):
    return update_user_by_id(user_id, user)

@user_router.delete("/{user_id}",tags=["Users"])
def delete_user(user_id: int):
    return delete_user_by_id(user_id)
