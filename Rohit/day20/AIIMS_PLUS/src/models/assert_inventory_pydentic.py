from pydantic import BaseModel, Field, field_validator  # Import Pydantic BaseModel, Field for validation, and field_validator for custom rules
from enum import Enum  # Import Enum to define fixed sets of values
from datetime import date, datetime  # Import date and datetime for date handling
from typing import Optional  # Import Optional to allow nullable fields

serial_number_set = set()  # Global set to track unique serial numbers and prevent duplicates

# -----------------------------
# ENUM CLASSES (fixed choices)
# -----------------------------

class Asset_type(str, Enum):  # Enum for asset types
    Laptop = "Laptop"         # Allowed value: Laptop
    Monitor = "Monitor"       # Allowed value: Monitor
    Keyboard = "Keyboard"     # Allowed value: Keyboard
    Mouse = "Mouse"           # Allowed value: Mouse

class Manufacturer(str, Enum):  # Enum for manufacturers
    Dell = "Dell"              # Allowed value: Dell
    HP = "HP"                  # Allowed value: HP
    Lenovo = "Lenovo"          # Allowed value: Lenovo
    Samsung = "Samsung"        # Allowed value: Samsung

class Condition(str, Enum):  # Enum for condition status
    New = "New"              # Allowed value: New
    Good = "Good"            # Allowed value: Good
    Used = "Used"            # Allowed value: Used
    Damaged = "Damaged"      # Allowed value: Damaged

class Location(str, Enum):  # Enum for asset location
    TVM = "TVM"              # Allowed value: TVM
    Bangalore = "Bangalore"  # Allowed value: Bangalore
    Chennai = "Chennai"      # Allowed value: Chennai
    Hyderabad = "Hyderabad"  # Allowed value: Hyderabad

class Asset(str, Enum):  # Enum for asset status
    Available = "Available"  # Allowed value: Available
    Assigned = "Assigned"    # Allowed value: Assigned
    Repair = "Repair"        # Allowed value: Repair
    Retired = "Retired"      # Allowed value: Retired

# -----------------------------
# MAIN Pydantic MODEL
# -----------------------------
class Asset_inventory(BaseModel):  # Define Asset_inventory model using Pydantic BaseModel
    asset_id: int = 0  # Asset ID, default value = 0
    asset_tag: str = Field(...)  # Asset tag, required field
    asset_type: Asset_type = Field(...)  # Asset type, must be one of Asset_type Enum
    serial_number: str = Field(..., description="unique alphanumeric")  # Serial number, required, must be unique
    manufacturer: Manufacturer = Field(...)  # Manufacturer, must be one of Manufacturer Enum
    model: str = Field(...)  # Model name, required
    purchase_date: date = Field(..., description="Date in YYYY-MM-DD format")  # Purchase date, required, must be valid date
    warranty_years: int = Field(..., ge=1, le=5)  # Warranty years, required, must be between 1 and 5
    condition_status: Condition = Field(...)  # Condition status, must be one of Condition Enum
    assigned_to: Optional[str] = None  # Assigned employee, optional (can be None)
    location: Location = Field(...)  # Location, must be one of Location Enum
    asset_status: Asset = Field(...)  # Asset status, must be one of Asset Enum

    # -----------------------------
    # CUSTOM VALIDATORS
    # -----------------------------

    @field_validator("asset_tag")  # Validator for asset_tag field
    def validate_asset_tag(cls, v):  # Function to validate asset_tag
        if not v.startswith("UST-"):  # Check if asset_tag starts with "UST-"
            raise ValueError("asset_tag must start with 'UST-'")  # Raise error if invalid
        return v  # Return validated value

    @field_validator("serial_number")  # Validator for serial_number field
    def check_unique_serial(cls, v):  # Function to validate serial_number
        if not v.isalnum():  # Check if serial_number is alphanumeric
            raise ValueError("Serial number must be alphanumeric")  # Raise error if invalid
        if v in serial_number_set:  # Check if serial_number already exists in set
            raise ValueError(f"Duplicate serial number: {v}")  # Raise error if duplicate
        serial_number_set.add(v)  # Add serial_number to set for uniqueness tracking
        return v  # Return validated value

    @field_validator("purchase_date")  # Validator for purchase_date field
    def validate_purchase_date(cls, v: date):  # Function to validate purchase_date
        if v > date.today():  # Check if purchase_date is in the future
            raise ValueError("purchase_date cannot be in the future")  # Raise error if invalid
        return v  # Return validated value
