"""from pydantic import BaseModel
from datetime import datetime


class TaskFileResponse(BaseModel):
    file_id: int
    task_id: int
    filename: str
    content_type: str
    uploaded_at: datetime

    class Config:
        from_attributes = True
"""

from pydantic import BaseModel
from datetime import datetime

class TaskFileResponse(BaseModel):
    file_id: int
    task_id: int
    filename: str
    content_type: str
    uploaded_at: datetime

    class Config:
        from_attributes = True