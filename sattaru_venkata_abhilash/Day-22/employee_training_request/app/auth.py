import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError
from pydantic import BaseModel
from app.crud import create_training_request, read_all_training_requests, read_training_request_by_id, update_training_request_by_id, delete_training_request_by_id

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI application
jwt_router = APIRouter(prefix="/jwt")  # Create a router for JWT-related endpoints

# Security settings
SECURITY_KEY = "change-this-key-in-real-projects"  # Replace this with a strong secret key in real applications
ALGORITHM = "HS256"  # The algorithm used for signing the JWT token
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # Expiration time for the access token in minutes

# Retrieve username and password from environment variables (used for demo purposes)
DEMO_USERNAME = os.getenv("DEMO_USERNAME")
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD")

# Pydantic models for request and response
class LoginRequest(BaseModel):
    username: str  # Username input for login
    password: str  # Password input for login

class Token(BaseModel):
    access_token: str  # The JWT access token returned after login
    token_type: str  # The type of token, usually "bearer"

class User(BaseModel):
    username: str  # Represents the current user's username

# Function to create a JWT access token
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    """
    Creates a JWT token.
    :param subject: The subject of the token (typically the username).
    :param expires_delta: Optional expiry time for the token.
    :return: Encoded JWT token.
    """
    to_encode = {"sub": subject}  # The subject (usually the username)

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta  # Custom expiry time
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)  # Default expiry time

    to_encode.update({"exp": expire})  # Adding expiry time to the token payload

    encoded = jwt.encode(to_encode, SECURITY_KEY, algorithm=ALGORITHM)  # Encoding the token
    return encoded

# Security dependency that requires the user to provide a token
security = HTTPBearer()

# Function to get the current user from the JWT token
def get_curr_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    """
    Decodes the JWT token and retrieves the current user.
    :param credentials: The token sent in the request header.
    :return: The current user (username).
    :raises HTTPException: If token is invalid or expired.
    """
    token = credentials.credentials  # Extract token from authorization header

    try:
        payload = jwt.decode(token, SECURITY_KEY, algorithms=[ALGORITHM])  # Decode the JWT
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")

    username = payload.get("sub")  # Extract the username from the payload

    if username != DEMO_USERNAME:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return User(username=username)  # Return the user if the token is valid

# Endpoint for user login and generating JWT token
@jwt_router.post("/login", response_model=Token)
def login(data: LoginRequest):
    """
    Validates login credentials and generates an access token if successful.
    :param data: Contains username and password for login.
    :return: JWT token with expiration.
    """
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)  # Set expiry time for the token
    token = create_access_token(subject=data.username, expires_delta=expires)  # Generate the token
    return Token(access_token=token, token_type="bearer")  # Return the token in the response

# Protected route that requires the user to be authenticated
@jwt_router.get("/me")
def read_me(current_user: User = Depends(get_curr_user)):
    """
    This is a protected route that returns the username of the authenticated user.
    :param current_user: The current authenticated user retrieved from the JWT token.
    :return: A message indicating successful authentication along with the user's username.
    """
    return {"message": "This is a protected JWT token route.", "username": current_user.username}
