from typing import Optional
from pydantic import BaseModel, Field, field_validator
from datetime import date

class TrainingRequest(BaseModel):
    """
    This model represents the base structure for a Training Request.
    It includes field validation to ensure data integrity and correctness.
    """
    # Employee ID field must match the pattern `UST` followed by digits (e.g., UST123)
    employee_id: str = Field(..., pattern=r"^UST\d+$")

    # Employee name must only contain alphabets and spaces, with at least one character
    employee_name: str = Field(..., min_length=1, pattern=r"^[A-Za-z ]+$")

    # The title of the training request must have a minimum length of 5 characters
    training_title: str = Field(..., min_length=5)

    # Training description must have at least 10 characters
    training_description: str = Field(..., min_length=10)

    # Requested date must be a valid date and should not be a future date
    requested_date: date

    @field_validator("requested_date")
    def valid_date(cls, val):
        """
        Custom validator for the requested_date to ensure it is not in the future.
        """
        if val > date.today():
            raise ValueError("Date should not be in the future")
        return val

    # Status can only be 'PENDING', 'APPROVED', or 'REJECTED'
    status: str = Field(..., pattern=r"^(PENDING|APPROVED|REJECTED)$")

    # Manager ID must match the pattern `UST` followed by digits (e.g., UST123)
    manager_id: str = Field(..., pattern=r"^UST\d+$")
   
class TrainingRequestCreate(TrainingRequest):
    """
    This model is used for creating new training requests.
    It inherits from TrainingRequest and does not add any additional fields.
    """
    pass    # No additional fields or methods needed, inherits everything from TrainingRequest.

class TrainingRequestUpdate(BaseModel):
    """
    This model is used for updating an existing training request.
    All fields are optional, and only provided fields will be updated.
    """
    # Optional fields for updating the training request
    employee_id: Optional[str] = Field(None, pattern=r"^UST\d+$")
    employee_name: Optional[str] = Field(None, min_length=1, max_length=100, pattern=r"^[A-Za-z ]+$")
    training_title: Optional[str] = Field(None, min_length=5, max_length=200)
    training_description: Optional[str] = Field(None, min_length=10)
    requested_date: Optional[date] = None
    status: Optional[str] = Field(None, pattern=r"^(PENDING|APPROVED|REJECTED)$")
    manager_id: Optional[str] = Field(None, pattern=r"^UST\d+$")

    @field_validator("requested_date")
    def valid_date(cls, val):
        """
        Custom validator for the requested_date to ensure it is not in the future when updating.
        """
        if val and val > date.today():  # Only validate if the value is not None
            raise ValueError("Date should not be in the future")
        return val

class TrainingRequestRead(TrainingRequest):
    """
    This model is used to read a training request from the database. 
    It includes the `id` and `last_updated` timestamp fields.
    """
    # The `id` is an integer field representing the unique identifier for the training request
    id: int

    # The `last_updated` field is optional and can store the timestamp of the last update
    last_updated: Optional[str] = None    # Format could be an ISO string, e.g., "2023-12-01T12:30:00"
