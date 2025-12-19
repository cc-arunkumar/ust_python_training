"""from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User, UserStatus
from app.models.employee import Employee


def create_user(db: Session, emp_id: int, password: str, role: str):
    employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not employee:
        raise HTTPException(404, "Employee does not exist")

    if db.query(User).filter(User.emp_id == emp_id).first():
        raise HTTPException(400, "User already exists")

    user = User(emp_id=emp_id, password=password, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_all_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, emp_id: int):
    user = db.query(User).filter(User.emp_id == emp_id).first()
    if not user:
        raise HTTPException(404, "User not found")
    return user


def update_password(db: Session, emp_id: int, password: str):
    user = get_user_by_id(db, emp_id)
    user.password = password
    db.commit()
    return {"message": "Password updated successfully"}


def update_status(db: Session, emp_id: int, status: UserStatus):
    user = get_user_by_id(db, emp_id)
    user.status = status
    db.commit()
    return {"message": "User status updated"}


def delete_user(db: Session, emp_id: int):
    user = get_user_by_id(db, emp_id)
    db.delete(user)
    db.commit()
    return {"message": "User deleted"}
"""
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User, UserStatus
from app.models.employee import Employee
# No pwd_context since we're using plain text

def get_user_by_id(db: Session, emp_id: int):
    user = db.query(User).filter(User.emp_id == emp_id).first()
    if not user:
        raise HTTPException(404, "User not found")
    return user

def create_user(db: Session, emp_id: int, password: str, role: str):
    employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not employee:
        raise HTTPException(404, "Employee does not exist")
    if db.query(User).filter(User.emp_id == emp_id).first():
        raise HTTPException(400, "User already exists")
    
    # Plain text password
    user = User(emp_id=emp_id, password=password, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_all_users(db: Session):
    return db.query(User).all()

def update_password(db: Session, emp_id: int, password: str):
    user = get_user_by_id(db, emp_id)  # Now this is defined above
    user.password = password  # Plain text
    db.commit()
    return {"message": "Password updated successfully"}

def update_status(db: Session, emp_id: int, status: UserStatus):
    user = get_user_by_id(db, emp_id)
    user.status = status
    db.commit()
    return {"message": "User status updated"}

def delete_user(db: Session, emp_id: int):
    user = get_user_by_id(db, emp_id)
    db.delete(user)
    db.commit()
    return {"message": "User deleted"}