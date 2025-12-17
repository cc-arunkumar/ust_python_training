from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status

from models.employees import Employee
from models.user import User
from auth.auth import create_access_token
from schemas.user import LoginRequest, LoginResponse


class LoginService:

    @staticmethod
    def login(payload: LoginRequest, db: Session) -> LoginResponse:
        try:
            # Validate input
            if not payload.email or not payload.password:
                raise HTTPException(
                    status.HTTP_400_BAD_REQUEST, 
                    "Email and password are required"
                )

            employee = db.query(Employee).filter(
                Employee.email == payload.email
            ).first()

            if not employee:
                raise HTTPException(
                    status.HTTP_401_UNAUTHORIZED, 
                    "Invalid credentials"
                )

            user = db.query(User).filter(
                User.emp_id == employee.emp_id
            ).first()

            if not user or user.password != payload.password:
                raise HTTPException(
                    status.HTTP_401_UNAUTHORIZED, 
                    "Invalid credentials"
                )

            if user.status != "ACTIVE":
                raise HTTPException(
                    status.HTTP_403_FORBIDDEN, 
                    "User inactive"
                )

            token = create_access_token(user.user_id)

            return LoginResponse(access_token=token, role=user.role)
        
        except HTTPException:
            raise
        except SQLAlchemyError as e:
            raise HTTPException(
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                f"Database error: {str(e)}"
            )
        except Exception as e:
            raise HTTPException(
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                f"Internal server error: {str(e)}"
            )