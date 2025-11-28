from pydantic import BaseModel, EmailStr
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

class Attachment(BaseModel):
    file_name: str
    size_kb: int

class EmployeeTask(BaseModel):
    # Employee Info
    employee_id: int
    employee_name: str
    email: EmailStr
    mobile: str
    band: BandEnum
    emergency_contact: str

    # Task Info
    task_id: int
    task_title: str
    task_description: str
    priority: PriorityEnum
    hours_spent: int
    completed: bool = False

    # Project Info
    project_code: str
    cost_center: str
    asset_code: str
    supervisor_id: int
    department: str
    location: str
    supervisor_approved: bool = False   # fixed
    # Dates
    start_date: date
    end_date: date
    project_timeline: int = 10          # fixed

    # Additional Info
    skills: List[str]
    attachments: List[Attachment]
    remarks: Optional[str]
    client_feedback: Optional[str]


Employees = []


def checking(task: EmployeeTask):
    # Unique employee_id
    for K in Employees:
        if K.employee_id == task.employee_id:
            return {"employee_id must be unique"}

    # Emergency contact check
    if task.mobile == task.emergency_contact:
        return {"emergency_contact cannot be same as mobile"}

    # Skills check
    if task.skills:
        for K in task.skills:
            if K not in ["python", "excel"]:
                return {"skills contain forbidden items"}

    # Attachments check
    if task.attachments:
        for K in task.attachments:
            if K.size_kb > 5000:
                return {"attachment size exceeds limit"}

    # Priority + hours check
    if task.priority == PriorityEnum.high and task.hours_spent > 8:
        return {"hours_spent exceeds daily limit for high priority"}

    # Weekend start_date check
    if task.start_date.weekday() in (5, 6):
        return {"start_date cannot be a weekend"}

    if task.client_feedback is None and task.completed is True:
        return {"client_feedback required when task is completed"}

    if task.band == BandEnum.B1 and task.priority == PriorityEnum.high:
        return {"B1 band cannot have high priority tasks"}

    if task.cost_center:
        matchs = task.department[0:2].upper()
        if not task.cost_center.startswith(matchs):
            return {"cost_center must match department code"}

    if task.project_code:
        for K in Employees:
            if K.project_code == task.project_code:
                return {"project_code already in use"}

    if task.skills:
        my_dict = {}
        for K in task.skills:
            my_dict[K] = my_dict.get(K, 0) + 1
        for k, v in my_dict.items():
            if v == 3:
                return {"skill usage exceeded maximum allowed"}

    if task.task_id:
        for K in Employees:
            if K.task_id == task.task_id:
                return {"task_id already exists in this project"}

    if task.hours_spent < 1 and task.completed is True:
        return {"cannot complete task with 0 hours spent"}

    if task.priority == PriorityEnum.high and task.supervisor_approved is False:
        return {"high priority tasks require supervisor approval"}

    if task.end_date.weekday() in (5, 6):   # fixed logic
        return {"end_date cannot be on weekend"}

    if task.attachments:
        sums = 0
        for K in task.attachments:
            sums += K.size_kb
        if sums > 10000:
            return {"total attachment size exceeds limit"}

    if task.client_feedback and len(task.client_feedback) > 500:
        return {"client_feedback exceeds 500 characters"}

    if task.band == BandEnum.M1 and task.hours_spent > 10:
        return {"M1 band cannot have hours_spent > 10"}

    if (task.end_date - task.start_date).days > task.project_timeline:
        return {"task dates must be within project timeline"}

  

# # Valid case
# task1 = EmployeeTask(
#     employee_id=1,
#     employee_name="Alice",
#     email="alice@ust.com",
#     mobile="9876543210",
#     band="B1",
#     emergency_contact="8765432109",
#     task_id=101,
#     task_title="Monthly Report",
#     task_description="Prepare monthly financial report",
#     priority="low",
#     hours_spent=5,
#     project_code="PRJ001",
#     cost_center="FI-123",
#     asset_code="ASSET1",
#     supervisor_id=2,
#     department="Finance",
#     location="Kochi",
#     start_date=date(2025, 1, 13),  # Monday
#     end_date=date(2025, 1, 15),
#     skills=["python", "excel"],
#     attachments=[Attachment(file_name="report.pdf", size_kb=200)],
#     remarks="Completed on time",
#     client_feedback="Good work"
# )
# print(checking(task1))
# # → {"status": "valid"}

# # Invalid: emergency_contact same as mobile
# task2 = task1.copy(update={"emergency_contact": "9876543210"})
# print(checking(task2))
# # → {"emergency_contact cannot be same as mobile"}

# # Invalid: forbidden skill
# task3 = task1.copy(update={"skills": ["java"]})
# print(checking(task3))
# # → {"skills contain forbidden items"}

# # Invalid: attachment too large
# task4 = task1.copy(update={"attachments": [Attachment(file_name="bigfile.pdf", size_kb=6000)]})
# print(checking(task4))
# # → {"attachment size exceeds limit"}

# # Invalid: high priority with too many hours
# task5 = task1.copy(update={"priority": "high", "hours_spent": 10})
# print(checking(task5))
# # → {"hours_spent exceeds daily limit for high priority"}

# # Invalid: start_date on weekend
# task6 = task1.copy(update={"start_date": date(2025, 1, 12)})
# print(checking(task6))
# # → {"start_date cannot be a weekend"}

# # Invalid: high priority without supervisor approval
# task7 = task1.copy(update={"priority": "high", "supervisor_approved": False})
# print(checking(task7))
# # → {"high priority tasks require supervisor approval"}

# # Invalid: total attachment size exceeds limit
# task8 = task1.copy(update={"attachments": [
#     Attachment(file_name="a.pdf", size_kb=6000),
#     Attachment(file_name="b.pdf", size_kb=5000)
# ]})
# print(checking(task8))
# # → {"total attachment size exceeds limit"}

# # Invalid: client_feedback too long
# task9 = task1.copy(update={"client_feedback": "x" * 600})
# print(checking(task9))
# # → {"client_feedback exceeds 500 characters"}

# # Invalid: M1 band with too many hours
# task10 = task1.copy(update={"band": "M1", "hours_spent": 12})
# print(checking(task10))
# # → {"M1 band cannot have hours_spent > 10"}

# # Invalid: project timeline exceeded
# task11 = task1.copy(update={"start_date": date(2025, 1, 1), "end_date": date(2025, 2, 15)})
# print(checking(task11))
# # → {"task dates must be within project timeline"}
