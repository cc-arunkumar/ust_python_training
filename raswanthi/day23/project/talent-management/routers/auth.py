# routers/auth.py
from fastapi import APIRouter, HTTPException, Depends, status
from jose import JWTError,jwt
from datetime import timedelta
from fastapi.security import HTTPBearer
from database import collections
from utils.security import verify_password, create_access_token, create_refresh_token, get_current_user
from datetime import datetime


SECRET_KEY = "your-super-secret-key-2025-change-in-prod!!!"  # Use env var in prod
ALGORITHM = "HS256"

router = APIRouter(prefix="/api/auth", tags=["Auth"])

bearer_scheme = HTTPBearer()

@router.post("/login")
async def login(username: str, password: str):
    user = await collections["users"].find_one({"employee_id": username})
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"sub": user["employee_id"], "role": user["role"]})
    refresh_token = create_refresh_token({"sub": user["employee_id"]})

    # Store refresh token
    await collections["refresh_tokens"].insert_one({
        "token": refresh_token,
        "employee_id": user["employee_id"],
        "created_at": datetime.utcnow(),
        "expires_at": datetime.utcnow() + timedelta(days=7)
    })

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "expires_in": 30 * 60  # 30 minutes
    }

@router.post("/refresh")
async def refresh_token(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        emp_id = payload.get("sub")
        token_type = payload.get("type")

        if token_type != "refresh":
            raise HTTPException(status_code=401, detail="Invalid refresh token")

        # Validate token exists in DB
        stored = await collections["refresh_tokens"].find_one({"token": refresh_token})
        if not stored:
            raise HTTPException(status_code=401, detail="Refresh token revoked")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    user = await collections["users"].find_one({"employee_id": emp_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_access_token = create_access_token({"sub": emp_id, "role": user["role"]})

    return {
        "access_token": new_access_token,
        "token_type": "bearer",
        "expires_in": 30 * 60
    }

@router.post("/logout")
async def logout(current_user=Depends(get_current_user)):
    # Optional: revoke all refresh tokens for this user
    await collections["refresh_tokens"].delete_many({"employee_id": current_user["employee_id"]})
    return {"message": "Logged out successfully"}