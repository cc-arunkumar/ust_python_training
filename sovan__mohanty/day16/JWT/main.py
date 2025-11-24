from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from jose import JWTError, jwt
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional

# Create FastAPI app
app = FastAPI(title="Minimal JWT Auth")

# JWT configuration
secret_key = "change-this-secret-key-in-real-project"
algorithm = "HS256"
access_token_expire = 30  # minutes

# Demo user credentials (entered at runtime)
user_name = input("Enter the username")
password = input("Enter the password")
demo_user = user_name
demo_password = password

# Request/Response models
class Loginrequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str

# Function to create JWT token
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    to_encode = {"sub": subject}
    # Set expiry time
    if expires_delta:
        expires = datetime.now(timezone.utc) + expires_delta
    else:
        expires = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expires})
    # Encode JWT
    encoded = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded

# Security scheme
security = HTTPBearer()

# Dependency to validate token and return user
def get_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    username = payload.get("sub")
    if username != demo_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    return User(username=username)

# Login endpoint: returns JWT token
@app.post("/login", response_model=Token)
def login_request(data: Loginrequest):
    if data.username != demo_user or data.password != demo_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token or token expires"
        )
    expires = timedelta(minutes=access_token_expire)
    token = create_access_token(subject=data.username, expires_delta=expires)
    return Token(access_token=token, token_type="bearer")

# Protected endpoint: requires valid JWT
@app.get("/me")
def read_me(current_user: User = Depends(get_user)):
    return {
        "message": "This is protected by authorised token",
        "user": current_user
    }
    
#Sample Execution
# POST /login

# {
#   "username": "alice",
#   "password": "mypassword"
# }

# {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6...",
#   "token_type": "bearer"
# }


# GET /me

# {
#   "message": "This is protected by authorised token",
#   "user": {
#     "username": "alice"
#   }
# }
