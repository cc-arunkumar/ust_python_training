from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt
from model import User, Token, LoginRequest

# Secret key used to encode/decode JWT tokens
SECRET_KEY = "UST-TaskTracker-Secret"
# Algorithm used for encoding the JWT token
ALGORITHM = "HS256"
# Expiration time for the access token (in minutes)
ACCESS_TOKEN_EXPIRE_MINUTES = 30 

# Demo users (for authentication)
users = {
    "rahul": {
        "username": "rahul",
        "password": "password123"
    }
}

# Using the demo user's credentials
DEMO_USERNAME = users["rahul"]["username"] 
DEMO_PASSWORD = users["rahul"]["password"]

# Function to create a JWT token
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    # Prepare the payload with the subject (username)
    to_encode = {"sub": subject}
    
    # Set expiration time for the token (either default or custom)
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)  # Default expiration time is 15 minutes
    
    to_encode.update({"exp": expire})  # Add expiration to the token payload
    
    # Encode the JWT token using the secret key and algorithm
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded

# HTTPBearer security scheme to handle authorization headers in requests
security = HTTPBearer()

# Dependency to extract the current user from the JWT token
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    # Get the token from the request header
    token = credentials.credentials
    try:
        # Decode and verify the JWT token using the secret key and algorithm
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        # If decoding fails, raise an unauthorized error (invalid or expired token)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    
    # Extract the username from the token payload
    username = payload.get("sub")
    
    # Ensure the extracted username matches the demo username
    if username != DEMO_USERNAME:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    
    # Return the current user object
    return User(username=username)
