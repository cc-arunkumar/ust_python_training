from pydantic import BaseModel, Field, field_validator
from enum import Enum
from datetime import date, datetime
from typing import Optional

serial_number_set = set()

class Asset_type(str, Enum):
    Laptop = "Laptop"
    Monitor = "Monitor"
    Keyboard = "Keyboard"
    Mouse = "Mouse"

class Manufacturer(str, Enum):
    Dell = "Dell"
    HP = "HP"
    Lenovo = "Lenovo"
    Samsung = "Samsung"

class Condition(str, Enum):
    New = "New"
    Good = "Good"
    Used = "Used"
    Damaged = "Damaged"

class Location(str, Enum):
    TVM = "TVM"
    Bangalore = "Bangalore"
    Chennai = "Chennai"
    Hyderabad = "Hyderabad"
    
    

class Asset(str, Enum):
    Available = "Available"
    Assigned = "Assigned"
    Repair = "Repair"
    Retired = "Retired"

class Asset_inventory(BaseModel):
    asset_id: int = 0
    asset_tag: str = Field(...)
    asset_type: Asset_type = Field(...)
    serial_number: str = Field(..., description="unique alphanumeric")
    manufacturer: Manufacturer = Field(...)
    model: str = Field(...)
    purchase_date: date = Field(..., description="Date in YYYY-MM-DD format")
    warranty_years: int = Field(..., ge=1, le=5)
    condition_status: Condition = Field(...)
    assigned_to: Optional[str] = None
    location: Location = Field(...)
    asset_status: Asset = Field(...)

    @field_validator("asset_tag")
    def validate_asset_tag(cls, v):
        if not v.startswith("UST-"):
            raise ValueError("asset_tag must start with 'UST-'")
        return v

    @field_validator("serial_number")
    def check_unique_serial(cls, v):
        if not v.isalnum():
            raise ValueError("Serial number must be alphanumeric")
        if v in serial_number_set:
            raise ValueError(f"Duplicate serial number: {v}")
        serial_number_set.add(v)
        return v

    @field_validator("purchase_date")
    def validate_purchase_date(cls, v: date):
        if v > date.today():
            raise ValueError("purchase_date cannot be in the future")
        return v
