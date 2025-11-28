from pydantic import BaseModel, Field, field_validator  # Importing BaseModel, Field, and field_validator from Pydantic for data validation
from typing import Optional  # Importing Optional to denote optional fields in the model
from datetime import date  # Importing date to work with date objects

# Model class for MaintenanceLog that will validate and store maintenance logs
class MaintenanceLogModel(BaseModel):
    # log_id is an optional field, it will automatically be assigned as the primary key in the database (auto-increment)
    log_id: Optional[int] = Field(default=None, description="Auto-increment integer primary key")
    
    # asset_tag is a required field and should start with 'UST-' as per the regex validation
    asset_tag: str = Field(..., description="Must follow UST- pattern")
    
    # maintenance_type is required and must be one of the specified values: 'Repair', 'Service', or 'Upgrade'
    maintenance_type: str = Field(..., description="Only 'Repair', 'Service', or 'Upgrade' allowed")
    
    # vendor_name is a required string that must contain only alphabets and spaces (no digits or special characters)
    vendor_name: str = Field(..., description="Alphabets only (no digits or special characters)")
    
    # description is a required string with a minimum length of 10 characters
    description: str = Field(..., min_length=10, description="Minimum 10 characters for description")
    
    # cost is a required float that must be greater than 0
    cost: float = Field(..., gt=0, description="Decimal with two digits after decimal, must be greater than 0")
    
    # maintenance_date is a required date field, and it cannot be a future date
    maintenance_date: date = Field(..., description="Date, cannot be a future date")
    
    # technician_name is a required field and should contain only alphabets and spaces
    technician_name: str = Field(..., description="Alphabets only (no digits or special characters)")
    
    # status is a required field and must be either 'Completed' or 'Pending'
    status: str = Field(..., description="Only 'Completed' or 'Pending' allowed")

    # Validator to ensure that asset_tag starts with 'UST-'
    @field_validator("asset_tag")
    def validate_asset_tag(cls, val):
        if not val.startswith("UST-"):
            raise ValueError("asset_tag must start with 'UST-'")
        return val

    # Validator to ensure maintenance_type is one of 'Repair', 'Service', or 'Upgrade'
    @field_validator("maintenance_type")
    def validate_maintenance_type(cls, val):
        valid_types = ["Repair", "Service", "Upgrade"]
        if val not in valid_types:
            raise ValueError(f"maintenance_type must be one of {', '.join(valid_types)}")
        return val

    # Validator to ensure vendor_name contains only alphabets and spaces (no digits or special characters)
    @field_validator("vendor_name")
    def validate_vendor_name(cls, val):
        # Checks if there are any digits or non-alphabet characters
        if any(char.isdigit() for char in val) or not all(char.isalpha() or char.isspace() for char in val):
            raise ValueError("vendor_name must only contain alphabets and spaces, no digits or special characters")
        return val

    # Validator to ensure cost is greater than 0
    @field_validator("cost")
    def validate_cost(cls, val):
        if val <= 0:
            raise ValueError("cost must be greater than 0")
        return val

    # Validator to ensure maintenance_date is not in the future
    @field_validator("maintenance_date")
    def validate_maintenance_date(cls, val):
        if val > date.today():
            raise ValueError("maintenance_date cannot be a future date")
        return val

    # Validator to ensure technician_name contains only alphabets and spaces (no digits or special characters)
    @field_validator("technician_name")
    def validate_technician_name(cls, val):
        # Checks if there are any digits or non-alphabet characters
        if any(char.isdigit() for char in val) or not all(char.isalpha() or char.isspace() for char in val):
            raise ValueError("technician_name must only contain alphabets and spaces, no digits or special characters")
        return val

    # Validator to ensure status is either 'Completed' or 'Pending'
    @field_validator("status")
    def validate_status(cls, val):
        if val not in ["Completed", "Pending"]:
            raise ValueError("status must be either 'Completed' or 'Pending'")
        return val
