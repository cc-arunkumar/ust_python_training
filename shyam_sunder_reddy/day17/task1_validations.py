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


class EmployeeTask(BaseModel):
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
    remarks: Optional[str]=None
    client_feedback: Optional[str]
    
def validate(emp:EmployeeTask):
    sum=0
    for sub in emp.subtasks:
        sum+=sub.hours_spent
    if sum>emp.hours_spent:
        print( "sum of subtask hours cannot exceed task hours")
        
    for sub in emp.subtasks:
        if not sub.completed and emp.completed:
            print( "cannot complete task with incomplete subtasks")
            
    for skill in emp.skills:
        if skill.lower() =="python" and emp.priority==PriorityEnum.low:
            print( "tasks with Python skill cannot have low priority")

    for att in emp.attachments:
        if att.file_name.lower().endswith(".docx"):
            # Check if task_id is present in filename
            if str(emp.task_id) not in att.file_name:
                print( "docx attachments must include task_id") 

    if emp.hours_spent>8 and emp.remarks is None :
        print( "remarks required when hours > 8")
      
    if emp.band==BandEnum.B3 and emp.cost_center[0:2]=="HR":
        print(   "B3 band cannot work on HR cost centers")

    if emp.priority==PriorityEnum.high:
        if emp.client_feedback is None:
            print( "client_feedback must be ≥10 chars for high priority completed tasks")
        elif len(emp.client_feedback) <10:
            print( "client_feedback must be ≥10 chars for high priority completed tasks")

    #start and end in the range
    start = emp.start_date
    end = emp.end_date

    fy_start = date(start.year, 4, 1)
    fy_end = date(start.year + 1, 3, 31)

    if not (fy_start <= start <= fy_end and fy_start <= end <= fy_end):
        print( "task dates must be within fiscal year")
    
    #Emergency contact
    if emp.mobile!=emp.emergency_contact:
        print(  "emergency_contact cannot be same as mobile")
    
    #skills 33
    if "hacking" in emp.skills:
        print("skills contain forbidden items")
        
    #attachments 34
    for att in emp.attachments:
        if att.size_kb>=5000:
            print( "attachment size exceeds limit")
    
    #hours_spent 35
    if emp.priority==PriorityEnum.high and emp.hours_spent>8:
        print("hours_spent exceeds daily limit for high priority")
        
    print("ALL GOOD!")

######################################

task1 = EmployeeTask(
    employee_id=1,
    employee_name="Alice",
    email="alice@example.com",
    mobile="1234567890",
    band=BandEnum.B2,
    emergency_contact="9876543210",
    task_id=101,
    task_title="Data Analysis",
    task_description="Analyze sales data",
    priority=PriorityEnum.high,
    hours_spent=10,
    subtasks=[
        SubTask(subtask_id=1, title="Collect Data", hours_spent=5),
        SubTask(subtask_id=2, title="Analyze Data", hours_spent=5),
    ],
    project_code="PRJ001",
    cost_center="FI-101",
    asset_code="AST001",
    supervisor_id=200,
    department="Finance",
    location="Mumbai",
    start_date=date(2025, 4, 1),
    end_date=date(2025, 4, 10),
    skills=["Python", "SQL"],
    attachments=[Attachment(file_name="report.pdf", size_kb=500)],
    remarks="Completed successfully",
    client_feedback="Well done"
)

task2 = EmployeeTask(
    employee_id=2,
    employee_name="Bob",
    email="bob@example.com",
    mobile="1234567890",
    band=BandEnum.B3,
    emergency_contact="1234567890",
    task_id=102,
    task_title="Testing",
    task_description="Test application",
    priority=PriorityEnum.low,
    hours_spent=10,
    subtasks=[
        SubTask(subtask_id=1, title="Unit Test", hours_spent=6),
        SubTask(subtask_id=2, title="Integration Test", hours_spent=5),
    ],
    project_code="PRJ002",
    cost_center="HR-102",
    asset_code="AST002",
    supervisor_id=201,
    department="QA",
    location="Pune",
    start_date=date(2025, 4, 5),
    end_date=date(2026, 4, 15),
    skills=["python","Testing", "Automation"],
    attachments=[Attachment(file_name="testplan.docx", size_kb=300)],
    client_feedback=None,
    completed=True
)

######################################

#32




#61
# print(subtask_hours(task1)) 
# print(subtask_hours(task2))
# Sample output
# 10
# sum of subtask hours cannot exceed task hours

#################################
#62
# print(subtask_completion(task1))
# print(subtask_completion(task2))
# Sample Output
# Completed
# cannot complete task with incomplete subtasks

##############################
#63
# print(skill_dependency(task1))
# print(skill_dependency(task2))
# Sample output
# ALL GOOD!
# tasks with Python skill cannot have low priority

###############################
#65
# print(attachments(task1))
# print(attachments(task2))
# Sample output
# ALL GOOD!
# docx attachments must include task_id

###############################
#66
# print(depandent_remark(task1))
# print(depandent_remark(task2))
# Sample output
# ALL GOOD!
# remarks required when hours > 8

###############################
#67
# print(Band_Project(task1))
# print(Band_Project(task2))
# Sample output
# ALL GOOD!
# B3 band cannot work on HR cost centers

################################
#68
# print(Client_feedback(task1))
# print(Client_feedback(task2))
# Sample output
# client_feedback must be ≥10 chars for high priority completed tasks
# ALL GOOD!

################################
#69
# print(start_end(task1))
# print(start_end(task2))
# Sample output
# ALL GOOD!
# task dates must be within fiscal year

################################


validate(task1)
print("################")
validate(task2)