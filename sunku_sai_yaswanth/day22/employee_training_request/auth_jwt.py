from datetime import datetime, timedelta, timezone
import os
from typing import Optional
from fastapi import HTTPException, status, Depends,APIRouter
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError
from pydantic import BaseModel
from pathlib import Path
from dotenv import load_dotenv
 
load_dotenv()  
 
DEMO_USERNAME = ("admin")
DEMO_PASSWORD = ("password123")
 
# Security settings
SECURITY_KEY = ("hguyegfgeif-bfuesufbuewb")
ALGORITHM = "HS256"  
ACCESS_TOKEN_EXPIRE_MINUTES = 30
 
# Pydantic models for login, token, and user
class LoginRequest(BaseModel):
    username: str
    password: str
 
class Token(BaseModel):
    access_token: str
    token_type: str
 
class User(BaseModel):
    username: str
 
# Helper function to create JWT access token
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    to_encode = {"sub": subject}
   
    # Set expiration time
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)  # Default 15 mins expiration
   
    to_encode.update({"exp": expire})
   
    # Encode the token
    encoded = jwt.encode(to_encode, SECURITY_KEY, algorithm=ALGORITHM)
    return encoded
 
# Authorization setup using HTTPBearer (basic token auth)
security = HTTPBearer()
 
# Dependency function to get current user from JWT token
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials
   
    try:
        # Decode the token using the SECURITY_KEY and the specified algorithm
        payload = jwt.decode(token, SECURITY_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
   
    # Extract username from token
    username = payload.get("sub")
   
    # Check if username matches the demo user (hardcoded for demo purposes)
    if username != DEMO_USERNAME:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
   
    return User(username=username)