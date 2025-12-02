from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from jose import JWTError, jwt

# Initialize FastAPI application
app = FastAPI(title="Minimal OAuth2 Auth Demo")

# Secret key and algorithm for JWT encoding/decoding
SECRET_KEY = "change-this-secret-key-in-real-projects"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Demo credentials (replace with DB lookup in real apps)
DEMO_USERNAME = "Felix"
DEMO_PASSWORD = "password123"

# Pydantic models
class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str

def create_access_token(subject: str, expires_delta: Optional[timedelta] = None) -> str:
    """Create a JWT token for a given subject (username)."""
    to_encode = {"sub": subject}

    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})

    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded

# OAuth2 scheme: clients must send token in "Authorization: Bearer <token>"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """Validate JWT token and return current user."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    username = payload.get("sub")
    if username != DEMO_USERNAME:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    return User(username=username)

@app.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """OAuth2 login endpoint. Validates credentials and returns JWT token."""
    if form_data.username != DEMO_USERNAME or form_data.password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=form_data.username, expires_delta=expires)

    return Token(access_token=token, token_type="bearer")

@app.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    """Protected endpoint that returns current logged-in user's info."""
    return {
        "message": "This is protected endpoint using OAuth2 + JWT",
        "user": current_user
    }