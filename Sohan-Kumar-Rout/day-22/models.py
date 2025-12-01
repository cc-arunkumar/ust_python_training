from pydantic import BaseModel, Field, field_validator
from datetime import date

class TrainingRequest(BaseModel):
    employee_id: str = Field(..., description="Must start with UST followed by digits (e.g., UST12345)")
    employee_name: str = Field(..., description="Full name; cannot be empty or contain numbers")
    training_title: str = Field(..., min_length=5, description="Minimum 5 characters")
    training_description: str = Field(..., min_length=10, description="Minimum 10 characters")
    requested_date: date = Field(..., description="Request date; cannot be in the future")
    status: str = Field(..., description="One of PENDING, APPROVED, REJECTED")
    manager_id: str = Field(..., description="Must start with UST followed by digits (e.g., UST56789)")

    @field_validator("employee_id")
    def validate_employee_id(cls, v):
        if not v.startswith("UST") or not v[3:].isdigit():
            raise ValueError("employee_id must match ^UST\\d+$")
        return v

    @field_validator("manager_id")
    def validate_manager_id(cls, v):
        if not v.startswith("UST") or not v[3:].isdigit():
            raise ValueError("manager_id must match ^UST\\d+$")
        return v

    @field_validator("employee_name")
    def validate_employee_name(cls, v):
        s = v.strip()
        if not s:
            raise ValueError("employee_name cannot be empty")
        if any(ch.isdigit() for ch in s):
            raise ValueError("employee_name cannot contain numbers")
        return v

    @field_validator("training_title")
    def validate_title(cls, v):
        if len(v.strip()) < 5:
            raise ValueError("training_title must be at least 5 characters")
        return v

    @field_validator("training_description")
    def validate_description(cls, v):
        if len(v.strip()) < 10:
            raise ValueError("training_description must be at least 10 characters")
        return v

    @field_validator("requested_date")
    def validate_requested_date(cls, v: date):
        from datetime import date as d
        if v > d.today():
            raise ValueError("requested_date cannot be a future date")
        return v

    @field_validator("status")
    def validate_status(cls, v):
        allowed = {"PENDING", "APPROVED", "REJECTED"}
        if v not in allowed:
            raise ValueError("status must be one of PENDING, APPROVED, REJECTED")
        return v


class TrainingUpdate(BaseModel):
    employee_id: str | None = None
    employee_name: str | None = None
    training_title: str | None = None
    training_description: str | None = None
    requested_date: date | None = None
    status: str | None = None
    manager_id: str | None = None

    @field_validator("employee_id")
    def validate_employee_id(cls, v):
        if v is None:
            return v
        if not v.startswith("UST") or not v[3:].isdigit():
            raise ValueError("employee_id must match ^UST\\d+$")
        return v

    @field_validator("manager_id")
    def validate_manager_id(cls, v):
        if v is None:
            return v
        if not v.startswith("UST") or not v[3:].isdigit():
            raise ValueError("manager_id must match ^UST\\d+$")
        return v

    @field_validator("employee_name")
    def validate_employee_name(cls, v):
        if v is None:
            return v
        s = v.strip()
        if not s:
            raise ValueError("employee_name cannot be empty")
        if any(ch.isdigit() for ch in s):
            raise ValueError("employee_name cannot contain numbers")
        return v

    @field_validator("training_title")
    def validate_title(cls, v):
        if v is None:
            return v
        if len(v.strip()) < 5:
            raise ValueError("training_title must be at least 5 characters")
        return v

    @field_validator("training_description")
    def validate_description(cls, v):
        if v is None:
            return v
        if len(v.strip()) < 10:
            raise ValueError("training_description must be at least 10 characters")
        return v

    @field_validator("requested_date")
    def validate_requested_date(cls, v: date | None):
        if v is None:
            return v
        from datetime import date as d
        if v > d.today():
            raise ValueError("requested_date cannot be a future date")
        return v

    @field_validator("status")
    def validate_status(cls, v):
        if v is None:
            return v
        allowed = {"PENDING", "APPROVED", "REJECTED"}
        if v not in allowed:
            raise ValueError("status must be one of PENDING, APPROVED, REJECTED")
        return v
