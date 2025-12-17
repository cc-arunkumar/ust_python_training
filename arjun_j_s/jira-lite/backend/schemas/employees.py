from pydantic import BaseModel, EmailStr
from typing import Optional


class EmployeeCreate(BaseModel):
    emp_name: str
    email: EmailStr
    designation: Optional[str] = None
    manager_id: Optional[int] = None


class EmployeeUpdate(BaseModel):
    emp_name: Optional[str] = None
    email: Optional[EmailStr] = None
    designation: Optional[str] = None
    manager_id: Optional[int] = None


class EmployeeResponse(EmployeeCreate):
    emp_id: int

    class Config:
        from_attributes = True
