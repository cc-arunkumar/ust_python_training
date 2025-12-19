from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.auth import create_access_token, verify_password

def login_user(db: Session, username: str, password: str):
    print("LOGIN INPUT ->", repr(username), repr(password))

    try:
        emp_id = int(username)
    except ValueError:
        print("USERNAME NOT INT")
        raise HTTPException(401, "Invalid credentials")

    user = db.query(User).filter(User.emp_id == emp_id).first()

    if not user:
        print("USER NOT FOUND IN DB")
        raise HTTPException(401, "Invalid credentials")

    print("DB PASSWORD ->", repr(user.password))

    if not verify_password(password, user.password):
        print("PASSWORD MISMATCH")
        raise HTTPException(401, "Invalid credentials")

    print("LOGIN SUCCESS")

    token = create_access_token({
        "emp_id": str(user.emp_id),
        "role": user.role.value
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }