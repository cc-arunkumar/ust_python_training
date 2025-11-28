from pydantic import BaseModel, Field  # Import Pydantic BaseModel and Field for validation and metadata
from uuid import UUID, uuid4          # Import UUID utilities (not used here, but useful for unique IDs)
from enum import Enum                 # Import Enum to define fixed sets of values

# -----------------------------
# ENUM CLASSES (fixed choices)
# -----------------------------

# Approved cities for vendor location
class City(str, Enum):  
    Mumbai = "Mumbai"        # Allowed city: Mumbai
    Delhi = "Delhi"          # Allowed city: Delhi
    Bangalore = "Bangalore"  # Allowed city: Bangalore
    Chennai = "Chennai"      # Allowed city: Chennai
    Hyderabad = "Hyderabad"  # Allowed city: Hyderabad
    Pune = "Pune"            # Allowed city: Pune
    Kolkata = "Kolkata"      # Allowed city: Kolkata

# Activity status for vendor
class Activity(str, Enum):  
    Active = "Active"        # Vendor is active
    Inactive = "Inactive"    # Vendor is inactive

# -----------------------------
# MAIN Pydantic MODEL
# -----------------------------
class VendorMaster(BaseModel):  # Define VendorMaster model using Pydantic BaseModel
    vendor_id: int = 0  # Vendor ID, default value = 0 (can be auto-incremented in DB)

    # Vendor name: required, max 100 chars, alphabets and spaces only
    vendor_name: str = Field(
        ...,  # Required field
        max_length=100,  # Maximum length = 100 characters
        pattern=r"^[A-Za-z ]+$",  # Regex: only alphabets and spaces allowed
        description="String, max 100 chars, alphabets and spaces only"  # Field description
    )

    # Contact person: required, max 100 chars, alphabets only
    contact_person: str = Field(
        ...,  # Required field
        max_length=100,  # Maximum length = 100 characters
        pattern=r"^[A-Za-z ]+$",  # Regex: only alphabets allowed
        description="String, max 100 chars, alphabets only"  # Field description
    )

    # Contact phone: required, must be valid Indian mobile number
    contact_phone: str = Field(
        ...,  # Required field
        pattern=r"^[6789]\d{9}$",  # Regex: must be 10 digits starting with 6/7/8/9
        description="Valid Indian mobile number (10 digits, starts with 6/7/8/9)"  # Field description
    )

    # GST number: required, must be exactly 15 alphanumeric characters
    gst_number: str = Field(
        ...,  # Required field
        pattern=r"^[A-Za-z0-9]{15}$",  # Regex: exactly 15 alphanumeric characters
        description="Exactly 15 alphanumeric characters (GSTIN format)"  # Field description
    )

    # Email: required, must follow valid email format
    email: str = Field(
        ...,  # Required field
        pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',  # Regex: standard email format
        description="Valid email format"  # Field description
    )

    # Address: required, max 200 characters
    address: str = Field(
        ...,  # Required field
        max_length=200,  # Maximum length = 200 characters
        description="String, max 200 characters"  # Field description
    )

    # City: required, must be one of approved cities from City Enum
    city: City = Field(..., description="Valid Indian city from approved list")

    # Activity status: required, must be Active or Inactive from Activity Enum
    activity_status: Activity = Field(..., description="Active or Inactive")
