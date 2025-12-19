from pydantic import BaseModel, Field, field_validator
from typing import List, Union


class UserSchema(BaseModel):
    emp_id: str = Field(..., min_length=3)
    password: str = Field(..., min_length=8)
    # role can be a single string or a list of strings; normalize to list
    role: Union[List[str], str]
    status: str

    @field_validator("role")
    def validate_role(cls, v):
        allowed = {"ADMIN", "MANAGER", "EMPLOYEE"}
        # Normalize string to single-item list
        if isinstance(v, str):
            v = [v]
        # Ensure list of uppercase roles and validate each
        normalized = []
        for item in v:
            rv = item.upper()
            if rv not in allowed:
                raise ValueError(f"role must be one of {allowed}")
            if rv not in normalized:
                normalized.append(rv)
        return normalized

    @field_validator("status")
    def validate_status(cls, v):
        allowed = {"ACTIVE", "INACTIVE"}
        v = v.upper()
        if v not in allowed:
            raise ValueError(f"status must be one of {allowed}")
        return v
