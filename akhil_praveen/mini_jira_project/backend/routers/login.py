from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from database.mysql import get_db
from schemas.user import LoginRequest, LoginResponse
from services.login import LoginService

login_router = APIRouter(prefix="/auth", tags=["Auth"])


@login_router.post("/login", response_model=LoginResponse)
def login(
    payload: LoginRequest,
    db: Session = Depends(get_db)
):
    try:
        return LoginService.login(payload, db)
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        raise HTTPException(500, f"Database error during login: {str(e)}")
    except Exception as e:
        raise HTTPException(500, f"Internal server error: {str(e)}")