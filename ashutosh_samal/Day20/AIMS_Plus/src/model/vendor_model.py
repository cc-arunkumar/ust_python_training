from pydantic import BaseModel, Field, field_validator
from typing import ClassVar, List
import re
import csv

# Vendor creation model
class VendorCreate(BaseModel):
    # Predefined allowed cities and status values
    allowed_cities: ClassVar[List[str]] = ["TVM", "Bangalore" , "Kolkata" ,"Chennai" ,"Mumbai" ," Hyderabad","Pune"]
    allowed_status: ClassVar[List[str]] = ["Active", "Inactive"]

    # Fields for vendor details
    vendor_name: str = Field(..., max_length=100)
    contact_person: str = Field(..., max_length=100)
    contact_phone: str = Field(..., min_length=10, max_length=10)
    gst_number: str = Field(..., min_length=15, max_length=15)
    email: str
    address: str = Field(..., max_length=200)
    city: str
    active_status: str

    # Validator to check if vendor name contains only alphabets and spaces
    @field_validator("vendor_name")
    def validate_name(cls, v):
        if not v.replace(" ", "").isalpha():
            raise ValueError("vendor_name must contain only alphabets and spaces")
        return v

    # Validator for contact person to ensure it contains only alphabets
    @field_validator("contact_person")
    def validate_contact(cls, v):
        if not v.replace(" ", "").isalpha():
            raise ValueError("contact_person must contain only alphabets")
        return v

    # Validator to ensure phone number is exactly 10 digits and starts with 6, 7, 8, or 9
    @field_validator("contact_phone")
    def validate_phone(cls, v):
        if not v.isdigit() or len(v) != 10:
            raise ValueError("contact_phone must be exactly 10 digits")
        if v[0] not in "6789":
            raise ValueError("contact_phone must start with 6, 7, 8, or 9")
        return v

    # Validator to check GST number length and ensure it's alphanumeric
    @field_validator("gst_number")
    def validate_gst_number(cls, v):
        if len(v) != 15 or not v.isalnum():
            raise ValueError("gst_number must be exactly 15 alphanumeric characters")
        return v.upper()

    # Validator for email format using a regex pattern
    @field_validator("email")
    def validate_email(cls, v):
        pattern = r"^[a-zA-Z0-9.%+-]+@[a-zA-Z0-9,-]+\.[A-Za-z]{2,}$"
        if not re.match(pattern, v):
            raise ValueError("Invalid email format")
        return v

    # Validator to ensure address length does not exceed 200 characters
    @field_validator("address")
    def validate_address(cls, v):
        if len(v) > 200:
            raise ValueError("address cannot exceed 200 characters")
        return v

    # Validator for city to ensure it belongs to the allowed cities
    @field_validator("city")
    def validate_city(cls, v):
        if v not in cls.allowed_cities:
            raise ValueError(f"city must be one of: {cls.allowed_cities}")
        return v

    # Validator for active_status to ensure it is either "Active" or "Inactive"
    @field_validator("active_status")
    def validate_status(cls, v):
        if v not in cls.allowed_status:
            raise ValueError(f"active_status must be one of: {cls.allowed_status}")
        return v

