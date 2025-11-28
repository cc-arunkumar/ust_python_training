from fastapi import FastAPI,APIRouter,HTTPException,Depends,status
from src.models.login_model import Token ,LoginRequest,User

from datetime import timedelta
from src.auth.jwt_auth import DEMO_PASSWORD,DEMO_USERNAME,get_current_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES
jwt_router = APIRouter(prefix="/jwt") 
@jwt_router.post("/login", response_model=Token)
def login(data: LoginRequest):
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
 
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)
    return Token(access_token=token, token_type="bearer")
 