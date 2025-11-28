from pydantic import BaseModel, Field, model_validator  # Import Pydantic classes for data validation and model creation
from datetime import date  # Import date for handling date fields
from typing import Literal  # Import Literal to specify fixed possible values for some fields

# StatusValidate model to validate the status of the maintenance (can either be 'Completed' or 'Pending')
class StatusValidate(BaseModel):
    status: Literal['Completed', 'Pending']  # The 'status' field must be one of these two values

# MaintenanceLog model to represent the structure of a maintenance record
class MaintenanceLog(BaseModel):
    # 'asset_tag' field must match a pattern starting with 'UST-' followed by alphanumeric characters or dashes
    asset_tag: str = Field(..., pattern=r"^UST-[A-Za-z0-9-]+$")
    
    # 'maintenance_type' field must be one of the predefined types: 'Repair', 'Service', or 'Upgrade'
    maintenance_type: Literal['Repair', 'Service', 'Upgrade']
    
    # 'vendor_name' field must consist of alphabetic characters and spaces only
    vendor_name: str = Field(..., pattern=r"^[A-Za-z ]+$")
    
    # 'description' field must be at least 10 characters long
    description: str = Field(..., min_length=10)
    
    # 'cost' field must be a positive float value (greater than 0)
    cost: float = Field(..., gt=0)
    
    # 'maintenance_date' field is a date representing when the maintenance occurred
    maintenance_date: date
    
    # 'technician_name' field must consist of alphabetic characters and spaces only
    technician_name: str = Field(..., pattern=r"^[A-Za-z ]+$")
    
    # 'status' field must be either 'Completed' or 'Pending'
    status: Literal['Completed', 'Pending']
    
    # Custom validation logic after the automatic validation
    @model_validator(mode="after")
    def validate_maintenance_date(self):
        # Ensure that the maintenance date is not in the future
        if self.maintenance_date > date.today():
            raise ValueError("maintenance_date cannot be in the future")
        
        # Return the instance after validation passes
        return self
