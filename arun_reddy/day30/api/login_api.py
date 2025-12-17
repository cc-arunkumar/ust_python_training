# routers/auth_router.py
from fastapi import APIRouter, HTTPException, status
from Models.user_model import LoginRequest, Token
from database.mysql_connection import SessionLocal, User
from authorise.auth import create_access_token

auth_router = APIRouter(prefix="/auth", tags=["Authentication"])

@auth_router.post("/login", response_model=Token)
def login(data: LoginRequest):

    db = SessionLocal()     
    try:
        user = db.query(User).filter(User.emp_id == data.emp_id).first()

        if not user or user.password != data.password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        if user.status.value != "active":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User is inactive"
            )

        token = create_access_token(
            subject=str(user.emp_id),
            role=user.role
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    finally:
        db.close()              
