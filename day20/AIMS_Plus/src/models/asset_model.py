from pydantic import BaseModel, Field, model_validator
from datetime import date
from typing import Optional, Literal

class StatusValidate(BaseModel):  # Validate allowed asset status values
    asset_status: Literal['Available', 'Assigned', 'Repair', 'Retired']

class AssetInventory(BaseModel):  # Asset inventory schema with validation rules
    asset_tag: str = Field(..., pattern=r"^UST-[A-Za-z0-9-]+$")  # Must start with UST- and contain letters/numbers/hyphen
    asset_type: Literal['Laptop', 'Monitor', 'Keyboard', 'Mouse']  # Restrict asset type
    serial_number: str  # Serial number string
    manufacturer: Literal['Dell', 'HP', 'Lenovo', 'Samsung', 'LG']  # Restrict manufacturer
    model: str  # Model name
    purchase_date: date  # Purchase date
    warranty_years: int = Field(..., ge=1, le=5)  # Warranty years between 1 and 5
    condition_status: Literal['New', 'Good', 'Used', 'Damaged']  # Restrict condition status
    assigned_to: Optional[str] = None  # Optional assigned employee
    location: Literal['TVM', 'Trivandrum', 'Bangalore', 'Chennai', 'Hyderabad']  # Restrict location
    asset_status: Literal['Available', 'Assigned', 'Repair', 'Retired']  # Restrict asset status

    @model_validator(mode="after")
    def validate_purchase_date(self):  # Ensure purchase_date is not in the future
        if self.purchase_date > date.today():
            raise ValueError("purchase_date cannot be in the future")
        return self