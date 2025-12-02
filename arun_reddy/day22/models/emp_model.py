from pydantic import BaseModel, Field
from datetime import date, datetime
from enum import Enum

# Allowed status values
class StatusEnum(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

# Employee training request model
class Employee(BaseModel):
    employee_id: str = Field(..., pattern=r"^UST\d+$")   # Must start with UST + digits
    employee_name: str = Field(..., pattern=r"^[A-Za-z]+$")  # Must contain only letters
    training_title: str = Field(..., min_length=5)       # At least 5 characters
    training_description: str = Field(..., min_length=10) # At least 10 characters
    requested_date: date                                 # Date of request
    status: StatusEnum                                   # Only PENDING/APPROVED/REJECTED
    manager_id: str = Field(..., pattern=r"^UST\d+$")    # Must start with UST + digits
    last_updated: datetime                               # Last updated timestamp

# Model for partial status update
class StatusModel(BaseModel):
    status: StatusEnum
