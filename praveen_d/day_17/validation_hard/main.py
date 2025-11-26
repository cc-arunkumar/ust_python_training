from pydantic import BaseModel, EmailStr, field_validator,model_validator
from enum import Enum
from typing import List, Optional
from datetime import date
from fastapi import FastAPI,HTTPException
emp_ids_list=[]
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
 @field_validator('employee_id')
 def employe_id_validatior(cls,value):
     for val in emp_ids_list:
         if value==val:
             raise HTTPException("employee_id must be unique")
         return value
 employee_name: str
 email: EmailStr
 mobile: str
 band: BandEnum
 emergency_contact: str
 # Task Info
 task_id: int
 task_title: str
 @model_validator(pre=True)
 def validate_task_title(cls, values):
        task_title = values.get('task_title', '')

        # Check if any banned word is in the task title
        for banned_word in cls.banned_words:
            if banned_word in task_title.lower():
                raise ValueError("task_title contains banned words")
        return values
 task_description: str
 priority: PriorityEnum
 @model_validator(pre=True)
 def employe_id_validatior(cls,value):
     band=value.get('band')
     priority=value.get('priority')
     if band=="B1" and priority=="high":
         raise HTTPException(detail= "B1 band cannot have high priority tasks")
     return value
 hours_spent: int
 completed: bool = False
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
#  Scenario 42 — attachments
# Validation: Must include at least one PDF and one docx
# Valid: [{"file_name":"plan.pdf","size_kb":200},{"file_name":"notes.docx","size_kb":100}]
# Invalid: [{"file_name":"plan.pdf","size_kb":200}]
# Error: "attachments must include PDF and DOCX"
@model_validator(pre=True)
def employe_id_validatior(cls,value):
     for attachment in cls.attachments:
            if attachment.file_name.lower().endswith('.pdf'):
                has_pdf = True
            if attachment.file_name.lower().endswith('.docx'):
                has_docx = True
     if not has_pdf or not has_docx:
         raise HTTPException("attachments must include PDF and DOCX")
     return value
         
        
 remarks: Optional[str]
 # Optional conditional field
 client_feedback: Optional[str]


 
 