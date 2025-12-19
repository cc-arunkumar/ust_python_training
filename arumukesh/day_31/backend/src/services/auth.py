# auth_service.py

from datetime import datetime, timedelta, timezone
from typing import Optional, List

from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from pydantic import BaseModel
from sqlalchemy.orm import Session

from src.database.db_connection import SessionLocal
from src.database.db_creation import User

# ---------------- CONFIG ----------------
SECRET_KEY = "UST-TaskTracker-Secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINS = 30

# ---------------- SCHEMAS ----------------
class LoginRequest(BaseModel):
    emp_id: int   # ← Changed this line
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


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
    Validate user_id and password from users table.
    """
    user = db.query(User).filter(User.emp_id == user_id).first()

    if not user:
        return None

    # Plain-text password check (as per your DB)
    if user.password != password:
        return None

    return user


# ---------------- JWT TOKEN CREATION ----------------
def create_access_token(
    subject: int,
    roles: List[str],
    expires_delta: Optional[timedelta] = None
):
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINS)
    )

    payload = {
        "sub": str(subject),  # JWT requires string
        "roles": roles,
        "exp": expire
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


# ---------------- GET CURRENT USER ----------------
security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload.get("sub"))
        roles = payload.get("roles", [])

    except (JWTError, ValueError):
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.emp_id == user_id).first()

    if not user:
        raise HTTPException(status_code=401, detail="User no longer exists")

    # Attach roles from token
    user.roles = roles
    return user


# ---------------- LOGIN HANDLER ----------------
def login(request: LoginRequest, db: Session):
    user = authenticate_user(db, request.emp_id, request.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid user_id or password")

    # ✅ Normalize roles → ALWAYS LIST
    if isinstance(user.role, str):
        roles = [r.strip() for r in user.role.split(",")]
    else:
        roles = []

    token = create_access_token(
        subject=user.emp_id,
        roles=roles
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "emp_id": user.emp_id,
            "roles": roles
        }
    }
