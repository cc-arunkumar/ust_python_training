from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import get_db
from schemas.users import UserCreate, UserResponse, UserLogin, UserUpdate
from services.users_service import create_user, get_user_by_id, delete_user, update_user, patch_user, get_users
from database.mongodb import log_activity
from utils.auth import get_current_user, role_guard

router = APIRouter(prefix="/api/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db),current=Depends(role_guard(["Admin"]))):
    created = create_user(db, user) 
    log_activity(current["user"].emp_id, "create_user", created.id) 
    return created


@router.get("/", response_model=list[UserResponse])
def get_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db),current=Depends(role_guard(["Admin", "Manager"]))):
    """Get paginated users. Use query params `skip` and `limit`.

    Example: /users?skip=0&limit=20
    """
    return get_users(db, skip=skip, limit=limit)

@router.get("/{user_id}", response_model=UserResponse)
def get_by_id(user_id: int, db: Session = Depends(get_db),current=Depends(role_guard(["Admin", "Manager"]))):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(404, "User not found")
    return user

@router.put("/{user_id}", response_model=UserResponse)
def update(
    user_id: int,
    data: UserUpdate,
    db: Session = Depends(get_db),
    current=Depends(role_guard(["Admin"]))
):
    user = update_user(db, user_id, data)
    log_activity(current["user"].emp_id, "update_user", user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.patch("/{user_id}")
def patch(user_id: int, data: dict, db: Session = Depends(get_db),current=Depends(role_guard(["Admin"]))):
    updated = patch_user(db, user_id, data)
    if not updated:
        raise HTTPException(404, "User not found")
    log_activity(current["user"].emp_id, "patch_user", user_id)
    return {"message": "User updated"}

@router.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db),current=Depends(role_guard(["Admin"]))):
    if not delete_user(db, user_id):
        raise HTTPException(404, "User not found")
    log_activity(current["user"].emp_id, "delete_user", user_id)
    return {"message": "User deleted"}
