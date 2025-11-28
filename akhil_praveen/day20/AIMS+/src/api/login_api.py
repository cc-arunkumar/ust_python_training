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

load_dotenv()

login_router = APIRouter(prefix="/login")



DEMO_USERNAME = os.getenv("DEMO_USERNAME")
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD")

ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")



# Login endpoint to authenticate and return a JWT token
@login_router.post("/login", response_model=Token)
def login(data: LoginRequest):
    # Check if the provided username and password match the demo credentials
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Username or Password")
    
    # Generate the access token with expiration time
    expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    token = create_access_token(subject=data.username, expires_delta=expires)
    
    # Return the JWT token
    return Token(access_token=token, token_type="bearer")

# # Protected endpoint to access user information
# @login_router.get("/me")
# def read_me(current_user: User = Depends(get_current_user)):
#     # This is a protected endpoint, only accessible with a valid JWT token
#     return {
#         "message": "This is a protected endpoint using JWT TOKEN",
#         "user": current_user
#     }