"""from fastapi import APIRouter, Depends,HTTPException,Query
from sqlalchemy.orm import Session
from app.utils.pagination import paginate
from app.database.connection import get_db
from app.schemas.user import (
    UserCreate, UserResponse,
    UserPasswordUpdate, UserStatusUpdate
)
from app.services.user_service import (
    create_user, get_all_users, get_user_by_id,
    update_password, update_status, delete_user
)
from app.utils.auth_dependency import require_role, get_current_user
from app.models.user import User

router = APIRouter(prefix="/api/users", tags=["Users"])


@router.post("/", response_model=UserResponse,
             dependencies=[Depends(require_role("admin"))])
def add_user(data: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, data.emp_id, data.password, data.role)


@router.get("/")
def get_all_users(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    query = db.query(User).order_by(User.emp_id.desc())
    return paginate(query, page, limit)


@router.get("/{emp_id}", response_model=UserResponse,
            dependencies=[Depends(require_role("admin"))])
def get_user(emp_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(db, emp_id)


@router.put("/{emp_id}/password")
def change_password(
    emp_id: int,
    data: UserPasswordUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    if current_user.role != "admin" and current_user.emp_id != emp_id:

        raise HTTPException(403, "Not allowed")
    return update_password(db, emp_id, data.password)


@router.patch("/{emp_id}/status",
              dependencies=[Depends(require_role("admin"))])
def change_status(
    emp_id: int,
    data: UserStatusUpdate,
    db: Session = Depends(get_db)
):
    return update_status(db, emp_id, data.status)


@router.delete("/{emp_id}",
               dependencies=[Depends(require_role("admin"))])
def remove_user(emp_id: int, db: Session = Depends(get_db)):
    return delete_user(db, emp_id)
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.user import UserCreate, UserResponse, UserPasswordUpdate, UserStatusUpdate
from app.services.user_service import create_user, get_user_by_id, update_password, update_status, delete_user
from app.utils.pagination import paginate
from app.utils.auth import require_roles, get_current_user
from app.models.user import User

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.post("/", response_model=UserResponse, dependencies=[Depends(require_roles("admin"))])
def add_user(data: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, data.emp_id, data.password, data.role)

@router.get("/")
def get_all_users(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    query = db.query(User).order_by(User.emp_id.desc())
    return paginate(query, page, limit)

@router.get("/{emp_id}", response_model=UserResponse, dependencies=[Depends(require_roles("admin"))])
def get_user(emp_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(db, emp_id)

@router.put("/{emp_id}/password")
def change_password(emp_id: int, data: UserPasswordUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    if current_user.role.value != "admin" and current_user.emp_id != emp_id:
        raise HTTPException(403, "Not allowed")
    return update_password(db, emp_id, data.password)

@router.patch("/{emp_id}/status", dependencies=[Depends(require_roles("admin"))])
def change_status(emp_id: int, data: UserStatusUpdate, db: Session = Depends(get_db)):
    return update_status(db, emp_id, data.status)

@router.delete("/{emp_id}", dependencies=[Depends(require_roles("admin"))])
def remove_user(emp_id: int, db: Session = Depends(get_db)):
    return delete_user(db, emp_id)