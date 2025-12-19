"""# app/utils/auth.py

from datetime import datetime, timedelta
from jose import jwt
from app.config import SECRET_KEY, ALGORITHM

# Remove passlib and bcrypt code for plain text comparison
# from passlib.context import CryptContext

# CHANGE THIS FUNCTION TO PLAIN TEXT COMPARISON
def verify_password(plain_password: str, hashed_password: str):
    Compare passwords as plain text (no hashing)
    return plain_password == hashed_password

# Keep this function as-is
def create_access_token(data: dict, expires_delta: timedelta = timedelta(hours=1)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)"""


from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from typing import Union, List
from app.config import SECRET_KEY, ALGORITHM
from app.models.user import User
from app.database.connection import get_db

# Removed passlib and CryptContext completely

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

def verify_password(plain_password: str, stored_password: str):
    """Plain text comparison - NO HASHING"""
    return plain_password == stored_password

def create_access_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(minutes=60)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        emp_id: str = payload.get("emp_id")
        if emp_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.emp_id == int(emp_id)).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

def require_roles(required_roles: Union[List[str], str]):
    if isinstance(required_roles, str):
        required_roles = [required_roles]
    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role.value not in required_roles:
            raise HTTPException(403, "Insufficient permissions")
        return current_user
    return role_checker