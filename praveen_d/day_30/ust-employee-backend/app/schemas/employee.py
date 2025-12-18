from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class EmployeeSchema(BaseModel):
    emp_id: str = Field(..., min_length=3, max_length=50)
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    designation: str = Field(..., min_length=2, max_length=100)
    mgr_id: Optional[str] = None

    # class Config:
    #     from_attributes = True
