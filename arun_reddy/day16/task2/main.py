from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from jose import JWTError, jwt

# Initialize FastAPI application
app = FastAPI(title="Minimal JWT Auth Demo")

# Secret key and algorithm used for JWT encoding/decoding
SECRET_KEY = "change-this-secret-key-in-real-projects"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20  # Token expiration time in minutes

# Demo credentials (taken from user input for simplicity)
user_name = input("Enter user name: ")
my_password = input("Enter password: ")
DEMO_USERNAME = user_name
DEMO_PASSWORD = my_password

# Request body model for login endpoint
class LoginRequest(BaseModel):
    username: str
    password: str

# Response model for token
class Token(BaseModel):
    access_token: str
    token_type: str

# User model (used for protected endpoints)
class User(BaseModel):
    username: str


# Function to create JWT access token
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    to_encode = {"sub": subject}  # "sub" claim stores the username
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)  # default expiry
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


# Login endpoint: verifies credentials and returns JWT token
@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        # Invalid credentials
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)
    return Token(access_token=token, token_type="bearer")


# Protected endpoint: requires valid JWT token
@app.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    return {
        "message": "This is a protected endpoint using JWT TOKEN",
        "user": current_user
    }
