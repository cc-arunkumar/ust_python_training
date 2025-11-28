from fastapi import APIRouter, HTTPException, Depends
from ..auth.auth_jwt_token import get_current_user, create_access_token
from ..models.user_model import User, Token, LoginRequest
from datetime import timedelta
import os
from dotenv import load_dotenv
 
# Load environment variables from .env file
load_dotenv()
 
# Credentials and token expiry configuration from environment
user_name = os.getenv("USER_NAME")
pass_word = os.getenv("PASSWORD")
expire = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
 
# Create a router with prefix "/login"
login_router = APIRouter(prefix="/login")
 
 
# -------------------- Login Endpoint --------------------
@login_router.post("/", response_model=Token)
def login(user: LoginRequest):
    """
    Authenticate user with username and password.
    If valid, generate and return a JWT access token.
    """
    try:
        # Validate credentials against environment variables
        if (user.username != user_name or user.password != pass_word):
            raise HTTPException(status_code=404, detail="Invalid username or password")
 
        # Set token expiration time
        expires = timedelta(minutes=int(expire))
 
        # Generate JWT token
        token = create_access_token(user.username, expires)
 
        # Return token response
        return Token(token=token, token_type="bearer")
 
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=404, detail=str(e))