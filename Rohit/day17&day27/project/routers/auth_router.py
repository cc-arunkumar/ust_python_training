from fastapi import APIRouter, HTTPException, Depends
from datetime import timedelta
from sqlalchemy.orm import Session

from models import LoginRequest, Token, UserDB
from auth import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from database import get_db

router = APIRouter(tags=["Authentication"])

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(
    UserDB.username == data.username,
    UserDB.password == data.password
).first()

    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)
    return Token(access_token=token, token_type="bearer")
