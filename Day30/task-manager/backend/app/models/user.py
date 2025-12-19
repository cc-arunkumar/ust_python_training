"""from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database.connection import Base
import enum

class UserRole(enum.Enum):
    admin = "admin"
    manager = "manager"
    employee = "employee"

class UserStatus(enum.Enum):
    active = "active"
    inactive = "inactive"

class User(Base):
    __tablename__ = "users"

    emp_id = Column(Integer, ForeignKey("employees.emp_id", ondelete="CASCADE"), primary_key=True)

    password = Column(String(255), nullable=False)

    role = Column(Enum(UserRole), nullable=False)
    status = Column(Enum(UserStatus), default=UserStatus.active, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
"""

from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database.connection import Base
import enum

class UserRole(enum.Enum):
    admin = "admin"
    manager = "manager"
    employee = "employee"

class UserStatus(enum.Enum):
    active = "active"
    inactive = "inactive"

class User(Base):
    __tablename__ = "users"
    emp_id = Column(Integer, ForeignKey("employees.emp_id", ondelete="CASCADE"), primary_key=True)
    password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    status = Column(Enum(UserStatus), default=UserStatus.active, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())