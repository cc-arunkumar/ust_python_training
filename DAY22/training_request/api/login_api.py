from fastapi import APIRouter, HTTPException, status
from models.login_model import LoginRequest, Token
from auth.training_auth import create_access_token
import os
from dotenv import load_dotenv

jwt_router = APIRouter(prefix="/login")

load_dotenv()

DEMO_USERNAME = os.getenv("DEMO_USERNAME")
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD")
SECURITY_KEY = os.getenv("SECURITY_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

@jwt_router.post("/training", response_model=Token)
def login(data: LoginRequest):
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    token = create_access_token(subject=data.username)
    
    return Token(access_token=token, token_type="bearer")