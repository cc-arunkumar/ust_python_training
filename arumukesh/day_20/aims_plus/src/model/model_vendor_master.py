from pydantic import BaseModel, Field, field_validator
from datetime import date, datetime
from typing import Optional
from enum import Enum
import csv
import os

# ---------------------------------------------------------
# Static City List
# ---------------------------------------------------------
CITIES = [
    "Delhi", "Mumbai", "Kolkata", "Bengaluru", "Chennai",
    "Hyderabad", "Ahmedabad", "Surat", "Pune", "Jaipur"
]


# ---------------------------------------------------------
# Enum Class for Active Status
# ---------------------------------------------------------
class ActiveStatus(str, Enum):
    active = "Active"
    inactive = "Inactive"


# ---------------------------------------------------------
# Vendor Master Validation Model Using Pydantic
# ---------------------------------------------------------
class VendorMaster(BaseModel):
    """
    Validation schema for Vendor Master records.
    Enforces formatting rules like GST, email format,
    valid city mapping, and contact conventions.
    """

    vendor_name: str = Field(..., max_length=100, pattern=r"^[A-Za-z ]+$")
    contact_person: str = Field(..., max_length=100, pattern=r"^[^0-9]+$")
    contact_phone: str = Field(..., pattern=r"^[6-9][0-9]{9}$")
    gst_number: str = Field(..., pattern=r"^[0-9]{2}[A-Za-z0-9]{10}[A-Za-z0-9]{3}$")
    email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    address: str = Field(..., max_length=200)
    city: str
    active_status: ActiveStatus

    @field_validator("city")
    def validate_city(cls, value):
        """
        Normalize city name and enforce allowed list.
        Also corrects common spelling variations.
        """
        value = value.strip().title()

        # Auto-correct spelling variations
        if value in ["Bangalore", "Banglore"]:
            value = "Bengaluru"

        if value in CITIES:
            return value

        raise ValueError(f"Invalid city '{value}'. Allowed cities: {CITIES}")

