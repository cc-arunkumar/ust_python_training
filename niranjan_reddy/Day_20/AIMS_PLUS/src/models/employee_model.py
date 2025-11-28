from typing import Optional
from pydantic import BaseModel, Field, field_validator
from datetime import date

class EmployeeDirectory(BaseModel):
    # Optional emp_id field with a default value of 0
    emp_id: Optional[int] = 0
    
    # emp_code must start with 'USTEMP' and have a minimum length of 7 characters
    emp_code: str = Field(..., min_length=7, description="Must start with USTEMP")

    # full_name should only contain alphabets and spaces, and have a maximum length of 100 characters
    full_name: str = Field(..., max_length=100, description="Alphabets + spaces only")

    # email must end with '@ust.com', with a maximum length of 100 characters
    email: str = Field(..., max_length=100, description="Must end with @ust.com")

    # phone must be a valid 10-digit Indian mobile number starting with 6, 7, 8, or 9
    phone: str = Field(..., max_length=15, description="Indian mobile (10 digits)")

    # department should specify the department, such as HR/IT/Admin/Finance/etc.
    department: str = Field(..., description="HR/IT/Admin/Finance/etc.")

    # location should specify the Indian UST locations
    location: str = Field(..., description="Indian UST locations")

    # join_date must not be in the future, and must follow the format YYYY-MM-DD
    join_date: date = Field(..., description="Cannot be in the future or invalid format")

    # status must be one of the following: Active, Inactive, Resigned
    status: str = Field(..., description="Active/Inactive/Resigned")

    # Validator for emp_code, ensuring it starts with 'USTEMP'
    @field_validator("emp_code")
    def validate_emp_code(cls, val):
        if not val.startswith("USTEMP"):
            raise ValueError("emp_code must start with 'USTEMP'")
        return val

    # Validator for email, ensuring it ends with '@ust.com'
    @field_validator("email")
    def validate_email(cls, val):
        if not val.endswith("@ust.com"):
            raise ValueError("email must end with '@ust.com'")
        return val

    # Validator for phone, ensuring it's a valid 10-digit number starting with 6, 7, 8, or 9
    @field_validator("phone")
    def validate_phone(cls, val):
        if not (val.isdigit() and len(val) == 10 and val[0] in "6789"):
            raise ValueError("phone must be a valid 10-digit Indian mobile starting with 6/7/8/9")
        return val

    # Validator for join_date, ensuring it's not a future date and follows the correct format
    @field_validator("join_date")
    def validate_join_date(cls, val):
        if val > date.today():  # Ensure join_date is not a future date
            raise ValueError("join_date cannot be a future date")
        try:
            val.strftime("%Y-%m-%d")  # Ensure the date is in YYYY-MM-DD format
        except ValueError:
            raise ValueError("join_date must be in the format YYYY-MM-DD")
        return val

    # Validator for status, ensuring it's one of the valid statuses
    @field_validator("status")
    def validate_status(cls, val):
        valid_statuses = ["Active", "Inactive", "Resigned"]  # Allowed status values
        if val not in valid_statuses:
            raise ValueError(f"status must be one of: {', '.join(valid_statuses)}")
        return val
