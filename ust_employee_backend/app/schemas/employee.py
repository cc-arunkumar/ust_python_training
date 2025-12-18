from pydantic import BaseModel, EmailStr,Field
from typing import Optional

class EmployeeBase(BaseModel):
    name: str=Field(...)
    email: EmailStr=Field(...)
    designation: str= Field(...)
    manager_id: Optional[int] = None

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    emp_id: int

    class Config:
        from_attributes = True
