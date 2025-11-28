from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
import re
from fastapi import HTTPException

class MaintenanceLog(BaseModel):
    log_id: Optional[int] = None
    asset_id: int
    maintenance_date: date
    description: str
    performed_by: str
    cost: Optional[float] = None
    status: str
    last_updated: Optional[datetime] = None

def validate_log(log: MaintenanceLog):
    if not log.description or len(log.description.strip()) < 10:
        raise HTTPException(status_code=422, detail="description must be at least 10 characters")
    if not re.match(r"^[A-Za-z ]+$", log.performed_by):
        raise HTTPException(status_code=422, detail="performed_by must contain only alphabets and spaces")
    if log.cost is not None and log.cost <= 0:
        raise HTTPException(status_code=422, detail="cost must be greater than 0")
    if log.maintenance_date > date.today():
        raise HTTPException(status_code=422, detail="maintenance_date cannot be in the future")
    if log.status not in {"Completed", "Pending"}:
        raise HTTPException(status_code=422, detail="status must be 'Completed' or 'Pending'")
