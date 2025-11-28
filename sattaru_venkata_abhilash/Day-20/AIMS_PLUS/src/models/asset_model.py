import re  # Importing the regex module for pattern matching
from typing import Optional  # Importing Optional for optional type annotations
from pydantic import BaseModel, Field, field_validator  # Importing BaseModel and Field for defining data models and validation
from datetime import date, datetime  # Importing date and datetime for date-related validation

# AssetInventory model class for managing asset records
class AssetInventory(BaseModel):
    # asset_id is optional and defaults to 0 if not provided
    asset_id: Optional[int] = 0

    # asset_tag is a string field, and it must match the regex pattern for asset tags (e.g., UST-LTP-0001)
    asset_tag: str = Field(..., pattern=r"^UST-(LTP|MNT)-\d{4}$")

    # Validator to ensure asset_tag follows the format "UST-LTP-0001" or "UST-MNT-0001"
    @field_validator("asset_tag")
    def validate_asset_tag(cls, val):
        if not re.match(r"^UST-(LTP|MNT)-\d{4}$", val):
            raise ValueError("asset_tag must follow format UST-LTP-0001 or UST-MNT-0001")
        return val

    # asset_type is a required field and its value must be "Laptop" or "Monitor"
    asset_type: str = Field(...)

    # Validator to check if asset_type is one of the valid types
    @field_validator("asset_type")
    def validate_asset_type(cls, val):
        valid_types = ["Laptop", "Monitor"]
        if val not in valid_types:
            raise ValueError(f"asset_type must be one of: {', '.join(valid_types)}")
        return val

    # serial_number is a required string and must match the regex pattern for alphanumeric or hyphenated values
    serial_number: str = Field(..., pattern=r"^[A-Za-z0-9\-]+$")

    # manufacturer is a required field with a string value
    manufacturer: str

    # Validator to ensure the manufacturer is one of the predefined valid manufacturers
    @field_validator("manufacturer")
    def validate_manufacturer(cls, val):
        valid_manufacturers = ["Dell", "HP", "Lenovo", "Samsung", "LG"]
        if val not in valid_manufacturers:
            raise ValueError(f"manufacturer must be one of: {', '.join(valid_manufacturers)}")
        return val

    # model is a required string field with a minimum length of 1
    model: str = Field(..., min_length=1)

    # purchase_date is a required field of type date
    purchase_date: date

    # Validator to ensure purchase_date is not a future date
    @field_validator("purchase_date")
    def validate_purchase_date(cls, val):
        if val > date.today():
            raise ValueError("purchase_date cannot be a future date")
        return val

    # warranty_years is an integer field with a value between 1 and 5
    warranty_years: int = Field(..., ge=1, le=5)

    # condition_status is a required string field with a validator to ensure valid values
    condition_status: str

    # Validator to ensure condition_status is one of the valid conditions
    @field_validator("condition_status")
    def validate_condition(cls, val):
        valid_conditions = ["New", "Good", "Fair", "Damaged"]
        if val not in valid_conditions:
            raise ValueError(f"condition_status must be one of: {', '.join(valid_conditions)}")
        return val

    # assigned_to is an optional field, defaulting to None
    assigned_to: Optional[str] = None

    # location is a required field with a validator to ensure it is one of the valid locations
    location: str

    # Validator to ensure location is one of the predefined valid locations
    @field_validator("location")
    def validate_location(cls, val):
        valid_locations = ["Trivandrum", "Bangalore", "Chennai", "Hyderabad"]
        if val not in valid_locations:
            raise ValueError(f"location must be one of: {', '.join(valid_locations)}")
        return val

    # asset_status is a required string field with a validator to ensure valid values
    asset_status: str

    # Validator to ensure asset_status is one of the valid statuses
    @field_validator("asset_status")
    def validate_asset_status(cls, val):
        valid_statuses = ["Assigned", "Available", "Repair", "Retired"]
        if val not in valid_statuses:
            raise ValueError(f"asset_status must be one of: {', '.join(valid_statuses)}")
        return val

    # last_updated is a datetime field, and it defaults to the current time when the object is created
    last_updated: datetime = datetime.now()
