from pydantic import BaseModel, Field, field_validator, ValidationError
from typing import List
from datetime import date
from datetime import datetime

STATUS_LIST = ["PENDING", "APPROVED", "REJECTED"]

class Training_Request(BaseModel):
    employee_id: str = Field(..., pattern=r"^UST\d+$")
    employee_name: str = Field(..., min_length=2, pattern=r"^[A-Za-z ]+$")
    training_title: str = Field(..., min_length=5)
    training_description: str = Field(..., min_length=10)
    requested_date: date
    status: str = Field(...)
    manager_id: str = Field(..., pattern=r"^UST\d+$")
    
    
def validate_requested_date(v: str) -> date:
    """Validate that requested_date is in correct format and not future."""
    try:
        dt = datetime.strptime(v, "%Y-%m-%d")
    except:
        raise ValueError("requested_date must be in YYYY-MM-DD format")

    if dt > date.today():
        raise ValueError("requested_date must not be in the future")

    return dt


def validate_status(v: str) -> str:
    """Validate that status is within allowed values."""
    v_upper = v.upper()
    if v_upper not in STATUS_LIST:
        raise ValueError(f"status must be one of {STATUS_LIST}")
    return v_upper
# Example usage:
# try:
#     tr = Training_Request(
#         employee_id="UST123",
#         employee_name="Arun Kumar",
#         training_title="Advanced SQL",
#         training_description="Deep dive into query optimization",
#         requested_date="2025-11-01",
#         status="PENDING",
#         manager_id="UST200"
#     )
# except ValidationError as e:
#     print(e)
