from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import (
    UserCreate,
    UserUpdate,
    UserStatusUpdate,
    UserResponse
)
from app.services.user_service import (
    create_user,
    get_user,
    update_user,
    update_user_status,
    delete_user
)
from app.core.security import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])


# ADMIN CHECK
def admin_only(current_user: dict = Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise Exception("Only admin allowed")
    return current_user


# CREATE USER
@router.post("/", response_model=UserResponse)
def create_user_api(
    data: UserCreate,
    db: Session = Depends(get_db),
    _: dict = Depends(admin_only)
):
    return create_user(db, data)


# GET USER
@router.get("/{employee_id}", response_model=UserResponse)
def get_user_api(
    employee_id: int,
    db: Session = Depends(get_db),
    _: dict = Depends(admin_only)
):
    return get_user(db, employee_id)


# UPDATE USER
@router.put("/{employee_id}", response_model=UserResponse)
def update_user_api(
    employee_id: int,
    data: UserUpdate,
    db: Session = Depends(get_db),
    _: dict = Depends(admin_only)
):
    return update_user(db, employee_id, data)


# UPDATE STATUS
@router.patch("/{employee_id}/status")
def update_status_api(
    employee_id: int,
    data: UserStatusUpdate,
    db: Session = Depends(get_db),
    _: dict = Depends(admin_only)
):
    return update_user_status(db, employee_id, data.status)


# DELETE USER
@router.delete("/{employee_id}")
def delete_user_api(
    employee_id: int,
    db: Session = Depends(get_db),
    _: dict = Depends(admin_only)
):
    return delete_user(db, employee_id)
