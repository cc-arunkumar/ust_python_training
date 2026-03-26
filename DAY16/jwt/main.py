from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from jose import jwt, JWTError

app = FastAPI(title="JWT demo")

# SECURITY NOTE: Do not hardcode secret keys in production.
# Use environment variables or a secure configuration system.
SECRET_KEY = "PPPPQQQQMMMM1111"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# ISSUE: Using input() here will block FastAPI startup.
# FastAPI applications should not rely on console input.
# Instead, set DEMO_USERNAME and DEMO_PASSWORD as constants or environment variables.
myuser_name = input("Enter User Name :")
password = input("Enter Password :")
DEMO_USERNAME = myuser_name
DEMO_PASSWORD = password


class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str   

class User(BaseModel):
    username: str


def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    # Create JWT payload with subject (username)
    to_encode = {"sub": subject}
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        # Default expiry if none provided
        expire = datetime.now(timezone.utc) + timedelta(minutes=20)
    to_encode.update({"exp": expire})
    # Encode JWT with secret key
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials
    try:
        # Decode JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        # If decoding fails, token is invalid or expired
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or Expired token"
        )
    username = payload.get("sub")
    if username != DEMO_USERNAME:
        # Token subject must match demo username
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or Expired token"
        )
    return User(username=username)


@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    # Validate username and password
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect Username and password"
        )
    # Generate JWT token with expiry
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)
    return Token(access_token=token, token_type="bearer")


@app.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    # Protected route, requires valid JWT
    return {
        "message": "This is a protected user",
        "user": current_user
    }



"""SAMPLE OUTPUT
{
  "message": "This is a protected user",
  "user": {
    "username": "gowtham"
  }
}
"""