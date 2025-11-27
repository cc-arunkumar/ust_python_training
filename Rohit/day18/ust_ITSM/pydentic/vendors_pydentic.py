from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from enum import Enum

# Approved cities
class City(str, Enum):
    Mumbai = "Mumbai"
    Delhi = "Delhi"
    Bangalore = "Bangalore"
    Chennai = "Chennai"
    Hyderabad = "Hyderabad"   # fixed typo
    Pune = "Pune"
    Kolkata = "Kolkata"

class Activity(str, Enum):
    Active = "Active"
    Inactive = "Inactive"

class VendorMaster(BaseModel):
    vendor_id:int=0

    vendor_name: str = Field(
        ..., 
        max_length=100, 
        pattern=r"^[A-Za-z ]+$", 
        description="String, max 100 chars, alphabets and spaces only"
    )

    contact_person: str = Field(
        ..., 
        max_length=100, 
        pattern=r"^[A-Za-z ]+$", 
        description="String, max 100 chars, alphabets only"
    )

    contact_phone: str = Field(
        ..., 
        pattern=r"^[6789]\d{9}$", 
        description="Valid Indian mobile number (10 digits, starts with 6/7/8/9)"
    )

    gst_number: str = Field(
        ..., 
        pattern=r"^[A-Za-z0-9]{15}$", 
        description="Exactly 15 alphanumeric characters (GSTIN format)"
    )

    email: str = Field(
        ..., 
        pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', 
        description="Valid email format"
    )

    address: str = Field(
        ..., 
        max_length=200, 
        description="String, max 200 characters"
    )

    city: City = Field(..., description="Valid Indian city from approved list")

    activity_status: Activity = Field(..., description="Active or Inactive")
