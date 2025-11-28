from pydantic import BaseModel, Field, field_validator
from datetime import date

VALID_TYPES = ["Repair", "Service", "Upgrade"]
VALID_STATUSES = ["Completed", "Pending"]

class MaintenanceCreate(BaseModel):
    asset_tag: str = Field(..., pattern=r"^UST-")
    maintenance_type: str
    vendor_name: str
    description: str = Field(..., min_length=10)
    cost: float = Field(..., gt=0)
    maintenance_date: date
    technician_name: str
    status: str = "Pending"

    @field_validator('asset_tag')
    def check_tag(cls, v):
        if not v.startswith("UST-"):
            raise ValueError("asset_tag must start with UST-")
        return v

    @field_validator('maintenance_type')
    def check_type(cls, v):
        if v not in VALID_TYPES:
            raise ValueError(f"maintenance_type must be one of {VALID_TYPES}")
        return v

    @field_validator('vendor_name', 'technician_name')
    def alpha_only(cls, v):
        if not v.replace(" ", "").isalpha():
            raise ValueError("Name must contain only letters and spaces")
        return v.strip()

    @field_validator('maintenance_date')
    def not_future(cls, v):
        if v > date.today():
            raise ValueError("maintenance_date cannot be future date")
        return v

    @field_validator('status')
    def valid_status(cls, v):
        if v not in VALID_STATUSES:
            raise ValueError(f"status must be one of {VALID_STATUSES}")
        return v

class MaintenanceUpdate(MaintenanceCreate):
    pass