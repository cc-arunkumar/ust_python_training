from pydantic import BaseModel, Field, model_validator
from datetime import date

class MaintenanceLog(BaseModel):
    asset_tag: str = Field(..., pattern=r"^UST-[A-Za-z0-9-]+$")
    maintenance_type: str
    vendor_name: str = Field(..., pattern=r"^[A-Za-z ]+$")
    description: str = Field(..., min_length=10)
    cost: float = Field(..., gt=0)
    maintenance_date: date
    technician_name: str = Field(..., pattern=r"^[A-Za-z ]+$")
    status: str

    @model_validator(mode="after")
    def validate_all(self):
        # Allowed values for maintenance_type
        if self.maintenance_type not in ["Repair", "Service", "Upgrade"]:
            raise ValueError("maintenance_type must be one of ['Repair', 'Service', 'Upgrade']")
        
        # Allowed values for status
        if self.status not in ["Completed", "Pending"]:
            raise ValueError("status must be either 'Completed' or 'Pending'")
        
        # Date check
        if self.maintenance_date > date.today():
            raise ValueError("maintenance_date cannot be in the future")
        
        # Cost precision check
        if round(self.cost, 2) != self.cost:
            raise ValueError("cost must have at most two digits after decimal")
        
        return self
