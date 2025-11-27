from pydantic import BaseModel, field_validator, model_validator
from datetime import date
import re

class MaintenanceLog(BaseModel):
    log_id: int
    asset_tag: str
    maintenance_type: str
    vendor_name: str
    description: str
    cost: float
    maintenance_date: date
    technician_name: str
    status: str

    @field_validator("asset_tag")
    def tag_valid(cls, v):
        if not v.startswith("UST-"):
            raise ValueError("asset_tag must start with UST")
        return v

    @field_validator("maintenance_type")
    def type_valid(cls, v):
        if v not in {"Repair", "Service", "Upgrade"}:
            raise ValueError("Invalid maintenance_type")
        return v

    @field_validator("vendor_name")
    def vendor_valid(cls, v):
        if not re.fullmatch(r"[A-Za-z ]+$", v):
            raise ValueError("vendor_name must be alphabets only")
        return v

    @field_validator("description")
    def description_valid(cls, v):
        if len(v.strip()) < 10:
            raise ValueError("Description too short")
        return v

    @field_validator("cost")
    def cost_valid(cls, v):
        if v <= 0:
            raise ValueError("Cost must be > 0")
        if not re.fullmatch(r"\d+\.\d{1,2}", f"{v:.2f}"):
            raise ValueError("Cost must have two decimal places")
        return v

    @field_validator("technician_name")
    def technician_valid(cls, v):
        if not re.fullmatch(r"[A-Za-z ]+", v):
            raise ValueError("Invalid technician_name")
        return v

    @field_validator("status")
    def status_valid(cls, v):
        if v not in {"Completed", "Pending"}:
            raise ValueError("Invalid status")
        return v

    @model_validator(mode="after")
    def check_date(cls, values):
        if values.maintenance_date > date.today():
            raise ValueError("maintenance_date cannot be in the future")
        return values
