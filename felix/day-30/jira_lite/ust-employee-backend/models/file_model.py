from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FileUpload(BaseModel):
    task_id: str
    file_name: str
    file_type: str  # e.g., "image/png", "application/pdf"
    file_size: int  # bytes

class TaskFile(BaseModel):
    task_id: str
    file_id: str
    file_name: str
    file_type: str
    file_size: int
    uploaded_by: int
    uploaded_at: datetime
    url: Optional[str] = None  # For external storage URLs
