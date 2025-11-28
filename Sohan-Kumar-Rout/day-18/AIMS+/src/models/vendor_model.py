from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional

valid_cities = ["Mumbai","Delhi","Bangalore","Chennai","Hyderabad","Pune","Kolkata"]

class VendorModel(BaseModel):
    vendor_id: int = Field(..., ge=1, description="Unique vendor ID")
    vendor_name: str = Field(..., max_length=100, description="Vendor name, alphabets and spaces only")
    contact_person: str = Field(..., max_length=100, description="Contact person, alphabets and spaces only")
    contact_phone: str = Field(..., description="10-digit phone number starting with 6-9")
    gst_number: str = Field(..., min_length=15, max_length=15, description="15-character alphanumeric GST number")
    email: EmailStr = Field(..., description="Valid email address")
    address: str = Field(..., max_length=200, description="Address up to 200 characters")
    city: str = Field(..., description="Valid city")
    active_status: str = Field(..., description="Active or Inactive")

    @field_validator("vendor_name")
    def validate_vendor_name(cls, v):
        if not v.replace(" ", "").isalpha():
            raise ValueError("Vendor name must contain only alphabets and spaces")
        return v

    @field_validator("contact_person")
    def validate_contact_person(cls, v):
        if not v.replace(" ", "").isalpha():
            raise ValueError("Contact person must contain only alphabets and spaces")
        return v

    @field_validator("contact_phone")
    def validate_contact_phone(cls, v):
        if not v.isdigit() or len(v) != 10 or v[0] not in "6789":
            raise ValueError("Contact phone must be a 10-digit number starting with 6-9")
        return v

    @field_validator("gst_number")
    def validate_gst_number(cls, v):
        if not v.isalnum() or len(v) != 15:
            raise ValueError("GST number must be 15 alphanumeric characters")
        return v

    @field_validator("city")
    def validate_city(cls, v):
        if v not in valid_cities:
            raise ValueError(f"City must be one of {valid_cities}")
        return v

    @field_validator("active_status")
    def validate_active_status(cls, v):
        if v not in ["Active", "Inactive"]:
            raise ValueError("active_status must be either 'Active' or 'Inactive'")
        return v
