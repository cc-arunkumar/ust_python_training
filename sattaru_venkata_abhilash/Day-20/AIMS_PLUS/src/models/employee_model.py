from typing import Optional  # Importing Optional for optional type annotations
from pydantic import BaseModel, Field, field_validator  # Importing BaseModel, Field, and field_validator for model validation
from datetime import date  # Importing date for date-related validation

# EmployeeDirectory model class for managing employee records
class EmployeeDirectory(BaseModel):
    # emp_id is an optional field, defaults to 0 if not provided
    emp_id: Optional[int] = 0

    # emp_code must be a string with a minimum length of 7 and must start with 'USTEMP'
    emp_code: str = Field(..., min_length=7, description="Must start with USTEMP")

    # full_name is a required string with a maximum length of 100, containing only alphabets and spaces
    full_name: str = Field(..., max_length=100, description="Alphabets + spaces only")

    # email is a required string with a maximum length of 100, and must end with '@ust.com'
    email: str = Field(..., max_length=100, description="Must end with @ust.com")

    # phone is a required string field with a maximum length of 15, representing an Indian mobile number
    phone: str = Field(..., max_length=15, description="Indian mobile (10 digits)")

    # department is a required string field describing the employee's department (e.g., HR, IT, Admin, Finance)
    department: str = Field(..., description="HR/IT/Admin/Finance/etc.")

    # location is a required string field representing the employee's UST location in India
    location: str = Field(..., description="Indian UST locations")

    # join_date is a required date field, with validation to ensure it is not in the future or in an invalid format
    join_date: date = Field(..., description="Cannot be in the future or invalid format")

    # status is a required string field, and it can be either 'Active', 'Inactive', or 'Resigned'
    status: str = Field(..., description="Active/Inactive/Resigned")

    # Validator to ensure emp_code starts with 'USTEMP'
    @field_validator("emp_code")
    def validate_emp_code(cls, val):
        if not val.startswith("USTEMP"):  # Check if the emp_code starts with 'USTEMP'
            raise ValueError("emp_code must start with 'USTEMP'")  # Raise an error if the condition fails
        return val

    # Validator to ensure email ends with '@ust.com'
    @field_validator("email")
    def validate_email(cls, val):
        if not val.endswith("@ust.com"):  # Check if email ends with '@ust.com'
            raise ValueError("email must end with '@ust.com'")  # Raise an error if the condition fails
        return val

    # Validator to ensure phone is a valid 10-digit Indian mobile number starting with 6, 7, 8, or 9
    @field_validator("phone")
    def validate_phone(cls, val):
        if not (val.isdigit() and len(val) == 10 and val[0] in "6789"):  # Validate phone number format
            raise ValueError("phone must be a valid 10-digit Indian mobile starting with 6/7/8/9")
        return val

    # Validator to ensure join_date is not a future date and follows the 'YYYY-MM-DD' format
    @field_validator("join_date")
    def validate_join_date(cls, val):
        if val > date.today():  # Ensure join_date is not a future date
            raise ValueError("join_date cannot be a future date")  # Raise error if the date is in the future
        try:
            val.strftime("%Y-%m-%d")  # Check if the date is in 'YYYY-MM-DD' format
        except ValueError:
            raise ValueError("join_date must be in the format YYYY-MM-DD")  # Raise error if format is incorrect
        return val

    # Validator to ensure status is one of the valid statuses: 'Active', 'Inactive', 'Resigned'
    @field_validator("status")
    def validate_status(cls, val):
        valid_statuses = ["Active", "Inactive", "Resigned"]  # List of valid status values

        if val not in valid_statuses:
            raise ValueError(f"status must be one of: {', '.join(valid_statuses)}")
        return val
