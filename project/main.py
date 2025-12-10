from datetime import datetime, timedelta, timezone
from typing import Optional, Dict

import csv
from fastapi import FastAPI, HTTPException, status, Depends, Body
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from jose import JWTError, jwt
import os

# ---------------------------
# App and security settings
# ---------------------------



app = FastAPI(title="Employee Auth API")

ACCESS_SECRET = os.getenv("ACCESS_SECRET", "access-secret-key")
REFRESH_SECRET = os.getenv("REFRESH_SECRET", "refresh-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1
REFRESH_TOKEN_EXPIRE_DAYS = 7

EMPLOYEE_CSV_PATH = os.getenv("EMPLOYEE_CSV_PATH", "employees.csv")

# ---------------------------
# Data loading from CSV
# ---------------------------

# employees_by_id: { employee_id: { "username": str, "password": str } }
employees_by_id: Dict[str, Dict[str, str]] = {}

# employees_by_username: { username: { "employee_id": str, "password": str } }
employees_by_username: Dict[str, Dict[str, str]] = {}


def load_employees():
    global employees_by_id, employees_by_username
    employees_by_id = {}
    employees_by_username = {}

    try:
        with open(EMPLOYEE_CSV_PATH, newline="") as f:
            reader = csv.DictReader(f)
            required_cols = {"employee_id", "username", "password"}
            if not required_cols.issubset(set(reader.fieldnames or [])):
                raise RuntimeError("CSV must contain columns: employee_id, username, password")

            for row in reader:
                emp_id = row["employee_id"].strip()
                username = row["username"].strip()
                password = row["password"].strip()  # For demo only. Use hashed passwords in production.

                if not emp_id or not username:
                    # Skip incomplete records
                    continue

                employees_by_id[emp_id] = {"username": username, "password": password}
                employees_by_username[username] = {"employee_id": emp_id, "password": password}
    except FileNotFoundError:
        # Provide a small in-memory fallback dataset for demo purposes
        employees_by_id = {
            "EMP001": {"username": "sohan", "password": "sohan123"},
            "EMP002": {"username": "ravi", "password": "ravi456"},
        }
        employees_by_username = {
            "sohan": {"employee_id": "EMP001", "password": "sohan123"},
            "ravi": {"employee_id": "EMP002", "password": "ravi456"},
        }


load_employees()

# ---------------------------
# Models
# ---------------------------

class LoginRequest(BaseModel):
    username: Optional[str] = None
    employee_id: Optional[str] = None
    password: str

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class AccessTokenResponse(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str
    employee_id: str

# ---------------------------
# JWT helpers
# ---------------------------

def create_access_token(subject: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = subject.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, ACCESS_SECRET, algorithm=ALGORITHM)

def create_refresh_token(subject: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = subject.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, REFRESH_SECRET, algorithm=ALGORITHM)

# ---------------------------
# Security dependency
# ---------------------------

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, ACCESS_SECRET, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid/expired token")

    username = payload.get("username")
    employee_id = payload.get("employee_id")

    # Validate user exists in current dataset
    record = employees_by_id.get(employee_id)
    if not record or record.get("username") != username:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return User(username=username, employee_id=employee_id)

# ---------------------------
# Auth endpoints
# ---------------------------

@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    # Validate that at least one identifier is provided
    if not data.username and not data.employee_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Provide username or employee_id")

    # Find user by employee_id OR username
    user_record = None
    username = None
    employee_id = None

    if data.employee_id:
        rec = employees_by_id.get(data.employee_id)
        if rec:
            user_record = rec
            username = rec["username"]
            employee_id = data.employee_id

    if not user_record and data.username:
        rec = employees_by_username.get(data.username)
        if rec:
            user_record = rec
            username = data.username
            employee_id = rec["employee_id"]

    if not user_record:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username/employee_id")

    # Check password (demo: plain text). Use hashed check in production.
    stored_password = user_record["password"]
    if data.password != stored_password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")

    subject = {"username": username, "employee_id": employee_id}
    access_token = create_access_token(subject=subject)
    refresh_token = create_refresh_token(subject=subject)

    return Token(access_token=access_token, refresh_token=refresh_token, token_type="bearer")

@app.post("/refresh", response_model=AccessTokenResponse)
def refresh(refresh_token: str = Body(..., embed=True)):
    # Expect body: { "refresh_token": "..." }
    try:
        payload = jwt.decode(refresh_token, REFRESH_SECRET, algorithms=[ALGORITHM])
        username: str = payload.get("username")
        employee_id: str = payload.get("employee_id")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid/expired refresh token")

    # Ensure user still exists
    record = employees_by_id.get(employee_id)
    if not record or record.get("username") != username:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    new_access_token = create_access_token(subject={"username": username, "employee_id": employee_id})
    return AccessTokenResponse(access_token=new_access_token, token_type="bearer")

# ---------------------------
# Protected endpoints
# ---------------------------

@app.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    return {
        "message": "This is a protected endpoint using JWT token",
        "user": current_user,
    }

@app.get("/dummy-data")
def get_dummy_data(current_user: User = Depends(get_current_user)):
    return {
        "message": "Here is some dummy data",
        "data": {
            "id": 1,
            "title": "FastAPI JWT Example",
            "owner": current_user.username,
            "employee_id": current_user.employee_id,
            "status": "active",
        },
    }
