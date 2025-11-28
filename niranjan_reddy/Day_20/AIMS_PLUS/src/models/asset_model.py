import re
from typing import Optional
from pydantic import BaseModel, Field, field_validator
from datetime import date, datetime

class AssetInventory(BaseModel):
    # Optional asset_id field with a default value of 0
    asset_id: Optional[int] = 0   
    
    # Asset tag must match a specific pattern like UST-LTP-0001 or UST-MNT-0001
    asset_tag: str = Field(..., pattern=r"^UST-(LTP|MNT)-\d{4}$")
    
    @field_validator("asset_tag")
    def validate_asset_tag(cls, val):
        # Ensure the asset tag follows the expected format
        if not re.match(r"^UST-(LTP|MNT)-\d{4}$", val):
            raise ValueError("asset_tag must follow format UST-LTP-0001 or UST-MNT-0001")
        return val

    # Asset type field with a predefined set of valid values
    asset_type: str = Field(...)
    
    @field_validator("asset_type")
    def validate_asset_type(cls, val):
        valid_types = ["Laptop", "Monitor"]  # Allowed asset types
        if val not in valid_types:
            raise ValueError(f"asset_type must be one of: {', '.join(valid_types)}")
        return val

    # Serial number must be alphanumeric and may include hyphens
    serial_number: str = Field(..., pattern=r"^[A-Za-z0-9\-]+$")
    
    manufacturer: str

    @field_validator("manufacturer")
    def validate_manufacturer(cls, val):
        valid_manufacturers = ["Dell", "HP", "Lenovo", "Samsung", "LG"]  # Allowed manufacturers
        if val not in valid_manufacturers:
            raise ValueError(f"manufacturer must be one of: {', '.join(valid_manufacturers)}")
        return val

    # Model must be a non-empty string
    model: str = Field(..., min_length=1)

    # Purchase date must not be in the future
    purchase_date: date

    @field_validator("purchase_date")
    def validate_purchase_date(cls, val):
        if val > date.today():  # Ensure purchase date is not a future date
            raise ValueError("purchase_date cannot be a future date")
        return val

    # Warranty years should be between 1 and 5
    warranty_years: int = Field(..., ge=1, le=5)
    
    condition_status: str

    @field_validator("condition_status")
    def validate_condition(cls, val):
        valid_conditions = ["New", "Good", "Fair", "Damaged"]  # Valid condition statuses
        if val not in valid_conditions:
            raise ValueError(f"condition_status must be one of: {', '.join(valid_conditions)}")
        return val

    # Optional field for who the asset is assigned to
    assigned_to: Optional[str] = None

    # Location must be one of the predefined valid locations
    location: str

    @field_validator("location")
    def validate_location(cls, val):
        valid_locations = ["Trivandrum", "Bangalore", "Chennai", "Hyderabad"]  # Valid locations
        if val not in valid_locations:
            raise ValueError(f"location must be one of: {', '.join(valid_locations)}")
        return val

    # Asset status must be one of the valid options like Assigned, Available, etc.
    asset_status: str

    @field_validator("asset_status")
    def validate_asset_status(cls, val):
        valid_statuses = ["Assigned", "Available", "Repair", "Retired"]  # Allowed asset statuses
        if val not in valid_statuses:
            raise ValueError(f"asset_status must be one of: {', '.join(valid_statuses)}")
        return val

    # Last updated timestamp, defaults to the current date and time
    last_updated: datetime = datetime.now()
