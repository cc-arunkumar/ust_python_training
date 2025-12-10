from pydantic import BaseModel,EmailStr,field_validator,model_validator
from enum import Enum
from typing import List, Optional
from datetime import date

class BandEnum(str, Enum):
    
    B1 ="B1"
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
    completed: bool= False


class EmployeeTask(BaseModel):
 # Employee Info
    employee_id: int
    employee_name: str
    email: EmailStr
    mobile: str
    band: BandEnum
    emergency_contact: str
    task_id: int
    task_title: str
    task_description: str
    priority: PriorityEnum
    hours_spent: int
    completed: bool = False
    subtasks: Optional[List[SubTask]] = []
    project_code: str
    cost_center: str
    asset_code: str
    supervisor_id: int
    department: str
    location: str
    start_date: date
    end_date: date
    skills: List[str]
    attachments: List[Attachment]
    remarks: Optional[str]
    client_feedback: Optional[str]
                
    @model_validator(mode="after")
    def validate_all_tasks(cls,model):
        total_subtask_hours = 0;
        if model.subtasks:
            for st in model.subtasks:
                total_subtask_hours+=st.hours_spent
            if total_subtask_hours>model.hours_spent:
                raise ValueError("sum of subtasks hours cannot be greater than task hours")

        if model.completed:
            if model.subtasks:
                for st in model.subtasks:
                    if not st.completed:
                        raise ValueError(
                            "Task cannot be marked completed=True if any subtask is incomplete"
                        )
        if model.skills:
            if model.priority:
                for sk in model.skills:
                    if sk=="python" and model.priority=="low":
                        raise ValueError("tasks with Python skill cannot have low priority")
        
        if model.emergency_contact and model.supervisor_id:
            if model.emergency_contact == str(model.supervisor_id):
                raise ValueError("emergency_contact cannot match supervisor_id")

        for att in model.attachments:
            if att.file_name.endswith(".docx") and str(model.task_id) not in att.file_name:
                raise ValueError("docx attachments must include task_id")

        if model.hours_spent > 8 and not model.remarks:
            raise ValueError("remarks required when hours > 8")

        if model.band == BandEnum.B3 and model.cost_center.startswith("HR"):
            raise ValueError("B3 band cannot work on HR cost centers")

        if model.completed and model.priority == PriorityEnum.high:
            if not model.client_feedback or len(model.client_feedback) < 10:
                raise ValueError("client_feedback must be ≥10 chars for high priority completed tasks")

        # Scenario 69 — Start/End cross-check (must be within fiscal year Apr–Mar)
        fiscal_start = date(model.start_date.year, 4, 1)
        fiscal_end = date(model.start_date.year + 1, 3, 31)
        if not (fiscal_start <= model.start_date <= fiscal_end and fiscal_start <= model.end_date <= fiscal_end):
            raise ValueError("task dates must be within fiscal year (Apr 1 – Mar 31)")

        for st in model.subtasks or []:
            for att in st.attachments or []:
                if att.size_kb > 2000:
                    raise ValueError("subtask attachment size cannot exceed 2000 KB")

        return model
            
        
                
        
    
