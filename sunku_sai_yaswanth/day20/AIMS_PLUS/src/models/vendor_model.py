from pydantic import BaseModel, Field, field_validator
from typing import Optional
import re

class VendorModel(BaseModel):
    vendor_id: Optional[int] = 0
    vendor_name: str = Field(..., max_length=100, description="Vendor name (no digits allowed)")

    contact_person: str = Field(..., max_length=100, description="Alphabets only, no numbers or special characters")

    contact_phone: str = Field(..., max_length=15, description="Valid 10-digit Indian mobile number starting with 6/7/8/9")

    gst_number: str = Field(..., min_length=15, max_length=15, description="Exactly 15 alphanumeric characters for GSTIN")

    email: str = Field(..., description="Valid email format (e.g., contact@domain.com)")

    address: str = Field(..., max_length=200, description="Vendor address (no strict validation beyond length)")

    city: str = Field(..., max_length=100, description="Valid Indian city name (must match from approved list)")

    active_status: str = Field(..., description="Status must be either 'Active' or 'Inactive'")

    @field_validator("vendor_name")
    def validate_vendor_name(cls, val):
        if any(char.isdigit() for char in val):
            raise ValueError("vendor_name must not contain digits")
        if not all(char.isalpha() or char.isspace() for char in val):
            raise ValueError("vendor_name must only contain alphabets and spaces")
        return val

    @field_validator("contact_person")
    def validate_contact_person(cls, val):
        if not all(char.isalpha() or char.isspace() for char in val):
            raise ValueError("contact_person must only contain alphabets and spaces")
        return val

    @field_validator("contact_phone")
    def validate_contact_phone(cls, val):
        if not re.match(r'^[6789]\d{9}$', val):
            raise ValueError("contact_phone must be a valid 10-digit Indian mobile number starting with 6/7/8/9")
        return val

    @field_validator("gst_number")
    def validate_gst_number(cls, val):
        if len(val) != 15 or not val.isalnum():
            raise ValueError("gst_number must be exactly 15 alphanumeric characters")
        return val

    @field_validator("email")
    def validate_email(cls, val):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, val):
            raise ValueError("email must be a valid email address")
        return val

    @field_validator("city")
    def validate_city(cls, val):
        approved_cities = [
            "Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune", "Ahmedabad", 
            "Jaipur", "Chandigarh", "Surat", "Lucknow", "Indore", "Vadodara", "Nagpur", "Patna", 
            "Bhopal", "Coimbatore", "Agra", "Nashik", "Visakhapatnam", "Guwahati", "Madurai", 
            "Vijayawada", "Ludhiana", "Jammu", "Aurangabad", "Dhanbad", "Goa", "Rajkot"
        ]
        if val not in approved_cities:
            raise ValueError(f"city must be one of the approved cities: {', '.join(approved_cities)}")
        return val

    @field_validator("active_status")
    def validate_active_status(cls, val):
        if val not in ["Active", "Inactive"]:
            raise ValueError("active_status must be either 'Active' or 'Inactive'")
        return val
