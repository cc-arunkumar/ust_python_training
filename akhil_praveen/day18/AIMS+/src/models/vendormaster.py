from pydantic import BaseModel, Field, EmailStr  # Pydantic BaseModel for validation, Field for constraints, EmailStr for email validation
from typing import Literal  # Literal allows restricting a field to specific values

# Model to validate the status of a vendor
class StatusValidate(BaseModel):
    active_status: Literal['Active', 'Inactive']  # Only 'Active' or 'Inactive' are allowed

# Main VendorMaster model representing the vendor entity
class VendorMaster(BaseModel):
    # Vendor name must consist of letters and spaces only
    vendor_name: str = Field(..., pattern=r"^[A-Za-z ]+$")
    
    # Contact person name must consist of letters and spaces only
    contact_person: str = Field(..., pattern=r"^[A-Za-z ]+$")
    
    # Phone number must be 10 digits starting with 6-9
    contact_phone: str = Field(..., pattern=r"^[6-9][0-9]{9}$")
    
    # GST number must be exactly 15 characters
    gst_number: str = Field(..., min_length=15, max_length=15)
    
    # Email must be a valid email string
    email: EmailStr
    
    # Address is a free text field
    address: str
    
    # City must be one of the predefined options
    city: str = Literal[
        "Delhi", "Mumbai", "Bengaluru", "Chennai", "Hyderabad", "Kolkata",
        "Pune", "Ahmedabad", "Surat", "Jaipur", "Lucknow", "Kanpur",
        "Nagpur", "Indore", "Bhopal", "Patna", "Ranchi", "Chandigarh",
        "Thiruvananthapuram", "Kochi", "Coimbatore", "Madurai", "Visakhapatnam",
        "Vijayawada", "Mysuru", "Guwahati", "Shillong", "Gangtok", "Imphal"
    ]
    
    # Vendor active status must be either 'Active' or 'Inactive'
    active_status: Literal['Active', 'Inactive']
