from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Literal

VALID_CITIES = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Pune", "Ahmedabad"]
VALID_STATUS = ["Active", "Inactive"]

class VendorCreate(BaseModel):
    vendor_name: str = Field(..., max_length=100)
    contact_person: str = Field(..., max_length=100)
    contact_phone: str = Field(..., pattern=r"^[6-9]\d{9}$")
    gst_number: str = Field(..., min_length=15, max_length=15)
    email: EmailStr
    address: str = Field(..., max_length=200)
    city: str
    active_status: Literal["Active", "Inactive"] = "Active"

    @field_validator('vendor_name')
    def no_digits(cls, v):
        if any(c.isdigit() for c in v):
            raise ValueError("vendor_name cannot contain digits")
        return v.strip()

    @field_validator('contact_person')
    def alpha_only(cls, v):
        if not v.replace(" ", "").isalpha():
            raise ValueError("contact_person must contain only letters and spaces")
        return v.strip()

    @field_validator('city')
    def valid_city(cls, v):
        if v not in VALID_CITIES:
            raise ValueError(f"city must be one of: {VALID_CITIES}")
        return v

class VendorUpdate(VendorCreate):
    pass