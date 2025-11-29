from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import date

# Employee model for validating input data
class Employee(BaseModel):
    # First name: required, max length 50, only alphabets, spaces, and hyphens allowed
    first_name: str = Field(
        ..., 
        max_length=50, 
        pattern=r"^[A-Za-z\s-]+$", 
        description="first_name is required"
    )

    # Last name: required, max length 50, only alphabets, spaces, and hyphens allowed
    last_name: str = Field(
        ..., 
        max_length=50, 
        pattern=r"^[A-Za-z\s-]+$", 
        description="last_name is required"
    )

    # Email: required, must be valid email format, max length 100, unique constraint handled at DB level
    email: EmailStr = Field(
        ..., 
        max_length=100, 
        description="email must be unique"
    )

    # Position: optional, max length 50, only alphabets, spaces, and hyphens allowed
    position: Optional[str] = Field(
        max_length=50, 
        pattern=r"^[A-Za-z\s-]+$"
    )

    # Salary: optional, must be greater than 0 if provided
    salary: Optional[float] = Field(gt=0)

    # Hire date: required, must follow YYYY-MM-DD format
    hire_date: date = Field(
        ..., 
        description="It should be in format YYYY-MM-DD"
    )


# Custom validator function to ensure hire_date is not in the future
def validate_date(self):
    # Check if hire_date is greater than today's date
    if self.hire_date > date.today():
        raise ValueError("Not a valid date")
