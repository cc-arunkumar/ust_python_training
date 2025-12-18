from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from database.connection import get_db
from models.employee import EmployeeDB
from models.users import UserDB, RefreshTokenDB, ResetTokenDB
from utils.auth import (
    verify_password,
    create_access_token,
    create_refresh_token,
    get_current_user,
    SECRET_KEY,
    ALGORITHM
)
from schemas.auth_model import LoginRequest, ForgotPasswordRequest, ResetPasswordRequest, VerifyCodeRequest
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import re
from jose import jwt, JWTError, ExpiredSignatureError
import random, string

auth_router = APIRouter(prefix="/api", tags=["Auth"])
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


# -----------------------
# LOGIN
# -----------------------
@auth_router.post("/auth/login")
async def login( request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.emp_id == request.username).first()
    if not user or not verify_password(request.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    employee = db.query(EmployeeDB).filter(EmployeeDB.emp_id == user.emp_id).first()
    
    access_token = create_access_token({"sub": user.emp_id, "role": user.roles})
    refresh_token = create_refresh_token({"sub": user.emp_id, "role": user.roles})

    # Save refresh token
    db.add(RefreshTokenDB(
        token=refresh_token,
        employee_id=user.emp_id,
        created_at=datetime.now(timezone.utc),
        expires_at=datetime.now(timezone.utc) + timedelta(days=7)
    ))
    db.commit()

    # Build employee sub-object
    employee_obj = None
    if employee:
        def _fmt_eid(x):
            if x is None:
                return None
            try:
                digits = re.sub(r"\D", "", str(x))
                n = int(digits) if digits else None
                return f"E{n:03d}" if n is not None else None
            except Exception:
                return None

        mgr_id = _fmt_eid(employee.manager_id)
        employee_obj = {
            "e_id": _fmt_eid(employee.emp_id) or None,
            "name": employee.name,
            "email": employee.email,
            "designation": employee.designation,
            "mgr_id": mgr_id
        }

    user_obj = {
        "id": user.id,
        "username": user.emp_id,
        "role": [r.lower() for r in (user.roles or [])] if isinstance(user.roles, list) else [str(user.roles).lower()],
        "status": user.status or "active",
        "employee": employee_obj
    }

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "expires_in": 300,
        "user": user_obj
    }

# -----------------------
# FORGOT PASSWORD
# -----------------------
@auth_router.post("/forgot-password")
async def forgot_password(request: ForgotPasswordRequest, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.emp_id == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Email not registered")

    code = ''.join(random.choices(string.digits, k=6))
    expiry = datetime.now(timezone.utc) + timedelta(minutes=10)

    token = db.query(ResetTokenDB).filter(ResetTokenDB.email == request.email).first()
    if token:
        token.code = code
        token.expiry = expiry
        token.verified = 0
    else:
        token = ResetTokenDB(email=request.email, code=code, expiry=expiry)
        db.add(token)
    db.commit()

    print(f"Verification code for {request.email}: {code}")  # Simulate email

    return {"message": "Verification code sent (check console for demo)"}

# -----------------------
# VERIFY CODE
# -----------------------
@auth_router.post("/verify-code")
async def verify_code(request: VerifyCodeRequest, db: Session = Depends(get_db)):
    token = db.query(ResetTokenDB).filter(ResetTokenDB.email == request.email).first()
    if not token or token.code != request.code:
        raise HTTPException(status_code=400, detail="Invalid code")

    if datetime.now(timezone.utc) > token.expiry:
        raise HTTPException(status_code=400, detail="Code expired")

    token.verified = 1
    db.commit()

    return {"message": "Code verified successfully"}

# -----------------------
# RESET PASSWORD
# -----------------------
@auth_router.post("/reset-password")
async def reset_password(request: ResetPasswordRequest, db: Session = Depends(get_db)):
    token = db.query(ResetTokenDB).filter(ResetTokenDB.email == request.email).first()
    if not token or not token.verified:
        raise HTTPException(status_code=400, detail="Code not verified")

    hashed_pw = pwd_context.hash(request.new_password)
    user = db.query(UserDB).filter(UserDB.emp_id == request.email).first()
    if user:
        user.password = hashed_pw
        db.delete(token)
        db.commit()

    return {"message": "Password updated successfully"}

# -----------------------
# REFRESH TOKEN
# -----------------------
@auth_router.post("/refresh")
async def refresh_token(refresh_token: str, db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        emp_id = payload.get("sub")
        token_type = payload.get("type")
        if token_type != "refresh":
            raise HTTPException(status_code=401, detail="Wrong Refresh token")

        stored = db.query(RefreshTokenDB).filter(RefreshTokenDB.token == refresh_token).first()
        if not stored:
            raise HTTPException(status_code=401, detail="Refresh token revoked")
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Refresh token expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    user = db.query(UserDB).filter(UserDB.emp_id == emp_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_access_token = create_access_token({"sub": emp_id, "role": user.roles})
    new_refresh_token = create_refresh_token({"sub": emp_id, "role": user.roles})

    # Delete old refresh token
    if stored:
        db.delete(stored)
    db.add(RefreshTokenDB(
        token=new_refresh_token,
        employee_id=emp_id,
        created_at=datetime.now(timezone.utc),
        expires_at=datetime.now(timezone.utc) + timedelta(days=7)
    ))
    db.commit()

    return {
        "access_token": new_access_token,
        "token_type": "bearer",
        "expires_in": "300 seconds"
    }

# -----------------------
# LOGOUT
# -----------------------
@auth_router.post("/logout")
async def logout(current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    tokens = db.query(RefreshTokenDB).filter(RefreshTokenDB.employee_id == current_user.emp_id).all()
    for token in tokens:
        db.delete(token)
    db.commit()
    return {"message": "Logged out successfully"}
