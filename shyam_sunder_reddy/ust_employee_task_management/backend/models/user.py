from pydantic import BaseModel, Field
from typing import Optional, List


class UserReqRes(BaseModel):
    e_id: Optional[int] = None
    password: Optional[str] = Field(None, min_length=6)
    role: List[str] = Field(..., description="List of roles: Admin, Manager, Developer")
    status: str = Field(..., description="active or inactive")

    class Config:
        orm_mode = True
        from_attributes = True
