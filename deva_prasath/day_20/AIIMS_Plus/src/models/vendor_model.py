from pydantic import BaseModel, Field, field_validator  # Import Pydantic for data validation
from typing import ClassVar, List  # Import typing components for type hinting
import re  # Import regex for pattern matching
import mysql.connector  # MySQL connector (though not used in this script)
import csv  # Import csv module for reading and writing CSV files
from ..exceptions.custom_exceptions import ValidationErrorException


# VendorCreate model to validate vendor data
class VendorCreate(BaseModel):
    # Class variables for allowed values for cities and status
    allowed_cities: ClassVar[List[str]] = ["TVM", "Banglore", "Chennai", "Hyderabad"]
    allowed_status: ClassVar[List[str]] = ["Active", "Inactive"]

    # Vendor attributes to validate
    vendor_name: str = Field(..., max_length=100)
    contact_person: str = Field(..., max_length=100)
    contact_phone: str = Field(..., min_length=10, max_length=10)
    gst_number: str = Field(..., min_length=15, max_length=15)
    email: str
    address: str = Field(..., max_length=200)
    city: str
    active_status: str

    # Validators for various fields
    @field_validator("vendor_name")
    def validate_name(cls, v):
        if not v.replace(" ", "").isalpha():  # vendor_name must contain only alphabets and spaces
            raise ValidationErrorException("vendor_name must contain only alphabets and spaces")
        return v

    @field_validator("contact_person")
    def validate_contact(cls, v):
        if not v.replace(" ", "").isalpha():  # contact_person must contain only alphabets
            raise ValidationErrorException("contact_person must contain only alphabets")
        return v

    @field_validator("contact_phone")
    def validate_phone(cls, v):
        if not v.isdigit() or len(v) != 10:  # contact_phone must be exactly 10 digits
            raise ValidationErrorException("contact_phone must be exactly 10 digits")
        if v[0] not in "6789":  # contact_phone must start with 6, 7, 8, or 9
            raise ValidationErrorException("contact_phone must start with 6, 7, 8, or 9")
        return v

    @field_validator("gst_number")
    def validate_gst_number(cls, v):
        if len(v) != 15 or not v.isalnum():  # gst_number must be exactly 15 alphanumeric characters
            raise ValidationErrorException("gst_number must be exactly 15 alphanumeric characters")
        return v.upper()  # Ensure GST number is in uppercase

    @field_validator("email")
    def validate_email(cls, v):
        pattern = r"^[a-zA-Z0-9.%+-]+@[a-zA-Z0-9,-]+\.[A-Za-z]{2,}$"  # Email regex pattern
        if not re.match(pattern, v):  # Validate email format
            raise ValidationErrorException("Invalid email format")
        return v

    @field_validator("address")
    def validate_address(cls, v):
        if len(v) > 200:  # address cannot exceed 200 characters
            raise ValidationErrorException("address cannot exceed 200 characters")
        return v

    @field_validator("city")
    def validate_city(cls, v):
        if v not in cls.allowed_cities:  # city must be one of the allowed cities
            raise ValidationErrorException(f"city must be one of: {cls.allowed_cities}")
        return v

    @field_validator("active_status")
    def validate_status(cls, v):
        if v not in cls.allowed_status:  # active_status must be one of the allowed statuses
            raise ValidationErrorException(f"active_status must be one of: {cls.allowed_status}")
        return v
