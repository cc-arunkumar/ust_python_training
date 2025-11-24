from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from jose import JWTError, jwt

# Initialize FastAPI app with a descriptive title
app = FastAPI(title="JWT Authorization Demo")

# Security configuration constants
SECRET_KEY = "secret-key-for project"   # Secret key used to sign JWT tokens (keep safe in production!)
ALGORITHM = "HS256"                     # Algorithm used for JWT encoding/decoding
ACCESS_TOKEN_EXPIRE_MINUTES = 30        # Token expiration time in minutes

# Demo credentials (for testing only; in production use a database or secure auth provider)
user_name = input("Enter user Name: ")
password = input("Enter password: ")
DEMO_USERNAME = user_name
DEMO_PASSWORD = password

# ---------------------------
# Pydantic Models (Data Schemas)
# ---------------------------

class LoginRequest(BaseModel):
    """Schema for login request payload"""
    username: str
    password: str

class Token(BaseModel):
    """Schema for JWT token response"""
    access_token: str
    token_type: str
    
class User(BaseModel):
    """Schema representing a user"""
    username: str

# ---------------------------
# Utility Functions
# ---------------------------

def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    # Create a JWT access token.
    # Args:
    #     subject (str): The username or identifier for the token subject.
    #     expires_delta (Optional[timedelta]): Custom expiration time.
    # Returns:
    #     str: Encoded JWT token.
    to_encod = {"sub": subject}

    # Set expiration time (default 15 minutes if not provided)
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encod.update({"exp": expire})
    
    # Encode JWT token using secret key and algorithm
    encoded = jwt.encode(to_encod, SECRET_KEY, algorithm=ALGORITHM)
    return encoded

# HTTP Bearer security scheme for token extraction
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:

    # Validate JWT token and return current user.
    # Args:
    #     credentials (HTTPAuthorizationCredentials): Extracted bearer token.
    # Returns:
    #     User: Authenticated user object.
    # Raises:
    #     HTTPException: If token is invalid, expired, or user not found.
        
    token = credentials.credentials  # Extract token string
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

# ---------------------------
# API Endpoints
# ---------------------------

@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    
    # Login endpoint to authenticate user and issue JWT token.
    # Args:
    #     data (LoginRequest): Login request payload containing username and password.
    # Returns:
    #     Token: JWT access token with type 'bearer'.
    # Raises:
    #     HTTPException: If credentials are invalid.
    
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
    
    # Protected endpoint that requires valid JWT token.
    # Args:
    #     current_user (User): Authenticated user object.
    # Returns:
    #     dict: Message and user information.
    
    return {
        "message": "This is a protected endpoint using JWT TOKEN",
        "user": current_user,
    }

# ---------------------------
# Sample Output Demonstration
# ---------------------------

# Example login request payload:
# {
#   "username": "Shyam",
#   "password": "Password1234"
# }

# Example response after successful login:
# {
#   "access_token": "<JWT_TOKEN_STRING>",
#   "token_type": "bearer"   
# }

# Example response from protected endpoint (/me) with valid token:
# {
#   "message": "This is a protected endpoint using JWT TOKEN",
#   "user": {
#     "username": "Shyam"
#   }
# }