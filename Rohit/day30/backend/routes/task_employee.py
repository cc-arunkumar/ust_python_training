from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.models import Employee
from deps import get_current_user
from mongo import log_activity

router = APIRouter(tags=["Employees"])

# List all employees (protected)
# @router.get("/employees")
# def list_employees(current_user=Depends(get_current_user), db: Session = Depends(get_db)):
#     log_activity(current_user["user_id"], "list_employees")
#     employees = db.query(Employee).all()
#     return employees
