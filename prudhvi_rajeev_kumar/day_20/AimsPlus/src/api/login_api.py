# src/api/login_api.py
from fastapi import APIRouter, HTTPException, status
from datetime import timedelta
from src.authentication.auth import (
    DEMO_USERNAME, DEMO_PASSWORD,
    create_access_token, LoginRequest, Token,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login", response_model=Token)
def login(data: LoginRequest):
    """
    Login endpoint: validates username/password and returns a JWT token.
    """
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password."
        )
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)
    return Token(access_token=token, token_type="bearer")
