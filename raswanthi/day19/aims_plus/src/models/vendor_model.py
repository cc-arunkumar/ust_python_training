from pydantic import BaseModel, Field, EmailStr
from typing import Literal

class VendorModel(BaseModel):
    # Vendor name must contain only alphabets and spaces
    vendor_name: str = Field(..., pattern=r"^[A-Za-z ]+$")

    # Contact person name must contain only alphabets and spaces
    contact_person: str = Field(..., pattern=r"^[A-Za-z ]+$")

    # Contact phone must be a 10-digit number starting with 6–9
    contact_phone: str = Field(..., pattern=r"^[6-9][0-9]{9}$")

    # GST number must be exactly 15 characters long
    gst_number: str = Field(..., min_length=15, max_length=15)

    # Email must be a valid email format (Pydantic’s EmailStr enforces this)
    email: EmailStr

    # Full address of the vendor
    address: str

    # City must be one of the predefined allowed values
    city: str = Literal[
        "Delhi", "Mumbai", "Bengaluru", "Chennai", "Hyderabad", "Kolkata",
        "Pune", "Ahmedabad", "Surat", "Jaipur", "Lucknow", "Kanpur",
        "Nagpur", "Indore", "Bhopal", "Patna", "Ranchi", "Chandigarh",
        "Thiruvananthapuram", "Kochi", "Coimbatore", "Madurai", "Visakhapatnam",
        "Vijayawada", "Mysuru", "Guwahati", "Shillong", "Gangtok", "Imphal"
    ]

    # Vendor status must be either 'Active' or 'Inactive'
    active_status: Literal['Active', 'Inactive']
