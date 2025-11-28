from pydantic import BaseModel, Field, field_validator  # Import Pydantic for data validation
from datetime import date  # Import date class to handle date fields
from typing import ClassVar, List  # Import typing components for type hinting
import csv  # Import csv module for reading and writing CSV files

from ..exceptions.custom_exceptions import ValidationErrorException



# MaintenanceCreate model to validate maintenance log data
class MaintenanceCreate(BaseModel):
    # Class variables for allowed values of maintenance types and status
    allowed_types: ClassVar[List[str]] = ["Repair", "Service", "Upgrade"]
    allowed_status: ClassVar[List[str]] = ["Completed", "Pending"]

    # Maintenance log attributes to validate
    asset_tag: str
    maintenance_type: str
    vendor_name: str
    description: str
    cost: float = Field(..., gt=0)  # Cost must be greater than 0
    maintenance_date: date
    technician_name: str
    status: str

    # Validators for each field
    @field_validator("asset_tag")
    def validate_asset_tag(cls, v):
        if not v.startswith("UST-"):  # asset_tag must start with 'UST-'
            raise ValidationErrorException("asset_tag must start with 'UST-'")
        return v

    @field_validator("maintenance_type")
    def validate_maintenance(cls, v):
        if v not in cls.allowed_types:  # maintenance_type must be one of the allowed types
            raise ValidationErrorException(f"maintenance_type must be one of: {cls.allowed_types}")
        return v

    @field_validator("vendor_name")
    def validate_name(cls, v):
        if not v.replace(" ", "").isalpha():  # vendor_name must contain only alphabets
            raise ValidationErrorException("vendor_name must contain only alphabets")
        return v

    @field_validator("description")
    def validate_description(cls, v):
        if len(v.strip()) < 10:  # description must be at least 10 characters long
            raise ValidationErrorException("description must be at least 10 characters long")
        return v.strip()

    @field_validator("maintenance_date")
    def validate_date(cls, v):
        if v > date.today():  # maintenance_date cannot be in the future
            raise ValidationErrorException("maintenance_date cannot be in the future")
        return v

    @field_validator("technician_name")
    def validate_technician(cls, v):
        if not v.replace(" ", "").isalpha():  # technician_name must contain only alphabets
            raise ValidationErrorException("technician_name must contain only alphabets")
        return v

    @field_validator("status")
    def validate_status(cls, v):
        if v not in cls.allowed_status:  # status must be one of the allowed statuses
            raise ValidationErrorException(f"status must be one of: {cls.allowed_status}")
        return v
