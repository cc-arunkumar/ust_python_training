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
class RemarkResponse(BaseModel):
    task_id: int
    comment: str
    created_by: int
    file_id: str | None = None
    file_name: str | None = None
    created_at: datetime