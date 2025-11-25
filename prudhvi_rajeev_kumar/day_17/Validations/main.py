from pydantic import BaseModel, EmailStr, Field, ValidationError
from enum import Enum

class BandEnum(str, Enum):
    B1 = "B1"
    B2 = "B2"
    B3 = "B3"
    M1 = "M1"

class EmployeeTask(BaseModel):
    # Scenario 1 — employee_id must be positive
    employee_id: int = Field(..., gt=0, description="employee_id must be positive")

    # Scenario 2 — employee_name min 3 chars
    employee_name: str = Field(..., min_length=3, pattern=r"^[A-Za-z ]+$", description="employee_name must be at least 3 characters and only letters/spaces")

    # Scenario 3 — email must be valid
    email: EmailStr

    # Scenario 4 — mobile must be exactly 10 digits
    mobile: str = Field(..., pattern=r"^\d{10}$", description="mobile must be exactly 10 digits")

    band: BandEnum

    # Scenario 6 — task_id positive (cannot equal employee_id → needs validator)
    task_id: int = Field(..., gt=0, description="task_id must be positive")

    # Scenario 7 — task_title min 3 chars
    task_title: str = Field(..., min_length=3, description="task_title must be at least 3 characters")

    # Scenario 8 — task_description min 10 chars
    task_description: str = Field(..., min_length=10, description="task_description must be at least 10 characters")

    # Scenario 9 — hours_spent between 1 and 12
    hours_spent: int = Field(..., ge=1, le=12, description="hours_spent must be between 1 and 12")

    # Scenario 10 — completed must be boolean
    completed: bool = Field(default=False, description="completed must be a boolean")

# Valid
try:
    task = EmployeeTask(
        employee_id=101,
        employee_name="Rahul Menon",
        email="rahul.menon@ust.com",
        mobile="9876543210",
        band="B1",
        task_id=501,
        task_title="Prepare Report",
        task_description="Complete the monthly report thoroughly",
        hours_spent=8,
        completed=False
    )
    print("Valid Task Created:", task)
except ValidationError as e:
    print("Validation Error:", e)

# Invalid Example: employee_id negative
try:
    EmployeeTask(
        employee_id=-5,
        employee_name="Rahul",
        email="rahul.menon@ust.com",
        mobile="9876543210",
        band="B1",
        task_id=501,
        task_title="Prepare Report",
        task_description="Complete the monthly report thoroughly",
        hours_spent=8,
        completed=False
    )
except ValidationError as e:
    print("Error (employee_id):", e)
