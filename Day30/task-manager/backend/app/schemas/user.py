"""from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class UserRole(str, Enum):
    admin = "admin"
    manager = "manager"
    employee = "employee"


class UserStatus(str, Enum):
    active = "active"
    inactive = "inactive"


class UserCreate(BaseModel):
    emp_id: int
    password: str
    role: UserRole


class UserPasswordUpdate(BaseModel):
    password: str


class UserStatusUpdate(BaseModel):
    status: UserStatus


class UserResponse(BaseModel):
    emp_id: int
    role: UserRole
    status: UserStatus
    created_at: datetime

    class Config:
        from_attributes = True
"""

from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class UserRole(str, Enum):
    admin = "admin"
    manager = "manager"
    employee = "employee"

class UserStatus(str, Enum):
    active = "active"
    inactive = "inactive"

class UserCreate(BaseModel):
    emp_id: int
    password: str
    role: UserRole

class UserPasswordUpdate(BaseModel):
    password: str

class UserStatusUpdate(BaseModel):
    status: UserStatus

class UserResponse(BaseModel):
    emp_id: int
    role: UserRole
    status: UserStatus
    created_at: datetime

    class Config:
        from_attributes = True