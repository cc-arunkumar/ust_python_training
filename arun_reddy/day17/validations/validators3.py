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

class SubTask(BaseModel):
    subtask_id: int
    title: str
    hours_spent: int
    completed: bool = False
    attachments: Optional[List[Attachment]] = []  # needed for Scenario 70

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
    subtasks: Optional[List[SubTask]] = []

    # Project Info
    project_code: str
    cost_center: str
    asset_code: str
    supervisor_id: int
    department: str
    location: str

    # Dates
    start_date: date
    end_date: date

    # Additional Info
    skills: List[str]
    attachments: List[Attachment]
    remarks: Optional[str]
    client_feedback: Optional[str]


# Simulated in-memory store of tasks in the "current project"
TasksInProject: List[EmployeeTask] = []


def checking_tasks(task: EmployeeTask):
    # Scenario 61 — Subtask hours
    if task.subtasks:
        sums = 0
        for K in task.subtasks:
            sums += K.hours_spent
        if sums > task.hours_spent:
            return {"sum of subtask hours cannot exceed task hours"}

    # Scenario 62 — Subtask completion
    if task.subtasks:
        for K in task.subtasks:
            if K.completed is False and task.completed is True:
                return {"cannot complete task with incomplete subtasks"}

    # Scenario 63 — Skill dependency
    if task.skills:
        if "python" in task.skills and task.priority == PriorityEnum.low:
            return {"tasks with Python skill cannot have low priority"}

    # Scenario 64 — Emergency contact cannot match any supervisor_id in current project (simulate in memory)
    # Compare against supervisor_id of tasks with the same project_code
    if task.emergency_contact:
        for T in TasksInProject:
            if T.project_code == task.project_code:
                if task.emergency_contact == str(T.supervisor_id):
                    return {"emergency_contact cannot match supervisor_id"}

    # Scenario 65 — Attachments naming (.docx must include task_id)
    if task.attachments:
        for A in task.attachments:
            if A.file_name.lower().endswith(".docx"):
                if str(task.task_id) not in A.file_name:
                    return {"docx attachments must include task_id"}

    # Scenario 66 — Dependent remarks (hours_spent > 8 requires remarks)
    if task.hours_spent > 8 and (task.remarks is None or task.remarks.strip() == ""):
        return {"remarks required when hours > 8"}

    # Scenario 67 — Band and project (B3 cannot work on HR cost centers)
    if task.band == BandEnum.B3 and task.cost_center.startswith("HR"):
        return {"B3 band cannot work on HR cost centers"}

    # Scenario 68 — Client feedback dependency (completed + high requires client_feedback ≥ 10 chars)
    if task.completed is True and task.priority == PriorityEnum.high:
        if task.client_feedback is None or len(task.client_feedback.strip()) < 10:
            return {"client_feedback must be ≥10 chars for high priority completed tasks"}

    # Scenario 69 — Start/End cross-check within fiscal year (01-Apr to 31-Mar next year)
    # Determine fiscal year window based on start_date
    fy_start_year = task.start_date.year if task.start_date.month >= 4 else task.start_date.year - 1
    fy_start = date(fy_start_year, 4, 1)
    fy_end = date(fy_start_year + 1, 3, 31)
    if not (fy_start <= task.start_date <= fy_end and fy_start <= task.end_date <= fy_end):
        return {"task dates must be within fiscal year"}

    # Scenario 70 — Nested attachments (each subtask attachment ≤ 2000 KB)
    if task.subtasks:
        for ST in task.subtasks:
            if ST.attachments:
                for A in ST.attachments:
                    if A.size_kb > 2000:
                        return {"subtask attachment size cannot exceed 2000"}




# # Helper to register tasks in project memory
# def register_task(task: EmployeeTask):
#     TasksInProject.append(task)
#     return task

# # Base valid task to derive variants
# base_task = EmployeeTask(
#     employee_id=1,
#     employee_name="Alice",
#     email="alice@example.com",
#     mobile="9876543210",
#     band="B1",
#     emergency_contact="8765432109",
#     task_id=501,
#     task_title="Main Task",
#     task_description="Main description",
#     priority="medium",
#     hours_spent=10,
#     completed=False,
#     subtasks=[
#         SubTask(subtask_id=1, title="ST1", hours_spent=5, completed=True, attachments=[Attachment(file_name="st1.pdf", size_kb=1500)]),
#         SubTask(subtask_id=2, title="ST2", hours_spent=5, completed=True, attachments=[Attachment(file_name="st2.pdf", size_kb=1500)]),
#     ],
#     project_code="PRJ-XYZ",
#     cost_center="FI-101",
#     asset_code="ASSET1",
#     supervisor_id=100,
#     department="Finance",
#     location="Kochi",
#     start_date=date(2025, 4, 1),
#     end_date=date(2026, 3, 30),
#     skills=["excel"],
#     attachments=[Attachment(file_name="task501_plan.docx", size_kb=200)],  # includes task_id
#     remarks="All good",
#     client_feedback=None
# )

# # Register a task in project for emergency_contact cross-check baseline
# register_task(base_task)

# # Scenario 61 — Subtask hours
# valid_61 = base_task.copy(update={"subtasks": [SubTask(subtask_id=1, title="A", hours_spent=5, completed=True),
#                                                SubTask(subtask_id=2, title="B", hours_spent=5, completed=True)]})
# invalid_61 = base_task.copy(update={"subtasks": [SubTask(subtask_id=1, title="A", hours_spent=6, completed=True),
#                                                  SubTask(subtask_id=2, title="B", hours_spent=5, completed=True)]})

# print("61 valid:", checking_tasks(valid_61))      # {"status": "valid"}
# print("61 invalid:", checking_tasks(invalid_61))  # {"sum of subtask hours cannot exceed task hours"}

# # Scenario 62 — Subtask completion
# valid_62 = base_task.copy(update={"completed": True})
# invalid_62 = base_task.copy(update={"completed": True,
#                                     "subtasks": [SubTask(subtask_id=1, title="A", hours_spent=5, completed=False)]})
# print("62 valid:", checking_tasks(valid_62))      # {"status": "valid"}
# print("62 invalid:", checking_tasks(invalid_62))  # {"cannot complete task with incomplete subtasks"}

# # Scenario 63 — Skill dependency
# valid_63 = base_task.copy(update={"skills": ["python"], "priority": "medium"})
# invalid_63 = base_task.copy(update={"skills": ["python"], "priority": "low"})
# print("63 valid:", checking_tasks(valid_63))      # {"status": "valid"}
# print("63 invalid:", checking_tasks(invalid_63))  # {"tasks with Python skill cannot have low priority"}

# # Scenario 64 — Emergency contact cannot match any supervisor_id in current project
# # Create another task in same project with supervisor_id 200 and test
# other_task_same_project = register_task(base_task.copy(update={"task_id": 502, "supervisor_id": 200}))
# valid_64 = base_task.copy(update={"emergency_contact": "5555555555"})
# invalid_64 = base_task.copy(update={"emergency_contact": "200"})  # matches supervisor_id of other task
# print("64 valid:", checking_tasks(valid_64))      # {"status": "valid"}
# print("64 invalid:", checking_tasks(invalid_64))  # {"emergency_contact cannot match supervisor_id"}

# # Scenario 65 — Attachments naming
# valid_65 = base_task.copy(update={"attachments": [Attachment(file_name="task501_plan.docx", size_kb=300)]})
# invalid_65 = base_task.copy(update={"attachments": [Attachment(file_name="plan.docx", size_kb=300)]})
# print("65 valid:", checking_tasks(valid_65))      # {"status": "valid"}
# print("65 invalid:", checking_tasks(invalid_65))  # {"docx attachments must include task_id"}

# # Scenario 66 — Dependent remarks
# valid_66 = base_task.copy(update={"hours_spent": 9, "remarks": "Extra work"})
# invalid_66 = base_task.copy(update={"hours_spent": 9, "remarks": None})
# print("66 valid:", checking_tasks(valid_66))      # {"status": "valid"}
# print("66 invalid:", checking_tasks(invalid_66))  # {"remarks required when hours > 8"}

# # Scenario 67 — Band and project
# valid_67 = base_task.copy(update={"band": "B3", "cost_center": "FI-101"})
# invalid_67 = base_task.copy(update={"band": "B3", "cost_center": "HR-202"})
# print("67 valid:", checking_tasks(valid_67))      # {"status": "valid"}
# print("67 invalid:", checking_tasks(invalid_67))  # {"B3 band cannot work on HR cost centers"}

# # Scenario 68 — Client feedback dependency
# valid_68 = base_task.copy(update={"completed": True, "priority": "high", "client_feedback": "Well done team!"})
# invalid_68 = base_task.copy(update={"completed": True, "priority": "high", "client_feedback": "OK"})
# print("68 valid:", checking_tasks(valid_68))      # {"status": "valid"}
# print("68 invalid:", checking_tasks(invalid_68))  # {"client_feedback must be ≥10 chars for high priority completed tasks"}

# # Scenario 69 — Start/End cross-check fiscal year
# valid_69 = base_task.copy(update={"start_date": date(2025, 4, 1), "end_date": date(2026, 3, 30)})
# invalid_69 = base_task.copy(update={"start_date": date(2025, 3, 30), "end_date": date(2026, 4, 1)})
# print("69 valid:", checking_tasks(valid_69))      # {"status": "valid"}
# print("69 invalid:", checking_tasks(invalid_69))  # {"task dates must be within fiscal year"}

# # Scenario 70 — Nested attachments (per subtask)
# valid_70 = base_task.copy(update={"subtasks": [SubTask(subtask_id=1, title="A", hours_spent=3, completed=True,
#                                                        attachments=[Attachment(file_name="a.pdf", size_kb=1500)])]})
# invalid_70 = base_task.copy(update={"subtasks": [SubTask(subtask_id=1, title="A", hours_spent=3, completed=True,
#                                                          attachments=[Attachment(file_name="a.pdf", size_kb=2500)])]})
# print("70 valid:", checking_tasks(valid_70))      # {"status": "valid"}
# print("70 invalid:", checking_tasks(invalid_70))  # {"subtask attachment size cannot exceed 2000"}
