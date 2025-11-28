from pydantic import BaseModel, field_validator, model_validator
from datetime import date
import re

class MaintenanceLog(BaseModel):
    log_id: int                 # unique ID for maintenance log
    asset_tag: str              # must start with UST-
    maintenance_type: str       # must be Repair, Service, or Upgrade
    vendor_name: str            # vendor name, alphabets only
    description: str            # description, minimum 10 characters
    cost: float                 # cost, >0 with two decimal places
    maintenance_date: date      # maintenance date, cannot be in the future
    technician_name: str        # technician name, alphabets only
    status: str                 # status, must be Completed or Pending

    @field_validator("asset_tag")
    def tag_valid(cls, v):
        # asset_tag must start with "UST-"
        if not v.startswith("UST-"):
            raise ValueError("asset_tag must start with UST")
        return v

    @field_validator("maintenance_type")
    def type_valid(cls, v):
        # maintenance_type must be one of allowed values
        if v not in {"Repair", "Service", "Upgrade"}:
            raise ValueError("Invalid maintenance_type")
        return v

    @field_validator("vendor_name")
    def vendor_valid(cls, v):
        # vendor_name must contain only alphabets and spaces
        if not re.fullmatch(r"[A-Za-z ]+$", v):
            raise ValueError("vendor_name must be alphabets only")
        return v

    @field_validator("description")
    def description_valid(cls, v):
        # description must be at least 10 characters long
        if len(v.strip()) < 10:
            raise ValueError("Description too short")
        return v

    @field_validator("cost")
    def cost_valid(cls, v):
        # cost must be >0 and have two decimal places
        if v <= 0:
            raise ValueError("Cost must be > 0")
        if not re.fullmatch(r"\d+\.\d{1,2}", f"{v:.2f}"):
            raise ValueError("Cost must have two decimal places")
        return v

    @field_validator("technician_name")
    def technician_valid(cls, v):
        # technician_name must contain only alphabets and spaces
        if not re.fullmatch(r"[A-Za-z ]+", v):
            raise ValueError("Invalid technician_name")
        return v

    @field_validator("status")
    def status_valid(cls, v):
        # status must be Completed or Pending
        if v not in {"Completed", "Pending"}:
            raise ValueError("Invalid status")
        return v

    @model_validator(mode="after")
    def check_date(cls, values):
        # maintenance_date cannot be in the future
        if values.maintenance_date > date.today():
            raise ValueError("maintenance_date cannot be in the future")
        return values
