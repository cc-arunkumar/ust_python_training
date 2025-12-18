# app/api/v1/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.mysql import get_db
from app.models.sql_models import User
from app.core.security import create_access_token
from app.utils.logger import create_log

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/login")
def login(emp_id: str, password: str, db: Session = Depends(get_db)):
    """
    Login endpoint. Returns JWT token if credentials are correct.
    """
    user = db.query(User).filter(
        User.emp_id == emp_id,
        User.password == password,
        User.status == "active"
    ).first()

    if not user:
        create_log(
            emp_id=emp_id,
            roles=[],
            module="AUTH",
            action="LOGIN_FAILED",
            description="Invalid credentials",
            status="FAILED"
        )
        raise HTTPException(status_code=401, detail="Invalid credentials")

    roles = user.roles.split(",") if user.roles else []

    token = create_access_token({
        "emp_id": user.emp_id,
        "roles": roles
    })

    create_log(
        emp_id=user.emp_id,
        roles=roles,
        module="AUTH",
        action="LOGIN_SUCCESS",
        description="User logged in successfully",
        status="SUCCESS"
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
