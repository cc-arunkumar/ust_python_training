from pydantic import BaseModel
from typing import Optional

class EmployeeCreate(BaseModel):
    emp_code: str
    full_name: str
    email: str
    phone: str
    department: str
    location: str
    join_date: str   # YYYY-MM-DD
    status: str


class EmployeeUpdate(BaseModel):
    full_name: str
    email: str
    phone: str
    department: str
    location: str
    join_date: str
    status: str


class EmployeeStatusUpdate(BaseModel):
    status: str
