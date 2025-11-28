from pydantic import BaseModel, Field, field_validator, model_validator
from datetime import date, datetime
from typing import Optional
from enum import Enum
import re
import csv
import os

# ---------------- ENUM DEFINITIONS ----------------
class AssetTypeEnum(str, Enum):
    Laptop = "Laptop"
    Monitor = "Monitor"
    Keyboard = "Keyboard"
    Mouse = "Mouse"

class ConditionEnum(str, Enum):
    New = "New"
    Good = "Good"
    Used = "Used"
    Damaged = "Damaged"

class LocationEnum(str, Enum):
    TVM = "TVM"
    Bangalore = "Bangalore"
    Chennai = "Chennai"
    Hyderabad = "Hyderabad"

class AssetStatusEnum(str, Enum):
    Available = "Available"
    Assigned = "Assigned"
    Repair = "Repair"
    Retired = "Retired"

# ---------------- MODEL ----------------
class AssetInventory(BaseModel):

    # asset_id: Optional[int] = None
    asset_tag: str
    asset_type: AssetTypeEnum
    serial_number: str
    manufacturer: str
    model: str
    purchase_date: date
    warranty_years: int
    condition_status: ConditionEnum
    assigned_to: Optional[str] = None
    location: LocationEnum
    asset_status: AssetStatusEnum
    last_updated: datetime = Field(default_factory=datetime.utcnow)

    # ---------------- NORMALIZATION ----------------
    @field_validator("*", mode="before")
    def strip_values(cls, v):
        """Trim whitespace for all string fields before validation."""
        return v.strip() if isinstance(v, str) else v

    @field_validator("asset_type", "condition_status", "location", "asset_status", mode="before")
    def normalize_enum(cls, value, info):
        """
        Standardize enum input and validate against defined Enum values.
        Example: 'laptop' -> 'Laptop'
        """
        if isinstance(value, str):
            cleaned = value.strip().lower().title()
            enum_class = info.annotation  # which enum belongs to this field
            
            # Validate cleaned value exists in enum
            if cleaned not in enum_class._value2member_map_:
                raise ValueError(f"Invalid value '{value}' for {info.field_name}. "
                                 f"Allowed: {list(enum_class._value2member_map_.keys())}")
            return cleaned
        return value

    # ---------------- FIELD VALIDATORS ----------------
    @field_validator("asset_tag")
    def validate_asset_tag(cls, v):
        """Ensure asset_tag follows format: UST-XXX-0001"""
        if not re.match(r"^UST-[A-Za-z]{3}-\d{4}$", v):
            raise ValueError("asset_tag must follow pattern: UST-XXX-0000 (e.g., UST-LTP-0001)")
        return v

    @field_validator("serial_number", mode="before")
    def clean_serial(cls, v):
        """Strip non-alphanumeric characters."""
        return re.sub(r"[^A-Za-z0-9]", "", v) if isinstance(v, str) else v

    @field_validator("serial_number")
    def validate_serial(cls, v):
        if not v.isalnum():
            raise ValueError("serial_number must be alphanumeric.")
        return v

    @field_validator("purchase_date", mode="before")
    def parse_date(cls, v):
        """Accept `2024-01-01`, `2024/01/01`, `01-01-2024`."""
        if isinstance(v, str):
            v = v.replace("/", "-")
            return date.fromisoformat(v)
        return v

    @field_validator("warranty_years", mode="before")
    def convert_warranty(cls, v):
        return int(v)

    @field_validator("assigned_to", mode="before")
    def normalize_assigned(cls, v):
        """Convert blank or 'None' text to actual None."""
        return None if v in ("", "None", "null", None) else v

    # ---------------- MODEL VALIDATION RULES ----------------
    @model_validator(mode="after")
    def assignment_rules(self):
        """Business rules: assigned_to required only when asset_status is Assigned."""
        if self.asset_status == AssetStatusEnum.Assigned and not self.assigned_to:
            raise ValueError("assigned_to is required when asset is Assigned.")

        if self.asset_status in {AssetStatusEnum.Available, AssetStatusEnum.Repair, AssetStatusEnum.Retired} and self.assigned_to:
            raise ValueError(f"assigned_to must be empty when asset_status is {self.asset_status}.")

        return self
