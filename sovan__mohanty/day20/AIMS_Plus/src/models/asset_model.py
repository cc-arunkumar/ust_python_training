from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime
import re
from fastapi import HTTPException

class Asset(BaseModel):
    asset_id: Optional[int] = None
    asset_tag: str = Field(..., max_length=50)
    asset_type: str
    serial_number: str = Field(..., max_length=100)
    manufacturer: str
    model: str
    purchase_date: date
    warranty_years: int
    condition_status: str
    assigned_to: Optional[str] = None
    location: str
    asset_status: str
    last_updated: Optional[datetime] = None

def validate_asset(asset: Asset):
    if not re.match(r"^UST-(LTP|MNT)-\d{4}$", asset.asset_tag):
        raise HTTPException(status_code=422, detail="Invalid asset_tag format")
    if asset.asset_type not in {"Laptop", "Monitor"}:
        raise HTTPException(status_code=422, detail="Invalid asset_type")
    if not re.match(r"^[A-Za-z0-9]+$", asset.serial_number):
        raise HTTPException(status_code=422, detail="Invalid serial_number format")
    if asset.manufacturer not in {"Dell", "HP", "Lenovo", "Samsung"}:
        raise HTTPException(status_code=422, detail="Invalid manufacturer")
    if not asset.model.strip():
        raise HTTPException(status_code=422, detail="Model cannot be blank")
    if asset.purchase_date > date.today():
        raise HTTPException(status_code=422, detail="purchase_date cannot be in the future")
    if asset.warranty_years < 1 or asset.warranty_years > 5:
        raise HTTPException(status_code=422, detail="warranty_years must be between 1 and 5")
    if asset.condition_status not in {"New", "Good", "Fair", "Poor", "Used", "Damaged"}:
        raise HTTPException(status_code=422, detail="Invalid condition_status")
    if asset.assigned_to is not None and not asset.assigned_to.strip():
        raise HTTPException(status_code=422, detail="assigned_to cannot be empty")
    if asset.location not in {"Trivandrum", "Bangalore", "Chennai", "Hyderabad","Bengaluru"}:
        raise HTTPException(status_code=422, detail="Invalid location")
    if asset.asset_status not in {"Available", "Assigned", "Repair", "Retired"}:
        raise HTTPException(status_code=422, detail="Invalid asset_status")
