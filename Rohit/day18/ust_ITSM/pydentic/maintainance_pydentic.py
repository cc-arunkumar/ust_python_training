from pydantic import BaseModel, Field, field_validator
from enum import Enum
from datetime import date, datetime
from typing import Optional

class MaintenanceType(str, Enum):
    Repair = "Repair"
    Service = "Service"
    Upgrade = "Upgrade"

class Status(str, Enum):
    Completed = "Completed"
    Pending = "Pending"

class MaintenanceLog(BaseModel):
    log_id:int =0

    asset_tag: str = Field(..., description="Must start with UST- (e.g., UST-LTP-0001)")
    maintenance_type: MaintenanceType = Field(..., description="Repair, Service, or Upgrade")
    vendor_name: str = Field(..., max_length=100, description="Alphabets only")
    description: str = Field(..., min_length=10, description="Minimum 10 characters")
    cost: str = Field(..., description="Decimal with two digits after decimal point, >0")
    maintenance_date: str = Field(..., description="Date in YYYY-MM-DD format, not future")
    technician_name: str = Field(..., max_length=100, description="Alphabets only")
    status: Status = Field(..., description="Completed or Pending")

    # --- Validators ---
    @field_validator("asset_tag")
    def validate_asset_tag(cls, v):
        if not v.startswith("UST-"):
            raise ValueError("asset_tag must start with 'UST-'")
        return v

    @field_validator("vendor_name", "technician_name")
    def validate_names(cls, v):
        if not v.isalpha() and not all(ch.isalpha() or ch.isspace() for ch in v):
            raise ValueError("Name must contain only alphabets and spaces")
        return v

    @field_validator("cost")
    def validate_cost(cls, v):
        try:
            val = float(v)
        except ValueError:
            raise ValueError("Cost must be a valid decimal number")
        if val <= 0:
            raise ValueError("Cost must be greater than 0")
        # enforce two decimal places
        if not v.isdigit() and not v.replace(".", "", 1).isdigit():
            raise ValueError("Cost must be numeric")
        if not v.count(".") == 1 or len(v.split(".")[1]) != 2:
            raise ValueError("Cost must have exactly two digits after decimal")
        return v

    @field_validator("maintenance_date")
    def validate_date(cls, v):
        try:
            parsed_date = datetime.strptime(v, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("maintenance_date must be in YYYY-MM-DD format")
        if parsed_date > date.today():
            raise ValueError("maintenance_date cannot be in the future")
        return v

# starts with n 0-9
# one special
# one -
# one upper 
# one lower 

