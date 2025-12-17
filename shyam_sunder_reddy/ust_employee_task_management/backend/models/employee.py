from pydantic import BaseModel, Field
from typing import Optional,List

class EmployeeReqRes(BaseModel):
    e_id: Optional[int] = None  # Optional for creating, required for updating
    name: str = Field(..., pattern=r"^[a-zA-Zà-ÿÀ-ÿ' -]+$", description="Name should contain only letters, spaces, and hyphens.")
    email: str = Field(..., pattern=r"^[a-zA-Z0-9_.+-]+@ust\.com$", description="Email must be valid and end with @ust.com")
    designation: str = Field(..., pattern=r"^[a-zA-Z0-9\s\-]+$", description="Designation should contain only letters, spaces, numbers, and allowed special characters.")
    mgr_id: int = Field(..., description="Manager ID must be given and should be an integer.")

    class Config:
        orm_mode = True  # Ensures compatibility with SQLAlchemy models
        from_attributes = True
        
class EmployeeCreateReq(BaseModel):
    employee: EmployeeReqRes
    assigning_role: List[str] = []