from pydantic import BaseModel,Field,model_validator
from datetime import date
from typing import Optional,Literal

class StatusValidate(BaseModel):
    asset_status: Literal['Available', 'Assigned', 'Repair', 'Retired']

class AssetInventory(BaseModel):
    asset_tag: str = Field(..., pattern=r"^UST-[A-Za-z0-9-]+$")
    asset_type: Literal['Laptop', 'Monitor', 'Keyboard', 'Mouse']
    serial_number: str
    manufacturer: Literal['Dell', 'HP', 'Lenovo', 'Samsung','LG']
    model: str
    purchase_date: date
    warranty_years: int = Field(..., ge=1, le=5)
    condition_status: Literal['New', 'Good', 'Used', 'Damaged']
    assigned_to: Optional[str] = None
    location: Literal['TVM','Trivandrum','Bangalore', 'Chennai', 'Hyderabad']
    asset_status: Literal['Available', 'Assigned', 'Repair', 'Retired']

    @model_validator(mode="after")
    def validate_purchase_date(self):
        if self.purchase_date > date.today():
            raise ValueError("purchase_date cannot be in the future")
        return self

