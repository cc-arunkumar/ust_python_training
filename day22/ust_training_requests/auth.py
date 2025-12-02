
# JWT Authentication Rules
# 1. Every endpoint (except login) must require a valid JWT token.
# 2. JWT token must be sent using:
# Authorization: Bearer <token_here>
# 3. A separate login endpoint must be created:
# URL: /auth/login
# Accepts: username and password
# Returns: JWT token (access token)
# 4. Password check use these credentials: "admin" / "password123"
# 5. JWT must include:
# sub (username)
# exp (expiration timestamp)
# 6. JWT secret key must be stored in an environment variable:
# JWT_SECRET_KEY
# 7. Algorithm: HS256
# 8. Token expiration: 1 hour
# 8.IMPLEMENTATION RULES




from fastapi import APIRouter, HTTPException  # Import FastAPI router and exception handling
from pydantic import BaseModel  # Import BaseModel for Pydantic model
from typing import Optional  # For optional typing
from datetime import datetime, timedelta  # For handling date and time
import jwt  # For creating and verifying JSON Web Tokens (JWT)


# Define constants for JWT authentication
SECRET_KEY = "mysecretkey"  # Secret key to encode the JWT
ALGORITHM = "HS256"  # The algorithm to be used for encoding/decoding the JWT
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # The expiration time for the access token (in minutes)

from fastapi.security import OAuth2PasswordBearer  # Import OAuth2PasswordBearer for token-based authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")  # OAuth2PasswordBearer used to retrieve token from request

# Pydantic model for the token response
class Token(BaseModel):
    access_token: str  # The access token
    token_type: str  # The type of token (usually 'bearer')

# Create an APIRouter instance to handle authentication-related routes
router = APIRouter()

# POST route for login
@router.post("/login", response_model=Token)
def login(username: str, password: str):
    # Check if the credentials are valid
    if username == "root" and password == "pass@word1":
        # If valid, create the access token
        token = create_access_token(data={"sub": username})
        # Return the token with the token type 'bearer'
        return {"access_token": token, "token_type": "bearer"}
    # If the credentials are invalid, raise an HTTP 401 Unauthorized error
    raise HTTPException(status_code=401, detail="Invalid credentials")

# Function to create the access token
def create_access_token(data: dict):
    # Set the expiration time of the token
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Copy the input data and add the expiration time
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    
    # Encode the JWT using the secret key and algorithm specified
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt  # Return the encoded JWT
