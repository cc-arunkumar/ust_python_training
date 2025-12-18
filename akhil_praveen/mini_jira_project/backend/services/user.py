from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from fastapi import HTTPException
from models.user import User
from models.employees import Employee
from services.employees import EmployeeService
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
DEFAULT_PASSWORD = "password"


class UserService:

    @staticmethod
    def create_if_not_exists(db: Session, emp_id: int, role: str):
        try:
            # Validate employee exists (use EmployeeService which has fallbacks for missing columns)
            employee = EmployeeService.get_by_id(db, emp_id)
            if not employee:
                raise HTTPException(404, f"Employee with ID {emp_id} not found")
            
            # Check if user already exists
            user = db.query(User).filter(User.emp_id == emp_id).first()

            if user:
                # Update roles if user exists
                roles = set(user.role.split(","))
                if role not in roles:
                    roles.add(role)
                    user.role = ",".join(sorted(roles))  # Sort for consistency
                    db.commit()
                    db.refresh(user)
                return user

            # Create new user
            user = User(
                emp_id=emp_id,
                password=DEFAULT_PASSWORD,  # Should be hashed in production
                role=role,
                status="ACTIVE"
            )
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        
        except HTTPException:
            db.rollback()
            raise
        except IntegrityError as e:
            db.rollback()
            raise HTTPException(400, f"Failed to create user: {str(e.orig)}")
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(500, f"Database error: {str(e)}")
        except Exception as e:
            db.rollback()
            raise HTTPException(500, f"Internal server error: {str(e)}")