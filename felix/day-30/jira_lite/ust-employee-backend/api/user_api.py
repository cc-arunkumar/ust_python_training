from fastapi import APIRouter, HTTPException, Depends
from services.user_services import update_user_role, create_User, get_User_by_id
from models.user_model import UpdateRole,UserModel

user_router = APIRouter()


@user_router.put("/users/{emp_id}/role",tags=["Users"])
def update_user_role_endpoint(emp_id: int, role_update: UpdateRole):
    updated_user = update_user_role(emp_id, role_update.role)
    if updated_user is None:
        raise HTTPException(status_code=500, detail="User role update failed")
    return updated_user
@user_router.post("/users",tags=["Users"])
def create_new_user(user_data: UserModel):
    new_user = create_User(user_data)
    if new_user is None:
        raise HTTPException(status_code=500, detail="User creation failed")
    return new_user

@user_router.get("/users/{emp_id}",tags=["Users"])
def get_user_by_id_endpoint(emp_id: int):
    user = get_User_by_id(emp_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user