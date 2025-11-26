from pydantic import BaseModel, field_validator,EmailStr,model_validator
from enum import Enum
from typing import List
from datetime import date,timedelta
from fastapi import FastAPI,HTTPException
import re
app=FastAPI()

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
 employee_name: str
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
 # Project Info
 project_code: str
 @field_validator('project_code')
 def project_code_validator(cls,value):
     if not re.match((r"^[A-Z]+[0-9]"),value) or len(value)<8 :
         raise HTTPException(detail="project_code must be 3–8 uppercase letters/numbers")
     return value
         
 cost_center: str
 @field_validator('cost_center')
 def cost_center_validator(cls,value):
      if not re.match(r"^[A-Z]{2}-[0-9]{3}$", value):
            raise HTTPException(status_code=400, detail="cost_center format invalid")
      return value
     
 asset_code: str
 @field_validator('asset_code')
 def asset_code_validator(cls,value):
     if not re.match((r"^[A-Z]+[0-9]"),value) or len(value)<8 :
         raise HTTPException(detail="asset_code must be 3–8 uppercase letters/numbers")
     return value
     
 supervisor_id: int
 @field_validator('supervisor_id')
 def supervisor_id_validator(cls,value):
     if value==EmployeeTask.employee_id:
         raise HTTPException("supervisor_id cannot be same as employee_id")
     if value<=0:
          raise HTTPException("supervisor_id must be positive")
     return value
         

 department: str
 @field_validator('department')
 def department_validatior(cls,value):
     if not re.match(r"^[A-Za-z]") or len(value)<4:
          raise HTTPException("department must contain only letters")
     return value
         
 location: str
 # Dates
 start_date: date
 @model_validator(pre=True)
 def department_validatior(cls,value):
     s_date=value.get('start_date')
     e_date=value.get('end_date')
     if s_date>e_date:
         raise HTTPException("start_date cannot be in the past") 
     return value
     
         
 end_date: date
 
 @model_validator(pre=True)
 def start_to_end_time_validatior(cls,value):
     start_date=value.get('start_date')
     end_date=value.get('end_date')
     if end_date>start_date+timedelta(days=30):
           raise HTTPException("end_date must be within 30 days of start_date") 
     return value
         
 
 skills: List[str]
 attachments: List[str]
 remarks: str

@app.post("/tasks")
def create(emp:EmployeeTask):
    return {"New task created"}