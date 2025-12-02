from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field, field_validator

# Pydantic model for TrainingRequest
class TrainingRequest(BaseModel):
    # Employee ID should start with 'UST' followed by one or more digits
    employee_id: str = Field(..., pattern=r'^UST\d+$')

    # Employee Name should only contain alphabetic characters and spaces
    employee_name: str = Field(..., min_length=1, pattern=r'^[A-Za-z ]+$')

    # Training title should have a minimum length of 5 characters
    training_title: str = Field(..., min_length=5)

    # Training description should have a minimum length of 10 characters
    training_description: str = Field(..., min_length=10)

    # Requested date should be before today (can't be a future date)
    requested_date: date = Field(..., lt=date.today())

    # Status can be PENDING, APPROVED, or REJECTED
    status: str = Field(...)

    # Validator to ensure 'status' is one of the valid options: "PENDING", "APPROVED", or "REJECTED"
    @field_validator("status")
    def validate_status(cls, val):
        valid_statuses = ["PENDING", "APPROVED", "REJECTED"]  # Allowed status values
        if val not in valid_statuses:
            # Raise an error if the status value is invalid
            raise ValueError(f"status must be one of: {', '.join(valid_statuses)}")
        return val

    # Manager ID should follow the same pattern as employee ID
    manager_id: str = Field(..., pattern=r'^UST\d+$')

    # The timestamp of when the record was last updated; default is the current time
    last_updated: datetime = datetime.now()

