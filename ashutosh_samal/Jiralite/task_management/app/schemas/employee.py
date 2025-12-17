from pydantic import BaseModel
from typing import Optional


class EmployeeBase(BaseModel):
    name: str
    email: str
    designation: str
    manager_id: Optional[int] = None


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(EmployeeBase):
    pass


class EmployeeOut(EmployeeBase):
    e_id: int

    class Config:
        from_attributes = True  # ✅ SQLAlchemy → Pydantic
