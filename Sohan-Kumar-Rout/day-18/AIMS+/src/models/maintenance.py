from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date

valid_types = ["Repair", "Service", "Upgrade"]
valid_status = ["Completed", "Pending"]

class MaintenanceBase(BaseModel):
    asset_tag: str = Field(..., description="Asset tag, must start with UST-")
    maintenance_type: str = Field(..., description="Type of maintenance")
    vendor_name: str = Field(..., description="Vendor name")
    description: str = Field(..., description="Maintenance description")
    cost: float = Field(..., ge=0, description="Cost of maintenance")
    maintenance_date: date = Field(..., description="Date of maintenance in YYYY-MM-DD format")
    technician_name: str = Field(..., description="Technician name")
    status: str = Field(..., description="Status of maintenance")

    @field_validator("asset_tag")
    def validate_asset_tag(cls, v):
        if not v.startswith("UST-"):
            raise ValueError("Asset tag must start with UST-")
        return v

    @field_validator("maintenance_type")
    def validate_type(cls, v):
        if v not in valid_types:
            raise ValueError(f"maintenance_type must be one of {valid_types}")
        return v

    @field_validator("vendor_name")
    def validate_vendor_name(cls, v):
        if not v.replace(" ", "").isalpha():
            raise ValueError("Vendor name must contain only alphabets and spaces")
        return v

    @field_validator("description")
    def validate_description(cls, v):
        if not v or len(v.strip()) < 10:
            raise ValueError("Description must be at least 10 characters long")
        return v

    @field_validator("technician_name")
    def validate_technician_name(cls, v):
        if not v.replace(" ", "").isalpha():
            raise ValueError("Technician name must contain only alphabets and spaces")
        return v

    @field_validator("status")
    def validate_status(cls, v):
        if v not in valid_status:
            raise ValueError(f"Status must be one of {valid_status}")
        return v


class MaintenanceCreate(MaintenanceBase):
    log_id: int = Field(..., ge=1, description="Unique log ID")


class MaintenanceUpdate(MaintenanceBase):
    pass  


class MaintenanceStatusUpdate(BaseModel):
    status: str = Field(..., description="Update only the status")

    @field_validator("status")
    def validate_status(cls, v):
        if v not in valid_status:
            raise ValueError(f"Status must be one of {valid_status}")
        return v


class MaintenanceResponse(MaintenanceCreate):
    pass
