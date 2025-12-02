from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import FastAPI, HTTPException, status, Depends,APIRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from models.auth_model import User
import os
from dotenv import load_dotenv
load_dotenv()
# Initialize FastAPI application


jwt_router=APIRouter(prefix="/auth")

# Secret key and algorithm used for JWT encoding/decoding
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # Token expiration time in minutes

# Demo credentials (taken from user input for simplicity)
DEMO_USERNAME = os.getenv("USER_NAME")
DEMO_PASSWORD = os.getenv("PASSWORD")


# Function to create JWT access token
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    to_encode = {"sub": subject}  # "sub" claim stores the username
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=60)  # default expiry
    to_encode.update({"exp": expire})  # "exp" claim stores expiration time
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded


# Security scheme: HTTP Bearer (Authorization header with Bearer token)
security = HTTPBearer()

# Dependency to get current user from JWT token
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials
    try:
        # Decode JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        # If decoding fails, token is invalid or expired
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    username = payload.get("sub")
    if username != DEMO_USERNAME:
        # If username in token doesn't match demo user
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return User(username=username)

