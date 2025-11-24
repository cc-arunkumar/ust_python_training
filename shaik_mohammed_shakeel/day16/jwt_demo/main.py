from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError
from pydantic import BaseModel

# Initialize FastAPI application
app = FastAPI(title="minimal Jwt demo")

# Security settings
SECURITY_KEY = "change-this-key-in-real-projects"  
ALGORITHM = "HS256"  
ACCESS_TOKEN_EXPIRE_MINUTES = 30 

# Prompt for username and password (you could move this to environment variables in production)
username = input("Enter User Name: ")
password = input("Enter User Password: ")

DEMO_USERNAME = username
DEMO_PASSWORD = password

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
def get_curr_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
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

# POST /login - Generate JWT token for valid user
@app.post("/login", response_model=Token)
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
@app.get("/me")
def read_me(current_user: User = Depends(get_curr_user)):
    return {
        "message": "This is a protected JWT token route.",
        "username": current_user.username,
    }

# Sample output
# In Put given user details
# {
#   "username": "Shakeel",
#   "password": "Shakeel123"
# }

# After got the token

# Code	
# 200	
# Response body
# Download
# {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJOaXJhbmpuYSIsImV4cCI6MTc2Mzk5MDI1NH0.z2jZBY6L0lM6CDQmAx9P0cGjHwqYDYQZViQR1RFQDJw",
#   "token_type": "bearer"
# }

# In get given access token

# Code
# 200	
# Response body
# Download
# {
#   "message": "this is a protected jwt token",
#   "username": {
#     "username": "Shakeel"
#   }
# }