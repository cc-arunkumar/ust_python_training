from pydantic import BaseModel, Field, EmailStr
from typing import Literal


class StatusValidate(BaseModel):
    """
    Model used to validate vendor active status updates.

    Attributes:
        active_status (Literal): Must be one of the predefined status values:
            - 'Active'
            - 'Inactive'
    """
    active_status: Literal['Active', 'Inactive']


class VendorMaster(BaseModel):
    """
    Model representing a vendor in the system.

    Attributes:
        vendor_name (str): Name of the vendor. Must contain only alphabets and spaces.
        contact_person (str): Name of the primary contact person. Must contain only alphabets and spaces.
        contact_phone (str): Contact phone number. Must start with digits 6–9 and be exactly 10 digits long.
        gst_number (str): GST number of the vendor. Must be exactly 15 characters long.
        email (EmailStr): Vendor's email address. Must be a valid email format.
        address (str): Full address of the vendor.
        city (Literal): City where the vendor is located. Must be one of the predefined major Indian cities.
        active_status (Literal): Current active status of the vendor. Allowed values: 'Active', 'Inactive'.
    """

    vendor_name: str = Field(..., pattern=r"^[A-Za-z ]+$")  # Vendor name must contain only letters and spaces
    contact_person: str = Field(..., pattern=r"^[A-Za-z ]+$")  # Contact person name must contain only letters and spaces
    contact_phone: str = Field(..., pattern=r"^[6-9][0-9]{9}$")  # Validates Indian mobile number format
    gst_number: str = Field(..., min_length=15, max_length=15)  # GST number must be exactly 15 characters
    email: EmailStr
    address: str
    city: str = Literal[
        "Delhi", "Mumbai", "Bengaluru", "Chennai", "Hyderabad", "Kolkata",
        "Pune", "Ahmedabad", "Surat", "Jaipur", "Lucknow", "Kanpur",
        "Nagpur", "Indore", "Bhopal", "Patna", "Ranchi", "Chandigarh",
        "Thiruvananthapuram", "Kochi", "Coimbatore", "Madurai", "Visakhapatnam",
        "Vijayawada", "Mysuru", "Guwahati", "Shillong", "Gangtok", "Imphal"
    ]
    active_status: Literal['Active', 'Inactive']