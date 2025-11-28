from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional

class AssetInventory(BaseModel):
    # Core asset fields
    asset_id: int = Field(...)
    asset_tag: str = Field(..., pattern=r'^UST-')  # Must start with UST-
    asset_type: str = Field(..., min_length=1)     # Laptop/Monitor/Keyboard/Mouse
    serial_number: str = Field(..., min_length=1)
    manufacturer: str = Field(..., min_length=1)   # Dell/HP/Lenovo/Samsung/LG
    model: str = Field(..., min_length=1)
    purchase_date: date = Field(...)               # Cannot be in the future
    warranty_years: int = Field(...)               # Must be between 1–5
    condition_status: str = Field(..., min_length=1)  # New/Good/Used/Damaged/Fair
    assigned_to: Optional[str] = None
    location: str = Field(..., min_length=1)       # Trivandrum/Bangalore/Chennai/Hyderabad
    asset_status: str = Field(..., min_length=1)   # Available/Assigned/Repair/Retired
    last_updated: datetime = datetime.now()

    # Validation methods
    def validate_asset_type(self):
        valid_types = ['Laptop', 'Monitor', 'Keyboard', 'Mouse']
        if self.asset_type not in valid_types:
            raise ValueError(f"Invalid asset type: {self.asset_type}, must be one of {valid_types}")

    def validate_manufacturer(self):
        valid_types = ['Dell', 'HP', 'Lenovo', 'Samsung', 'LG']
        if self.manufacturer not in valid_types:
            raise ValueError(f"Invalid manufacturer: {self.manufacturer}, must be one of {valid_types}")

    def validation_purchasedate(self):
        if self.purchase_date > date.today():
            raise ValueError("Purchase Date cannot be in the future")

    def validation_warranty(self):
        if not (1 <= self.warranty_years <= 5):
            raise ValueError("Warranty must be between 1 and 5 years")

    def validation_condition_status(self):
        if self.condition_status not in ['New', 'Good', 'Used', 'Damaged', 'Fair']:
            raise ValueError("Invalid Condition Status")

    def validation_location(self):
        if self.location not in ['Trivandrum', 'Bangalore', 'Chennai', 'Hyderabad']:
            raise ValueError("Invalid Location")

    def validation_asset_status(self):
        if self.asset_status not in ['Available', 'Assigned', 'Repair', 'Retired']:
            raise ValueError("Invalid Asset Status")

    # Run validations on initialization
    def __init__(self, **data):
        super().__init__(**data)
        self.validate_asset_type()
        self.validate_manufacturer()
        self.validation_purchasedate()
        self.validation_warranty()
        self.validation_condition_status()
        self.validation_location()
        self.validation_asset_status()
