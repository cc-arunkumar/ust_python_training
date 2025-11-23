from fastapi import FastAPI, HTTPException,Query
from pydantic import BaseModel,Field,field_validator
from typing import Optional
import re

app = FastAPI(title="UST Employee Telecom DeviceRegistration")

class EmployeeModel(BaseModel):
    emp_id:int = Field(...,ge=1000,le=999999,description="id in between 1000 and 999999")
    name:str = Field(...,min_length=2,description="Name length should be minimum 2")
    official_email:str
    department:Optional[str] = Field(default="Telecom")
    location:Optional[str] = Field(default="Bamgaluru")
    
# constr(regex=r'^[a-zA-Z0-9._%+-]+@ust\.com$') = Field(...,description="email structure does not match")
@field_validator('official_email')
@classmethod
def email_regex(cls,v):
    if not re.match(r'^[a-zA-Z0-9._%+-]+@ust.com$',v):
        raise ValueError("Email error")
    return v
    
class SimModel(BaseModel):
    number:str = Field(...,max_length=10,min_length=10,description="invalid phone number")
    provider:Optional[str] = Field(default="Jio")
    is_esim:Optional[bool] = Field(default=False)
    activation_year:int = Field(...,ge=2020,le=2025,description="activation year is invalid")
    
class DataPlan(BaseModel):
    name:str = Field(...,min_length=3,max_length=50,description="name length should between 3 and 50")
    monthly_gb:int = Field(...,gt=0,le=1000,description="monthly gb should between 0 amd 1000")
    speed_mbps:Optional[int] = Field(default=50,ge=1,le=1000)
    is_roaming_included:Optional[bool] = Field(default=False)

class VoicePlan(BaseModel):
    name:str = Field(...,min_length=3,description="name length should be minimum 3")
    monthly_minutes:int = Field(...,ge=0,le=1000,description="monthly minutes should between 0 and 1000")
    has_isd:Optional[bool] = Field(default=False)
    per_minute_charge_paise:Optional[int] = Field(default=0,ge=0,le=1000)
    
class EmergencyContact(BaseModel):
    name:str = Field(...,min_length=2,description="name length should be minimum 2")
    relation:str = Field(default="Family")
    phone:str = Field(...,pattern=r"^[6-9]d{9}$",description="Invalid phome number")
    per_minute_charge_paise:Optional[int] = Field(default=0,ge=0,le=1000)

class EmployeeTelecomProfile(BaseModel):
    employee:EmployeeModel = Field(...,description="Missing mandatory field") 
    sim:SimModel = Field(...,description="Missing mandatory field") 
    data_plan:Optional[DataPlan] 
    voice_plan:Optional[VoicePlan] 
    emergency_contact:Optional[EmergencyContact] 
    

       
    
data = []

@app.post("/telocom/profiles")
def profile(employees:EmployeeTelecomProfile):
    for i in data:
        if employees.employee.emp_id == i.employee.emp_id:
            raise HTTPException(status_code=409,detail="employee id already exist")
    data.append(employees)
    return {"Employee added successfully":employees.__dict__}

@app.get("/telecom/profiles")
def list_of_profiles():
    return data

@app.get("/telecom/profiles/{id}")
def profile_by_id(id:int):
    for i in data:
        if i.employee.emp_id == id:
            return i
    raise HTTPException(status_code=404,detail="Profile not found")

@app.put("/telecom/profiles/{emp_id}")
def update_profile(emp_id:int,profile_data:EmployeeTelecomProfile):
    for i in range(len(data)):
        if data[i].employee.emp_id == emp_id:
            data[i] = profile_data
            return {"Employee updated":profile_data}
    raise HTTPException(status_code=404,detail="No data found")

@app.delete("/telecom/profiles/{emp_id}")
def update_profile(emp_id:int):
    for i in range(len(data)):
        if data[i].employee.emp_id == emp_id:
            return {"Profile deleted":data.pop(i)
            }
    raise HTTPException(status_code=404,detail="No data found")

@app.get("/telecom/profiles_search")
async def filter_by_department_and_provider(
    department:Optional[str] = Query(None),
    provider:Optional[str] = Query(None)
    ):
    emp = []
    if department and provider:
        for i in data:
            if i.employee.department == department and i.sim.provider == provider:
                emp.append(i)
    elif department:
        for i in data:
            if i.employee.department == department:
                emp.append(i)
    elif provider:
        for i in data:
            if i.sim.provider == provider:
                emp.append(i)
    else:
        return data
    if emp:
        return emp
    else:
        raise HTTPException(status_code=404,detail="No data Found")