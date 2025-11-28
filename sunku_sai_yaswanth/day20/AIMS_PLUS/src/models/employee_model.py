from typing import Optional
from pydantic import BaseModel, Field, field_validator
from datetime import date

class EmployeeDirectory(BaseModel):

    emp_id: Optional[int]=0

    emp_code: str = Field(..., min_length=7, description="Must start with USTEMP")

    full_name: str = Field(..., max_length=100, description="Alphabets + spaces only")

    email: str = Field(..., max_length=100, description="Must end with @ust.com")

    phone: str = Field(..., max_length=15, description="Indian mobile (10 digits)")

    department: str = Field(..., description="HR/IT/Admin/Finance/etc.")

    location: str = Field(..., description="Indian UST locations")

    join_date: date = Field(..., description="Cannot be in the future or invalid format")

    status: str = Field(..., description="Active/Inactive/Resigned")

    @field_validator("emp_code")
    def validate_emp_code(cls, val):
        if not val.startswith("USTEMP"):
            raise ValueError("emp_code must start with 'USTEMP'")
        return val

    @field_validator("email")
    def validate_email(cls, val):
        if not val.endswith("@ust.com"):
            raise ValueError("email must end with '@ust.com'")
        return val

    @field_validator("phone")
    def validate_phone(cls, val):
        if not (val.isdigit() and len(val) == 10 and val[0] in "6789"):
            raise ValueError("phone must be a valid 10-digit Indian mobile starting with 6/7/8/9")
        return val

    @field_validator("join_date")
    def validate_join_date(cls, val):
        if val > date.today():
            raise ValueError("join_date cannot be a future date")
        try:
            val.strftime("%Y-%m-%d")
        except ValueError:
            raise ValueError("join_date must be in the format YYYY-MM-DD")
        return val

    @field_validator("status")
    def validate_status(cls, val):
        valid_statuses = ["Active", "Inactive", "Resigned"]
        if val not in valid_statuses:
            raise ValueError(f"status must be one of: {', '.join(valid_statuses)}")
        return val
