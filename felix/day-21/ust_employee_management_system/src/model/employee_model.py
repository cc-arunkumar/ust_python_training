from pydantic import BaseModel, Field, model_validator, EmailStr
from datetime import date
from typing import Optional

# EmployeeModel defines the schema and validation rules for employee data.
# It ensures that incoming data (e.g., from API requests) is properly validated
# before being processed or stored in the database.
class EmployeeModel(BaseModel):
    """
    Data model for Employee records.

    This model enforces validation rules on employee attributes such as
    name, email, position, salary, and hire date. It is used to ensure
    data integrity when creating or updating employee records.
    """

    # First name: Required, max length 50, only letters, spaces, and hyphens allowed
    first_name: str = Field(
        ...,
        max_length=50,
        pattern=r"^[A-Za-z\s-]+$",
        description="First name is required and must contain only letters, spaces, or hyphens."
    )

    # Last name: Required, max length 50, only letters, spaces, and hyphens allowed
    last_name: str = Field(
        ...,
        max_length=50,
        pattern=r"^[A-Za-z\s-]+$",
        description="Last name must contain only letters, spaces, or hyphens."
    )

    # Email: Required, must be a valid email format, max length 100
    email: EmailStr = Field(
        ...,
        max_length=100,
        description="Email must be valid and unique."
    )

    # Position: Optional, max length 50, only letters, spaces, and hyphens allowed
    position: Optional[str] = Field(
        None,
        max_length=50,
        pattern=r"^[A-Za-z\s-]+$",
        description="Position title must contain only letters, spaces, or hyphens."
    )

    # Salary: Optional, must be greater than 0 if provided
    salary: Optional[float] = Field(
        None,
        gt=0,
        description="Salary must be greater than 0."
    )

    # Hire date: Required, must not be in the future
    hire_date: date = Field(
        ...,
        description="Hire date must not be in the future."
    )

    @model_validator(mode="after")
    def hire_date_validate(self):
        """
        Validate that the hire_date is not set in the future.

        Raises:
            ValueError: If hire_date is greater than today's date.
        """
        if self.hire_date > date.today():
            raise ValueError("Hire date cannot be in the future.")
        return self