from pydantic import BaseModel, Field, field_validator  # Import Pydantic for model validation
from typing import Optional, ClassVar, List  # Import typing components for type hinting
from datetime import date  # Import date class to handle date fields
import re  # Import regex for pattern matching
import csv  # Import csv module for reading and writing CSV files

from ..exceptions.custom_exceptions import ValidationErrorException



# AssetCreate model to validate asset data
class AssetCreate(BaseModel):
    # Allowed values for asset types, manufacturers, etc.
    allowed_asset_types: ClassVar[List[str]] = ["Laptop", "Monitor", "Keyboard", "Mouse"]
    allowed_manufactureres: ClassVar[List[str]] = ["Dell", "HP", "Samsung", "Lenovo"]
    allowed_condition_status: ClassVar[List[str]] = ["New", "Good", "Used", "Damaged"]
    allowed_location: ClassVar[List[str]] = ["TVM", "Banglore", "Chennai", "Hyderabad"]
    allowed_asset_status: ClassVar[List[str]] = ["Available", "Assigned", "Repair", "Retired"]

    # Asset attributes to validate
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

    # Validator functions for various fields
    @field_validator("asset_tag")
    def validate_tag(cls, v):
        if not re.match(r"^UST-", v):
            raise ValidationErrorException("asset_tag must start with 'UST-'")
        return v

    @field_validator("asset_type")
    def validate_atype(cls, v):
        if v not in cls.allowed_asset_types:
            raise ValidationErrorException(f"asset_type must be one of: {cls.allowed_asset_types}")
        return v

    @field_validator("serial_number")
    def validate_sn(cls, v):
        if not v or v.strip() == "":
            raise ValidationErrorException("serial_number cannot be empty")
        return v.strip()

    @field_validator("manufacturer")
    def validate_man(cls, v):
        if v not in cls.allowed_manufactureres:
            raise ValidationErrorException(f"manufacturer must be one of: {cls.allowed_manufactureres}")
        return v

    @field_validator("model")
    def validate_model(cls, v):
        if not v.strip():
            raise ValidationErrorException("model cannot be empty")
        return v.strip()

    @field_validator("purchase_date")
    def validate_date(cls, v):
        if v > date.today():
            raise ValidationErrorException("purchase_date cannot be in the future")
        return v

    @field_validator("condition_status")
    def validate_con(cls, v):
        if v not in cls.allowed_condition_status:
            raise ValidationErrorException(f"condition_status must be one of: {cls.allowed_condition_status}")
        return v

    @field_validator("assigned_to")
    def validate_assigned(cls, v):
        if v and not v.strip():
            raise ValidationErrorException("assigned_to cannot be empty if provided")
        return v

    @field_validator("location")
    def validate_location(cls, v):
        normalized_location = v.strip().title()
        location_mapping = {
            "Trivandrum": "TVM",
            "Bangalore": "Banglore",
            
        }
        normalized_location = location_mapping.get(normalized_location, normalized_location)

        if normalized_location not in cls.allowed_location:
            raise ValidationErrorException(f"location must be one of: {cls.allowed_location}")
        return normalized_location

    @field_validator("asset_status")
    def validate_asset_stat(cls, v):
        if v not in cls.allowed_asset_status:
            raise ValidationErrorException(f"asset_status must be one of: {cls.allowed_asset_status}")
        return v

    @field_validator("warranty_years")
    def validate_warranty(cls, v):
        if v < 1:
            raise ValidationErrorException("warranty_years must be greater than or equal to 1")
        return v

