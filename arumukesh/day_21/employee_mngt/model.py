from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date


class Employee(BaseModel):
    """
    Employee model used for request validation in FastAPI.
    This ensures that incoming data follows the correct format
    before storing it in the database.
    """

    # First name: required field with a maximum length of 50 characters
    first_name: str = Field(..., max_length=50)

    # Last name: required field with a maximum length of 50 characters
    last_name: str = Field(..., max_length=50)

    # Email: required and validated using regex pattern
    email: str = Field(
        ...,
        pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,20}$",
        description="Must be a valid email format"
    )

    # Position: optional field (can be None)
    position: Optional[str] = None

    # Salary: optional but must be a positive value if provided
    salary: Optional[float] = None

    # Hire date: required, must be a valid date format (YYYY-MM-DD)
    hire_date: date

    @field_validator("salary")
    def validate_salary(cls, value):
        """
        Ensures that salary, if provided, must be a positive number.
        """
        if value is not None and value < 0:
            raise ValueError("Salary must be a positive value.")
        return value
