 
from fastapi import Depends,APIRouter, HTTPException,status
from src.model.model_maintenance_log import MaintenanceLog
from src.auth.jwt_authentication import get_current_user,User,DEMO_PASSWORD,DEMO_USERNAME,LoginRequest,ACCESS_TOKEN_EXPIRE_MINUTES,create_access_token
from datetime import timedelta
from src.model.model_login import User,LoginRequest,Token
router = APIRouter(prefix="/jwt")

@router.post("/login", response_model=Token)
def login(data: LoginRequest):
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
 
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)
    return Token(access_token=token, token_type="bearer")
 