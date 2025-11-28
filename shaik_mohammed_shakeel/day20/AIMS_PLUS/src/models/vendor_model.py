from pydantic import BaseModel, Field, field_validator
from typing import Optional
import re

class VendorModel(BaseModel):
    # Optional vendor_id with a default value of 0 (auto-incremented primary key)
    vendor_id: Optional[int] = 0
    
    # Vendor name must not contain digits, and it can include spaces (max length of 100 characters)
    vendor_name: str = Field(..., max_length=100, description="Vendor name (no digits allowed)")

    # Contact person name should contain only alphabets and spaces, with a max length of 100 characters
    contact_person: str = Field(..., max_length=100, description="Alphabets only, no numbers or special characters")

    # Contact phone must be a valid 10-digit Indian mobile number starting with 6, 7, 8, or 9
    contact_phone: str = Field(..., max_length=15, description="Valid 10-digit Indian mobile number starting with 6/7/8/9")

    # GST number must be exactly 15 alphanumeric characters (GSTIN format)
    gst_number: str = Field(..., min_length=15, max_length=15, description="Exactly 15 alphanumeric characters for GSTIN")

    # Email must be in a valid format (e.g., contact@domain.com)
    email: str = Field(..., description="Valid email format (e.g., contact@domain.com)")

    # Vendor address can have up to 200 characters, no strict validation beyond length
    address: str = Field(..., max_length=200, description="Vendor address (no strict validation beyond length)")

    # City must be a valid Indian city from an approved list
    city: str = Field(..., max_length=100, description="Valid Indian city name (must match from approved list)")

    # Active status must be either 'Active' or 'Inactive'
    active_status: str = Field(..., description="Status must be either 'Active' or 'Inactive'")

    # Validator for vendor_name: ensures it does not contain digits and only includes alphabets and spaces
    @field_validator("vendor_name")
    def validate_vendor_name(cls, val):
        if any(char.isdigit() for char in val):  # Ensure no digits in vendor name
            raise ValueError("vendor_name must not contain digits")
        if not all(char.isalpha() or char.isspace() for char in val):  # Ensure only alphabets and spaces
            raise ValueError("vendor_name must only contain alphabets and spaces")
        return val

    # Validator for contact_person: ensures it only contains alphabets and spaces
    @field_validator("contact_person")
    def validate_contact_person(cls, val):
        if not all(char.isalpha() or char.isspace() for char in val):  # Ensure only alphabets and spaces
            raise ValueError("contact_person must only contain alphabets and spaces")
        return val

    # Validator for contact_phone: checks if it's a valid 10-digit Indian mobile number starting with 6, 7, 8, or 9
    @field_validator("contact_phone")
    def validate_contact_phone(cls, val):
        if not re.match(r'^[6789]\d{9}$', val):  # Check the mobile number pattern
            raise ValueError("contact_phone must be a valid 10-digit Indian mobile number starting with 6/7/8/9")
        return val

    # Validator for gst_number: checks if it is exactly 15 alphanumeric characters (GSTIN format)
    @field_validator("gst_number")
    def validate_gst_number(cls, val):
        if len(val) != 15 or not val.isalnum():  # Ensure GST number is 15 alphanumeric characters
            raise ValueError("gst_number must be exactly 15 alphanumeric characters")
        return val

    # Validator for email: ensures the email matches a valid pattern
    @field_validator("email")
    def validate_email(cls, val):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # Email format pattern
        if not re.match(email_regex, val):  # Match the email format pattern
            raise ValueError("email must be a valid email address")
        return val

    # Validator for city: checks if the city is in the approved list of Indian cities
    @field_validator("city")
    def validate_city(cls, val):
        approved_cities = [
            "Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune", "Ahmedabad", 
            "Jaipur", "Chandigarh", "Surat", "Lucknow", "Indore", "Vadodara", "Nagpur", "Patna", 
            "Bhopal", "Coimbatore", "Agra", "Nashik", "Visakhapatnam", "Guwahati", "Madurai", 
            "Vijayawada", "Ludhiana", "Jammu", "Aurangabad", "Dhanbad", "Goa", "Rajkot"
        ]
        if val not in approved_cities:  # Check if city is in the approved list
            raise ValueError(f"city must be one of the approved cities: {', '.join(approved_cities)}")
        return val

    # Validator for active_status: ensures it's either 'Active' or 'Inactive'
    @field_validator("active_status")
    def validate_active_status(cls, val):
        if val not in ["Active", "Inactive"]:  # Ensure valid status
            raise ValueError("active_status must be either 'Active' or 'Inactive'")
        return val
