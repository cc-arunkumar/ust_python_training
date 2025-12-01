from pydantic import BaseModel, Field, model_validator
from datetime import date
from typing import Literal

class TrainingRequest(BaseModel):
    """
    Pydantic model representing a training request.
    Includes validation rules for employee and manager IDs, names, and request details.
    """

    # Employee ID must start with 'UST' followed by digits
    employee_id: str = Field(..., pattern=r"^UST[0-9]+$", description="Invalid employee id")

    # Employee name must not be empty and cannot contain digits
    employee_name: str = Field(..., min_length=1, description="Digits are not allowed in name")

    # Training title must be at least 5 characters long
    training_title: str = Field(..., min_length=5)

    # Training description must be at least 10 characters long
    training_description: str = Field(..., min_length=10)

    # Requested date must be a valid date (not in the future)
    requested_date: date = Field(...)

    # Status must be one of the allowed literal values
    status: Literal["PENDING", "APPROVED", "REJECTED"]

    # Manager ID must start with 'UST' followed by digits
    manager_id: str = Field(..., pattern=r"^UST[0-9]+$", description="Invalid manager id")

    @model_validator(mode="after")
    def emp_name(self):
        """
        Validator to ensure employee name does not contain digits.
        """
        if any(ch.isdigit() for ch in self.employee_name):
            raise ValueError("Employee name cannot contain digits")
        return self

    @model_validator(mode="after")
    def req_date(self):
        """
        Validator to ensure requested date is not set in the future.
        """
        if self.requested_date > date.today():
            raise ValueError("Request date cannot be a future date")
        return self


class RequestModel(BaseModel):
    """
    Pydantic model for partial updates (PATCH).
    Only allows updating the status field of a training request.
    """
    status: Literal["PENDING", "APPROVED", "REJECTED"]