from fastapi import APIRouter, HTTPException, status
from src.models.login_model import LoginRequest, Token
from src.auth.auth import create_access_token
from datetime import timedelta
from src.auth.auth import get_curr_user
import os
from dotenv import load_dotenv

# Initialize FastAPI router
jwt_router = APIRouter(prefix="/login")

load_dotenv()

DEMO_USERNAME = os.getenv("DEMO_USERNAME")
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD")
SECURITY_KEY = os.getenv("SECURITY_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

@jwt_router.post("/login", response_model=Token)
def login(data: LoginRequest):
    # Check if the provided username and password match the demo credentials
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    # Generate access token with specified expiration time
    token = create_access_token(subject=data.username)
    
    return Token(access_token=token, token_type="bearer")