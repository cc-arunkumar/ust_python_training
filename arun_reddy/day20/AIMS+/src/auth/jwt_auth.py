from fastapi import FastAPI, HTTPException, status, Depends,APIRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt
import os
from dotenv import load_dotenv
load_dotenv()
from ..models.user_model import User
# Load environment variables from .env file
 

# Initialize the FastAPI app
jwt_router=APIRouter(prefix="/jwt")
# Secret key used to encode/decode JWTs (make sure to change this in real projects)
SECRECT_KEY= "hi-hello-how-are-you"
ALGORITHM = "HS256"  # The algorithm used to sign the JWT (HS256 is a commonly used symmetric key algorithm)
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Expiration time for the token (30 minutes)
# Input the demo username and password (not secure for production use

DEMO_USERNAME = os.getenv("USER_NAME")
DEMO_PASSWORD = os.getenv("PASSWORD")

# Pydantic model for the login request


# Function to create an access token for a user
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    # JWT payload includes the 'sub' (subject) which is the username
    to_encode = {"sub": subject}
    # Set the expiration time (default is 15 minutes, but can be overridden)
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    # Add the expiration time to the payload
    to_encode.update({"exp": expire})
    # Encode the payload into a JWT token using the secret key and algorithm
    encoded = jwt.encode(to_encode, SECRECT_KEY, algorithm=ALGORITHM)
    return encoded



# HTTPBearer used to extract and validate the token from requests

security = HTTPBearer()
# Function to get the current user based on the JWT token
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials  # Extract the token from the Authorization header
    try:
        # Decode the JWT token to get the payload
        payload = jwt.decode(token, SECRECT_KEY, algorithms=[ALGORITHM])
    except JWTError:
        # If token is invalid or expired, raise an HTTPException
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    # Get the 'sub' (username) from the payload
    username = payload.get("sub")

    # Check if the username matches the expected one (for demo purposes)
    if username != DEMO_USERNAME:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")


    # Return the current user information
    return User(username=username)

 
# Protected route that requires a valid JWT token to access
# @jwt_router.get("/me")
# def read_me(current_user: User = Depends(get_current_user)):
#     # This endpoint is protected; the user must be authenticated with a valid JWT token
#     return {
#         "message": "This is a protected endpoint using JWT TOKEN",
#         "user": current_user,
#     }

 


