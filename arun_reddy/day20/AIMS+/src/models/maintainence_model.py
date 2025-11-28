from decimal import Decimal, ROUND_DOWN
from pydantic import BaseModel, Field
from datetime import date
from ..exceptions.custom_exceptions import InvalidInputException,ValidationErrorException

# Pydantic model for Maintenance records
class Maintenence(BaseModel):
    # Asset tag must start with "UST-"
    asset_tag: str = Field(..., pattern=r"^UST-")
    # Type of maintenance (Repair, Service, Upgrade)
    maintenance_type: str
    # Vendor name must contain only alphabets and spaces, max length 100
    vendor_name: str = Field(..., pattern=r"^[A-Za-z ]+$", max_length=100)
    # Description must be between 10 and 200 characters
    description: str = Field(..., min_length=10, max_length=200)
    # Cost must be greater than 0
    cost: float = Field(..., gt=0)
    # Maintenance date cannot be in the future
    maintenance_date: date
    # Technician name must contain only alphabets and spaces, max length 100
    technician_name: str = Field(..., pattern=r"^[A-Za-z ]+$", max_length=100)
    # Status must be either Completed or Pending
    status: str

    # Validate maintenance type against allowed values
    def validate_maintainence_type(self):
        if self.maintenance_type not in ["Repair", "Service", "Upgrade"]:
            raise InvalidInputException("Invalid maintainence type")
     
    # Validate maintenance date is not in the future
    def validate_maintainence_date(self):
        if self.maintenance_date > date.today():
            raise ValidationErrorException("Invalid Date: cannot be in the future")

    # Validate status against allowed values
    def validate_status(self):
        if self.status not in ["Completed", "Pending"]:
            raise InvalidInputException("Invalid Status")
        
    # Run all custom validations after initialization
    def __init__(self, **data):
        super().__init__(**data)
        self.validate_maintainence_date()
        self.validate_maintainence_type()
        self.validate_status()
