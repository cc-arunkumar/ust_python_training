import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError
from pydantic import BaseModel

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI application
jwt_router = APIRouter(prefix="/jwt")  # Create a router for JWT-related endpoints

# Security settings
SECURITY_KEY = "change-this-key-in-real-projects"  # Replace this with a strong secret key in real applications
ALGORITHM = "HS256"  # The algorithm used for signing the JWT token
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Expiration time for the access token in minutes

# Retrieve username and password from environment variables (used for demo purposes)
DEMO_USERNAME = os.getenv("DEMO_USERNAME")
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD")

# Pydantic models for request and response validation
class LoginRequest(BaseModel):
    username: str  # Username field for login request
    password: str  # Password field for login request

class Token(BaseModel):
    access_token: str  # JWT access token
    token_type: str  # Type of the token (usually "bearer")

class User(BaseModel):
    username: str  # User model with a single field for username

# Helper function to create a JWT access token
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    """
    Function to create and return a JWT access token.
    :param subject: The subject (usually the username) for whom the token is generated.
    :param expires_delta: Optional expiration time for the token. If not provided, defaults to 15 minutes.
    """
    to_encode = {"sub": subject}  # The payload will include the subject (username)

    # Set expiration time if provided, else default to 15 minutes
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)  # Default expiration of 15 minutes

    to_encode.update({"exp": expire})  # Add expiration time to the payload

    # Encode the token using the secret key and specified algorithm
    encoded = jwt.encode(to_encode, SECURITY_KEY, algorithm=ALGORITHM)
    return encoded  # Return the encoded JWT token

# Authorization setup using HTTPBearer (basic token auth)
security = HTTPBearer()  # Use HTTPBearer to extract and pass the token

# Dependency function to get the current user from the JWT token
def get_curr_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    """
    Extracts and decodes the JWT token, then returns the current user (based on the token).
    :param credentials: The HTTP authorization credentials (token) passed in the request.
    :return: The current authenticated user.
    :raises HTTPException: If the token is invalid or expired.
    """
    token = credentials.credentials  # Extract the token from the request

    try:
        # Decode the token using the secret key and the specified algorithm
        payload = jwt.decode(token, SECURITY_KEY, algorithms=[ALGORITHM])
    except JWTError:
        # If decoding fails (invalid or expired token), raise an HTTPException
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")

    # Extract the username (subject) from the token payload
    username = payload.get("sub")

    # Check if the username matches the demo user (for simplicity, hardcoded here)
    if username != DEMO_USERNAME:
        # If username doesn't match the demo user, raise an error
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return User(username=username)  # Return the user model with the username

# POST /login - Generate JWT token for a valid user
@jwt_router.post("/login", response_model=Token)
def login(data: LoginRequest):
    """
    Endpoint to authenticate a user and return a JWT token.
    :param data: The login request containing the username and password.
    :return: A JWT token if the credentials are valid.
    :raises HTTPException: If the username or password is incorrect.
    """
    # Check if the provided username and password match the demo credentials
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        # If invalid credentials, raise an unauthorized error
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    # Generate an access token with the specified expiration time (30 minutes)
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)

    # Return the generated token in the response
    return Token(access_token=token, token_type="bearer")

# GET /me - Protected route that returns the logged-in user's details
@jwt_router.get("/me")
def read_me(current_user: User = Depends(get_curr_user)):
    """
    A protected route that returns the details of the current logged-in user.
    This route requires a valid JWT token to access.
    :param current_user: The current authenticated user.
    :return: A message with the username of the current user.
    """
    return {
        "message": "This is a protected JWT token route.",
        "username": current_user.username,  # Return the username of the current user
    }
