from pydantic import BaseModel
from typing import Optional

class AssetCreate(BaseModel):
    asset_tag: str
    asset_type: str
    serial_number: str
    manufacturer: str
    model: str
    purchase_date: str
    warranty_years: int
    condition_status: str
    assigned_to: Optional[str] = None
    location: str
    asset_status: str


class AssetUpdate(BaseModel):
    asset_type: str
    manufacturer: str
    model: str
    purchase_date: str
    warranty_years: int
    condition_status: str
    assigned_to: Optional[str] = None
    location: str
    asset_status: str


class AssetStatusUpdate(BaseModel):
    asset_status: str
