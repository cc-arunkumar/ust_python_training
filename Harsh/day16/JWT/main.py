# ============================
# Minimal JWT Auth Demo with FastAPI
# ============================

# Import libraries for time handling
from datetime import datetime, timedelta, timezone
# Pydantic for request/response models
from pydantic import BaseModel
# Optional type hint
from typing import Optional
# FastAPI core + error handling + dependency injection
from fastapi import FastAPI, HTTPException, status, Depends
# Security helpers for Bearer tokens
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# JWT library for encoding/decoding tokens
from jose import JWTError, jwt

# Create FastAPI app instance
app = FastAPI(title="Minimal JWT Auth demo")

# Security configuration
SECRET_KEY = "change-this-secret-key-in-real-projects"  # Secret key to sign JWTs
ALGORITHM = "HS256"                                    # Algorithm used for JWT
ACCESS_TOKEN_EXPIRE_MINUTES = 30                       # Token validity duration

# Demo user setup (prompting input when app starts)
user_name = input("enter the username:")   # Ask for username
my_password = input("enter the password:") # Ask for password

DEMO_USER = user_name                      # Save demo username
DEMO_PASSWORD = my_password                # Save demo password

# ============================
# Data Models
# ============================

class LoginRequest(BaseModel):
    username: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class User(BaseModel):
    username: str
    
# ============================
# Token Creation Function
# ============================

def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    # Payload starts with subject (username)
    to_encode = {"sub": subject}
    if expires_delta:
        # If expiration provided, add it
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        # Default expiration = 15 minutes
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        
    # Add expiration to payload
    to_encode.update({"exp": expire})
    # Encode payload into JWT using secret key
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded

# ============================
# Security Dependency
# ============================

security = HTTPBearer()  # Expect Authorization header with Bearer token

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials  # Extract token from header
    try:
        # Decode token using secret key
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    except JWTError:
        # If decoding fails → unauthorized
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    username = payload.get("sub")  # Get username from token
    if username != DEMO_USER:
        # If username doesn’t match demo user → unauthorized
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    return User(username=username)  # Return user object

# ============================
# Login Endpoint
# ============================

@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    # Check if credentials match demo user
    if data.username != DEMO_USER or data.password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    # Create token with expiration
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)

    # Return token
    return Token(access_token=token, token_type="bearer")

# ============================
# Protected Endpoint
# ============================

@app.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    # Only accessible if valid token is provided
    return {
        "message": "This is a protected endpoint using JWT TOKEN",
        "user": current_user,
    }

# ============================
# Example Inputs and Outputs
# ============================

# """
#  Login Request (POST /login)
# --------------------------------
# Input:
# {
#   "username": "alice",
#   "password": "mypassword"
# }

# Output (Success):
# {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...", 
#   "token_type": "bearer"
# }

# Output (Failure - wrong password):
# {
#   "detail": "Incorrect username or password"
# }


#  Access Protected Endpoint (GET /me)
# ----------------------------------------
# Headers:
# Authorization: Bearer <your_access_token>

# Output (Success):
# {
#   "message": "This is a protected endpoint using JWT TOKEN",
#   "user": {
#     "username": "alice"
#   }
# }

# Output (Failure - invalid/expired token):
# {
#   "detail": "Invalid or expired token"
# }
# """
