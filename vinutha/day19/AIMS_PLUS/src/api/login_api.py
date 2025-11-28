from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.auth.jwt_auth import create_token

login_router = APIRouter(prefix="/login", tags=["Login"])


class Login(BaseModel):
    username: str
    password: str


# Simple login (no DB)
@login_router.post("/")
def login_user(data: Login):
    if data.username == "admin" and data.password == "password123":
        token = create_token({"username": data.username})
        return {"access_token": token}

    raise HTTPException(status_code=401, detail="Invalid username or password")
