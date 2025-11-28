from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import date

class AssetInventory(BaseModel):
    # Unique identifier for the asset, must start with "UST-" followed by alphanumeric or hyphen
    asset_tag: str = Field(..., pattern=r"^UST-[A-Za-z0-9-]+$")
    # Type of asset, restricted to specific categories
    asset_type: Literal['Laptop', 'Monitor', 'Keyboard', 'Mouse']
    # Manufacturer-provided serial number for the asset
    serial_number: str
    # Manufacturer name, restricted to specific vendors
    manufacturer: Literal['Dell', 'HP', 'Lenovo', 'Samsung', 'LG']
    model: str
    purchase_date: date
    # Warranty period in years, must be between 1 and 5
    warranty_years: int = Field(..., ge=1, le=5)
    # Current condition of the asset
    condition_status: Literal['New', 'Good', 'Used', 'Damaged']
    # Name of the employee the asset is assigned to (optional)
    assigned_to: Optional[str] = None
    # Physical location of the asset, restricted to specific office locations
    location: Literal['TVM', 'Trivandrum', 'Bangalore', 'Chennai', 'Hyderabad']
    # Current status of the asset in inventory
    asset_status: Literal['Available', 'Assigned', 'Repair', 'Retired']

    # Custom validation method to ensure purchase_date is not set in the future
    def validate_purchase_date(self):
        if self.purchase_date > date.today():
            raise ValueError("purchase_date cannot be in the future")
        return self
