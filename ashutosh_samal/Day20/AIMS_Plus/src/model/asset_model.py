from pydantic import BaseModel, Field, field_validator
from typing import Optional, ClassVar, List
from datetime import date
import re
import csv

# Asset creation model with validation for various fields
class AssetCreate(BaseModel):
    # Class variables defining allowed values for asset attributes
    allowed_asset_types: ClassVar[List[str]] = ["Laptop", "Monitor", "Keyboard", "Mouse"]
    allowed_manufacturers: ClassVar[List[str]] = ["Dell", "HP", "Samsung", "Lenovo", "LG"] 
    allowed_condition_status: ClassVar[List[str]] = ["New", "Good", "Used", "Damaged"]
    allowed_location: ClassVar[List[str]] = ["Trivandrum", "Banglore", "Chennai", "Hyderabad"]
    allowed_asset_status: ClassVar[List[str]] = ["Available", "Assigned", "Repair", "Retired"]
    
    # Instance variables for asset details
    asset_tag: str
    asset_type: str
    serial_number: str
    manufacturer: str
    model: str
    purchase_date: date
    warranty_years: int = Field(..., ge=1, le=5)  # Warranty years should be between 1 and 5
    condition_status: str
    assigned_to: Optional[str]
    location: str
    asset_status: str

    # Validator to ensure asset_tag starts with 'UST-'
    @field_validator("asset_tag")
    def validate_asset_tag(cls, v):
        if not re.match(r"^UST-", v):  # Regex checks if the asset_tag starts with 'UST-'
            raise ValueError("asset_tag must start with 'UST-'")
        return v

    # Validator for asset_type to ensure it's one of the allowed types
    @field_validator("asset_type")
    def validate_asset_type(cls, v):
        if v not in cls.allowed_asset_types:
            raise ValueError(f"asset_type must be one of: {cls.allowed_asset_types}")
        return v

    # Validator for serial_number to ensure it's not empty
    @field_validator("serial_number")
    def validate_serial_number(cls, v):
        if not v or v.strip() == "":
            raise ValueError("serial_number cannot be empty")
        return v.strip()

    # Validator for manufacturer to ensure it's one of the allowed manufacturers
    @field_validator("manufacturer")
    def validate_manufacturer(cls, v):
        if v not in cls.allowed_manufacturers:
            raise ValueError(f"manufacturer must be one of: {cls.allowed_manufacturers}")
        return v

    # Validator for model to ensure it is not empty
    @field_validator("model")
    def validate_model(cls, v):
        if not v.strip():
            raise ValueError("model cannot be empty")
        return v.strip()

    # Validator for purchase_date to ensure it's not in the future
    @field_validator("purchase_date")
    def validate_purchase_date(cls, v):
        if v > date.today():
            raise ValueError("purchase_date cannot be in the future")
        return v

    # Validator for condition_status to ensure it's one of the allowed conditions
    @field_validator("condition_status")
    def validate_condition_status(cls, v):
        if v not in cls.allowed_condition_status:
            raise ValueError(f"condition_status must be one of: {cls.allowed_condition_status}")
        return v

    # Validator for assigned_to to ensure it is not empty if provided
    @field_validator("assigned_to")
    def validate_assigned_to(cls, v):
        if v and not v.strip():  # If assigned_to is provided, it should not be empty
            raise ValueError("assigned_to cannot be empty if provided")
        return v

    # Validator for location to ensure it is one of the allowed locations
    @field_validator("location")
    def validate_location(cls, v):
        normalized_location = v.strip().title()  # Normalize location to proper title case
        if normalized_location not in cls.allowed_location:
            raise ValueError(f"location must be one of:{cls.allowed_location}")
        return normalized_location

    # Validator for asset_status to ensure it's one of the allowed statuses
    @field_validator("asset_status")
    def validate_asset_status(cls, v):
        if v not in cls.allowed_asset_status:
            raise ValueError(f"asset_status must be one of: {cls.allowed_asset_status}")
        return v

    # Validator for warranty_years to ensure it is between 1 and 5
    @field_validator("warranty_years")
    def validate_warranty_years(cls, v):
        if v < 1:
            raise ValueError("warranty_years must be greater than or equal to 1")
        return v
