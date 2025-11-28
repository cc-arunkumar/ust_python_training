from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, status, Depends
from fastapi import APIRouter
# from aims_plus.env import DEMO_USERNAME,DEMO_PASSWORD,ACCESS_TOKEN_EXPIRE_MINUTES
# aims_plus\.env
from auth.login_function import create_access_token,get_current_user
from models.login_model import LoginRequest,User,Token
from dotenv import load_dotenv
import os

load_dotenv()

login_router=APIRouter(prefix="/login")


DEMO_USERNAME =os.getenv("DEMO_USERNAME")
DEMO_PASSWORD=os.getenv("DEMO_PASSWORD")

ACCESS_TOKEN_EXPIRE_MINUTES=os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


# /login endpoint → returns JWT token
@login_router.post("/login", response_model=Token)
def login(data: LoginRequest):
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    token = create_access_token(subject=data.username, expires_delta=expires)

    return Token(access_token=token, token_type="bearer")


# Protected endpoint

# @login_router.get("/me")
# def read_me(current_user: User = Depends(get_current_user)):
#     return {
#         "message": "This is a protected endpoint using JWT TOKEN",
#         "user": current_user,
#     }