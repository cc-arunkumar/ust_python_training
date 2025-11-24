from jose import jwt, JWTError
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
from typing import Optional

# Initialize FastAPI app
app = FastAPI(title="Minimal Authentication")

# Secret key and algorithm for JWT
SECRECT_KEY = "abcdefg"   # Used to sign JWT tokens (keep this secret in real apps!)
ALGORITHM = "HS256"       # Hashing algorithm for JWT
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiry time

# Demo credentials (entered at runtime)
user_name = input("Enter username:")
password = input("Enter password:")

DEMO_USERNAME = user_name
DEMO_PASSWORD = password

# ------------------ Pydantic Models ------------------

class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str

# ------------------ JWT Utility ------------------

def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    """
    Create a JWT access token with subject (username) and expiry.
    """
    to_encode = {"sub": subject}

    # Set expiry time
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})

    # Encode JWT
    encoded = jwt.encode(to_encode, SECRECT_KEY, algorithm=ALGORITHM)
    return encoded

# ------------------ Security Dependency ------------------

security = HTTPBearer()  # Extracts Authorization header

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    """
    Validate JWT token and return current user.
    """
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRECT_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")

    username = payload.get("sub")
    if username != DEMO_USERNAME:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return User(username=username)

# ------------------ Routes ------------------

@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    """
    Login endpoint: validates credentials and returns JWT token.
    """
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")

    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)

    return Token(access_token=token, token_type="bearer")

@app.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    """
    Protected endpoint: requires valid JWT token.
    """
    return {
        "message": "This is a protected endpoint",
        "user": current_user
    }

#Output
# {
#   "message": "This is a protected endpoint",
#   "user": {
#     "username": "arjun"
#   }
# }