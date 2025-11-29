from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class Employee(BaseModel):
    employee_id: Optional[int] = None
    first_name: str = Field(..., max_length=50, pattern=r"^[A-Za-z- ]*$")
    last_name: str = Field(..., max_length=50, pattern=r"^[A-Za-z- ]*$")
    email: str = Field(..., max_length=100, pattern=r"^[A-Za-z0-9-.]+@ust.com$")
    position: Optional[str] = Field(None, max_length=50, pattern=r"[A-Za-z ]*+$")
    salary: Optional[float] = Field(None, gt=0)
    hire_date: date
