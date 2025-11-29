from pydantic import BaseModel, Field, field_validator  # Import Pydantic BaseModel, Field for validation, and field_validator for custom rules
from enum import Enum  # Import Enum to define fixed sets of values
from datetime import date, datetime  # Import date and datetime for date handling
from typing import Optional  # Import Optional to allow nullable fields

# -----------------------------
# ENUM CLASSES (fixed choices)
# -----------------------------
class MaintenanceType(str, Enum):  # Enum for maintenance types
    Repair = "Repair"              # Allowed value: Repair
    Service = "Service"            # Allowed value: Service
    Upgrade = "Upgrade"            # Allowed value: Upgrade

class Status(str, Enum):  # Enum for maintenance status
    Completed = "Completed"  # Allowed value: Completed
    Pending = "Pending"      # Allowed value: Pending

# -----------------------------
# MAIN Pydantic MODEL
# -----------------------------
class MaintenanceLog(BaseModel):  # Define MaintenanceLog model using Pydantic BaseModel
    log_id: int = 0  # Log ID, default value = 0

    asset_tag: str = Field(..., description="Must start with UST- (e.g., UST-LTP-0001)")  # Asset tag, required, must start with UST-
    maintenance_type: MaintenanceType = Field(..., description="Repair, Service, or Upgrade")  # Maintenance type, must be one of MaintenanceType Enum
    vendor_name: str = Field(..., max_length=100, description="Alphabets only")  # Vendor name, required, max length 100, alphabets only
    description: str = Field(..., min_length=10, description="Minimum 10 characters")  # Description, required, at least 10 characters
    cost: str = Field(..., description="Decimal with two digits after decimal point, >0")  # Cost, required, must be decimal >0 with 2 digits after decimal
    maintenance_date: str = Field(..., description="Date in YYYY-MM-DD format, not future")  # Maintenance date, required, must be valid date not in future
    technician_name: str = Field(..., max_length=100, description="Alphabets only")  # Technician name, required, max length 100, alphabets only
    status: Status = Field(..., description="Completed or Pending")  # Status, must be one of Status Enum

    # -----------------------------
    # CUSTOM VALIDATORS
    # -----------------------------

    @field_validator("asset_tag")  # Validator for asset_tag field
    def validate_asset_tag(cls, v):  # Function to validate asset_tag
        if not v.startswith("UST-"):  # Check if asset_tag starts with "UST-"
            raise ValueError("asset_tag must start with 'UST-'")  # Raise error if invalid
        return v  # Return validated value

    @field_validator("vendor_name", "technician_name")  # Validator for vendor_name and technician_name fields
    def validate_names(cls, v):  # Function to validate names
        # Ensure only alphabets and spaces are allowed
        if not v.isalpha() and not all(ch.isalpha() or ch.isspace() for ch in v):
            raise ValueError("Name must contain only alphabets and spaces")
        return v  # Return validated value

    @field_validator("cost")  # Validator for cost field
    def validate_cost(cls, v):  # Function to validate cost
        try:
            val = float(v)  # Try converting cost to float
        except ValueError:
            raise ValueError("Cost must be a valid decimal number")  # Raise error if not numeric
        if val <= 0:  # Ensure cost is greater than 0
            raise ValueError("Cost must be greater than 0")
        # enforce two decimal places
        if not v.isdigit() and not v.replace(".", "", 1).isdigit():  # Ensure numeric with decimal
            raise ValueError("Cost must be numeric")
        if not v.count(".") == 1 or len(v.split(".")[1]) != 2:  # Ensure exactly two digits after decimal
            raise ValueError("Cost must have exactly two digits after decimal")
        return v  # Return validated value

    @field_validator("maintenance_date")  # Validator for maintenance_date field
    def validate_date(cls, v):  # Function to validate maintenance_date
        try:
            parsed_date = datetime.strptime(v, "%Y-%m-%d").date()  # Parse date in YYYY-MM-DD format
        except ValueError:
            raise ValueError("maintenance_date must be in YYYY-MM-DD format")  # Raise error if invalid format
        if parsed_date > date.today():  # Ensure date is not in the future
            raise ValueError("maintenance_date cannot be in the future")
        return v  # Return validated value

