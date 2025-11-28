from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel, Field, ValidationError
import re


# Asset model definition using Pydantic for validation and type enforcement
class Asset(BaseModel):
    asset_id: Optional[int] = None              # Primary key (optional, auto-generated in DB)
    asset_tag: str                              # Unique tag identifier, must start with "UST"
    asset_type: str                             # Type of asset (Laptop, Monitor, etc.)
    serial_number: str                          # Unique serial number (alphanumeric)
    manufacturer: str                           # Manufacturer name (Dell, HP, etc.)
    model: str                                  # Model name/number
    purchase_date: date                         # Date of purchase
    warranty_years: int                         # Warranty period (1–5 years)
    condition_status: str                       # Condition (New, Good, Used, Damaged, Fair)
    assigned_to: Optional[str] = None           # Employee name if asset is assigned
    location: str                               # Location (Trivandrum, Bangalore, etc.)
    asset_status: str                           # Status (Available, Assigned, Repair, Retired)
    last_updated: Optional[datetime] = Field(default_factory=datetime.now)  # Timestamp auto-set


# Function: Validate asset fields against business rules
def validate_asset(asset: Asset) -> list[str]:
    errors = []

    # Asset tag must start with "UST"
    if not re.match(r"^UST.*", asset.asset_tag):
        errors.append(f"Invalid asset_tag: {asset.asset_tag}")

    # Asset type must be one of the allowed categories
    allowed_types = ["Laptop", "Monitor", "Keyboard", "Mouse", "Printer", "DockingStation"]
    if asset.asset_type not in allowed_types:
        errors.append(f"Invalid asset_type: {asset.asset_type}")

    # Serial number must be non-empty alphanumeric
    if (not asset.serial_number or not re.match(r"^[A-Za-z0-9-]+$", asset.serial_number)):
        errors.append("Serial number must be non-empty alphanumeric and unique")

    # Manufacturer must be in the allowed list
    allowed_manufacturers = ["Dell", "HP", "Lenovo", "Samsung", "Acer", "Asus", "LG"]
    if asset.manufacturer not in allowed_manufacturers:
        errors.append(f"Invalid manufacturer: {asset.manufacturer}")

    # Model cannot be blank
    if not asset.model.strip():
        errors.append("Model cannot be blank")

    # Purchase date cannot be in the future
    if asset.purchase_date > date.today():
        errors.append("Purchase date cannot be in the future")

    # Warranty years must be between 1 and 5
    if asset.warranty_years < 1 or asset.warranty_years > 5:
        errors.append("Warranty years must be between 1 and 5")

    # Condition must be valid
    allowed_conditions = ["New", "Good", "Used", "Damaged", "Fair"]
    if asset.condition_status not in allowed_conditions:
        errors.append(f"Invalid condition_status: {asset.condition_status}")

    # Business rules for assignment based on status
    if asset.asset_status == "Assigned":
        if not asset.assigned_to or not asset.assigned_to.strip():
            errors.append("Assigned assets must have a valid employee name")
    elif asset.asset_status in ["Available", "Retired"]:
        if asset.assigned_to:
            errors.append("Available/Retired assets cannot be assigned")

    # Location must be valid
    allowed_locations = ["Trivandrum", "Bangalore", "Chennai", "Hyderabad"]
    if asset.location not in allowed_locations:
        errors.append(f"Invalid location: {asset.location}")

    # Status must be valid
    allowed_status = ["Available", "Assigned", "Repair", "Retired"]
    if asset.asset_status not in allowed_status:
        errors.append(f"Invalid asset_status: {asset.asset_status}")

    return errors

