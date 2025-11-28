from pydantic import BaseModel, Field, field_validator  # Importing Pydantic features for model creation and validation
from typing import Optional  # Importing Optional to denote optional fields
import re  # Importing regular expression module for pattern matching

# VendorModel class defines the structure and validation logic for vendor records
class VendorModel(BaseModel):
    # vendor_id is an optional field, with a default value of 0 if not provided
    vendor_id: Optional[int] = 0
    
    # vendor_name is a required string field with a max length of 100 characters. 
    # It must not contain digits.
    vendor_name: str = Field(..., max_length=100, description="Vendor name (no digits allowed)")

    # contact_person is a required string field with a max length of 100 characters. 
    # It must only contain alphabets and spaces (no digits or special characters).
    contact_person: str = Field(..., max_length=100, description="Alphabets only, no numbers or special characters")

    # contact_phone is a required string field for the phone number. 
    # It must be a valid 10-digit Indian mobile number starting with 6, 7, 8, or 9.
    contact_phone: str = Field(..., max_length=15, description="Valid 10-digit Indian mobile number starting with 6/7/8/9")

    # gst_number is a required string field for GSTIN. It must be exactly 15 alphanumeric characters.
    gst_number: str = Field(..., min_length=15, max_length=15, description="Exactly 15 alphanumeric characters for GSTIN")

    # email is a required string field for the email address.
    # It must match the regular expression for a valid email format (e.g., contact@domain.com).
    email: str = Field(..., description="Valid email format (e.g., contact@domain.com)")

    # address is a required string field for the vendor's address. 
    # No strict validation beyond the length of the field.
    address: str = Field(..., max_length=200, description="Vendor address (no strict validation beyond length)")

    # city is a required string field for the city. It must be one of the approved Indian cities.
    city: str = Field(..., max_length=100, description="Valid Indian city name (must match from approved list)")

    # active_status is a required string field that must be either 'Active' or 'Inactive'.
    active_status: str = Field(..., description="Status must be either 'Active' or 'Inactive'")

    # Validator to ensure vendor_name does not contain digits and contains only alphabets and spaces
    @field_validator("vendor_name")
    def validate_vendor_name(cls, val):
        if any(char.isdigit() for char in val):  # Check if the name contains digits
            raise ValueError("vendor_name must not contain digits")
        if not all(char.isalpha() or char.isspace() for char in val):  # Ensure only alphabets and spaces are present
            raise ValueError("vendor_name must only contain alphabets and spaces")
        return val

    # Validator to ensure contact_person contains only alphabets and spaces
    @field_validator("contact_person")
    def validate_contact_person(cls, val):
        if not all(char.isalpha() or char.isspace() for char in val):  # Ensure only alphabets and spaces
            raise ValueError("contact_person must only contain alphabets and spaces")
        return val

    # Validator to ensure contact_phone is a valid 10-digit Indian mobile number starting with 6/7/8/9
    @field_validator("contact_phone")
    def validate_contact_phone(cls, val):
        if not re.match(r'^[6789]\d{9}$', val):  # Check if the phone number matches the Indian mobile format
            raise ValueError("contact_phone must be a valid 10-digit Indian mobile number starting with 6/7/8/9")
        return val

    # Validator to ensure gst_number is exactly 15 alphanumeric characters
    @field_validator("gst_number")
    def validate_gst_number(cls, val):
        if len(val) != 15 or not val.isalnum():  # Ensure GST number is exactly 15 characters and alphanumeric
            raise ValueError("gst_number must be exactly 15 alphanumeric characters")
        return val

    # Validator to ensure email is in a valid email format
    @field_validator("email")
    def validate_email(cls, val):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # Regular expression for email format
        if not re.match(email_regex, val):  # Check if email matches the regex
            raise ValueError("email must be a valid email address")
        return val

    # Validator to ensure city is one of the approved Indian cities
    @field_validator("city")
    def validate_city(cls, val):
        approved_cities = [
            "Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune", "Ahmedabad", 
            "Jaipur", "Chandigarh", "Surat", "Lucknow", "Indore", "Vadodara", "Nagpur", "Patna", 
            "Bhopal", "Coimbatore", "Agra", "Nashik", "Visakhapatnam", "Guwahati", "Madurai", 
            "Vijayawada", "Ludhiana", "Jammu", "Aurangabad", "Dhanbad", "Goa", "Rajkot"
        ]
        if val not in approved_cities:  # Ensure the city is in the approved list
            raise ValueError(f"city must be one of the approved cities: {', '.join(approved_cities)}")
        return val

    # Validator to ensure active_status is either 'Active' or 'Inactive'
    @field_validator("active_status")
    def validate_active_status(cls, val):
        if val not in ["Active", "Inactive"]:  # Ensure the status is either 'Active' or 'Inactive'
            raise ValueError("active_status must be either 'Active' or 'Inactive'")
        return val