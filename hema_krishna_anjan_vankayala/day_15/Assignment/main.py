# UST Employee Telecom Management
# API Specification and Validation Assignment
# 1. Context
# UST manages telecom services for its employees. For each employee, the system
# must store:
# Employee identity and contact information
# Company SIM details
# Optional data and voice plan information
# Optional emergency contact information
# You are required to design:
# 1. Pydantic models that validate the structure and constraints of this data.
# 2. FastAPI endpoints that use these models for request parsing and validation,
# with in-memory storage (lists) only.
# The focus is on correct modelling, validation behaviour, and clear API contracts.
# No database or authentication is required.

from typing import List, Optional
from fastapi import FastAPI , HTTPException
from pydantic import BaseModel,Field

# FastAPI application instance
app = FastAPI(title="UST Employee Telecom Device Registration")


class EmployeeBasic(BaseModel):
    # basic employee details used inside telecom profile
    emp_id : int = Field(...,ge=1000,le=999999,description="Employee Id not valid")
    name: str = Field(...,min_length=2,description="name should be minimum of length 2")
    official_mail : str = Field(...,pattern="[a-zA-Z0-9_%+-]+@ust\\.com$")
    department : Optional[str] = Field(default="General", description="Department name")
    location : Optional[str] = Field(default="Bengaluru") 
    
class SimCard(BaseModel):
    # sim card details associated with the employee
    sim_number : str = Field(...,pattern="^\\d{10}$",description="Must be exactly 10 digits")
    provider : str = Field(default="Jio", description="Department name")
    is_esim : Optional[bool] = Field(default= False)
    activation_year : int = Field(...,ge=2000,le=2025,description="Year Must be from 2020 to 2025")

class DataPlan(BaseModel):
    # optional data plan attached to the sim
    name : str = Field(...,min_length=3,max_length=50)
    monthly_gb : int = Field(...,gt=0,le=1000)
    speed_mbps : Optional[int] = Field(default=50,ge=1,le=1000)
    is_roaming_included : Optional[bool] = Field(default=False)

class VoicePlan(BaseModel):
    # optional voice plan attached to the sim
    name : str = Field(...,min_length=3)
    monthly_minutes : int = Field(...,ge=0,le=10000)
    has_isd : Optional[bool] = Field(default=False)
    per_minute_charge_paise : Optional[int] = Field(default=0,ge=0,le=1000)
    
class EmergencyContact(BaseModel):
    # emergency contact information for the employee
    name : str = Field(...,min_length=2)
    relation : Optional[str] = Field(default="Family")
    phone : str = Field(...,pattern='[6-9]\\d{9}$')

class EmployeeTelecomProfile(BaseModel):
    # full telecom profile combining employee, sim and optional plans
    employee : EmployeeBasic 
    sim : SimCard
    data_plan : Optional[DataPlan] = Field(default=None)
    voice_plan : Optional[VoicePlan] = Field(default=None)
    emergency_contact : Optional[EmergencyContact] = Field(default=None)

# in-memory list storing all telecom profiles for demo/testing
employee_profile : List[EmployeeTelecomProfile] =[]

@app.post('/telecom/profiles',response_model=EmployeeTelecomProfile)
def create_telecom_profile(new_profile : EmployeeTelecomProfile):
    # create a new telecom profile, error if emp_id already exists
    for emp in employee_profile:
        if emp.employee.emp_id == new_profile.employee.emp_id:
            raise HTTPException(status_code=409,detail="Employee Already Exists")
    employee_profile.append(new_profile)
    return new_profile   # return the created profile

@app.get('/telecom/profiles', response_model=List[EmployeeTelecomProfile])
def all_profiles():
    # return all stored profiles
    return employee_profile

@app.get('/telecom/profiles/search', response_model=List[EmployeeTelecomProfile])
def filter_profiles(department: str=None, provider: str=None):
    # search/filter profiles by department and/or provider
    if department is None and provider is None:
        return employee_profile
    else:
        new_li = []
        if department is not None or provider is not None:
            stored_department = ""
            stored_provider = ""
            for idx, stored in enumerate(employee_profile):
                if department is not None:
                    stored_department = stored['employee']['department'] if isinstance(stored, dict) else stored.employee.department
                    
                if provider is not None:
                    stored_provider = stored['sim']['provider'] if isinstance(stored, dict) else stored.sim.provider
                   
                if stored_department != "" and stored_provider != "":
                    if stored_provider == provider and stored_department == department:
                        new_li.append(stored)
                if stored_department != "" and stored_provider == "":
                    if stored_department == department:
                        new_li.append(stored)
                if stored_department == "" and stored_provider != "":
                    if stored_provider == provider:
                        new_li.append(stored)
        return new_li

@app.get('/telecom/profiles/{emp_id}')
def get_profile_id(emp_id : int):
    # retrieve a single profile by employee id
    for emp in employee_profile:
        stored_id = emp['employee']['emp_id'] if isinstance(emp, dict) else emp.employee.emp_id
        if stored_id == emp_id:
            return emp 
    raise HTTPException(status_code=404,detail="Profile Not Found")

@app.put('/telecom/profiles/{emp_id}',response_model=EmployeeTelecomProfile)
def update_profile(emp_id : int,updated_emp : EmployeeTelecomProfile):
    # enforce path/body id consistency
    if updated_emp.employee.emp_id != emp_id:
        raise HTTPException(status_code=400, detail="Path emp_id and body employee.emp_id do not match")
    # find existing profile and replace it
    for idx, stored in enumerate(employee_profile):
        stored_id = stored['employee']['emp_id'] if isinstance(stored, dict) else stored.employee.emp_id
        if stored_id == emp_id:
            employee_profile[idx] = updated_emp
            return updated_emp
    # not found
    raise HTTPException(status_code=404, detail="Profile Not Found")

@app.delete('/telecom/profiles/{emp_id}')

def delete_profile(emp_id : int):
    # delete a profile by employee id
    for idx,stored in enumerate(employee_profile):
        stored_id = stored['employee']['emp_id'] if isinstance(stored,dict) else stored.employee.emp_id
        if stored_id == emp_id:
            employee_profile.pop(idx)
            return {"detail": "Profile deleted"} 
    raise HTTPException(status_code=404,detail='Profile Not Found')





