from pydantic import BaseModel

class MaintenanceCreate(BaseModel):
    asset_tag: str
    maintenance_type: str
    vendor_name: str
    description: str
    cost: float
    maintenance_date: str   # YYYY-MM-DD
    technician_name: str
    status: str


class MaintenanceUpdate(BaseModel):
    asset_tag: str
    maintenance_type: str
    vendor_name: str
    description: str
    cost: float
    maintenance_date: str
    technician_name: str
    status: str


class MaintenanceStatusUpdate(BaseModel):
    status: str
