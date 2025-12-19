from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.auth.jwt_handler import create_access_token

ADMIN_USERNAME = "1"
ADMIN_PASSWORD = "password@123"

def login_user(db: Session, username: str, password: str):
    if username == ADMIN_USERNAME:
        if password != ADMIN_PASSWORD:
            raise HTTPException(401, "Invalid admin credentials")

        token = create_access_token({
            "emp_id": 0,
            "role": "admin",
            "username": ADMIN_USERNAME
        })
        return {"access_token": token, "token_type": "bearer"}

    user = db.query(User).filter(User.emp_id == int(username)).first()
    if not user or user.password != password:
        raise HTTPException(401, "Invalid credentials")

    token = create_access_token({
        "emp_id": user.emp_id,
        "role": user.role.value
    })
    return {"access_token": token, "token_type": "bearer"}
