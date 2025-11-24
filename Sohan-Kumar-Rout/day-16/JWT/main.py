from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from jose import JWTError, jwt

# FastAPI app
app = FastAPI(title="Minimal API")

# JWT configuration
SECURITY_KEY = "sohan-kumar-rout"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Demo user credentials (taken from input)
user_name = input("Enter the user name")
my_password = input("Enter the password ")

DEMO_USERNAME = user_name
DEMO_PASSWORD = my_password

# Pydantic models
class LoginRequest(BaseModel):
    username: str
    password: str   # note: typo in 'password'

class Token(BaseModel):
    access_token: str
    token_type: str
    
class User(BaseModel):
    username: str

# Helper to create JWT token
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    to_encode = {"sub": subject}
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded = jwt.encode(to_encode, SECURITY_KEY, algorithm=ALGORITHM)
    return encoded

# Security dependency
security = HTTPBearer()

# Decode and validate JWT
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECURITY_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid/expired token")
    username = payload.get("sub")
    if username != DEMO_USERNAME:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return User(username=username)

# Login endpoint
@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)
    return Token(access_token=token, token_type="bearer")

# Protected endpoint
@app.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    return {
        "message": "This is a protected endpoint using JWT TOKEN",
        "user": current_user,
    }


# -------------------------
# Example Outputs (JSON)
# -------------------------

# POST /login
# Request body:
# {
#   "username": "sohan",
#   "password": "sohan123"
# }
# Response:
# {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzb2hhbiIsImV4cCI6MTc2Mzk4NzA2Mn0.xUJL-FsqOwOGDIQtsKUZ831LoZ8hvZiJC-nLTd6pR5o",
#   "token_type": "bearer"
# }

# GET /me (with Authorization header: Bearer <token>)
# {
#   "message": "This is a protected endpoint using JWT TOKEN",
#   "user": {
#     "username": "sohan"
#   }
# }

# Error Example (wrong credentials for /login)
# {
#   "detail": "Incorrect username or password"
# }
