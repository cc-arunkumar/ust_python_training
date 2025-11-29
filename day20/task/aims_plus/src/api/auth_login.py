from fastapi import HTTPException, status, Depends, APIRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt
from dotenv import load_dotenv
import os
from models.auth_models import LoginRequest,Token,User
from auth.auth_jwt_token import DEMO_PASSWORD,DEMO_USERNAME,ACCESS_TOKEN_EXPIRE_MINUTES,create_access_token

jwt_router = APIRouter(prefix="/jwt")
load_dotenv(os.path.join(os.path.dirname(__file__), "user_credentials.env"))

@jwt_router.post("/login", response_model=Token)
def login(data: LoginRequest):
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
 
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)
    return Token(access_token=token, token_type="bearer")
 