from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.mysql import get_db
from models.user import User
from auth.dependencies import admin_only
from pydantic import BaseModel
from utils.audit_logger import log_audit
 
router = APIRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[Depends(admin_only)]
)
 
# ---------------- SCHEMA ----------------
class UserStatusUpdate(BaseModel):
    status: str  # ACTIVE or INACTIVE
 
 
# ---------------- GET USER ----------------
@router.get("/{emp_id}")
def get_user(emp_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.emp_id == emp_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
 
    log_audit(
        action="USER_VIEWED",
        emp_id=emp_id,
        ref_id=emp_id
    )
 
    return user
 
 
@router.post("/{emp_id}")
def create_user(emp_id: int, role: str, db: Session = Depends(get_db)):
    user = User(
        emp_id=emp_id,
        role=role,
        password="password",
        status="ACTIVE"
    )
    db.add(user)
    db.commit()
    db.refresh(user)
 
    log_audit(
        action="USER_CREATED",
        emp_id=emp_id,
        ref_id=emp_id
    )
 
    return user
 
 
@router.put("/{emp_id}")
def update_user(emp_id: int, role: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.emp_id == emp_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
 
    user.role = role
    db.commit()
 
    log_audit(
        action="USER_ROLE_UPDATED",
        emp_id=emp_id,
        ref_id=emp_id
    )
 
    return user
 
 
@router.delete("/{emp_id}")
def soft_delete_user(emp_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.emp_id == emp_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
 
    user.status = "INACTIVE"
    db.commit()
 
    log_audit(
        action="USER_DEACTIVATED",
        emp_id=emp_id,
        ref_id=emp_id
    )
 
    return {"message": "User deactivated successfully"}
 
 
@router.patch("/{emp_id}")
def update_user_status(
    emp_id: int,
    payload: UserStatusUpdate,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.emp_id == emp_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
 
    if payload.status not in ["ACTIVE", "INACTIVE"]:
        raise HTTPException(
            status_code=400,
            detail="Status must be either ACTIVE or INACTIVE"
        )
 
    user.status = payload.status
    db.commit()
 
    log_audit(
        action="USER_STATUS_UPDATED",
        emp_id=emp_id,
        ref_id=emp_id
    )
 
    return {
        "message": f"User status updated to {payload.status}",
        "emp_id": emp_id
    }
 
 