from pydantic import BaseModel, Field, field_validator
from datetime import date
import re

class EmployeeMaster(BaseModel):
    # Employee ID: Auto-incremented by DB, optional on create
    emp_id: int | None = None

    # Employee code: Must start with 'USTEMP' and can be at most 20 characters
    emp_code: str = Field(..., max_length=20, description="Must start with USTEMP")
    
    # Full name: Only alphabets and spaces allowed, maximum 100 characters
    full_name: str = Field(..., max_length=100, description="Alphabets + spaces only")
    
    # Email: Must end with '@ust.com'
    email: str = Field(..., max_length=100, description="Must end with @ust.com")
    
    # Phone: Must be a 10-digit Indian mobile number
    phone: str = Field(..., max_length=15, description="10-digit Indian mobile")
    
    # Department: Should be one of the predefined departments (HR/IT/Admin/Finance/etc.)
    department: str = Field(..., max_length=50, description="HR/IT/Admin/Finance/etc.")
    
    # Location: Should be one of the UST locations in India
    location: str = Field(..., max_length=100, description="Indian UST locations")
    
    # Join date: Cannot be a future date
    join_date: date = Field(..., description="Cannot be future date")
    
    # Status: Should be one of the predefined statuses (Active/Inactive/Resigned)
    status: str = Field(..., max_length=20, description="Active/Inactive/Resigned")

    # field_validator for emp_code: Ensures the employee code starts with 'USTEMP'
    @field_validator('emp_code')
    def emp_code_must_start_with_ustemp(cls, v):
        if not v.startswith("USTEMP"):
            raise ValueError('emp_code must start with "USTEMP"')
        return v

    # field_validator for full_name: Ensures the name only contains alphabets and spaces
    @field_validator('full_name')
    def full_name_must_be_alpha_space(cls, v):
        if not re.match(r"^[A-Za-z\s]+$", v):
            raise ValueError('full_name must only contain alphabets and spaces')
        return v

    # field_validator for email: Ensures the email ends with '@ust.com'
    @field_validator('email')
    def email_must_end_with_ust(cls, v):
        if not v.endswith("@ust.com"):
            raise ValueError('email must end with @ust.com')
        return v

    # field_validator for phone: Ensures the phone number is a 10-digit Indian mobile number
    @field_validator('phone')
    def phone_must_be_valid_indian_number(cls, v):
        if not re.match(r"^\d{10}$", v):
            raise ValueError('phone must be a valid 10-digit Indian mobile number')
        return v

    # field_validator for department: Ensures the department is valid
    @field_validator('department')
    def department_valid(cls, v):
        valid_departments = {"HR", "IT", "Admin", "Finance", "Operations", "Marketing"}
        if v not in valid_departments:
            raise ValueError(f"department must be one of {', '.join(valid_departments)}")
        return v

    # field_validator for location: Ensures the location is valid and within UST India locations
    @field_validator('location')
    def location_valid(cls, v):
        valid_locations = {"Bangalore", "Chennai", "Hyderabad", "Mumbai", "Delhi", "Trivandrum"}
        if v not in valid_locations:
            raise ValueError(f"location must be one of {', '.join(valid_locations)}")
        return v

    # field_validator for join_date: Ensures the join_date is not in the future
    @field_validator('join_date')
    def join_date_not_in_future(cls, v):
        if v > date.today():
            raise ValueError('join_date cannot be in the future')
        return v

    # field_validator for status: Ensures the status is either Active, Inactive, or Resigned
    @field_validator('status')
    def status_valid(cls, v):
        valid_status = {"Active", "Inactive", "Resigned"}
        if v not in valid_status:
            raise ValueError(f"status must be one of {', '.join(valid_status)}")
        return v
