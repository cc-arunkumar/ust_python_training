from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class EmployeeBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    designation: str = Field(..., min_length=1, max_length=50)
    manager_id: Optional[str] = Field(None, max_length=10)


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    designation: Optional[str] = Field(None, min_length=1, max_length=50)
    manager_id: Optional[str] = Field(None, max_length=10)


class EmployeeResponse(EmployeeBase):
    emp_id: str
    class Config:
        from_attributes = True  # Pydantic v2 uses from_attributes
        # If using Pydantic v1, it should be: orm_mode = True
