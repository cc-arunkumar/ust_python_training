from pydantic import BaseModel, EmailStr, validator  # Import necessary modules from Pydantic
from typing import Optional  # For optional fields in the models
from datetime import date  # To handle date values
import re  # For regular expression matching

# Pydantic model for creating a new training request
class TrainingRequestCreate(BaseModel):
    # Fields for the training request
    employee_id: str  # Employee ID (should match the format 'UST' followed by digits)
    employee_name: str  # Name of the employee (should not contain numbers)
    training_title: str  # Title of the training (minimum length of 5 characters)
    training_description: str  # Description of the training (minimum length of 10 characters)
    requested_date: date  # The requested date for the training (should not be in the future)
    status: str  # Status of the request (must be one of 'PENDING', 'APPROVED', 'REJECTED')
    manager_id: str  # Manager's ID (should follow the same format as the employee ID)

    # Validator for employee_id: Checks that the ID starts with 'UST' followed by digits
    @validator("employee_id")
    def validate_employee_id(cls, v):
        if not re.match(r"^UST\d+$", v):
            raise ValueError("Employee ID must start with 'UST' followed by digits.")
        return v

    # Validator for employee_name: Ensures the name is not empty and does not contain numbers
    @validator("employee_name")
    def validate_employee_name(cls, v):
        if not v or any(char.isdigit() for char in v):  # Checks for any digits in the name
            raise ValueError("Employee name cannot be empty and cannot contain numbers.")
        return v

    # Validator for training_title: Ensures the title is at least 5 characters long
    @validator("training_title")
    def validate_training_title(cls, v):
        if len(v) < 5:  # Training title should be at least 5 characters
            raise ValueError("Training title must be at least 5 characters long.")
        return v

    # Validator for training_description: Ensures the description is at least 10 characters long
    @validator("training_description")
    def validate_training_description(cls, v):
        if len(v) < 10:  # Description should be at least 10 characters
            raise ValueError("Training description must be at least 10 characters long.")
        return v

    # Validator for requested_date: Ensures the requested date is not in the future
    @validator("requested_date")
    def validate_requested_date(cls, v):
        if v > date.today():  # Cannot be in the future
            raise ValueError("Requested date cannot be in the future.")
        return v

    # Validator for status: Ensures the status is one of the allowed values
    @validator("status")
    def validate_status(cls, v):
        if v not in ["PENDING", "APPROVED", "REJECTED"]:
            raise ValueError("Status must be one of 'PENDING', 'APPROVED', or 'REJECTED'.")
        return v

    # Validator for manager_id: Ensures the manager's ID follows the same format as employee_id
    @validator("manager_id")
    def validate_manager_id(cls, v):
        if not re.match(r"^UST\d+$", v):  # Must match the same format as employee_id
            raise ValueError("Manager ID must follow the same format as Employee ID (starting with 'UST' followed by digits).")
        return v

# Pydantic model for the output data (training request with ID and last updated date)
class TrainingRequestOut(TrainingRequestCreate):
    id: int  # ID for the training request (added for output purposes)
    last_updated: Optional[str] = None  # Optional field for the last update timestamp (can be null)
