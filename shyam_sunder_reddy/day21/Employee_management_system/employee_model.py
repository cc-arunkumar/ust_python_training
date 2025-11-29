# Import BaseModel and Field from Pydantic for data validation and schema definition
from pydantic import BaseModel, Field
# Import Optional type hint to allow fields to be optional
from typing import Optional
# Import date type for representing hire_date
from datetime import date

class Employee(BaseModel):
    """
    Employee data model using Pydantic.
    Provides validation rules and type hints for employee records.
    """

    # Primary key for employee, auto-generated in DB, optional in API requests
    employee_id: Optional[int] = None

    # First name: required, max length 50, only letters, hyphens, and spaces allowed
    first_name: str = Field(..., max_length=50, pattern=r"^[A-Za-z- ]*$")

    # Last name: required, max length 50, only letters, hyphens, and spaces allowed
    last_name: str = Field(..., max_length=50, pattern=r"^[A-Za-z- ]*$")

    # Email: required, must end with @ust.com, max length 100
    email: str = Field(..., max_length=100, pattern=r"^[A-Za-z0-9-.]+@ust.com$")

    # Position: optional, max length 50, only letters and spaces allowed
    position: Optional[str] = Field(None, max_length=50, pattern=r"[A-Za-z ]*+$")

    # Salary: optional, must be greater than 0 if provided
    salary: Optional[float] = Field(None, gt=0)

    # Hire date: required, represented as a date object
    hire_date: date
