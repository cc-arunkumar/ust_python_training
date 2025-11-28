from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date

# MaintenanceLogModel represents the maintenance log entry for assets.
class MaintenanceLogModel(BaseModel):
    
    # log_id is an auto-incrementing primary key (Optional, default None).
    # This field represents the unique identifier for each maintenance log.
    log_id: Optional[int] = Field(default=None, description="Auto-increment integer primary key")

    # asset_tag is required and must follow the UST- pattern (e.g., UST-LTP-0001)
    asset_tag: str = Field(..., description="Must follow UST- pattern")

    # maintenance_type must be one of 'Repair', 'Service', or 'Upgrade'.
    maintenance_type: str = Field(..., description="Only 'Repair', 'Service', or 'Upgrade' allowed")

    # vendor_name is a required field, must contain only alphabets and spaces (no digits or special characters).
    vendor_name: str = Field(..., description="Alphabets only (no digits or special characters)")

    # description should be at least 10 characters long.
    # Describes the maintenance performed or any other details about the service.
    description: str = Field(..., min_length=10, description="Minimum 10 characters for description")

    # cost must be a positive float (greater than 0) with two decimal places.
    cost: float = Field(..., gt=0, description="Decimal with two digits after decimal, must be greater than 0")

    # maintenance_date is required and should not be a future date.
    maintenance_date: date = Field(..., description="Date, cannot be a future date")

    # technician_name is required and must contain only alphabets and spaces.
    technician_name: str = Field(..., description="Alphabets only (no digits or special characters)")

    # status can only be 'Completed' or 'Pending'.
    # Represents the current status of the maintenance (whether it is done or still pending).
    status: str = Field(..., description="Only 'Completed' or 'Pending' allowed")

    # Validator for asset_tag field
    # Ensures the asset_tag starts with 'UST-'
    @field_validator("asset_tag")
    def validate_asset_tag(cls, val):
        if not val.startswith("UST-"):
            raise ValueError("asset_tag must start with 'UST-'")
        return val

    # Validator for maintenance_type field
    # Ensures maintenance_type is one of 'Repair', 'Service', or 'Upgrade'
    @field_validator("maintenance_type")
    def validate_maintenance_type(cls, val):
        valid_types = ["Repair", "Service", "Upgrade"]
        if val not in valid_types:
            raise ValueError(f"maintenance_type must be one of {', '.join(valid_types)}")
        return val

    # Validator for vendor_name field
    # Ensures vendor_name contains only alphabets and spaces (no digits or special characters)
    @field_validator("vendor_name")
    def validate_vendor_name(cls, val):
        # Check if there are any digits or special characters in the vendor name
        if any(char.isdigit() for char in val) or not all(char.isalpha() or char.isspace() for char in val):
            raise ValueError("vendor_name must only contain alphabets and spaces, no digits or special characters")
        return val

    # Validator for cost field
    # Ensures that cost is a positive number (greater than 0)
    @field_validator("cost")
    def validate_cost(cls, val):
        if val <= 0:
            raise ValueError("cost must be greater than 0")
        return val

    # Validator for maintenance_date field
    # Ensures the maintenance_date is not a future date
    @field_validator("maintenance_date")
    def validate_maintenance_date(cls, val):
        if val > date.today():
            raise ValueError("maintenance_date cannot be a future date")
        return val

    # Validator for technician_name field
    # Ensures technician_name contains only alphabets and spaces (no digits or special characters)
    @field_validator("technician_name")
    def validate_technician_name(cls, val):
        if any(char.isdigit() for char in val) or not all(char.isalpha() or char.isspace() for char in val):
            raise ValueError("technician_name must only contain alphabets and spaces, no digits or special characters")
        return val

    # Validator for status field
    # Ensures status is either 'Completed' or 'Pending'
    @field_validator("status")
    def validate_status(cls, val):
        if val not in ["Completed", "Pending"]:
            raise ValueError("status must be either 'Completed' or 'Pending'")
        return val
