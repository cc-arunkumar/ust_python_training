from fastapi import APIRouter,HTTPException,Depends
from ..auth.authentication import get_current_user,create_access_token
from ..models.user_model import User,Token,LoginRequest
from datetime import timedelta
import os
from dotenv import load_dotenv

load_dotenv()

user_name = os.getenv("USER_NAME")
pass_word = os.getenv("PASSWORD")

expire = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


login_router = APIRouter(prefix="/login")


@login_router.post("/",response_model=Token)
def login(user:LoginRequest):
    try:
        if(user.username!=user_name or user.password!=pass_word):
            raise HTTPException(status_code=404,detail="Invalid username or password")
        expires = timedelta(minutes=int(expire))
        token = create_access_token(user.username,expires)
        return Token(token=token,token_type="bearer")
    except Exception as e:
        raise HTTPException(status_code=404,detail=str(e))
        
