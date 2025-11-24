from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from jose import JWTError, jwt


# FastAPI app

app = FastAPI(title="Minimal JWT Auth Demo")


# JWT configuration
SECRET_KEY = "change-this-secret-key-in-real-projects"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Demo user (in-memory)
user_name = input("Enter user name: ")
my_password = input("Enter passowrd: ")
DEMO_USERNAME = user_name

DEMO_PASSWORD = my_password


# Pydantic models
class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str


# Helper to create JWT
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    to_encode = {"sub": subject}

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded

# HTTPBearer for Authorization: Bearer <token>
security = HTTPBearer()

# Decode + verify token
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials  # extract token only
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


# /login endpoint → returns JWT token
@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)

    return Token(access_token=token, token_type="bearer")


# Protected endpoint

@app.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    return {
        "message": "This is a protected endpoint using JWT TOKEN",
        "user": current_user,
    }
# Sample output
# In Put given user details
# {
#   "username": "vikash",
#   "password": "Password123"
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
#     "username": "vikash"
#   }
# }