from pydantic import BaseModel,Field,EmailStr,model_validator
from datetime import date
from typing import Literal

class EmployeeDirectory(BaseModel):
    emp_code: str = Field(..., pattern=r"^USTEMP[A-Za-z0-9-]+$")
    full_name: str = Field(..., pattern=r"^[A-Za-z ]+$")
    email: EmailStr
    phone: str = Field(..., pattern=r"^[6-9][0-9]{9}$")
    department: Literal['HR', 'IT', 'Admin', 'Finance','Support']
    location: Literal['Trivandrum', 'Bangalore', 'Chennai', 'Hyderabad', 'Mumbai', 'Delhi', 'Pune']
    join_date: date
    status: Literal['Active', 'Inactive', 'Resigned']

    @model_validator(mode="after")
    def validate(self):
        if not self.email.endswith("@ust.com"):
            raise ValueError("Email must belong to @ust.com domain")
        if self.join_date > date.today():
            raise ValueError("join_date cannot be in the future")
        return self
