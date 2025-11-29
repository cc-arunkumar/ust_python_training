from fastapi import APIRouter,HTTPException,status
from ..model.user_model import UserModel
from ..model.user_model import Token
from ..auth.jwt_auth import create_asset_token
import os
from dotenv import load_dotenv


login_router = APIRouter(prefix="/login")

load_dotenv()
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")

@login_router.post("",response_model=Token)
def login(user:UserModel):
    username = user.username
    password = user.password
    
    if username != USER_NAME or password != PASSWORD:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid username or password")
    
    token = create_asset_token(username)
    
    return Token(token=token,token_type="bearer")
    