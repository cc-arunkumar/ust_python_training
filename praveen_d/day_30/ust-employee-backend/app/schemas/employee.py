from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional, List, Union


class EmployeeSchema(BaseModel):
    emp_id: str = Field(..., min_length=3, max_length=50)
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    # designation can be a single string or a list (e.g. ["Developer","MANAGER"])
    designation: Union[List[str], str] = Field(..., min_length=2, max_length=200)
    mgr_id: Optional[str] = None

    @field_validator("designation")
    def normalize_designation(cls, v):
        # normalize to list for validation/consistency
        if isinstance(v, str):
            return [v]
        return v

    # class Config:
    #     from_attributes = True
