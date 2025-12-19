"""from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    designation: str
    manager_id: Optional[int] = None


class EmployeeCreate(EmployeeBase):
    # Optional account creation fields
    password: Optional[str] = None
    role: Optional[str] = None


class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    designation: Optional[str] = None
    manager_id: Optional[int] = None
    # Allow admin to update associated user account details
    password: Optional[str] = None
    role: Optional[str] = None
    status: Optional[str] = None


class EmployeeResponse(EmployeeBase):
    emp_id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
"""
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    designation: str
    manager_id: Optional[int] = None

class EmployeeCreate(EmployeeBase):
    # Optional account creation fields - accept from frontend so we can
    # create an associated `users` row when admin provides credentials.
    password: Optional[str] = None
    role: Optional[str] = None

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    designation: Optional[str] = None
    manager_id: Optional[int] = None

class EmployeeResponse(EmployeeBase):
    emp_id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True