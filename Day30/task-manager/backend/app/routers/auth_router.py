"""# app/routers/auth_router.py

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.models.user import User
from app.utils.auth import verify_password, create_access_token
from app.utils.auth_dependency import get_current_user  # if you use /me
from fastapi.security import OAuth2PasswordRequestForm 

router = APIRouter(prefix="/api/auth", tags=["Auth"])

## app/routers/auth_router.py


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.emp_id == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token({
        "emp_id": str(user.emp_id),
        "role": user.role.value
    })

    return {"access_token": access_token, "token_type": "bearer"}"""
    
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.services.auth_service import login_user

router = APIRouter(prefix="/api/auth", tags=["Auth"])

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return login_user(db, form_data.username, form_data.password)