import re
from typing import Optional
from pydantic import BaseModel, Field, field_validator
from datetime import date, datetime

# Define the AssetInventory model, inheriting from Pydantic's BaseModel
class AssetInventory(BaseModel):
    # Optional asset_id with default value 0
    asset_id: Optional[int] = 0
    
    # Asset tag must follow the format: UST-LTP-0001 or UST-MNT-0001
    asset_tag: str = Field(..., pattern=r"^UST-(LTP|MNT)-\d{4}$")
    
    # Validator for the asset_tag to check its format
    @field_validator("asset_tag")
    def validate_asset_tag(cls, val):
        # Check that the asset_tag matches the desired pattern
        if not re.match(r"^UST-(LTP|MNT)-\d{4}$", val):
            raise ValueError("asset_tag must follow format UST-LTP-0001 or UST-MNT-0001")
        return val

    # Asset type should be either 'Laptop' or 'Monitor'
    asset_type: str = Field(...)

    # Validator for asset_type to ensure it matches the allowed types
    @field_validator("asset_type")
    def validate_asset_type(cls, val):
        valid_types = ["Laptop", "Monitor"]
        if val not in valid_types:
            raise ValueError(f"asset_type must be one of: {', '.join(valid_types)}")
        return val

    # Serial number can contain alphanumeric characters and hyphens
    serial_number: str = Field(..., pattern=r"^[A-Za-z0-9\-]+$")

    # Manufacturer name should be one of the specified valid manufacturers
    manufacturer: str

    # Validator for the manufacturer to ensure it matches a list of valid manufacturers
    @field_validator("manufacturer")
    def validate_manufacturer(cls, val):
        valid_manufacturers = ["Dell", "HP", "Lenovo", "Samsung", "LG"]
        if val not in valid_manufacturers:
            raise ValueError(f"manufacturer must be one of: {', '.join(valid_manufacturers)}")
        return val

    # Model name should have a minimum length of 1
    model: str = Field(..., min_length=1)

    # Purchase date should not be in the future
    purchase_date: date

    # Validator for purchase_date to ensure it is not a future date
    @field_validator("purchase_date")
    def validate_purchase_date(cls, val):
        if val > date.today():
            raise ValueError("purchase_date cannot be a future date")
        return val

    # Warranty years must be between 1 and 5 years
    warranty_years: int = Field(..., ge=1, le=5)
    
    # Condition status of the asset, must be one of: NEW, GOOD, FAIR, DAMAGED
    condition_status: str

    # Validator for condition_status to check if the value is valid
    @field_validator("condition_status")
    def validate_condition(cls, val):
        valid_conditions = ["NEW", "GOOD", "FAIR", "DAMAGED"]
        if val not in valid_conditions:
            raise ValueError(f"condition_status must be one of: {', '.join(valid_conditions)}")
        return val

    # The asset can optionally be assigned to someone (can be None)
    assigned_to: Optional[str] = None

    # Location of the asset, must be one of the specified valid locations
    location: str

    # Validator for location to ensure it matches a list of valid locations
    @field_validator("location")
    def validate_location(cls, val):
        valid_locations = ["Trivandrum", "Bangalore", "Chennai", "Hyderabad"]
        if val not in valid_locations:
            raise ValueError(f"location must be one of: {', '.join(valid_locations)}")
        return val

    # Status of the asset, must be one of: Assigned, Available, Repair, Retired
    asset_status: str

    # Validator for asset_status to ensure it matches one of the allowed values
    @field_validator("asset_status")
    def validate_asset_status(cls, val):
        valid_statuses = ["Assigned", "Available", "Repair", "Retired"]
        if val not in valid_statuses:
            raise ValueError(f"asset_status must be one of: {', '.join(valid_statuses)}")
        return val

    # Timestamp of the last update, defaulting to the current datetime
    last_updated: datetime = datetime.now()
