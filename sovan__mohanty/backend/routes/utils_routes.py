from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.models import Employee, User
from deps import get_current_user  # JWT + HTTPBearer dependency
from text import validate_remark_length
router = APIRouter(tags=["Utils"])

# Health check (public)
@router.get("/health")
def health_check():
    return {"status": "ok", "message": "Backend running smoothly"}

# Get employee with user account info (protected)
@router.get("/employee/{emp_id}")
def get_employee_with_user(emp_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {
        "emp_id": employee.emp_id,
        "name": employee.name,
        "designation": employee.designation,
        "user": {
            "user_id": employee.user.user_id if employee.user else None,
            "role": employee.user.role if employee.user else None,
            "status": employee.user.status if employee.user else None,
        }
    }

# Quick role check (protected)
@router.get("/role/{user_id}")
def check_role(user_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user.user_id, "role": user.role, "status": user.status}


