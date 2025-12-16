from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import UserCreate, UserLogin, UserUpdate, UserOut
from app.schemas.common import Token
from app.db.mongo import get_mongo_db
from app.services.user_service import UserService
from app.core.dependencies import require_admin, get_current_user, AuthUser

router = APIRouter(prefix="/api/users", tags=["users"])

# -------------------------
# LOGIN: issues JWT token
# -------------------------
@router.post("/login", response_model=Token)
def login(body: UserLogin, db=Depends(get_mongo_db)):
    service = UserService(db)
    try:
        token = service.authenticate(body.user_id, body.password)
        return {"access_token": token, "token_type": "bearer"}
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

# -------------------------
# CREATE USER (admin only)
# -------------------------
@router.post("", response_model=UserOut)
def create_user(
    body: UserCreate,
    _: AuthUser = Depends(require_admin),
    db=Depends(get_mongo_db)
):
    service = UserService(db)
    try:
        user = service.create(body.user_id, body.password, body.role, body.status)
        return user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

# -------------------------
# UPDATE USER (admin only)
# -------------------------
@router.put("/{user_id}", response_model=UserOut)
def update_user(
    user_id: str,
    body: UserUpdate,
    _: AuthUser = Depends(require_admin),
    db=Depends(get_mongo_db)
):
    service = UserService(db)
    try:
        user = service.update(user_id, body.role, body.status)
        return user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

# -------------------------
# DELETE USER (admin only)
# -------------------------
@router.delete("/{user_id}")
def delete_user(
    user_id: str,
    _: AuthUser = Depends(require_admin),
    db=Depends(get_mongo_db)
):
    service = UserService(db)
    ok = service.delete(user_id)
    if not ok:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return {"deleted": True}

# -------------------------
# GET USER (admin only)
# -------------------------
@router.get("/{user_id}", response_model=UserOut)
def get_user(
    user_id: str,
    _: AuthUser = Depends(require_admin),
    db=Depends(get_mongo_db)
):
    service = UserService(db)
    user = service.get(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return {
        "user_id": user["UserId"],
        "role": user["role"],
        "status": user["status"]
    }

# -------------------------
# PATCH USER STATUS (admin only)
# -------------------------
@router.patch("/{user_id}/status", response_model=UserOut)
def patch_status(
    user_id: str,
    status_value: dict,
    _: AuthUser = Depends(require_admin),
    db=Depends(get_mongo_db)
):
    status_str = status_value.get("status")
    if status_str not in {"active", "inactive"}:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid status"
        )
    service = UserService(db)
    try:
        user = service.update(user_id, None, status_str)
        return user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
