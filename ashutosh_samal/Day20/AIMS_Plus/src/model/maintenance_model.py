from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import ClassVar, List
import csv

# Model to define the structure of maintenance log data
class MaintenanceCreate(BaseModel):
    allowed_types: ClassVar[List[str]] = ["Repair", "Service", "Upgrade"]  # Allowed maintenance types
    allowed_status: ClassVar[List[str]] = ["Completed", "Pending"]  # Allowed status values
    
    # Fields for maintenance log data
    asset_tag: str
    maintenance_type: str
    vendor_name: str
    description: str
    cost: float = Field(..., gt=0)  # Cost must be greater than 0
    maintenance_date: date
    technician_name: str
    status: str

    # Validator for the 'asset_tag' field to ensure it starts with 'UST-'
    @field_validator("asset_tag")
    def validate_asset_tag(cls, v):
        # Ensure the asset_tag starts with 'UST-' for consistency
        if not v.startswith("UST-"):
            raise ValueError("asset_tag must start with 'UST-'")
        return v

    # Validator for the 'maintenance_type' field to check if it's one of the allowed types
    @field_validator("maintenance_type")
    def validate_maintenance(cls, v):
        # Check if the maintenance type is valid (Repair, Service, or Upgrade)
        if v not in cls.allowed_types:
            raise ValueError(f"maintenance_type must be one of: {cls.allowed_types}")
        return v

    # Validator for the 'vendor_name' field to ensure it contains only alphabetic characters and spaces
    @field_validator("vendor_name")
    def validate_name(cls, v):
        # Ensure the vendor name contains only alphabets and spaces (no special characters or numbers)
        if not v.replace(" ", "").isalpha():
            raise ValueError("vendor_name must contain only alphabets")
        return v

    # Validator for the 'description' field to ensure it has a minimum length of 10 characters
    @field_validator("description")
    def validate_description(cls, v):
        # Check if the description has at least 10 characters
        if len(v.strip()) < 10:
            raise ValueError("description must be at least 10 characters long")
        return v.strip()

    # Validator for the 'maintenance_date' field to ensure it's not a future date
    @field_validator("maintenance_date")
    def validate_date(cls, v):
        # Ensure the maintenance date is not in the future
        if v > date.today():
            raise ValueError("maintenance_date cannot be in the future")
        return v

    # Validator for the 'technician_name' field to ensure it contains only alphabetic characters and spaces
    @field_validator("technician_name")
    def validate_technician(cls, v):
        # Ensure the technician name contains only alphabets and spaces (no special characters or numbers)
        if not v.replace(" ", "").isalpha():
            raise ValueError("technician_name must contain only alphabets")
        return v

    # Validator for the 'status' field to ensure it's one of the allowed status values
    @field_validator("status")
    def validate_status(cls, v):
        # Check if the status is valid (Completed or Pending)
        if v not in cls.allowed_status:
            raise ValueError(f"status must be one of: {cls.allowed_status}")
        return v

