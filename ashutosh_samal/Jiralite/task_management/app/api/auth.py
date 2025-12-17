from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.core.database import get_db
from app.models.user import User
from app.core.security import create_access_token, get_current_user

router = APIRouter(prefix="/auth", tags=["Auth"])


# ---------------------------
# LOGIN REQUEST SCHEMA
# ---------------------------
class LoginRequest(BaseModel):
    e_id: int
    password: str


# ---------------------------
# LOGIN API (JSON BODY)
# ---------------------------
@router.post("/login")
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.e_id == data.e_id, User.password == data.password)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token({
        "emp_id": user.e_id,
        "roles": user.roles
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# ---------------------------
# SWITCH ROLE (POST LOGIN)
# ---------------------------
@router.post("/switch-role")
def switch_role(
    active_role: str,
    user=Depends(get_current_user)
):
    if active_role not in user["roles"]:
        raise HTTPException(
            status_code=403,
            detail="User does not have this role"
        )

    token = create_access_token({
        "emp_id": user["emp_id"],
        "roles": user["roles"],
        "active_role": active_role
    })

    return {
        "access_token": token,
        "active_role": active_role
    }
