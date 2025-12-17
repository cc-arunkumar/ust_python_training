from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.models import User, Employee, RoleEnum, StatusEnum
from auth import create_access_token   # only JWT helpers now
from deps import get_current_user      # HTTPBearer-based dependency
from datetime import timedelta
from mongo import log_activity 
router = APIRouter(tags=["Users"])

# Create a new user account
@router.post("/")
def create_user(emp_id: int, password: str, role: RoleEnum, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    existing = db.query(User).filter(User.emp_id == emp_id).first()
    if existing:
        raise HTTPException(status_code=409, detail="User already exists for this employee")

    # store plain password directly
    user = User(emp_id=emp_id, password=password, role=role, status=StatusEnum.ACTIVE)
    db.add(user)
    db.commit()
    db.refresh(user)
    log_activity(user.user_id, "user_created", {"emp_id": emp_id, "role": role})
    return user

# List all users (protected)
@router.get("/")
def list_users(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    log_activity(current_user.user_id, "list_users")
    return db.query(User).all()

# Get user by user_id (protected)
@router.get("/{user_id}")
def get_user(user_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    log_activity(current_user.user_id, "get_user", {"target_user": user_id})
    return user

# Login with user_id + password → returns JWT
@router.post("/login/by-user")
def login_by_user(user_id: int, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if user.status != StatusEnum.ACTIVE:
        raise HTTPException(status_code=403, detail=f"Account {user.status}")

    token = create_access_token(
        data={"user_id": user.user_id, "role": user.role},
        expires_delta=timedelta(minutes=30)
    )
    log_activity(user.user_id, "login_success", {"role": user.role})
    return {"access_token": token, "token_type": "bearer"}

# Login with emp_id + password → returns JWT
@router.post("/login/by-emp")
def login_by_emp(emp_id: int, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.emp_id == emp_id).first()
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if user.status != StatusEnum.ACTIVE:
        raise HTTPException(status_code=403, detail=f"Account {user.status}")

    token = create_access_token(
        data={"user_id": user.user_id, "role": user.role},
        expires_delta=timedelta(minutes=30)
    )
    log_activity(user.user_id, "login_success", {"role": user.role})
    return {"access_token": token, "token_type": "bearer"}

# Update user status (protected, only ADMIN)
@router.patch("/{user_id}/status")
def update_user_status(
    user_id: int,
    status: StatusEnum,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.role != RoleEnum.ADMIN:
        raise HTTPException(status_code=403, detail="Only ADMIN can update user status")

    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.status = status
    db.commit()
    db.refresh(user)
    log_activity(current_user.user_id, "update_user_status", {"target_user": user_id, "new_status": status})
    return {"user_id": user.user_id, "status": user.status}
