import os
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException
from jose import jwt, JWTError
from pydantic import BaseModel

# Create a new APIRouter for authentication-related routes
router = APIRouter(prefix="/auth", tags=["Auth"])

# JWT settings
ALGORITHM = "HS256"  # Hashing algorithm for JWT signature (HS256 is HMAC using SHA-256)
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # The expiration time for the access token in minutes

# Fetch JWT_SECRET_KEY from environment variables
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "changeme")  # Default to "changeme" for local dev

# Raise an error if the JWT_SECRET_KEY is not found (important for security)
if not JWT_SECRET_KEY:
    raise RuntimeError("JWT_SECRET_KEY environment variable is required")

# Pydantic model for the login request (used to validate input)
class LoginRequest(BaseModel):
    username: str
    password: str

# Pydantic model for the token response (used to structure the response)
class TokenResponse(BaseModel):
    access_token: str
    token_type: str

# Function to create an access token (JWT)
def create_access_token(sub: str):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)  # Set expiration time
    payload = {"sub": sub, "exp": expire}  # JWT payload (contains the username and expiration time)
    return jwt.encode(payload, JWT_SECRET_KEY, algorithm=ALGORITHM)  # Encode and return the JWT

# Function to verify a JWT token and return the username (subject)
def verify_token(token: str):
    try:
        # Decode the JWT token (this will raise an error if the token is invalid or expired)
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")  # Extract the username from the token's payload
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username  # Return the username if the token is valid
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")  # Handle JWT errors

# Login endpoint to authenticate the user and issue a token
@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest):
    # Validate the user's credentials (for simplicity, you're checking hardcoded values)
    if payload.username != "admin" or payload.password != "password123":
        raise HTTPException(status_code=401, detail="Invalid credentials")  # Raise error if credentials are wrong

    # If credentials are valid, generate and return the JWT token
    token = create_access_token(sub=payload.username)
    return {"access_token": token, "token_type": "bearer"}  # Respond with the token and type
