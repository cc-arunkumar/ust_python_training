from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import Optional
from enum import Enum

# ---------------------------------------------------------
# Enum Class: Status
# Purpose: Restrict employee status to predefined values
# ---------------------------------------------------------
class Status(str, Enum):
    active = "Active"
    resigned = "Resigned"


# ---------------------------------------------------------
# Model: Employee
# Purpose: Schema for employee data validation
# ---------------------------------------------------------
class Employee(BaseModel):
    """
    Employee data model used for validating input data in APIs.
    Includes field-level validations, formatting rules, and input normalization.
    """

    # Employee code must follow format: USTEMP-XXXX (e.g., USTEMP-0001)
    emp_code: str = Field(
        ...,
        pattern=r"^USTEMP-\d{4}$",
        description="Unique employee code in format USTEMP-XXXX"
    )

    # Employee full name (no strict pattern applied)
    full_name: str

    # Valid email format (basic email regex pattern)
    email: str = Field(
        ...,
        pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$",
        description="Valid company/official email address"
    )

    # Phone must start with digits 6-9 and total 10 numbers
    phone: str = Field(
        ...,
        pattern=r"^[6-9][0-9]{9}$",
        description="Valid 10-digit Indian phone number"
    )

    department: str
    location: str

    # Join date must be in YYYY-MM-DD format; can be optional
    join_date: Optional[date]

    # Employee status must match Status enum: Active | Resigned
    status: Status


    # -------------------------------
    # Validators Section
    # -------------------------------

    @field_validator("department", "location", mode="before")
    def normalize_text(cls, value):
        """
        Ensures department and location fields are formatted correctly
        (proper capitalization and no extra spaces).
        """
        return value.strip().title() if isinstance(value, str) else value


    @field_validator("status", mode="before")
    def normalize_status(cls, value):
        """
        Normalizes input for status field (case-insensitive matching).
        Converts text to title case so 'active', 'ACTIVE', etc., become 'Active'.
        """
        return value.strip().title() if isinstance(value, str) else value


    @field_validator("join_date", mode="before")
    def validate_date(cls, value):
        """
        Validates date format strictly as YYYY-MM-DD.
        Automatically converts string input to `date` object.
        """
        if not value:
            return None
        try:
            return date.fromisoformat(value)
        except:
            raise ValueError("Invalid date format. Expected YYYY-MM-DD.")


