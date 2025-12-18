from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database.connection import Base

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    # One employee → one user account
    # Link to employees.emp_id (external employee identifier) so values match the employee table's emp_id
    emp_id = Column(String(155), ForeignKey("employees.emp_id"), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    roles = Column(JSON, nullable=False)

    status = Column(String(50))  # ACTIVE / INACTIVE

    employee = relationship("EmployeeDB", back_populates="user")


class RefreshTokenDB(Base): 
    __tablename__ = "refresh_tokens" 
    id = Column(Integer, primary_key=True, index=True) 
    token = Column(String(500), unique=True, nullable=False) 
    employee_id = Column(String(100), nullable=False) 
    created_at = Column(DateTime, default=datetime.utcnow) 
    expires_at = Column(DateTime) 

class ResetTokenDB(Base): 
    __tablename__ = "reset_tokens" 
    id = Column(Integer, primary_key=True, index=True) 
    email = Column(String(255), nullable=False) 
    code = Column(String(6), nullable=False) 
    expiry = Column(DateTime, nullable=False) 
    verified = Column(Integer, default=0) # 0 = False, 1 = True