from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class RemarkReqRes(BaseModel):
    _id: Optional[str] = None
    task_id: int = Field(...)
    comment: str = Field(..., max_length=1000)
    created_by: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True
