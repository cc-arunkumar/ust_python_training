from pydantic import BaseModel, Field, field_validator
from datetime import date, datetime
from typing import Optional
from enum import Enum
import csv
import os

# ---------------------------------------------------------
# ENUM CLASSES
# ---------------------------------------------------------

class MaintenanceType(str, Enum):
    """Allowed maintenance types."""
    repair = "Repair"
    service = "Service"
    upgrade = "Upgrade"


class Status(str, Enum):
    """Allowed status values for maintenance log."""
    completed = "Completed"
    pending = "Pending"


# ---------------------------------------------------------
# Pydantic Model: Maintenance Log Schema
# ---------------------------------------------------------

class MaintenanceLog(BaseModel):
    """
    Data validation model for maintenance entries.
    Ensures formatting rules for vendor, date, description,
    maintenance type and cost.
    """

    asset_tag: str = Field(..., pattern=r"^UST", description="Asset tag must start with UST")
    maintenance_type: MaintenanceType
    vendor_name: str = Field(..., pattern=r"^[A-Za-z ]+$", description="Vendor name should contain only alphabets and spaces")
    description: str = Field(..., min_length=10, description="Minimum 10 characters required")
    cost: float = Field(..., gt=0, description="Cost must be greater than zero")
    maintenance_date: date
    technician_name: str = Field(..., pattern=r"^[A-Za-z ]+$")
    status: Status

    @field_validator("maintenance_date")
    def validate_date(cls, value: date):
        """Ensures maintenance date is not in the future."""
        if value <= datetime.today().date():
            return value
        raise ValueError("Maintenance date cannot be in the future.")


# ---------------------------------------------------------
# CSV Processing Paths
# ---------------------------------------------------------
