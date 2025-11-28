from pydantic import BaseModel, Field, model_validator
from datetime import date
from typing import Literal

class StatusValidator(BaseModel):  # Validate allowed maintenance status values
    status: Literal['Completed', 'Pending']

class MaintenanceLog(BaseModel):  # Maintenance log schema with validation rules
    asset_tag: str = Field(..., pattern=r"^UST-[A-Za-z0-9-]+$")  # Asset tag must start with UST-
    maintenance_type: Literal['Repair', 'Service', 'Upgrade']  # Restrict maintenance type values
    vendor_name: str = Field(..., pattern=r"^[A-Za-z ]+$")  # Vendor name must contain only letters/spaces
    description: str = Field(..., min_length=10)  # Description must be at least 10 characters
    cost: float = Field(..., gt=0)  # Cost must be greater than 0
    maintenance_date: date  # Maintenance date
    technician_name: str = Field(..., pattern=r"^[A-Za-z ]+$")  # Technician name must contain only letters/spaces
    status: Literal['Completed', 'Pending']  # Restrict status values

    @model_validator(mode="after")
    def validate_maintenance_date(self):  # Ensure maintenance_date is not in the future
        if self.maintenance_date > date.today():
            raise ValueError("maintenance_date cannot be in the future")
        return self