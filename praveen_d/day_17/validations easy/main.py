from pydantic import BaseModel, field_validator,Field
from enum import Enum
from typing import List
from datetime import date
from fastapi import FastAPI,HTTPException
import re
app=FastAPI()

class BandEnum(str, Enum):
 B1 = "B1"
 B2 = "B2"
 B3 = "B3"
 M1 = "M1"
 
class EmployeeTask(BaseModel):
 # Employee Info
 employee_id: int=Field()
 @field_validator('employee_id')
 def emp_id_validation(cls,value):
    if value<=0:
        raise HTTPException(status_code=404,detail="The integer should be positive")
    print(f"Employee ID: {value}")  # Debugging print statement
    return value

 employee_name: str
 @field_validator('employee_name')
 def emp_name_validation(cls,value):
     if len(value)<3 or value.strip()=="":
         raise HTTPException(status_code=404,detail="employee_name must be at least 3 characters")
     return value
     
 email: str
 # Scenario 3 — email
# Validation: Must be a valid email
# Valid: "rahul.menon@ust.com" , "asha.nair@ust.com"
# Invalid: "rahul.menonust.com" , "asha@ust"
# Expected Error: ""
 @field_validator('email')
 def emp_email_validator(cls,value):
     if not re.match(r"^[A-Za-z]+@+.com$",value):
         raise HTTPException(status_code=404,detail="email must be a valid email address") 
     else:
         return value
         
 mobile: str
 band: BandEnum
 # Task Info
 task_id: int
 task_title: str
 task_description: str
 hours_spent: int
 completed: bool = False



# Scenario 4 — mobile
# Validation: Must be 10 digits
# Valid: "9876543210" , "9123456789"
# Validation Practice 2
# Invalid: "12345" , "98765432101"
# Expected Error: "mobile must be exactly 10 digits"
# Scenario 5 — band
# Validation: Enum → Allowed: B1, B2, B3, M1
# Valid: "B1" , "M1"
# Invalid: "B5" , "C2"
# Expected Error: "band must be one of: B1, B2, B3, M1"
# Scenario 6 — task_id
# Validation: Positive integer, cannot equal employee_id
# Valid: 501 (employee_id=101), 102 (employee_id=100)
# Invalid: -10, 101 (employee_id=101)
# Expected Errors:
# "task_id must be positive"
# "task_id cannot be same as employee_id"
# Scenario 7 — task_title
# Validation: String, min 3 chars
# Valid: "Prepare Report" , "QA Testing"
# Invalid: "Hi" , ""
# Expected Error: "task_title must be at least 3 characters"
# Scenario 8 — task_description
# Validation: String, min 10 chars
# Valid: "Complete the monthly report" , "Test login thoroughly"
# Validation Practice 3
# Invalid: "Too short" , "Update"
# Expected Error: "task_description must be at least 10 characters"
# Scenario 9 — hours_spent
# Validation: Integer, 1–12
# Valid: 5, 8
# Invalid: 0, 15
# Expected Error: "hours_spent must be between 1 and 12"
# Scenario 10 — completed
# Validation: Boolean, default False
# Valid: True, False
# Invalid: "yes" , 1
# Expected Error: "completed must be a boolean"
@app.post('/tasks')
def emp_id_validation(emp:EmployeeTask):
    return{"Task has been created"}
