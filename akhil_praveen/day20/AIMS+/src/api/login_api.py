# Login API router for AIMS+ application.
# Exposes endpoints to authenticate users and obtain JWT access tokens.
# This module uses environment variables for demo credentials and token expiry.

from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import FastAPI, HTTPException, status, Depends,APIRouter
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel
from jose import JWTError, jwt
from ..auth.jwt_auth import create_access_token,get_current_user
import os
from dotenv import load_dotenv
from ..models.login_model import Token,LoginRequest,User

# Load environment variables from a .env file so DEMO_USERNAME/DEMO_PASSWORD and token settings are available.
load_dotenv()

# API router with prefix '/login' to group authentication endpoints.
login_router = APIRouter(prefix="/login")

# Demo credentials read from environment — used for this simple example application.
DEMO_USERNAME = os.getenv("DEMO_USERNAME")
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD")

# Token lifetime in minutes (as string in env, converted to int when used).
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")



# Login endpoint to authenticate and return a JWT token
@login_router.post("/login", response_model=Token)
def login(data: LoginRequest):
    # Validate provided credentials against demo values loaded from environment.
    # If credentials do not match, return 401 Unauthorized.
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Username or Password")
    
    # Create an expiration timedelta and generate a signed JWT access token.
    expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    token = create_access_token(subject=data.username, expires_delta=expires)
    
    # Return the token in the expected Token response model.
    return Token(access_token=token, token_type="bearer")

# Example protected endpoint (commented out).
# Use Depends(get_current_user) to require a valid Bearer token and extract the User model.
# @login_router.get("/me")
# def read_me(current_user: User = Depends(get_current_user)):
#     # This is a protected endpoint, only accessible with a valid JWT token
#     return {
#         "message": "This is a protected endpoint using JWT TOKEN",
#         "user": current_user
#     }