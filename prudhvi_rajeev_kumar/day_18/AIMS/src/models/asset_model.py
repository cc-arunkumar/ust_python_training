from pydantic import BaseModel, field_validator, model_validator
from datetime import date, datetime
import re

class AssetInventory(BaseModel):
    asset_id: int | None = None  
    asset_tag: str
    asset_type: str
    serial_number: str
    manufacturer: str
    model: str
    purchase_date: date
    warranty_years: int
    condition_status: str
    assigned_to: str | None = None
    location: str
    asset_status: str
    last_updated: datetime | None = None  # optional, set in DB

    @field_validator("asset_tag")
    def tag_must_start_with_ust(cls, v):
        if not v.startswith("UST-"):
            raise ValueError("asset_tag must start with UST")
        return v

    @field_validator("serial_number")
    def serial_number_valid(cls, v):
        if not re.fullmatch(r"SN-[A-Z]{2,3}-\d{5}", v):
            raise ValueError("Invalid Serial Number.")
        return v

    @field_validator("manufacturer")
    def manufacturer_valid(cls, v):
        valid = {"Dell", "HP", "Lenovo", "Samsung", "LG"}
        if v not in valid:
            raise ValueError("Invalid manufacturer")
        return v

    @field_validator("warranty_years")
    def warranty_range(cls, v):
        if not (1 <= v <= 5):
            raise ValueError("warranty_years must be between 1 and 5")
        return v

    @field_validator("condition_status")
    def condition_valid(cls, v):
        valid = {"New", "Good", "Used", "Damaged", "Fair"}
        if v not in valid:
            raise ValueError("Invalid condition_status")
        return v

    @field_validator("location")
    def location_valid(cls, v):
        valid = {"TVM", "Bangalore", "Chennai", "Hyderabad", "Trivandrum"}
        if v not in valid:
            raise ValueError("Invalid location")
        return v

    @field_validator("asset_status")
    def status_valid(cls, v):
        valid = {"Available", "Assigned", "Repair", "Retired"}
        if v not in valid:
            raise ValueError("Invalid asset_status")
        return v

    @model_validator(mode="after")
    def check_purchase_date(cls, values):
        if values.purchase_date > date.today():
            raise ValueError("purchase_date cannot be in the future")
        return values
