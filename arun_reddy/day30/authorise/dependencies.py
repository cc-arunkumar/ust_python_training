# auth/dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from database.mysql_connection import SessionLocal, User
from authorise.auth import decode_access_token
from Models.user_model import UserSchema

security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> UserSchema:

    payload = decode_access_token(credentials.credentials)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    emp_id = int(payload["sub"])

    db = SessionLocal()        
    try:
        user = db.query(User).filter(User.emp_id == emp_id).first()

        if not user or user.status.value != "active":
            raise HTTPException(status_code=401, detail="User not authorized")

        return UserSchema(
            emp_id=user.emp_id,
            role=user.role
        )

    finally:
        db.close()               
