from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import FastAPI, HTTPException, status, Depends,APIRouter
from pydantic import BaseModel
from jose import JWTError, jwt
import os
from dotenv import load_dotenv


load_dotenv()
# Initialize FastAPI application
jwt_router = APIRouter(prefix="/jwt")

# Secret key and algorithm for JWT encoding/decoding
# NOTE: In production, never hardcode secrets. Use environment variables or a secret manager.
SECRET_KEY = "change-this-secret-key-in-real-projects"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # JWT token expiry in minutes



# Demo credentials
DEMO_USERNAME = os.getenv("USER_NAME")
DEMO_PASSWORD = os.getenv("PASSWORD")

# Pydantic models for request and response validation
class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str

def create_access_token(subject: str, expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a JWT token for a given subject (username).
    
    Args:
        subject (str): The identity for whom the token is issued.
        expires_delta (Optional[timedelta]): Token expiration duration. Defaults to 15 minutes if None.
        
    Returns:
        str: Encoded JWT token.
    """
    to_encode = {"sub": subject}

    # Set token expiration time
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        
    to_encode.update({"exp": expire})

    # Encode the JWT token using the secret key and algorithm
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded

# Initialize HTTP Bearer security scheme
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    """
    Dependency to extract and validate the current user from JWT token.
    
    Args:
        credentials (HTTPAuthorizationCredentials): Bearer token from request header.
        
    Returns:
        User: Pydantic User model containing username.
    
    Raises:
        HTTPException: If token is invalid, expired, or username not recognized.
    """
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

@jwt_router.post("/login", response_model=Token)
def login(data: LoginRequest):
    """
    Endpoint for user login. Validates credentials and returns a JWT token.
    
    Args:
        data (LoginRequest): Request body containing username and password.
    
    Returns:
        Token: JWT access token and token type.
    
    Raises:
        HTTPException: If username or password is incorrect.
    """
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    
    # Create JWT token with expiration
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)
    
    return Token(access_token=token, token_type="bearer")

@jwt_router.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    """
    Protected endpoint that returns the current logged-in user's info.
    
    Args:
        current_user (User): Injected via dependency that validates JWT token.
    
    Returns:
        dict: Message and user information.
    """
    return {
        "message": "This is protected endpoint using JWT TOKEN",
        "user": current_user
    }

