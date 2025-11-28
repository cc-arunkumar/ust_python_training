from pydantic import BaseModel, Field, field_validator
from typing import Optional
import re

class VendorModel(BaseModel):
    # vendor_id is optional and has a default value of 0. It represents the unique identifier for the vendor.
    vendor_id: Optional[int] = 0

    # vendor_name is required and cannot contain any digits, only alphabets and spaces.
    # This represents the name of the vendor.
    vendor_name: str = Field(..., max_length=100, description="Vendor name (no digits allowed)")

    # contact_person is required and must only contain alphabets and spaces (no digits or special characters).
    # Represents the name of the person to contact at the vendor's organization.
    contact_person: str = Field(..., max_length=100, description="Alphabets only, no numbers or special characters")

    # contact_phone is required and must be a valid 10-digit Indian mobile number starting with 6/7/8/9.
    contact_phone: str = Field(..., max_length=15, description="Valid 10-digit Indian mobile number starting with 6/7/8/9")

    # gst_number is required and must be exactly 15 alphanumeric characters, which is the GSTIN format.
    gst_number: str = Field(..., min_length=15, max_length=15, description="Exactly 15 alphanumeric characters for GSTIN")

    # email is required and must be in a valid email format.
    email: str = Field(..., description="Valid email format (e.g., contact@domain.com)")

    # address is required, and its length cannot exceed 200 characters.
    # Represents the vendor's address. There's no strict validation beyond length.
    address: str = Field(..., max_length=200, description="Vendor address (no strict validation beyond length)")

    # city is required and must be a valid Indian city name from an approved list.
    city: str = Field(..., max_length=100, description="Valid Indian city name (must match from approved list)")

    # active_status is required and must be either 'Active' or 'Inactive'.
    active_status: str = Field(..., description="Status must be either 'Active' or 'Inactive'")

    # Validator for vendor_name
    # Ensures that the vendor name does not contain any digits, and contains only alphabets and spaces.
    @field_validator("vendor_name")
    def validate_vendor_name(cls, val):
        if any(char.isdigit() for char in val):
            raise ValueError("vendor_name must not contain digits")
        if not all(char.isalpha() or char.isspace() for char in val):
            raise ValueError("vendor_name must only contain alphabets and spaces")
        return val

    # Validator for contact_person
    # Ensures that the contact person name contains only alphabets and spaces.
    @field_validator("contact_person")
    def validate_contact_person(cls, val):
        if not all(char.isalpha() or char.isspace() for char in val):
            raise ValueError("contact_person must only contain alphabets and spaces")
        return val

    # Validator for contact_phone
    # Ensures that the contact phone is a valid 10-digit Indian mobile number starting with 6, 7, 8, or 9.
    @field_validator("contact_phone")
    def validate_contact_phone(cls, val):
        if not re.match(r'^[6789]\d{9}$', val):
            raise ValueError("contact_phone must be a valid 10-digit Indian mobile number starting with 6/7/8/9")
        return val

    # Validator for gst_number
    # Ensures that the GST number is exactly 15 alphanumeric characters.
    @field_validator("gst_number")
    def validate_gst_number(cls, val):
        if len(val) != 15 or not val.isalnum():
            raise ValueError("gst_number must be exactly 15 alphanumeric characters")
        return val

    # Validator for email
    # Ensures that the email is in a valid format using regex.
    @field_validator("email")
    def validate_email(cls, val):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, val):
            raise ValueError("email must be a valid email address")
        return val

    # Validator for city
    # Ensures that the city is part of the approved list of Indian cities.
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

    # Validator for active_status
    # Ensures that the active status is either 'Active' or 'Inactive'.
    @field_validator("active_status")
    def validate_active_status(cls, val):
        if val not in ["Active", "Inactive"]:
            raise ValueError("active_status must be either 'Active' or 'Inactive'")
        return val
