from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from utils.security import verify_password, create_access_token, create_refresh_token
from database import collections
from datetime import datetime

router = APIRouter()

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await collections["users"].find_one({"employee_id": form_data.username})
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"sub": user["employee_id"], "role": user["role"]})
    refresh_token = create_refresh_token({"sub": user["employee_id"]})

    await collections["refresh_tokens"].insert_one({
        "token": refresh_token,
        "employee_id": user["employee_id"],
        "created_at": datetime.utcnow()
    })

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }