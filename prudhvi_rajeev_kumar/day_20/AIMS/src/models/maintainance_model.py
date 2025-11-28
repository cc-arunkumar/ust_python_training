from pydantic import BaseModel, field_validator, model_validator
from datetime import date
import re

class MaintenanceLog(BaseModel):
    # Log ID: Auto-generated unique identifier for the maintenance log
    log_id: int
    
    # Asset tag: A unique identifier for the asset, must start with "UST-"
    asset_tag: str
    
    # Maintenance type: Type of maintenance performed (e.g., Repair, Service, Upgrade)
    maintenance_type: str
    
    # Vendor name: Name of the vendor performing the maintenance, only alphabets allowed
    vendor_name: str
    
    # Description: A description of the maintenance performed, must be at least 10 characters long
    description: str
    
    # Cost: The cost of the maintenance, must be greater than 0 and formatted with two decimal places
    cost: float
    
    # Maintenance date: Date when the maintenance took place, cannot be in the future
    maintenance_date: date
    
    # Technician name: Name of the technician performing the maintenance, only alphabets allowed
    technician_name: str
    
    # Status: Maintenance status, either 'Completed' or 'Pending'
    status: str

    # Validator for asset_tag: Ensures the asset tag starts with "UST-"
    @field_validator("asset_tag")
    def tag_valid(cls, v):
        if not v.startswith("UST-"):
            raise ValueError("asset_tag must start with UST")
        return v

    # Validator for maintenance_type: Ensures the type is either 'Repair', 'Service', or 'Upgrade'
    @field_validator("maintenance_type")
    def type_valid(cls, v):
        if v not in {"Repair", "Service", "Upgrade"}:
            raise ValueError("Invalid maintenance_type")
        return v

    # Validator for vendor_name: Ensures the vendor name only contains alphabetic characters and spaces
    @field_validator("vendor_name")
    def vendor_valid(cls, v):
        if not re.fullmatch(r"[A-Za-z ]+$", v):
            raise ValueError("vendor_name must be alphabets only")
        return v

    # Validator for description: Ensures the description is at least 10 characters long
    @field_validator("description")
    def description_valid(cls, v):
        if len(v.strip()) < 10:
            raise ValueError("Description too short")
        return v

    # Validator for cost: Ensures the cost is greater than 0 and has exactly two decimal places
    @field_validator("cost")
    def cost_valid(cls, v):
        if v <= 0:
            raise ValueError("Cost must be > 0")
        # Ensure cost is formatted with two decimal places
        if not re.fullmatch(r"\d+\.\d{1,2}", f"{v:.2f}"):
            raise ValueError("Cost must have two decimal places")
        return v

    # Validator for technician_name: Ensures the technician's name contains only alphabets and spaces
    @field_validator("technician_name")
    def technician_valid(cls, v):
        if not re.fullmatch(r"[A-Za-z ]+", v):
            raise ValueError("Invalid technician_name")
        return v

    # Validator for status: Ensures the status is either 'Completed' or 'Pending'
    @field_validator("status")
    def status_valid(cls, v):
        if v not in {"Completed", "Pending"}:
            raise ValueError("Invalid status")
        return v

    # Model-level validation: Ensures that maintenance_date is not in the future
    @model_validator(mode="after")
    def check_date(cls, values):
        if values.maintenance_date > date.today():
            raise ValueError("maintenance_date cannot be in the future")
        return values
