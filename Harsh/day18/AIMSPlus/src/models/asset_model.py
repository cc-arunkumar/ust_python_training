from pydantic import BaseModel, field_validator, model_validator
from datetime import date, datetime
import re

class AssetInventory(BaseModel):
    asset_id: int | None = None   # optional primary key
    asset_tag: str                # must start with UST-
    asset_type: str               # type of asset (Laptop, Monitor, etc.)
    serial_number: str            # validated serial number format
    manufacturer: str             # must be one of valid manufacturers
    model: str                    # model name/number
    purchase_date: date           # purchase date (not in future)
    warranty_years: int           # warranty between 1 and 5 years
    condition_status: str         # condition of asset
    assigned_to: str | None = None # optional employee assignment
    location: str                 # must be valid location
    asset_status: str             # status of asset (Available, Assigned, etc.)
    last_updated: datetime | None = None  # optional, set in DB

    @field_validator("asset_tag")
    def tag_must_start_with_ust(cls, v):
        # asset_tag must start with "UST-"
        if not v.startswith("UST-"):
            raise ValueError("asset_tag must start with UST")
        return v

    @field_validator("serial_number")
    def serial_number_valid(cls, v):
        # serial_number must match pattern SN-XX-12345
        if not re.fullmatch(r"SN-[A-Z]{2,3}-\d{5}", v):
            raise ValueError("Invalid Serial Number.")
        return v

    @field_validator("manufacturer")
    def manufacturer_valid(cls, v):
        # manufacturer must be one of the allowed set
        valid = {"Dell", "HP", "Lenovo", "Samsung", "LG"}
        if v not in valid:
            raise ValueError("Invalid manufacturer")
        return v

    @field_validator("warranty_years")
    def warranty_range(cls, v):
        # warranty must be between 1 and 5 years
        if not (1 <= v <= 5):
            raise ValueError("warranty_years must be between 1 and 5")
        return v

    @field_validator("condition_status")
    def condition_valid(cls, v):
        # condition_status must be one of allowed values
        valid = {"New", "Good", "Used", "Damaged", "Fair"}
        if v not in valid:
            raise ValueError("Invalid condition_status")
        return v

    @field_validator("location")
    def location_valid(cls, v):
        # location must be one of allowed cities
        valid = {"TVM", "Bangalore", "Chennai", "Hyderabad", "Trivandrum"}
        if v not in valid:
            raise ValueError("Invalid location")
        return v

    @field_validator("asset_status")
    def status_valid(cls, v):
        # asset_status must be one of allowed statuses
        valid = {"Available", "Assigned", "Repair", "Retired"}
        if v not in valid:
            raise ValueError("Invalid asset_status")
        return v

    @model_validator(mode="after")
    def check_purchase_date(cls, values):
        # purchase_date must not be in the future
        if values.purchase_date > date.today():
            raise ValueError("purchase_date cannot be in the future")
        return values
