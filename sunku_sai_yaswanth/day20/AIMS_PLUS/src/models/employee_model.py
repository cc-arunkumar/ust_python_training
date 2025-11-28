from typing import Optional
from pydantic import BaseModel, Field, field_validator
from datetime import date

# Define the EmployeeDirectory model which represents an employee's data
class EmployeeDirectory(BaseModel):

    # Optional employee ID (default is 0)
    emp_id: Optional[int] = 0

    # Employee code must be at least 7 characters long and start with "USTEMP"
    emp_code: str = Field(..., min_length=7, description="Must start with USTEMP")

    # Full name of the employee, restricted to alphabets and spaces (max 100 characters)
    full_name: str = Field(..., max_length=100, description="Alphabets + spaces only")

    # Email must be a valid email that ends with "@ust.com"
    email: str = Field(..., max_length=100, description="Must end with @ust.com")

    # Phone number must be a valid 10-digit Indian mobile number starting with 6, 7, 8, or 9
    phone: str = Field(..., max_length=15, description="Indian mobile (10 digits)")

    # Department of the employee (e.g., HR, IT, Admin, Finance, etc.)
    department: str = Field(..., description="HR/IT/Admin/Finance/etc.")

    # Location of the employee in India (e.g., UST offices in various cities)
    location: str = Field(..., description="Indian UST locations")

    # Joining date must not be in the future and should be a valid date format
    join_date: date = Field(..., description="Cannot be in the future or invalid format")

    # Status of the employee (Active, Inactive, Resigned)
    status: str = Field(..., description="Active/Inactive/Resigned")

    # Validator for emp_code field
    # Ensures that the employee code starts with "USTEMP"
    @field_validator("emp_code")
    def validate_emp_code(cls, val):
        if not val.startswith("USTEMP"):
            raise ValueError("emp_code must start with 'USTEMP'")
        return val

    # Validator for email field
    # Ensures the email ends with "@ust.com"
    @field_validator("email")
    def validate_email(cls, val):
        if not val.endswith("@ust.com"):
            raise ValueError("email must end with '@ust.com'")
        return val

    # Validator for phone field
    # Ensures that the phone number is exactly 10 digits and starts with 6, 7, 8, or 9
    @field_validator("phone")
    def validate_phone(cls, val):
        if not (val.isdigit() and len(val) == 10 and val[0] in "6789"):
            raise ValueError("phone must be a valid 10-digit Indian mobile starting with 6/7/8/9")
        return val

    # Validator for join_date field
    # Ensures the join date is not in the future and is in the correct format (YYYY-MM-DD)
    @field_validator("join_date")
    def validate_join_date(cls, val):
        if val > date.today():
            raise ValueError("join_date cannot be a future date")  # The join date should not be in the future
        try:
            # Ensures the date is in the correct format (YYYY-MM-DD)
            val.strftime("%Y-%m-%d")
        except ValueError:
            raise ValueError("join_date must be in the format YYYY-MM-DD")
        return val

    # Validator for status field
    # Ensures that the status is one of the allowed values: "Active", "Inactive", or "Resigned"
    @field_validator("status")
    def validate_status(cls, val):
        valid_statuses = ["Active", "Inactive", "Resigned"]
        if val not in valid_statuses:
            raise ValueError(f"status must be one of: {', '.join(valid_statuses)}")
        return val
