from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional
from ..exceptions.custom_exceptions import ValidationErrorException,InvalidInputException
import re

# Allowed lists for validation
predefined_types = {"Laptop", "Monitor", "Keyboard", "Mouse"}   # Valid asset types
manufacturerlist = {"Dell", "HP", "Lenovo", "Samsung", "LG"}    # Valid manufacturers
allowed_conditions = {"New", "Good", "Used", "Damaged"}         # Valid condition statuses
approved_locations = {"Trivandrum", "Bangalore", "Hyderabad", "Chennai"}  # Valid office locations
allowed_status = {"Available", "Assigned", "Repair", "Retired"} # Valid asset statuses

class AssetInventory(BaseModel):
    # Asset fields with validation rules
    asset_tag: str = Field(..., pattern=r"^UST-")   # Must start with "UST-"
    asset_type: str
    serial_number: str
    manufacturer: str
    model: str
    purchase_date: date
    warranty_years: int
    condition_status: str
    assigned_to: str | None = None   # Optional field
    location: str
    asset_status: str
    last_updated: Optional[str]      # Optional field

    def __init__(self, **data):
        super().__init__(**data)   
        # Run custom validation methods after initialization
        self.validate_asset_type()
        self.validate_serial_number()
        self.validate_manufacturer()
        self.validate_model()
        self.validate_purchase_date()
        self.validate_warranty_years()
        self.validate_condition_status()
        self.validate_assigned_to()
        self.validate_location()
        self.validate_asset_status()

    # Validate asset type against predefined list
    def validate_asset_type(self):
        if self.asset_type not in predefined_types:
            raise InvalidInputException(f"Invalid asset_type: {self.asset_type}")

    # Validate serial number format (alphanumeric + hyphen allowed)
    def validate_serial_number(self):
        if not re.match(r"^[A-Za-z0-9-]+$", self.serial_number):
            raise ValidationErrorException(f"Invalid serial_number: {self.serial_number}")

    # Validate manufacturer against allowed list
    def validate_manufacturer(self):
        if self.manufacturer not in manufacturerlist:
            raise InvalidInputException(f"Invalid manufacturer: {self.manufacturer}")

    # Validate model is not empty
    def validate_model(self):
        if not self.model.strip():
            raise InvalidInputException("Model cannot be empty")

    # Validate purchase date is not in the future
    def validate_purchase_date(self):
        if self.purchase_date > datetime.today().date():
            raise ValidationErrorException("Purchase date cannot be in the future")

    # Validate warranty years between 1 and 5
    def validate_warranty_years(self):
        if not (1 <= self.warranty_years <= 5):
            raise ValidationErrorException("Warranty years must be between 1 and 5")

    # Validate condition status against allowed list
    def validate_condition_status(self):
        if self.condition_status not in allowed_conditions:
            raise InvalidInputException(f"Invalid condition_status: {self.condition_status}")

    # Validate assigned_to field (must be at least 2 characters if provided)
    def validate_assigned_to(self):
        if self.assigned_to and len(self.assigned_to.strip()) < 2:
            raise InvalidInputException("Assigned_to must be a valid name")

    # Validate location against approved list
    def validate_location(self):
        if self.location not in approved_locations:
            raise InvalidInputException(f"Invalid location: {self.location}")

    # Validate asset status against allowed list
    def validate_asset_status(self):
        if self.asset_status not in allowed_status:
            raise InvalidInputException(f"Invalid asset_status: {self.asset_status}")
