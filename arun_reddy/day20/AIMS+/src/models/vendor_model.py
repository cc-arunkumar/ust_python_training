from pydantic import BaseModel, Field, EmailStr
from ..exceptions.custom_exceptions import InvalidInputException,ValidationErrorException

# List of valid cities for vendor location
valid_cities = ["pune", "chennai", "mumbai", "kolkata", "hyderabad","trivandram","bangalore"]

class Vendor(BaseModel):
    # Vendor unique ID
    vendor_id: int
    # Vendor name must contain only alphabets and spaces, max length 100
    vendor_name: str = Field(..., max_length=100, pattern=r"^[A-Za-z ]+$")
    # Contact person name must contain only alphabets and spaces, max length 100
    contact_person: str = Field(..., max_length=100, pattern=r"^[A-Za-z ]+$")
    # Contact phone must be a valid 10-digit number starting with 6–9
    contact_phone: str = Field(..., pattern=r"^[6-9][0-9]{9}$")
    # GST number must be exactly 15 alphanumeric characters
    gst_number: str = Field(..., pattern=r"^[A-Za-z0-9]{15}$")
    # Email must be valid format
    email: EmailStr
    # Address with maximum length of 200 characters
    address: str = Field(..., max_length=200)
    # City must be one of the valid cities
    city: str
    # Active status must be either Active or Inactive
    active_status: str
    
    # Custom initialization to run validations after Pydantic checks
    def __init__(self,**data):
        super().__init__(**data)
        self.validate_active_status()
        self.validate_city()
        self.validate_phone_number()
        
    # Validate phone number length (must be exactly 10 digits)
    def validate_phone_number(self):
        if len(self.contact_phone)!=10:
            raise ValidationErrorException("Invalid contact")
    
    # Validate active status against allowed values
    def validate_active_status(self):
        if self.active_status not in ["Active", "Inactive"]:
            raise InvalidInputException("Invalid active_status, must be 'Active' or 'Inactive'")
      
    # Validate city against predefined list of valid cities
    def validate_city(self):
        if self.city.lower() not in valid_cities:
            raise InvalidInputException(f"City '{self.city}' is not in the approved list")
