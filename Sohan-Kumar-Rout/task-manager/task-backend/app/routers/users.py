from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.deps import get_current_user

router = APIRouter(prefix="/api/users", tags=["Users"])


@router.post("", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_current_user)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("", response_model=list[schemas.UserOut])
def get_users(db: Session = Depends(get_current_user)):
    return db.query(models.User).all()


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(404, "User not found")
    return user


@router.put("/{id}", response_model=schemas.UserOut)
def update_user(id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(404, "User not found")

    for field, value in user_update.dict(exclude_unset=True).items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user


@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(404, "User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}


@router.post("/login")
def user_login(payload: schemas.UserLogin, db: Session = Depends(get_current_user)):
    emp = db.query(models.Employee).filter(models.Employee.email == payload.email).first()
    if not emp:
        raise HTTPException(404, "Employee not found")

    user = db.query(models.User).filter(models.User.emp_id == emp.id).first()
    if not user:
        raise HTTPException(404, "User account not found")

    if user.password != payload.password:
        raise HTTPException(401, "Invalid password")

    return {
        "message": "Login successful",
        "token": f"user-token-{user.id}",
        "roles": user.roles,
        "emp_id": emp.id
    }
