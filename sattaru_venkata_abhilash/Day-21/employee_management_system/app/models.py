from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class EmployeeCreate(BaseModel):
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)
    email: EmailStr
    position: Optional[str] = Field(None, max_length=50)
    salary: Optional[float] = Field(None, gt=0)
    hire_date: str

    class Config:
        min_anystr_length = 1
        anystr_strip_whitespace = True

class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    email: Optional[EmailStr]
    position: Optional[str] = Field(None, max_length=50)
    salary: Optional[float] = Field(None, gt=0)
    hire_date: Optional[str]
    
class EmployeeInDB(EmployeeCreate):
    employee_id: int
