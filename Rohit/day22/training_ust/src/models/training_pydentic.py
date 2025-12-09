from pydantic import BaseModel, Field, field_validator
from datetime import date
from enum import Enum

class Status(str, Enum):
    Pending = "PENDING"
    Approved = "APPROVED"
    Rejected = "REJECTED"

class TrainingPydantic(BaseModel):
    id: int = Field(default=0, description="Auto-incremented ID, no need to provide")
    employee_id: str = Field(..., pattern=r"^UST\d+$")
    employee_name: str = Field(..., max_length=100, pattern=r"^[^0-9]+$")
    training_title: str = Field(..., min_length=5)
    training_description: str = Field(..., min_length=10)
    requested_date: date = Field(...)
    status: Status = Field(default=Status.Pending)
    manager_id: str = Field(..., pattern=r"^UST\d+$")

    @field_validator("requested_date")
    def validate_requested_date(cls, v):
        if v > date.today():
            raise ValueError("requested_date cannot be a future date")
        return v
