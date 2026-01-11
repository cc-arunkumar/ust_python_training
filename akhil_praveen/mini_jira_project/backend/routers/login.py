from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from database.mysql import get_db
from schemas.user import LoginRequest, LoginResponse
from services.login import LoginService
from auth.auth import get_current_user
from database.mysql import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from models.employees import Employee

login_router = APIRouter(prefix="/auth", tags=["Auth"])


@login_router.post("/login", response_model=LoginResponse)
def login(
    payload: LoginRequest,
    db: Session = Depends(get_db)
):
    try:
        return LoginService.login(payload, db)
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        raise HTTPException(500, f"Database error during login: {str(e)}")
    except Exception as e:
        raise HTTPException(500, f"Internal server error: {str(e)}")




@login_router.get("/me")
def me(current=Depends(get_current_user), db: Session = Depends(get_db)):
    """Return current user information (emp_id, roles, emp_name)"""
    try:
        emp_name = None
        if current.emp_id:
            try:
                emp = db.query(Employee).filter(Employee.emp_id == current.emp_id).first()
                if emp:
                    # emp may be an ORM instance
                    emp_name = getattr(emp, "emp_name", None)
            except SQLAlchemyError:
                # Fallback: the employees table may not have all mapped columns yet (e.g., status).
                # Do a raw select for only the columns we need.
                row = db.execute(
                    text("SELECT emp_name FROM employees WHERE emp_id = :id LIMIT 1"),
                    {"id": current.emp_id},
                ).mappings().first()
                if row:
                    emp_name = row.get("emp_name")

        return {
            "user_id": current.user_id,
            "emp_id": current.emp_id,
            "roles": current.role,
            "emp_name": emp_name,
        }
    except Exception as e:
        raise HTTPException(500, f"Internal server error: {str(e)}")