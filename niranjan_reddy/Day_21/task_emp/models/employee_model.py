from datetime import date  # Importing the date class from datetime module to work with date values
from pydantic import BaseModel, Field, field_validator  # Importing Pydantic BaseModel and Field for data validation
from typing import Optional  # Importing Optional from typing for fields that are optional

# Pydantic model for employee data with validation
class EmployeeModel(BaseModel):
    # Optional employee ID, defaults to 0 if not provided
    emp_id: Optional[int] = 0

    # First name with validation: must be between 1 and 50 characters and can only contain letters, hyphens, and spaces
    first_name: str = Field(..., min_length=1, max_length=50,
                            pattern=r'^[A-Za-z\- ]+$')

    # Last name with validation: similar to first name (letters, hyphens, and spaces allowed)
    last_name: str = Field(..., min_length=1, max_length=50,
                           pattern=r'^[A-Za-z\- ]+$')

    # Email with validation: must match a basic email format pattern and can have a maximum of 100 characters
    email: str = Field(..., max_length=100,
                       pattern=r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')

    # Position is optional with a max length of 50 characters and can contain alphanumeric characters, hyphens, and spaces
    position: Optional[str] = Field(default=None, max_length=50,
                                    pattern=r'^[A-Za-z0-9\- ]+$')

    # Salary is optional but must be greater than 0 if provided
    salary: Optional[float] = Field(default=None, gt=0)

    # Hire date must be in the past or today, cannot be a future date
    hire_date: date

    @field_validator('hire_date')
    def validate_date(cls, val):
        if val > date.today():  # Check if the hire date is in the future
            raise ValueError("Hire date cannot be in the future")  # Raise error if the date is in the future
        return val  # Return the validated date


# Pydantic model for employee request, used for creating or updating employee data
class EmployeeRequest(BaseModel):
    # First name with validation (same as EmployeeModel)
    first_name: str = Field(..., min_length=1, max_length=50,
                            pattern=r'^[A-Za-z\- ]+$')

    # Last name with validation (same as EmployeeModel)
    last_name: str = Field(..., min_length=1, max_length=50,
                           pattern=r'^[A-Za-z\- ]+$')

    # Email with validation (same as EmployeeModel)
    email: str = Field(..., max_length=100,
                       pattern=r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')

    # Position with validation (same as EmployeeModel)
    position: Optional[str] = Field(default=None, max_length=50,
                                    pattern=r'^[A-Za-z0-9\- ]+$')

    # Salary with validation (same as EmployeeModel)
    salary: Optional[float] = Field(default=None, gt=0)

    # Hire date with validation (same as EmployeeModel)
    hire_date: date

    @field_validator('hire_date')
    def validate_date(cls, val):
        if val > date.today():  # Check if the hire date is in the future
            raise ValueError("Hire date cannot be in the future")  # Raise error if the date is in the future
        return val  # Return the validated date
