from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Models.user_model import LoginRequest
from database.mysql_connection import User as UserORM
from authorise.auth import create_access_token

def authenticate_user(db: Session, data: LoginRequest):

    user = db.query(UserORM).filter(UserORM.emp_id == data.emp_id).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if user.password != data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if user.status.value != "active":
        raise HTTPException(status_code=403, detail="User is inactive")

    return create_access_token(
        subject=str(user.emp_id),
        role=user.role
    )
