from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from database.mysql import get_db
from auth.auth import get_current_user
from models.user import User
from models.employees import Employee

users_router = APIRouter(prefix="/users", tags=["Users"])


@users_router.get("/", summary="List users")
def list_users(db: Session = Depends(get_db), user=Depends(get_current_user)):
    try:
        if "ADMIN" not in user.role:
            raise HTTPException(403, "Admin only")

        # Join users with employees to include employee name
        rows = db.query(User, Employee).join(Employee, User.emp_id == Employee.emp_id).all()
        result = []
        for u, e in rows:
            result.append({
                "id": getattr(u, "user_id", None),
                "emp_id": getattr(u, "emp_id", None),
                "username": getattr(e, "emp_name", None),
                "email": getattr(e, "email", None),
                "role": getattr(u, "role", None),
                "status": getattr(u, "status", None),
            })
        return result
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        raise HTTPException(500, f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(500, f"Internal server error: {str(e)}")


@users_router.get("/{user_id}", summary="Get user")
def get_user(user_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    try:
        if "ADMIN" not in user.role:
            raise HTTPException(403, "Admin only")
        u = db.query(User).filter(User.user_id == user_id).first()
        if not u:
            raise HTTPException(404, "User not found")
        e = db.query(Employee).filter(Employee.emp_id == u.emp_id).first()
        return {
            "id": u.user_id,
            "emp_id": u.emp_id,
            "username": getattr(e, "emp_name", None),
            "email": getattr(e, "email", None),
            "role": u.role,
            "status": u.status,
        }
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        raise HTTPException(500, f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(500, f"Internal server error: {str(e)}")


@users_router.post("/", status_code=201)
def create_user(payload: dict, db: Session = Depends(get_db), user=Depends(get_current_user)):
    try:
        if "ADMIN" not in user.role:
            raise HTTPException(403, "Admin only")

        emp_id = payload.get("emp_id")
        role_v = payload.get("role", "USER")
        if not emp_id:
            raise HTTPException(400, "emp_id is required")

        # Ensure employee exists
        emp = db.query(Employee).filter(Employee.emp_id == emp_id).first()
        if not emp:
            raise HTTPException(404, "Employee not found")

        new = User(emp_id=emp_id, password=payload.get("password", "password"), role=role_v, status=payload.get("status", "ACTIVE"))
        db.add(new)
        db.commit()
        db.refresh(new)
        return {"id": new.user_id, "emp_id": new.emp_id, "role": new.role, "status": new.status}
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(400, f"Integrity error: {str(e.orig)}")
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(500, f"Database error: {str(e)}")
    except Exception as e:
        db.rollback()
        raise HTTPException(500, f"Internal server error: {str(e)}")


@users_router.put("/{user_id}")
def update_user(user_id: int, payload: dict, db: Session = Depends(get_db), user=Depends(get_current_user)):
    try:
        if "ADMIN" not in user.role:
            raise HTTPException(403, "Admin only")
        u = db.query(User).filter(User.user_id == user_id).first()
        if not u:
            raise HTTPException(404, "User not found")
        # allow updating role and status
        if "role" in payload:
            u.role = payload["role"]
        if "status" in payload:
            u.status = payload["status"]
        db.commit()
        db.refresh(u)
        return {"id": u.user_id, "emp_id": u.emp_id, "role": u.role, "status": u.status}
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(500, f"Database error: {str(e)}")
    except Exception as e:
        db.rollback()
        raise HTTPException(500, f"Internal server error: {str(e)}")


@users_router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    try:
        if "ADMIN" not in user.role:
            raise HTTPException(403, "Admin only")
        u = db.query(User).filter(User.user_id == user_id).first()
        if not u:
            raise HTTPException(404, "User not found")
        db.delete(u)
        db.commit()
        return
    except HTTPException:
        raise
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(500, f"Database error: {str(e)}")
    except Exception as e:
        db.rollback()
        raise HTTPException(500, f"Internal server error: {str(e)}")
