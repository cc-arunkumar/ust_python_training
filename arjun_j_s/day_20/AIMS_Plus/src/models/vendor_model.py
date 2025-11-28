from pydantic import BaseModel, Field, EmailStr
from typing import Literal

class StatusValidator(BaseModel):  # Validate allowed vendor status values
    active_status: Literal['Active', 'Inactive']

class VendorMaster(BaseModel):  # Vendor master schema with validation rules
    vendor_name: str = Field(..., pattern=r"^[A-Za-z ]+$")  # Vendor name must contain only letters/spaces
    contact_person: str = Field(..., pattern=r"^[A-Za-z ]+$")  # Contact person must contain only letters/spaces
    contact_phone: str = Field(..., pattern=r"^[6-9][0-9]{9}$")  # Phone must be a valid 10-digit Indian mobile number
    gst_number: str = Field(..., min_length=15, max_length=15)  # GST number must be exactly 15 characters
    email: EmailStr  # Valid email format
    address: str  # Vendor address
    city: str = Literal[  # Restrict city values to predefined list
        "Delhi", "Mumbai", "Bengaluru", "Chennai", "Hyderabad", "Kolkata",
        "Pune", "Ahmedabad", "Surat", "Jaipur", "Lucknow", "Kanpur",
        "Nagpur", "Indore", "Bhopal", "Patna", "Ranchi", "Chandigarh",
        "Thiruvananthapuram", "Kochi", "Coimbatore", "Madurai", "Visakhapatnam",
        "Vijayawada", "Mysuru", "Guwahati", "Shillong", "Gangtok", "Imphal"
    ]
    active_status: Literal['Active', 'Inactive']  # Restrict active status values