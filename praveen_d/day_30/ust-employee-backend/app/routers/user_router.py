from fastapi import APIRouter, HTTPException, status, Depends
from schemas.users import UserSchema
from services.user_service import *
from utils.authorization import require_permission

user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# ---------------- LOGIN (OPEN) ----------------
@user_router.post("/login", status_code=status.HTTP_200_OK)
def login(emp_id: str, password: str):
    user = get_user(emp_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "message": "Login successful",
        "emp_id": user["emp_id"],
        "role": user["role"]
    }


# ---------------- CREATE USER (ADMIN ONLY) ----------------
@user_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission("user:create"))]
)
def create(user: UserSchema):
    created = create_user(user)
    if not created:
        raise HTTPException(status_code=400, detail="User already exists")
    return created


# ---------------- GET USER (ADMIN ONLY) ----------------
@user_router.get(
    "/{emp_id}",
    dependencies=[Depends(require_permission("user:read"))]
)
def get(emp_id: str):
    user = get_user(emp_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# ---------------- UPDATE USER (ADMIN ONLY) ----------------
@user_router.put(
    "/{emp_id}",
    dependencies=[Depends(require_permission("user:update"))]
)
def update(emp_id: str, user: UserSchema):
    updated = update_user(emp_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated


# ---------------- PATCH USER (ADMIN ONLY) ----------------
@user_router.patch(
    "/{emp_id}",
    dependencies=[Depends(require_permission("user:update"))]
)
def patch(emp_id: str, role: str | None = None, status_: str | None = None):
    data = {}
    if role:
        data["role"] = role
    if status_:
        data["status"] = status_

    updated = patch_user(emp_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated


# ---------------- DELETE USER (ADMIN ONLY) ----------------
@user_router.delete(
    "/{emp_id}",
    dependencies=[Depends(require_permission("user:delete"))]
)
def delete(emp_id: str):
    if not delete_user(emp_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
