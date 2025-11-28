from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime
import re
from fastapi import HTTPException

class Employee(BaseModel):
    emp_id: Optional[int] = None
    emp_code: str = Field(..., max_length=20)
    full_name: str = Field(..., max_length=100)
    email: str = Field(..., max_length=100)
    phone: str = Field(..., max_length=15)
    department: str = Field(..., max_length=50)
    location: str = Field(..., max_length=100)
    join_date: date
    status: str = Field(..., max_length=20)
    last_updated: Optional[datetime] = None

def validate_employee(emp: Employee):
    if not emp.emp_code.startswith("USTEMP"):
        raise HTTPException(status_code=422, detail="emp_code must start with 'USTEMP'")
    if not re.match(r"^[A-Za-z ]+$", emp.full_name):
        raise HTTPException(status_code=422, detail="full_name must contain only alphabets and spaces")
    if not emp.email.endswith("@ust.com"):
        raise HTTPException(status_code=422, detail="email must end with '@ust.com'")
    if not re.match(r"^[6-9]\d{9}$", emp.phone):
        raise HTTPException(status_code=422, detail="phone must be a valid 10-digit Indian mobile number")
    if emp.department not in {"HR", "IT", "Admin", "Finance"}:
        raise HTTPException(status_code=422, detail="Invalid department")
    if emp.location not in {"Bangalore", "Chennai", "Hyderabad", "Pune", "Trivandrum"}:
        raise HTTPException(status_code=422, detail="Invalid location")
    if emp.join_date > date.today():
        raise HTTPException(status_code=422, detail="join_date cannot be in the future")
    if emp.status not in {"Active", "Inactive", "Resigned"}:
        raise HTTPException(status_code=422, detail="Invalid status")
