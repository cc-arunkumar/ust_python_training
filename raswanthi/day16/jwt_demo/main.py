#JWT 
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
# For simplicity, credentials are taken via input (not recommended in production!)
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
    """
    Create a JWT access token.
    - subject: the username (stored in 'sub' claim)
    - expires_delta: optional expiration time
    """
    to_encode = {"sub": subject}

    # Set expiration time
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})  # Add expiration claim
    
    # Encode JWT using secret key and algorithm
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded

# HTTPBearer for Authorization: Bearer <token>
security = HTTPBearer()

# HELPER FUNCTION: Decode + verify token
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    """
    Verify JWT token and return current user.
    - Decodes token
    - Validates signature & expiration
    - Checks if user exists
    """
    token = credentials.credentials  # extract token string only
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        # Raised if token is invalid or expired
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    username = payload.get("sub")
    if username != DEMO_USERNAME:
        # Reject if username in token doesn't match demo user
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    return User(username=username)


# /login endpoint → returns JWT token
@app.post("/login", response_model=Token)



def login(data: LoginRequest): 
    # Login endpoint:
    # - Validates username & password
    # - Returns JWT token if valid

    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    
    # Create token with expiration
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)

    return Token(access_token=token, token_type="bearer")


# Protected endpoint

@app.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    
    # Protected endpoint:
    # - Requires valid JWT in Authorization header
    # - Returns current user info
    return {
        "message": "This is a protected endpoint using JWT TOKEN",
        "user": current_user,
    }
