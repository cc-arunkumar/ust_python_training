from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.mysql import get_db
from app.models.sql_models import User, Employee
from app.schemas.user_schema import UserCreate, UserResponse
from app.api.deps import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

ALLOWED_ROLES = {"developer", "manager", "admin"}


# ---------------------------------------------------
# ROLE VALIDATION
# ---------------------------------------------------
def validate_roles(roles: list[str]):
    for role in roles:
        if role not in ALLOWED_ROLES:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid role: {role}"
            )


# ---------------------------------------------------
# CREATE USER (SIGNUP) - ADMIN ONLY
# ---------------------------------------------------
@router.post(
    "/signup",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def signup(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if "admin" not in current_user["roles"]:
        raise HTTPException(status_code=403, detail="Only admin can create users")

    validate_roles(user.roles)

    # Employee must exist
    employee = db.query(Employee).filter(
        Employee.emp_id == user.emp_id
    ).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    # User must not already exist
    existing = db.query(User).filter(User.emp_id == user.emp_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(
        emp_id=user.emp_id,
        password=user.password,
        roles=",".join(user.roles),
        status=user.status
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return UserResponse(
        emp_id=new_user.emp_id,
        roles=new_user.roles.split(","),
        status=new_user.status
    )


# ---------------------------------------------------
# GET USER BY EMP_ID - ADMIN ONLY
# ---------------------------------------------------
@router.get("/{emp_id}", response_model=UserResponse)
def get_user(
    emp_id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if "admin" not in current_user["roles"]:
        raise HTTPException(status_code=403, detail="Only admin can view users")

    user = db.query(User).filter(User.emp_id == emp_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return UserResponse(
        emp_id=user.emp_id,
        roles=user.roles.split(","),
        status=user.status
    )


# ---------------------------------------------------
# UPDATE USER BY EMP_ID (PUT) - ADMIN ONLY
# ---------------------------------------------------
@router.put("/{emp_id}", response_model=UserResponse)
def update_user(
    emp_id: str,
    user_data: UserCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if "admin" not in current_user["roles"]:
        raise HTTPException(status_code=403, detail="Only admin can update users")

    validate_roles(user_data.roles)

    user = db.query(User).filter(User.emp_id == emp_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.password = user_data.password
    user.roles = ",".join(user_data.roles)
    user.status = user_data.status

    db.commit()
    db.refresh(user)

    return UserResponse(
        emp_id=user.emp_id,
        roles=user.roles.split(","),
        status=user.status
    )


# ---------------------------------------------------
# PATCH USER BY EMP_ID - ADD/REMOVE ROLES OR CHANGE STATUS
# ---------------------------------------------------
@router.patch("/{emp_id}", response_model=UserResponse)
def patch_user(
    emp_id: str,
    add_roles: list[str] | None = None,
    remove_roles: list[str] | None = None,
    status: str | None = None,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if "admin" not in current_user["roles"]:
        raise HTTPException(status_code=403, detail="Only admin can patch users")

    user = db.query(User).filter(User.emp_id == emp_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    current_roles = set(user.roles.split(","))

    if add_roles:
        validate_roles(add_roles)
        current_roles.update(add_roles)

    if remove_roles:
        current_roles.difference_update(remove_roles)

    if status:
        user.status = status

    user.roles = ",".join(sorted(current_roles))

    db.commit()
    db.refresh(user)

    return UserResponse(
        emp_id=user.emp_id,
        roles=user.roles.split(","),
        status=user.status
    )


# ---------------------------------------------------
# DELETE USER BY EMP_ID - ADMIN ONLY
# ---------------------------------------------------
@router.delete("/{emp_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    emp_id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if "admin" not in current_user["roles"]:
        raise HTTPException(status_code=403, detail="Only admin can delete users")

    user = db.query(User).filter(User.emp_id == emp_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return None
