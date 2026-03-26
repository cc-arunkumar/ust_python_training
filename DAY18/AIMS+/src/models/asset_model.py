from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import Optional

VALID_ASSET_TYPES = ["Laptop", "Monitor", "Keyboard", "Mouse"]
VALID_MANUFACTURERS = ["Dell", "HP", "Lenovo", "Samsung"]
VALID_CONDITIONS = ["New", "Good", "Used", "Damaged"]
VALID_LOCATIONS = ["TVM", "Bangalore", "Chennai", "Hyderabad"]
VALID_STATUSES = ["Available", "Assigned", "Repair", "Retired"]

class AssetCreate(BaseModel):
    asset_tag: str = Field(..., pattern=r"^UST-")
    asset_type: str
    serial_number: str = Field(..., min_length=1)
    manufacturer: str
    model: str = Field(..., min_length=1)
    purchase_date: date
    warranty_years: int = Field(..., ge=1, le=5)
    condition_status: str
    assigned_to: Optional[str] = None
    location: str
    asset_status: str = "Available"

    @field_validator('asset_tag')
    def check_tag(cls, v):
        if not v.startswith("UST-"):
            raise ValueError("Must start with UST-")
        return v

    @field_validator('asset_type')
    def check_type(cls, v):
        if v not in VALID_ASSET_TYPES:
            raise ValueError("Invalid asset_type")
        return v

    @field_validator('manufacturer')
    def check_manufacturer(cls, v):
        if v not in VALID_MANUFACTURERS:
            raise ValueError("Invalid manufacturer")
        return v

    @field_validator('condition_status')
    def check_condition(cls, v):
        if v not in VALID_CONDITIONS:
            raise ValueError("Invalid condition_status")
        return v

    @field_validator('location')
    def check_location(cls, v):
        if v not in VALID_LOCATIONS:
            raise ValueError("Invalid location")
        return v

    @field_validator('asset_status')
    def check_status(cls, v):
        if v not in VALID_STATUSES:
            raise ValueError("Invalid asset_status")
        return v

    @field_validator('purchase_date')
    def check_date(cls, v):
        if v > date.today():
            raise ValueError("purchase_date cannot be future")
        return v

class AssetUpdate(AssetCreate):
    pass