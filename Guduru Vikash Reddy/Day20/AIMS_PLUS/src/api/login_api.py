from datetime import  timedelta
import os
from fastapi import HTTPException, status, Depends,APIRouter
from dotenv import load_dotenv

from src.auth.jwt_auth import ACCESS_TOKEN_EXPIRE_MINUTES, DEMO_PASSWORD, DEMO_USERNAME, LoginRequest, Token, User, create_access_token, get_curr_user


# Initialize FastAPI application
jwt_router=APIRouter(prefix="/jwt")


# POST /login - Generate JWT token for valid user
@jwt_router.post("/login", response_model=Token)
def login(data: LoginRequest):
    # Check if the provided username and password match the demo credentials
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    # Generate access token with specified expiration time
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)
    
    return Token(access_token=token, token_type="bearer")

# GET /me - Protected route that returns the logged-in user's details
@jwt_router.get("/me")
def read_me(current_user: User = Depends(get_curr_user)):
    return {
        "message": "This is a protected JWT token route.",
        "username": current_user.username,
    }


