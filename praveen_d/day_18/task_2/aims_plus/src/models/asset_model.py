from pydantic import BaseModel, field_validator, ValidationError
from datetime import datetime
from typing import Optional
import re
import csv

# Constants
asset_type_list = ['Laptop', 'Monitor', 'Keyboard', 'Mouse']
manufacturer_list = ['Dell', 'HP', 'Lenovo', 'Samsung', 'LG']
condition_status_list = ['New', 'Good', 'Used', 'Damaged']
location_list = ['TVM', 'Bangalore', 'Chennai', 'Hyderabad']
asset_status_list = ['Available', 'Assigned', 'Repair', 'Retired']

class UpdateStatusRequest(BaseModel):
    asset_status: str
    
class AssetInventory(BaseModel):
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
    last_updated: Optional[datetime] = None

    # Field Validators (Pydantic v2)
    @field_validator('asset_tag')
    def validate_asset_tag(cls, v):
        if not v.startswith('UST-'):
            raise ValueError('The asset_tag must start with "UST-"')
        return v

    @field_validator('asset_type')
    def validate_asset_type(cls, v):
        if v not in asset_type_list:
            raise ValueError(f'Asset type must be one of {", ".join(asset_type_list)}')
        return v

    @field_validator('serial_number')
    def validate_serial_number(cls, v, values):
        # Use a class-level attribute to track serial numbers (static set)
        serial_numbers = getattr(cls, 'serial_numbers', set())
        if v in serial_numbers:
            raise ValueError('Duplicate serial number found')
        serial_numbers.add(v)
        cls.serial_numbers = serial_numbers
        return v

    @field_validator('manufacturer')
    def validate_manufacturer(cls, v):
        if v not in manufacturer_list:
            raise ValueError(f'Manufacturer must be one of {", ".join(manufacturer_list)}')
        return v

    @field_validator('model')
    def validate_model(cls, v):
        if not v.strip():
            raise ValueError('Model number cannot be blank')
        return v

    @field_validator('purchase_date')
    def validate_purchase_date(cls, v):
        date_pattern = r"^\d{4}-\d{2}-\d{2}$"
        if not re.match(date_pattern, v):
            raise ValueError('Purchase date format should be YYYY-MM-DD')
        try:
            purchase_date_obj = datetime.strptime(v, "%Y-%m-%d")
            if purchase_date_obj > datetime.now():
                raise ValueError('Purchase date cannot be in the future')
        except ValueError:
            raise ValueError('Invalid date format or value')
        return v

    @field_validator('warranty_years')
    def validate_warranty_years(cls, v):
        if not (1 <= v <= 5):
            raise ValueError('Warranty years must be between 1 and 5')
        return v

    @field_validator('condition_status')
    def validate_condition_status(cls, v):
        if v not in condition_status_list:
            raise ValueError(f'Condition status must be one of {", ".join(condition_status_list)}')
        return v

    @field_validator('assigned_to')
    def validate_assigned_to(cls, v):
        if v and not v.strip():
            raise ValueError('Assigned_to must be a non-empty string')
        return v

    @field_validator('location')
    def validate_location(cls, v):
        if v not in location_list:
            raise ValueError(f'Location must be one of {", ".join(location_list)}')
        return v

    @field_validator('asset_status')
    def validate_asset_status(cls, v):
        if v not in asset_status_list:
            raise ValueError(f'Asset status must be one of {", ".join(asset_status_list)}')
        return v

