from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Union
from jose import JWTError, jwt
from fastapi import Depends, HTTPException,status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from models.users import UserDB
from database.connection import get_db
import os
from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "UST-TaskTracker-Secret")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 7))

bearer_scheme = HTTPBearer()

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "type": "access"})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db)
):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        emp_id: str = payload.get("sub")
        token_type: str = payload.get("type")
        role: str = payload.get("role")

        if not emp_id or token_type != "access":
            raise HTTPException(status_code=401, detail="Invalid token")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user = db.query(UserDB).filter(UserDB.emp_id == emp_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return {"emp_id": emp_id, "roles": user.roles, "user": user}
# utils/auth.py

def verify_password(plain_password: str, stored_password: str) -> bool:
    # Direct comparison for plain-text passwords
    return plain_password == stored_password


def role_guard(required: Union[str, list[str]]):
    """
    Strict role-based authorization.
    - No role bypass
    - Only explicitly allowed roles can access
    """
    def _guard(current_user: Dict[str, Any] = Depends(get_current_user)):
        roles_raw = current_user.get("roles", []) or []
        # Normalize roles to a list (handle string or other types) and lowercase
        if isinstance(roles_raw, str):
            roles_list = [roles_raw]
        else:
            try:
                roles_list = list(roles_raw)
            except Exception:
                roles_list = []

        try:
            roles_lower = [str(r).lower() for r in roles_list]
        except Exception:
            roles_lower = []

        if isinstance(required, str):
            req_lower = required.lower()
            if req_lower not in roles_lower:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Only {required} role authorized"
                )
        else:
            required_lowers = [str(r).lower() for r in required]
            if not any(req in roles_lower for req in required_lowers):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Authorized roles: {required}"
                )

        return current_user
    return _guard

