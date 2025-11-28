from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date

class MaintenanceLogModel(BaseModel):
    # Optional log_id, auto-incremented primary key (for database purposes)
    log_id: Optional[int] = Field(default=None, description="Auto-increment integer primary key")
    
    # Asset tag must follow the UST- pattern (e.g., UST-XXXX)
    asset_tag: str = Field(..., description="Must follow UST- pattern")
    
    # Maintenance type must be one of 'Repair', 'Service', or 'Upgrade'
    maintenance_type: str = Field(..., description="Only 'Repair', 'Service', or 'Upgrade' allowed")
    
    # Vendor name must only contain alphabets and spaces (no digits or special characters)
    vendor_name: str = Field(..., description="Alphabets only (no digits or special characters)")
    
    # Description must be at least 10 characters long
    description: str = Field(..., min_length=10, description="Minimum 10 characters for description")
    
    # Cost must be a positive decimal value with two digits after the decimal point
    cost: float = Field(..., gt=0, description="Decimal with two digits after decimal, must be greater than 0")
    
    # Maintenance date must be a valid date and cannot be in the future
    maintenance_date: date = Field(..., description="Date, cannot be a future date")
    
    # Technician name must only contain alphabets and spaces (no digits or special characters)
    technician_name: str = Field(..., description="Alphabets only (no digits or special characters)")
    
    # Status must be either 'Completed' or 'Pending'
    status: str = Field(..., description="Only 'Completed' or 'Pending' allowed")

    # Validator for asset_tag: ensures it starts with 'UST-'
    @field_validator("asset_tag")
    def validate_asset_tag(cls, val):
        if not val.startswith("UST-"):
            raise ValueError("asset_tag must start with 'UST-'")
        return val

    # Validator for maintenance_type: ensures it's one of the valid types
    @field_validator("maintenance_type")
    def validate_maintenance_type(cls, val):
        valid_types = ["Repair", "Service", "Upgrade"]
        if val not in valid_types:
            raise ValueError(f"maintenance_type must be one of {', '.join(valid_types)}")
        return val

    # Validator for vendor_name: ensures it contains only alphabets and spaces
    @field_validator("vendor_name")
    def validate_vendor_name(cls, val):
        if any(char.isdigit() for char in val) or not all(char.isalpha() or char.isspace() for char in val):
            raise ValueError("vendor_name must only contain alphabets and spaces, no digits or special characters")
        return val

    # Validator for cost: ensures the cost is a positive value
    @field_validator("cost")
    def validate_cost(cls, val):
        if val <= 0:
            raise ValueError("cost must be greater than 0")
        return val

    # Validator for maintenance_date: ensures it's not a future date
    @field_validator("maintenance_date")
    def validate_maintenance_date(cls, val):
        if val > date.today():
            raise ValueError("maintenance_date cannot be a future date")
        return val

    # Validator for technician_name: ensures it contains only alphabets and spaces
    @field_validator("technician_name")
    def validate_technician_name(cls, val):
        if any(char.isdigit() for char in val) or not all(char.isalpha() or char.isspace() for char in val):
            raise ValueError("technician_name must only contain alphabets and spaces, no digits or special characters")
        return val

    # Validator for status: ensures it's either 'Completed' or 'Pending'
    @field_validator("status")
    def validate_status(cls, val):
        if val not in ["Completed", "Pending"]:
            raise ValueError("status must be either 'Completed' or 'Pending'")
        return val
