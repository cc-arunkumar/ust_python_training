from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.mysql import get_db
from models.user import User
from models.employees import Employee
from auth.dependencies import admin_only
from pydantic import BaseModel
from utils.audit_logger import log_audit
from typing import List, Optional
 
router = APIRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[Depends(admin_only)]
)
 
# ---------------- SCHEMA ----------------
class UserStatusUpdate(BaseModel):
    status: str  # ACTIVE or INACTIVE


class CreateUser(BaseModel):
    emp_id: Optional[int] = None
    email: Optional[str] = None
    role: str
    password: Optional[str] = None


class UpdateUser(BaseModel):
    role: str
 
 
# ---------------- GET USER ----------------
@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    emp = None
    if user.emp_id:
        emp = db.query(Employee).filter(Employee.emp_id == user.emp_id).first()

    log_audit(action="USER_VIEWED", emp_id=user.emp_id, ref_id=user.user_id)

    return {
        "user_id": user.user_id,
        "emp_id": user.emp_id,
        "role": user.role,
        "status": user.status,
        "full_name": emp.full_name if emp else None,
        "email": emp.email if emp else None,
    }
 
 
@router.get("/", response_model=List[dict])
def list_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    # Return user fields plus basic employee info
    result = []
    for u in users:
        emp = None
        if u.emp_id:
            emp = db.query(Employee).filter(Employee.emp_id == u.emp_id).first()

        result.append(
            {
                "user_id": u.user_id,
                "emp_id": u.emp_id,
                "role": u.role,
                "status": u.status,
                "full_name": emp.emp_name if emp else None,
                "email": emp.email if emp else None,
            }
        )

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(payload: CreateUser, db: Session = Depends(get_db)):
    # payload may contain emp_id or we may try to resolve by email if provided in payload
    emp = None
    if hasattr(payload, "emp_id") and payload.emp_id:
        emp = db.query(Employee).filter(Employee.emp_id == payload.emp_id).first()
    else:
        # try to resolve by email if provided in payload (backwards compatibility)
        # payload may include an 'email' attribute in some calls
        email = getattr(payload, "email", None)
        if email:
            emp = db.query(Employee).filter(Employee.email == email).first()

    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found; create an employee first or provide emp_id")

    user = User(
        emp_id=emp.emp_id,
        role=payload.role,
        password=payload.password or "password",
        status="ACTIVE",
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    log_audit(action="USER_CREATED", emp_id=emp.emp_id, ref_id=user.user_id)

    return {
        "user_id": user.user_id,
        "emp_id": user.emp_id,
        "role": user.role,
        "status": user.status,
        "full_name": emp.emp_name if emp else None,
        "email": emp.email if emp else None,
    }
 
 
 
@router.put("/{user_id}")
def update_user(user_id: int, payload: UpdateUser, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.role = payload.role
    db.commit()

    log_audit(action="USER_ROLE_UPDATED", emp_id=user.emp_id, ref_id=user.user_id)

    emp = db.query(Employee).filter(Employee.emp_id == user.emp_id).first()
    return {
        "user_id": user.user_id,
        "emp_id": user.emp_id,
        "role": user.role,
        "status": user.status,
        "full_name": emp.full_name if emp else None,
        "email": emp.email if emp else None,
    }
 
@router.patch("/{user_id}")
def update_user_status(
    user_id: int,
    payload: UserStatusUpdate,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
 
    if payload.status not in ["ACTIVE", "INACTIVE"]:
        raise HTTPException(
            status_code=400,
            detail="Status must be either ACTIVE or INACTIVE"
        )
 
    user.status = payload.status
    db.commit()

    log_audit(action="USER_STATUS_UPDATED", emp_id=user.emp_id, ref_id=user.user_id)

    return {"message": f"User status updated to {payload.status}", "user_id": user.user_id}


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # soft-delete: mark user inactive
    user.status = "INACTIVE"
    db.commit()

    log_audit(action="USER_DEACTIVATED", emp_id=user.emp_id, ref_id=user.user_id)

    return {"message": "User deactivated successfully", "user_id": user.user_id}
 
 