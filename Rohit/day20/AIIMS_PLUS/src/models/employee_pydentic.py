from pydantic import BaseModel, field_validator, model_validator  # Import Pydantic BaseModel and validators
from datetime import date, datetime  # Import date and datetime for date handling
import re  # Import regex module for pattern-based validation

# Define EmployeeDirectory model using Pydantic
class EmployeeDirectory(BaseModel):
    emp_code: str        # Employee code (must follow USTEMP-XXXX format)
    full_name: str       # Full name of employee (alphabets and spaces only)
    email: str           # Email address (must follow valid email format)
    phone: str           # Phone number (must be exactly 10 digits)
    department: str      # Department (must be one of allowed departments)
    location: str        # Location (must be one of allowed locations)
    join_date: date      # Joining date (must not be in the future)
    status: str          # Employment status (must be one of allowed statuses)

    # -----------------------------
    # VALIDATORS
    # -----------------------------

    @field_validator("emp_code")  # Validator for emp_code field
    def emp_code_valid(cls, v):   # Function to validate emp_code
        if not re.match(r"^USTEMP-\d+$", v):  # Regex: must start with USTEMP- followed by digits
            raise ValueError("emp_code must start with USTEMP- followed by digits")
        return v  # Return validated value

    @field_validator("full_name")  # Validator for full_name field
    def full_name_valid(cls, v):   # Function to validate full_name
        if not re.match(r"^[A-Za-z ]+$", v):  # Regex: only alphabets and spaces allowed
            raise ValueError("full_name must contain only alphabets and spaces")
        return v  # Return validated value

    @field_validator("email")  # Validator for email field
    def email_valid(cls, v):   # Function to validate email
        # Regex: standard email format (username@domain.extension)
        if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", v):
            raise ValueError("Invalid email format")
        return v  # Return validated value

    @field_validator("phone")  # Validator for phone field
    def phone_valid(cls, v):   # Function to validate phone
        if not re.match(r"^\d{10}$", v):  # Regex: must be exactly 10 digits
            raise ValueError("Phone must be exactly 10 digits")
        return v  # Return validated value

    @field_validator("department")  # Validator for department field
    def department_valid(cls, v):   # Function to validate department
        valid = {"IT", "HR", "Finance", "Admin", "Sales", "Support"}  # Allowed departments
        if v not in valid:  # Check if department is valid
            raise ValueError("Invalid department")
        return v  # Return validated value

    @field_validator("location")  # Validator for location field
    def location_valid(cls, v):   # Function to validate location
        valid = {"Trivandrum", "Bangalore", "Chennai", "Hyderabad"}  # Allowed locations
        if v not in valid:  # Check if location is valid
            raise ValueError("Invalid location")
        return v  # Return validated value

    @field_validator("status")  # Validator for status field
    def status_valid(cls, v):   # Function to validate status
        valid = {"Active", "Inactive", "Resigned"}  # Allowed statuses
        if v not in valid:  # Check if status is valid
            raise ValueError("Invalid status")
        return v  # Return validated value

    @field_validator("join_date")  # Validator for join_date field
    def join_date_not_future(cls, v: date):  # Function to validate join_date
        if v > date.today():  # Check if join_date is in the future
            raise ValueError("join_date cannot be in the future")
        return v  # Return validated value
