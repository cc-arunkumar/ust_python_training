from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from pydantic import BaseModel

# Initialize FastAPI application
app = FastAPI(title="Minimal OAuth2 Auth Demo")

# Secret key and algorithm used for JWT encoding/decoding
SECRET_KEY = "change-this-secret-key-in-real-projects"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20

# Demo credentials
DEMO_USERNAME = "demo_user"
DEMO_PASSWORD = "demo_pass"

# Response model for token
class Token(BaseModel):
    access_token: str
    token_type: str

# User model
class User(BaseModel):
    username: str


# Function to create JWT access token
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    to_encode = {"sub": subject}
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded


# OAuth2 scheme: expects Authorization header with Bearer token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Dependency to get current user from JWT token
def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username != DEMO_USERNAME:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        return User(username=username)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")


# Token endpoint (OAuth2 standard: POST /token)
@app.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != DEMO_USERNAME or form_data.password != DEMO_PASSWORD:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=form_data.username, expires_delta=expires)
    return Token(access_token=token, token_type="bearer")


# Protected endpoint
@app.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    return {
        "message": "This is a protected endpoint using OAuth2 + JWT",
        "user": current_user
    }
