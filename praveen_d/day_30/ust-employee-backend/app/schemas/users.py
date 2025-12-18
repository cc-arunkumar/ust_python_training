from pydantic import BaseModel, Field, field_validator

class UserSchema(BaseModel):
    emp_id: str = Field(..., min_length=3)
    password: str = Field(..., min_length=8)
    role: str
    status: str

    @field_validator("role")
    def validate_role(cls, v):
        allowed = {"ADMIN", "MANAGER", "EMPLOYEE"}
        v = v.upper()
        if v not in allowed:
            raise ValueError(f"role must be one of {allowed}")
        return v

    @field_validator("status")
    def validate_status(cls, v):
        allowed = {"ACTIVE", "INACTIVE"}
        v = v.upper()
        if v not in allowed:
            raise ValueError(f"status must be one of {allowed}")
        return v
