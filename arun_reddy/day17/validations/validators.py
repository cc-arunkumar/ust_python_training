from pydantic import BaseModel, EmailStr, Field
from enum import Enum
from typing import List, Optional
from datetime import date



class BandEnum(str, Enum):
    B1 = "B1"
    B2 = "B2"
    B3 = "B3"
    M1 = "M1"


class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class EmployeeTask(BaseModel):
    # Employee Info
    employee_id: int
    employee_name: str = Field(pattern=r"^[A-Za-z]+$", min_length=3, max_length=8)
    email: EmailStr
    mobile: str
    band: BandEnum

    # Task Info
    task_id: int
    task_title: str
    task_description: str
    priority: PriorityEnum
    hours_spent: int
    completed: bool = False
    project_code: str
    cost_center: str = Field(pattern=r"^[A-Z]{2}-\d{3}$")
    asset_code: str = Field(pattern=r"^[A-Z]+\d+[A-Z0-9]*$", min_length=5, max_length=10)
    department: str = Field(pattern=r"^[A-Za-z]+$", min_length=3)
    start_date: date
    end_date: date
    location: str = Field(pattern=r"^[A-Za-z]+$", description="Must be a valid city name")
    supervisor_id: int = Field(gt=0)
    skills: List[str]
    attachments: List[str]
    remarks: Optional[str]


def validate_task(task: EmployeeTask):
    # Supervisor check
    if task.supervisor_id == task.employee_id:
        return {"supervisor_id cannot equal employee_id"}

    # Date check
    if task.end_date < task.start_date:
        return {"end_date must be after start_date"}

    # Hours spent check
    if task.hours_spent <= 0 or task.hours_spent > 12:
        return {"hours_spent must be between 1 and 12"}

    # Skills check
    if len(task.skills) == 0:
        return {"skills list must contain at least one skill"}
    else:
        seen = set()
        for skill in task.skills:
            if len(skill) < 2:
                return {"each skill must be at least 2 characters"}
            if skill in seen:
                return {"skills cannot contain duplicates"}
            seen.add(skill)

    # Attachments check
    for file in task.attachments:
        if file.strip() == "":
            return {"attachments must be non-empty"}
        elif not file.lower().endswith(".pdf"):
            return {"all attachments must be pdf files"}

    # Remarks check
    if task.remarks and len(task.remarks) < 5:
        return {"remarks must be at least 5 characters"}

    # Mobile check
    if not task.mobile.startswith(('6', '7', '8', '9')):
        return {"mobile must start with 6,7,8, or 9"}

    # Email domain check
    parts = task.email.split('@')
    if parts[1] != "ust.com":
        return {"email must end with @ust.com"}

    # Title/description length check
    if len(task.task_title) > 50:
        return {"task_title must not exceed 50 characters"}
    if len(task.task_description) > 300:
        return {"task_description must not exceed 300 characters"}

    return {"status": "valid"}




# # Valid case
# task1 = EmployeeTask(
#     employee_id=1,
#     employee_name="Alice",
#     email="alice@ust.com",
#     mobile="9876543210",
#     band="B1",
#     task_id=101,
#     task_title="Monthly Report",
#     task_description="Prepare monthly financial report",
#     priority="low",
#     hours_spent=5,
#     project_code="PRJ001",
#     cost_center="AB-123",
#     asset_code="ASSET1",
#     department="Finance",
#     start_date=date(2025, 1, 10),
#     end_date=date(2025, 1, 15),
#     location="Kochi",
#     supervisor_id=2,
#     skills=["excel", "analysis"],
#     attachments=["report.pdf"],
#     remarks="Completed on time"
# )
# print(validate_task(task1))
# # → {"status": "valid"}


# # Invalid: supervisor_id == employee_id
# task2 = task1.copy(update={"supervisor_id": 1})
# print(validate_task(task2))
# # → {"supervisor_id cannot equal employee_id"}


# # Invalid: end_date before start_date
# task3 = task1.copy(update={"end_date": date(2025, 1, 5)})
# print(validate_task(task3))
# # → {"end_date must be after start_date"}


# # Invalid: mobile not starting with 6–9
# task4 = task1.copy(update={"mobile": "1234567890"})
# print(validate_task(task4))
# # → {"mobile must start with 6,7,8, or 9"}


# # Invalid: email domain not ust.com
# task5 = task1.copy(update={"email": "alice@gmail.com"})
# print(validate_task(task5))
# # → {"email must end with @ust.com"}


# # Invalid: skills duplicate
# task6 = task1.copy(update={"skills": ["python", "python"]})
# print(validate_task(task6))
# # → {"skills cannot contain duplicates"}
