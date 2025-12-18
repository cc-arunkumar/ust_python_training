from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AttachmentResponse(BaseModel):
    attachment_id: str
    task_id: str
    filename: str
    content_type: str
    uploaded_by: str
    uploaded_at: datetime
    is_active: bool
