import csv
import re
from datetime import datetime
from pydantic import BaseModel, field_validator, ValidationError
import os

# Define custom exceptions
class ValidationErrorException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Predefined valid values
valid_maintenance_types = ['Repair', 'Service', 'Upgrade']
valid_statuses = ['Completed', 'Pending']

# Pydantic Model for Maintenance Log
class MaintenanceLog(BaseModel):
    log_id: str
    asset_tag: str
    maintenance_type: str
    vendor_name: str
    description: str
    cost: float
    maintenance_date: str
    technician_name: str
    status: str

    # Field Validators for each field

    @field_validator('log_id')
    def validate_log_id(cls, v):
        log_ids = getattr(cls, 'log_ids', set())  # Use a class-level variable to track log_ids
        if v in log_ids:
            raise ValueError(f"Duplicate log_id: {v}")
        log_ids.add(v)
        cls.log_ids = log_ids  # Store the updated set of log_ids
        return v

    @field_validator('asset_tag')
    def validate_asset_tag(cls, v):
        if v is None or not v.startswith('UST-'):
            raise ValueError(f"Invalid asset_tag: {v}")
        return v

    @field_validator('maintenance_type')
    def validate_maintenance_type(cls, v):
        if v not in valid_maintenance_types:
            raise ValueError(f"Invalid maintenance_type: {v}")
        return v

    @field_validator('vendor_name')
    def validate_vendor_name(cls, v):
        if not v.isalpha() and ' ' not in v:
            raise ValueError(f"Invalid vendor_name: {v}")
        return v

    @field_validator('description')
    def validate_description(cls, v):
        if len(v) < 10:
            raise ValueError(f"Description is too short: {v}")
        return v

    @field_validator('cost')
    def validate_cost(cls, v):
        if v <= 0:
            raise ValueError(f"Invalid cost: {v}")
        return v

    @field_validator('maintenance_date')
    def validate_maintenance_date(cls, v):
        date_pattern = r"^\d{4}-\d{2}-\d{2}$"
        if not re.match(date_pattern, v):
            raise ValueError(f"Invalid date format for maintenance_date: {v}")
        try:
            maintenance_date_obj = datetime.strptime(v, '%Y-%m-%d')
            if maintenance_date_obj > datetime.today():
                raise ValueError(f"Invalid maintenance_date (future date): {v}")
        except ValueError:
            raise ValueError(f"Invalid date format for maintenance_date: {v}")
        return v

    @field_validator('technician_name')
    def validate_technician_name(cls, v):
        if not v.isalpha() and ' ' not in v:
            raise ValueError(f"Invalid technician_name: {v}")
        return v

    @field_validator('status')
    def validate_status(cls, v):
        if v not in valid_statuses:
            raise ValueError(f"Invalid status: {v}")
        return v

