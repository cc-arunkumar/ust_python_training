import csv
import re
from datetime import datetime
from pydantic import BaseModel, field_validator, ValidationError
import os

# Define custom exceptions for handling validation errors
class ValidationErrorException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Predefined valid values for 'active_status' and 'city' fields
valid_active_statuses = ['Active', 'Inactive']
valid_cities = ['Bangalore', 'Kolkata', 'Chennai', 'Mumbai', 'Hyderabad', 'Delhi']

# Pydantic Model for Vendor to validate vendor data
class Vendor(BaseModel):
    vendor_id: str
    vendor_name: str
    contact_person: str
    contact_phone: str
    gst_number: str
    email: str
    address: str
    city: str
    active_status: str

    # Field Validators for each field to ensure data validity

    # Validator for 'vendor_id' to check for duplicates
    @field_validator('vendor_id')
    def validate_vendor_id(cls, v):
        vendor_ids = getattr(cls, 'vendor_ids', set())  # Use a class-level variable to track vendor_ids
        if v in vendor_ids:  # Check if vendor_id is already in the set
            raise ValueError(f"Duplicate vendor_id: {v}")
        vendor_ids.add(v)  # Add new vendor_id to the set
        cls.vendor_ids = vendor_ids  # Store the updated set of vendor_ids
        return v

    # Validator for 'vendor_name' to ensure it's not empty and only contains letters and spaces
    @field_validator('vendor_name')
    def validate_vendor_name(cls, v):
        if v is None or v.strip() == "":  # Check if vendor_name is empty
            raise ValueError("Vendor name cannot be empty")
        if not re.match(r"^[A-Za-z\s]+$", v):  # Ensure vendor_name contains only letters and spaces
            raise ValueError(f"Invalid vendor_name: {v}")
        return v

    # Validator for 'contact_person' to ensure it's not empty and only contains letters and spaces
    @field_validator('contact_person')
    def validate_contact_person(cls, v):
        if v is None or v.strip() == "":  # Check if contact_person is empty
            raise ValueError("Contact person cannot be empty")
        if not re.match(r"^[A-Za-z\s]+$", v):  # Ensure contact_person contains only letters and spaces
            raise ValueError(f"Invalid contact_person: {v}")
        return v

    # Validator for 'contact_phone' to ensure it's a valid 10-digit phone number starting with 6-9
    @field_validator('contact_phone')
    def validate_contact_phone(cls, v):
        if v is None or v.strip() == "":  # Check if contact_phone is empty
            raise ValueError("Contact phone cannot be empty")
        v = str(v)  # Convert to string for validation
        if not re.match(r"^[6-9]\d{9}$", v):  # Ensure contact_phone is a valid 10-digit number
            raise ValueError(f"Invalid contact_phone: {v}")
        return v

    # Validator for 'gst_number' to ensure it matches the GST format (15 alphanumeric characters)
    @field_validator('gst_number')
    def validate_gst_number(cls, v):
        if v is None or v.strip() == "":  # Check if gst_number is empty
            raise ValueError("GST number cannot be empty")
        pattern = r"^[A-Z0-9]{15}$"  # GST number format
        if not re.match(pattern, v):  # Ensure gst_number matches the pattern
            raise ValueError(f"Invalid gst_number: {v}")
        return v

    # Validator for 'email' to ensure it matches a standard email format
    @field_validator('email')
    def validate_email(cls, v):
        if v is None or v.strip() == "":  # Check if email is empty
            raise ValueError("Email cannot be empty")
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", v):  # Ensure email format is valid
            raise ValueError(f"Invalid email: {v}")
        return v

    # Validator for 'address' to ensure it is not empty
    @field_validator('address')
    def validate_address(cls, v):
        if v is None or v.strip() == "":  # Check if address is empty
            raise ValueError("Address cannot be empty")
        return v

    # Validator for 'city' to ensure it is in the predefined list of valid cities
    @field_validator('city')
    def validate_city(cls, v):
        if v is None or v.strip() == "":  # Check if city is empty
            raise ValueError("City cannot be empty")
        if v not in valid_cities:  # Check if city is in the predefined valid cities list
            raise ValueError(f"Invalid city: {v}")
        return v

    # Validator for 'active_status' to ensure it is either 'Active' or 'Inactive'
    @field_validator('active_status')
    def validate_active_status(cls, v):
        if v is None or v.strip() == "":  # Check if active_status is empty
            raise ValueError("Active status cannot be empty")
        if v not in valid_active_statuses:  # Check if active_status is valid
            raise ValueError(f"Invalid active_status: {v}")
        return v
