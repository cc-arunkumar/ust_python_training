from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from jose import JWTError, jwt

app = FastAPI(title="Minimal JWT Auth API")

# ----------------------------------------------------------
# JWT / Security Settings
# ----------------------------------------------------------
SECRET_KEY = "khdcsk"            # Change to a strong secret in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINS = 30

# ----------------------------------------------------------
# Demo Credentials (for testing only)
# ----------------------------------------------------------
DEMO_USERNAME = input("Enter username: ")
DEMO_PASSWORD = input("Enter password: ")

# ----------------------------------------------------------
# Pydantic Models
# ----------------------------------------------------------

class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str

# ----------------------------------------------------------
# Function: Create JWT Token
# ----------------------------------------------------------

def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    """
    Generates a JWT token containing:
      - subject (username)
      - expiration time
    """
    to_encode = {"sub": subject}

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# HTTP Bearer auth (for token reading)
security = HTTPBearer()

# ----------------------------------------------------------
# Function: Validate Current User
# ----------------------------------------------------------

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials

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

# ----------------------------------------------------------
# Login Endpoint (Generate Token)
# ----------------------------------------------------------

@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    """
    Checks username/password.
    Returns a valid JWT access token.
    """
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINS)

    access_token = create_access_token(subject=data.username, expires_delta=expires)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# ----------------------------------------------------------
# Protected Endpoint
# ----------------------------------------------------------

@app.get("/read_me")
def read_me(current_user: User = Depends(get_current_user)):
    """
    Protected endpoint — requires a valid JWT token.
    """
    return {
        "message": "This is a protected endpoint using JWT TOKEN",
        "user": current_user,
    }
