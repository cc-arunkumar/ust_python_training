from pydantic import BaseModel, Field, EmailStr, model_validator
from datetime import date
from typing import Literal


class StatusValidate(BaseModel):
    """
    Model used to validate employee status updates.

    Attributes:
        status (Literal): Must be one of the predefined status values:
            - 'Active'
            - 'Inactive'
            - 'Resigned'
    """
    status: Literal['Active', 'Inactive', 'Resigned']


class EmployeeDirectory(BaseModel):
    """
    Model representing an employee in the directory system.

    Attributes:
        emp_code (str): Unique employee code. Must follow the pattern 'USTEMP<alphanumeric>'.
        full_name (str): Employee's full name. Only alphabets and spaces are allowed.
        email (EmailStr): Employee's email address. Must be a valid email format and belong to '@ust.com' domain.
        phone (str): Employee's phone number. Must start with digits 6–9 and be exactly 10 digits long.
        department (Literal): Department name. Allowed values: 'HR', 'IT', 'Admin', 'Finance', 'Support'.
        location (Literal): Work location. Allowed values: 'Trivandrum', 'Bangalore', 'Chennai', 'Hyderabad', 'Mumbai', 'Delhi', 'Pune'.
        join_date (date): Date when the employee joined. Cannot be in the future.
        status (Literal): Current employment status. Allowed values: 'Active', 'Inactive', 'Resigned'.
    """

    emp_code: str = Field(..., pattern=r"^USTEMP[A-Za-z0-9-]+$")  # Enforces USTEMP-prefixed employee codes
    full_name: str = Field(..., pattern=r"^[A-Za-z ]+$")  # Only alphabets and spaces allowed
    email: EmailStr
    phone: str = Field(..., pattern=r"^[6-9][0-9]{9}$")  # Validates Indian mobile number format
    department: Literal['HR', 'IT', 'Admin', 'Finance', 'Support']
    location: Literal['Trivandrum', 'Bangalore', 'Chennai', 'Hyderabad', 'Mumbai', 'Delhi', 'Pune']
    join_date: date
    status: Literal['Active', 'Inactive', 'Resigned']

    @model_validator(mode="after")
    def validate(self):
        """
        Custom validator to enforce additional rules:
        - Email must belong to '@ust.com' domain.
        - join_date cannot be set in the future.

        Raises:
            ValueError: If email domain is invalid or join_date is greater than today's date.

        Returns:
            EmployeeDirectory: The validated model instance.
        """
        if not self.email.endswith("@ust.com"):
            raise ValueError("Email must belong to @ust.com domain")
        if self.join_date > date.today():
            raise ValueError("join_date cannot be in the future")
        return self