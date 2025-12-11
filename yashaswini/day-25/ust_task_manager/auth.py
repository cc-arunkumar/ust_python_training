# auth_service.py

from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from pydantic import BaseModel
from sqlalchemy.orm import Session

from db_connection import SessionLocal
from database import Employee


# ---------------- CONFIG ----------------
SECRET_KEY = "UST-TaskTracker-Secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINS = 30


# ---------------- SCHEMAS ----------------
class LoginRequest(BaseModel):
    user_id: int
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class User(BaseModel):
    id: int


# ---------------- DB SESSION ----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- AUTHENTICATION ----------------
def authenticate_user(db: Session, user_id: int, password: str):
    """
    Validate user_id and password from employees table.
    """
    user = db.query(Employee).filter(Employee.user_id == user_id).first()

    if not user:
        return None

    if user.password != password:  # Plain password check since your table has plain text
        return None

    return user


# ---------------- JWT TOKEN CREATION ----------------
def create_access_token(subject: int, expires_delta: Optional[timedelta] = None):
    """
    Create a JWT token with user_id as 'sub'.
    JWT standard requires sub to be a string.
    """
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINS)
    )

    payload = {
        "sub": str(subject),  # must be string
        "exp": expire
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


# ---------------- GET CURRENT USER ----------------
security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    """
    Decode JWT, validate token, and fetch user from DB.
    """
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        sub_value = payload.get("sub")

        if sub_value is None:
            raise HTTPException(status_code=401, detail="Token missing subject")

        # Convert back to integer
        user_id = int(sub_value)

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid subject in token")

    user = db.query(Employee).filter(Employee.user_id == user_id).first()

    if not user:
        raise HTTPException(status_code=401, detail="User no longer exists")

    return {"id": user.user_id}


# ---------------- LOGIN HANDLER ----------------
def login(request: LoginRequest, db: Session):
    """
    Verify credentials and return JWT token.
    """
    user = authenticate_user(db, request.user_id, request.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid user_id or password")

    token = create_access_token(subject=user.user_id)

    return {
        "access_token": token,
        "token_type": "bearer"
    }
