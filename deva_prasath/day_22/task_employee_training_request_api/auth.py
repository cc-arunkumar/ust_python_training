from fastapi import HTTPException, status, Depends, APIRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt
from dotenv import load_dotenv
import os
 
jwt_router = APIRouter(prefix="/auth")   # Router for authentication endpoints
 
# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), "cred.env"))   # Load .env from current directory
 
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret")    # JWT secret key
ALGORITHM = "HS256"                                        # Token signing algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = 60                           # Token expiry time
 
DEMO_USERNAME = os.getenv("DEMO_USERNAME")                 # Demo login username
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD")                 # Demo login password
 
print("Loaded DEMO_USERNAME:", DEMO_USERNAME)              # Debug print to confirm user
print("Loaded DEMO_PASSWORD:", DEMO_PASSWORD)              # Debug print to confirm password
 
class LoginRequest(BaseModel):
    username: str                                          # Username input model
    password: str                                          # Password input model
 
class Token(BaseModel):
    access_token: str                                      # JWT token value
    token_type: str                                        # Token type (usually bearer)
 
class User(BaseModel):
    username: str                                          # User model for authenticated user
 
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    to_encode = {"sub": subject}                           # Set token subject
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))  # Set expiry
    to_encode.update({"exp": expire})                      # Add expiration to payload
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)   # Encode token
 
security = HTTPBearer()                                    # Bearer authentication dependency
 
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials                         # Extract token from header
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])   # Decode JWT token
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")  # Token invalid
 
    username = payload.get("sub")                          # Get username from token
    if username != DEMO_USERNAME:                          # Compare with stored demo credentials
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
 
    return User(username=username)                          # Return authenticated user
 
@jwt_router.post("/login", response_model=Token)
def login(data: LoginRequest):
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:   # Validate login credentials
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
 
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)   # Set token expiry
    token = create_access_token(subject=data.username, expires_delta=expires)  # Generate token
    return Token(access_token=token, token_type="bearer")      # Return JWT token
