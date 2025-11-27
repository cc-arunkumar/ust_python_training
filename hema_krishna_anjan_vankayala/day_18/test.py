from pydantic import BaseModel, Field, field_validator
from datetime import date, datetime
import re

class AssetInventory(BaseModel):
    asset_id: int = Field(...)
    asset_tag: str = Field(...)  # Matches UST-LTP-XXXX format
    asset_type: str  # To be validated as Laptop/Monitor/Keyboard/Mouse etc.
    serial_number: str
    manufacturer: str
    model: str
    purchase_date: date
    warranty_years: int
    condition_status: str
    assigned_to: str = None
    location: str
    asset_status: str
    last_updated: datetime

    


valid_data = {
    "asset_id": 1,
    "asset_tag": "UST-LTP-0001",
    "asset_type": "Laptop",
    "serial_number": "SN12345ABC",
    "manufacturer": "Dell",
    "model": "XPS 13",
    "purchase_date": "2023-01-01",
    "warranty_years": 2,
    "condition_status": "New",
    "assigned_to": "John Doe",
    "location": "Bangalore",
    "asset_status": "Available",
    "last_updated": datetime.now()
}

print(AssetInventory(**valid_data))