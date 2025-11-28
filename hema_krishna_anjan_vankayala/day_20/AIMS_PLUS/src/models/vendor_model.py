from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class VendorMaster(BaseModel):
    # Core vendor fields
    vendor_id: int
    vendor_name: str = Field(..., max_length=100, pattern=r"^[A-Za-z ]+$")   # Alphabets only
    contact_person: str = Field(..., max_length=100, pattern=r"^[A-Za-z ]+$") # Alphabets only
    contact_phone: str = Field(..., pattern=r"^[6-9]\d{9}$")                  # Valid Indian mobile number
    gst_number: str = Field(..., min_length=15, max_length=15, pattern=r"^[A-Za-z0-9]{15}$") # GST format
    email: EmailStr                                                           # Valid email
    address: Optional[str] = Field(None, max_length=200)                      # Optional address
    city: str                                                                 # Must be approved city
    active_status: str                                                        # Active/Inactive

    # Validate city against approved list
    def validate_city(self):
        approved = [
            "Trivandrum",
            "Bangalore",
            "Chennai",
            "Hyderabad",
            "Mumbai",
            "Pune",
            "Kolkata"
        ]
        if self.city not in approved:
            raise ValueError(f"Invalid city: {self.city}. Must be one of {approved}")

    # Validate active status
    def validate_active_status(self):
        if self.active_status not in ["Active", "Inactive"]:
            raise ValueError("active_status must be either 'Active' or 'Inactive'")

    # Run validations on initialization
    def __init__(self, **data):
        super().__init__(**data)
        self.validate_city()
        self.validate_active_status()
