from pydantic import BaseModel, Field, EmailStr
from typing import Literal

# Define the VendorModel class to validate vendor-related information
class VendorModel(BaseModel):
    # Vendor name should contain only alphabets and spaces (pattern: A-Z, a-z, spaces)
    vendor_name: str = Field(..., pattern=r"^[A-Za-z ]+$")
    
    # Contact person name should contain only alphabets and spaces (pattern: A-Z, a-z, spaces)
    contact_person: str = Field(..., pattern=r"^[A-Za-z ]+$")
    
    # Contact phone must be a valid Indian 10-digit mobile number, starting with 6, 7, 8, or 9
    contact_phone: str = Field(..., pattern=r"^[6-9][0-9]{9}$")
    
    # GST number must be exactly 15 characters long
    gst_number: str = Field(..., min_length=15, max_length=15)
    
    # Email must be a valid email address as per the EmailStr type in Pydantic
    email: EmailStr
    
    # Address field without additional validation, as it's free-text input
    address: str
    
    # City must be one of the predefined cities listed as valid options using Literal
    city: str = Literal[
        "Delhi", "Mumbai", "Bengaluru", "Chennai", "Hyderabad", "Kolkata",
        "Pune", "Ahmedabad", "Surat", "Jaipur", "Lucknow", "Kanpur",
        "Nagpur", "Indore", "Bhopal", "Patna", "Ranchi", "Chandigarh",
        "Thiruvananthapuram", "Kochi", "Coimbatore", "Madurai", "Visakhapatnam",
        "Vijayawada", "Mysuru", "Guwahati", "Shillong", "Gangtok", "Imphal"
    ]
    
    # Active status must be either 'Active' or 'Inactive'
    active_status: Literal['Active', 'Inactive']

    # Config to set additional validation rules (if needed)
    class Config:
        # Strip leading/trailing whitespace from string fields
        anystr_strip_whitespace = True

