from pydantic import BaseModel, validator, EmailStr
from enum import Enum
from typing import List
from datetime import date


class BandEnum(str, Enum):
    B1 = "B1"
    B2 = "B2"
    B3 = "B3"
    M1 = "M1"


class EmployeeTask(BaseModel):
    # Employee Info
    employee_id: int
    employee_name: str
    email: EmailStr
    mobile: str
    band: BandEnum
    # Task Info
    task_id: int
    task_title: str
    task_description: str
    hours_spent: int
    completed: bool = False

    # Validation for employee_id
    @validator('employee_id')
    def employee_id_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("employee_id must be positive")
        return value

    # Validation for employee_name
    @validator('employee_name')
    def employee_name_must_be_valid(cls, value):
        if len(value) < 3:
            raise ValueError("employee_name must be at least 3 characters")
        if not value.isalpha() and " " not in value:
            raise ValueError("employee_name must contain only letters and spaces")
        return value

    # Validation for email
    @validator('email')
    def email_must_be_valid(cls, value):
        if '@' not in value or '.' not in value.split('@')[1]:
            raise ValueError("email must be a valid email address")
        return value

    # Validation for mobile number
    @validator('mobile')
    def mobile_must_be_valid(cls, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("mobile must be exactly 10 digits")
        if value[0] not in ['6', '7', '8', '9']:
            raise ValueError("mobile must start with 6,7,8, or 9")
        return value

    # Validation for band
    @validator('band')
    def band_must_be_valid(cls, value):
        if value not in BandEnum._value2member_map_:
            raise ValueError("band must be one of: B1, B2, B3, M1")
        return value

    # Validation for task_id
    @validator('task_id')
    def task_id_must_be_positive(cls, value, values):
        if value <= 0:
            raise ValueError("task_id must be positive")
        if value == values.get('employee_id'):
            raise ValueError("task_id cannot be same as employee_id")
        return value

    # Validation for task_title
    @validator('task_title')
    def task_title_must_be_valid(cls, value):
        if len(value) < 3:
            raise ValueError("task_title must be at least 3 characters")
        return value

    # Validation for task_description
    @validator('task_description')
    def task_description_must_be_valid(cls, value):
        if len(value) < 10:
            raise ValueError("task_description must be at least 10 characters")
        return value

    # Validation for hours_spent
    @validator('hours_spent')
    def hours_spent_must_be_valid(cls, value):
        if value < 1 or value > 12:
            raise ValueError("hours_spent must be between 1 and 12")
        return value

    # Validation for completed
    @validator('completed')
    def completed_must_be_boolean(cls, value):
        if not isinstance(value, bool):
            raise ValueError("completed must be a boolean")
        return value


# Test cases for validation
def test_employee_task():
    valid_task = EmployeeTask(
        employee_id=101,
        employee_name="Rahul Menon",
        email="rahul.menon@ust.com",
        mobile="9876543210",
        band=BandEnum.B1,
        task_id=501,
        task_title="Prepare Report",
        task_description="Complete the monthly report",
        hours_spent=5,
        completed=False
    )
    print(valid_task)

    # Invalid cases
    try:
        invalid_task = EmployeeTask(
            employee_id=-5,
            employee_name="Asha",
            email="asha@ust",
            mobile="98765432101",
            band="B5",
            task_id=-10,
            task_title="Hi",
            task_description="Update",
            hours_spent=0,
            completed="yes"
        )
    except ValueError as e:
        print(e)

test_employee_task()
