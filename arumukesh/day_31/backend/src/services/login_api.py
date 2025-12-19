
from fastapi import FastAPI, Depends, HTTPException,status,APIRouter
from sqlalchemy.orm import Session
# from logger import log_action
from src.database.db_creation import User
from src.services.auth import (
    login, 
    LoginRequest, 
    get_current_user, 
    get_db
)
from src.models.models import UserCreate,UserResponse,UserUpdate
# router = FastAPI(title="Task Manager API", version="1.0.0")

router = APIRouter(
    prefix="",
    tags=["login"]
)
# ---------------- LOGIN ROUTE ----------------
@router.post("/login")
def login_user(request: LoginRequest, db: Session = Depends(get_db)):
    return login(request, db)

@router.post(
    "/api/v1/users",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Users"]
)
async def create_user(
    user: UserCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new user (ADMIN only)"""

    if current_user.role.lower() != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admin users can create new users"
        )

    existing_user = db.query(User).filter(User.emp_id == user.emp_id).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this employee ID already exists"
        )

    db_user = User(
        emp_id=user.emp_id,
        password=user.password,
        role=user.role
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


@router.get(
    "/api/v1/users",
    response_model=list[UserResponse],
    status_code=status.HTTP_200_OK,
    tags=["Users"]
)
async def get_users(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all users (ADMIN only)"""

    if current_user.role.lower() != "admin":
        raise HTTPException(status_code=403, detail="Admin privileges required")

    users = db.query(User).all()
    return users


@router.get(
    "/api/v1/users/{emp_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    tags=["Users"]
)
async def get_user_by_emp_id(
    emp_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get user by employee ID (ADMIN only)"""

    if current_user.role.lower() != "admin":
        raise HTTPException(status_code=403, detail="Admin privileges required")

    user = db.query(User).filter(User.emp_id == emp_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

@router.put(
    "/api/v1/users/{emp_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    tags=["Users"]
)
async def update_user(
    emp_id: int,
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update user details (ADMIN only)"""

    if current_user.role.lower() != "admin":
        raise HTTPException(status_code=403, detail="Admin privileges required")

    user = db.query(User).filter(User.emp_id == emp_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user_update.password is not None:
        user.password = user_update.password

    if user_update.role is not None:
        user.role = user_update.role

    db.commit()
    db.refresh(user)

    return user

@router.delete(
    "/api/v1/users/{emp_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Users"]
)
async def delete_user(
    emp_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete user (ADMIN only)"""

    if current_user.role.lower() != "admin":
        raise HTTPException(status_code=403, detail="Admin privileges required")

    user = db.query(User).filter(User.emp_id == emp_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return None
