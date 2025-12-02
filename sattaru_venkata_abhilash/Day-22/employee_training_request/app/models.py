from pydantic import BaseModel, Field, field_validator  # Import necessary classes from Pydantic
from typing import Optional
from datetime import date  # Import date class from datetime module
import re  # Import the regular expression module for pattern matching

# Model representing a training request (used for reading from the database or returning data)
class TrainingRequest(BaseModel):
    id: int  # ID of the training request
    employee_id: str  # ID of the employee making the request
    employee_name: str  # Name of the employee making the request
    training_title: str  # The title of the requested training
    training_description: str  # The description of the training request
    requested_date: str  # The date when the request was made
    status: str  # Status of the request (PENDING, APPROVED, REJECTED)
    manager_id: str  # ID of the manager approving the request

# Model for creating a new training request (used for input data in POST requests)
class TrainingRequestCreate(BaseModel):
    employee_id: str  # ID of the employee
    employee_name: str  # Name of the employee
    training_title: str  # Title of the requested training
    training_description: str  # Description of the training
    requested_date: date  # The date when the training request is made
    status: str  # The current status of the request
    manager_id: str  # ID of the manager approving the request

# Base model that defines the structure and validation rules for the training request data
class TrainingRequestBase(BaseModel):
    # Field definitions with validation rules and descriptions
    employee_id: str = Field(..., description="Employee ID starting with 'UST' followed by digits")

    employee_name: str = Field(..., max_length=100, description="Employee name (no digits allowed)")

    training_title: str = Field(..., min_length=5, description="Training title (minimum 5 characters)")

    training_description: str = Field(..., min_length=10, description="Training description (minimum 10 characters)")

    requested_date: date = Field(..., description="Requested date for the training (cannot be in the future)")

    status: str = Field(..., description="Status of the request (PENDING, APPROVED, REJECTED)")

    manager_id: str = Field(..., description="Manager ID starting with 'UST' followed by digits")

    # Field validator for employee_id: ensures it starts with 'UST' followed by digits
    @field_validator("employee_id")
    def validate_employee_id(cls, val):
        if not re.match(r"^UST\d+$", val):
            raise ValueError("employee_id must start with 'UST' followed by digits")
        return val

    # Field validator for employee_name: ensures it doesn't contain digits and only allows alphabets and spaces
    @field_validator("employee_name")
    def validate_employee_name(cls, val):
        if any(char.isdigit() for char in val):  # Checks if the name contains any digits
            raise ValueError("employee_name must not contain digits")
        if not all(char.isalpha() or char.isspace() for char in val):  # Ensures only alphabets and spaces are allowed
            raise ValueError("employee_name must only contain alphabets and spaces")
        if len(val.strip()) == 0:  # Ensures the name is not empty
            raise ValueError("employee_name cannot be empty")
        return val

    # Field validator for training_title: ensures the title is at least 5 characters long
    @field_validator("training_title")
    def validate_training_title(cls, val):
        if len(val) < 5:
            raise ValueError("training_title must be at least 5 characters long")
        return val

    # Field validator for training_description: ensures the description is at least 10 characters long
    @field_validator("training_description")
    def validate_training_description(cls, val):
        if len(val) < 10:
            raise ValueError("training_description must be at least 10 characters long")
        return val

    # Field validator for requested_date: ensures the date is not in the future
    @field_validator("requested_date")
    def validate_requested_date(cls, val):
        if val > date.today():  # If the requested date is in the future, raise an error
            raise ValueError("requested_date cannot be a future date")
        return val

    # Field validator for status: ensures the status is one of the predefined values (PENDING, APPROVED, REJECTED)
    @field_validator("status")
    def validate_status(cls, val):
        if val not in ['PENDING', 'APPROVED', 'REJECTED']:  # Checks if status is valid
            raise ValueError("status must be one of 'PENDING', 'APPROVED', or 'REJECTED'")
        return val

    # Field validator for manager_id: ensures it starts with 'UST' followed by digits
    @field_validator("manager_id")
    def validate_manager_id(cls, val):
        if not re.match(r"^UST\d+$", val):  # Validates that the manager ID follows the required pattern
            raise ValueError("manager_id must start with 'UST' followed by digits")
        return val
