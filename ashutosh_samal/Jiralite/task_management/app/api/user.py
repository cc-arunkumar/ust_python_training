from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.user import (
    UserCreate,
    UserUpdate,
    UserPatch,
    UserOut
)

router = APIRouter(prefix="/users", tags=["Users"])


def admin_only(user: dict):
    if user.get("active_role") != "ADMIN":
        raise HTTPException(status_code=403, detail="Admin only")


# 🔹 GET ALL USERS
@router.get("/", response_model=List[UserOut])
def get_all_users(
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    admin_only(user)
    return db.query(User).all()


# 🔹 GET USER BY EMP ID
@router.get("/{emp_id}", response_model=UserOut)
def get_user(
    emp_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    admin_only(user)

    usr = db.query(User).filter(User.e_id == emp_id).first()
    if not usr:
        raise HTTPException(status_code=404)

    return usr


# 🔹 CREATE USER
@router.post("/", response_model=UserOut)
def create_user(
    user_in: UserCreate,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    admin_only(user)

    if db.query(User).filter(User.e_id == user_in.e_id).first():
        raise HTTPException(status_code=400, detail="User already exists")

    usr = User(**user_in.dict())
    db.add(usr)
    db.commit()
    db.refresh(usr)
    return usr


# 🔹 UPDATE USER (ALL FIELDS)
@router.put("/{emp_id}", response_model=UserOut)
def update_user(
    emp_id: int,
    user_in: UserUpdate,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    admin_only(user)

    usr = db.query(User).filter(User.e_id == emp_id).first()
    if not usr:
        raise HTTPException(status_code=404)

    usr.password = user_in.password
    usr.roles = user_in.roles
    usr.status = user_in.status

    db.commit()
    db.refresh(usr)
    return usr


# 🔹 PATCH USER (STATUS ONLY)
@router.patch("/{emp_id}", response_model=UserOut)
def patch_user(
    emp_id: int,
    patch: UserPatch,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    admin_only(user)

    usr = db.query(User).filter(User.e_id == emp_id).first()
    if not usr:
        raise HTTPException(status_code=404)

    usr.status = patch.status
    db.commit()
    db.refresh(usr)
    return usr


# 🔹 DELETE USER
@router.delete("/{emp_id}")
def delete_user(
    emp_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    admin_only(user)

    usr = db.query(User).filter(User.e_id == emp_id).first()
    if not usr:
        raise HTTPException(status_code=404)

    db.delete(usr)
    db.commit()
    return {"message": "User deleted"}
