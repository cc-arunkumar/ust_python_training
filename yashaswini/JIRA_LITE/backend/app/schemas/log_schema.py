from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime


class LogResponse(BaseModel):
    action: str
    entity: str
    entity_id: str
    performed_by: str
    timestamp: datetime
    details: Optional[Dict]
