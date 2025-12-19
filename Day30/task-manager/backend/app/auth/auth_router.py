from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.auth.auth_service import login_user

router = APIRouter(prefix="/api/auth", tags=["Auth"])

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    return login_user(db, username, password)
