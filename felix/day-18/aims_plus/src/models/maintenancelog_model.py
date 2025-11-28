from pydantic import BaseModel,Field,model_validator
from datetime import date
from typing import Literal
 
 
class MaintenanceLog(BaseModel):
    asset_tag: str = Field(..., pattern=r"^UST-[A-Za-z0-9-]+$")
    maintenance_type: Literal['Repair', 'Service', 'Upgrade']
    vendor_name: str = Field(..., pattern=r"^[A-Za-z ]+$")
    description: str = Field(..., min_length=10)
    cost: float = Field(..., gt=0)
    maintenance_date: date
    technician_name: str = Field(..., pattern=r"^[A-Za-z ]+$")
    status: Literal['Completed', 'Pending']
 
    @model_validator(mode="after")
    def validate_maintenance_date(self):
        if self.maintenance_date > date.today():
            raise ValueError("maintenance_date cannot be in the future")
        return self
 