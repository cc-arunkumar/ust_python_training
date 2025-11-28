import re
from typing import Optional
from pydantic import BaseModel, Field, field_validator
from datetime import date, datetime

class AssetInventory(BaseModel):
    asset_id: Optional[int]=0
    asset_tag: str = Field(..., pattern=r"^UST-(LTP|MNT)-\d{4}$")
    
    @field_validator("asset_tag")
    def validate_asset_tag(cls, val):
        if not re.match(r"^UST-(LTP|MNT)-\d{4}$", val):
            raise ValueError("asset_tag must follow format UST-LTP-0001 or UST-MNT-0001")
        return val

    asset_type: str = Field(...)

    @field_validator("asset_type")
    def validate_asset_type(cls, val):
        valid_types = ["Laptop", "Monitor"]
        if val not in valid_types:
            raise ValueError(f"asset_type must be one of: {', '.join(valid_types)}")
        return val

    serial_number: str = Field(..., pattern=r"^[A-Za-z0-9\-]+$")
    
    manufacturer: str

    @field_validator("manufacturer")
    def validate_manufacturer(cls, val):
        valid_manufacturers = ["Dell", "HP", "Lenovo", "Samsung","LG"]
        if val not in valid_manufacturers:
            raise ValueError(f"manufacturer must be one of: {', '.join(valid_manufacturers)}")
        return val

    model: str = Field(..., min_length=1)

    purchase_date: date

    @field_validator("purchase_date")
    def validate_purchase_date(cls, val):
        if val > date.today():
            raise ValueError("purchase_date cannot be a future date")
        return val

    warranty_years: int = Field(..., ge=1, le=5)
    
    condition_status: str

    @field_validator("condition_status")
    def validate_condition(cls, val):
        valid_conditions = ["NEW", "GOOD", "FAIR", "DAMAGED"]
        if val not in valid_conditions:
            raise ValueError(f"condition_status must be one of: {', '.join(valid_conditions)}")
        return val

    assigned_to:Optional[str] = None

    location: str

    @field_validator("location")
    def validate_location(cls, val):
        valid_locations = ["Trivandrum", "Bangalore", "Chennai", "Hyderabad"]
        if val not in valid_locations:
            raise ValueError(f"location must be one of: {', '.join(valid_locations)}")
        return val

    asset_status: str

    @field_validator("asset_status")
    def validate_asset_status(cls, val):
        valid_statuses = ["Assigned", "Available", "Repair", "Retired"]
        if val not in valid_statuses:
            raise ValueError(f"asset_status must be one of: {', '.join(valid_statuses)}")
        return val

    last_updated: datetime=datetime.now()
