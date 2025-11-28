from pydantic import BaseModel, Field, model_validator
from typing import Optional
from datetime import date
import re

class EmployeeModel(BaseModel):
    emp_id: Optional[int] = None   # Auto-increment, handled by DB
    emp_code: str = Field(..., pattern=r"^USTEMP-[A-Za-z0-9]+$")
    full_name: str = Field(..., pattern=r"^[A-Za-z ]+$")
    email: str = Field(..., pattern=r"^[A-Za-z0-9._%+-]+@ust\.com$")
    phone: str = Field(..., pattern=r"^[6-9]\d{9}$")
    department: str
    location: str
    join_date: date
    status: str

    @model_validator(mode="after")
    def validate_all(self):
        # department check
        allowed_departments = ["HR", "IT", "Admin", "Finance", "Support"]
        if self.department not in allowed_departments:
            raise ValueError(f"department must be one of {allowed_departments}")

        # location check
        allowed_locations = ["Trivandrum", "Bangalore", "Chennai", "Hyderabad", "Pune", "Mumbai", "Delhi"]
        if self.location not in allowed_locations:
            raise ValueError(f"location must be one of {allowed_locations}")

        # join_date check
        if self.join_date > date.today():
            raise ValueError("join_date cannot be in the future")

        # status check
        allowed_status = ["Active", "Inactive", "Resigned"]
        if self.status not in allowed_status:
            raise ValueError(f"status must be one of {allowed_status}")

        return self
