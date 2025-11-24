
# Minimal JWT Authentication Demo using FastAPI
# ---------------------------------------------
# This example demonstrates how to implement JWT-based authentication
# with FastAPI. It includes:
# - Login endpoint to issue JWT tokens
# - Protected endpoint that requires a valid token

from fastapi import FastAPI, HTTPException, status, Depends
from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from jose import JWTError, jwt

# Initialize FastAPI app
app = FastAPI(title="Minimal JWT Auth Demo.")

# Security constants (Replace with secure values in production)
SECRET_KEY = "change-this-secret-key-in-real-projects"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Demo credentials (Replace with DB or secure auth provider in production)
user_name = input("Enter user name : ")
my_password = input("Enter password : ")

DEMO_USERNAME = user_name
DEMO_PASSWORD = my_password

# Request model for login
class LoginRequest(BaseModel):
    username: str
    password: str

# Response model for JWT token
class Token(BaseModel):
    access_token: str
    token_type: str

# User model for authenticated user
class User(BaseModel):
    username: str

# Function to generate JWT access token
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    to_encode = {"sub": subject}  # "sub" claim stores username
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})  # Add expiration claim
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded

# Security dependency using HTTP Bearer authentication
security = HTTPBearer()

# Function to validate JWT and return current user
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    username = payload.get("sub")
    if username != DEMO_USERNAME:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    return User(username=username)

# Login endpoint: validates credentials and returns JWT token
@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password."
        )
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)
    return Token(access_token=token, token_type="bearer")

# Protected endpoint: requires valid JWT token
@app.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    return {
        "message": "This is a protected endpoint using JWT Token.",
        "user": current_user
    }


# ===========================
#  SAMPLE RUN & OUTPUT (Demo)
# ===========================

# Input:
# ------
# Enter user name : Prudhvi
# Enter password : Password123

# Step 1: Login Request
# ---------------------
# POST /login
# Content-Type: application/json

# {
#   "username": "Prudhvi",
#   "password": "Password123"
# }

# Step 2: Login Response
# ----------------------
# {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",  # JWT token
#   "token_type": "bearer"
# }

# Step 3: Access Protected Endpoint
# ---------------------------------
# GET /me
# Authorization: Bearer <access_token>

# Step 4: Response
# ----------------
# {
#   "message": "This is a protected endpoint using JWT Token.",
#   "user": {
#     "username": "Prudhvi"
#   }
# }

