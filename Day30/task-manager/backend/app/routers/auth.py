from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.auth import LoginRequest, LoginResponse
from app.database import get_db
from app.models.user import User
from app.core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):

    # 🔴 ADMIN LOGIN (HARDCODED)
    if data.username == "madhan" and data.password == "password@123":
        token = create_access_token({
            "sub": "admin",
            "role": "admin"
        })
        return {"access_token": token}

    # 🔵 USER LOGIN (Manager / Developer)
    user = db.query(User).filter(User.employee_id == int(data.username)).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    if user.password != data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    token = create_access_token({
        "sub": str(user.employee_id),
        "role": user.role
    })

    return {"access_token": token}

# print("DB PASSWORD:", user.password)
# print("INPUT PASSWORD:", data.password)

