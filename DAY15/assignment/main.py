



from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from typing import Optional

app=FastAPI(title="UST Telecom")

class EmployeeBasic(BaseModel):
    emp_id:int=Field(...,ge=1000,le=999999)
    name:str=Field(...,min_length=2)
    official_email:str=Field(...,pattern=r"^[a-zA-Z0-9._%+-]+@ust\.com$")
    department:str="Telecom"
    location:str="Bengaluru"

class SimCard(BaseModel):
    sim_number:str=Field(...,pattern=r"^\d{10}$")
    provider:str="Jio"
    is_esim:bool=False
    activation_year:int=Field(...,ge=2020,le=2025)

class DataPlan(BaseModel):
    name:str=Field(...,min_length=3,max_length=50)
    monthly_gb:int=Field(...,gt=0,le=1000)
    speed_mbps:int=Field(50,ge=1,le=1000)
    is_roaming_included:bool=False

class VoicePlan(BaseModel):
    name:str=Field(...,min_length=3)
    monthly_minutes:int=Field(...,ge=0,le=10000)
    has_isd:bool=False
    per_minute_charge_paise:int=Field(0,ge=0,le=1000)

class EmergencyContact(BaseModel):
    name:str=Field(...,min_length=2)
    relation:str="Family"
    phone:str=Field(...,pattern=r"^[6-9]\d{9}$")

class EmployeeTelecomProfile(BaseModel):
    employee:EmployeeBasic
    sim:SimCard
    data_plan:Optional[DataPlan]=None
    voice_plan:Optional[VoicePlan]=None
    emergency_contact:Optional[EmergencyContact]=None

profiles=[]

@app.post("/telecom/profiles",response_model=EmployeeTelecomProfile,status_code=201)
def create_profile(profile:EmployeeTelecomProfile):
    for p in profiles:
        if p.employee.emp_id==profile.employee.emp_id:
            raise HTTPException(409,"Profile already exists")
    profiles.append(profile)
    return profile

@app.get("/telecom/profiles",response_model=list[EmployeeTelecomProfile])
def get_all():
    return profiles

@app.get("/telecom/profiles/{emp_id}",response_model=EmployeeTelecomProfile)
def get_one(emp_id:int):
    for p in profiles:
        if p.employee.emp_id==emp_id:
            return p
    raise HTTPException(404,"Profile not found")

@app.put("/telecom/profiles/{emp_id}",response_model=EmployeeTelecomProfile)
def update_profile(emp_id:int,profile:EmployeeTelecomProfile):
    if emp_id!=profile.employee.emp_id:
        raise HTTPException(400,"ID mismatch")
    for i,p in enumerate(profiles):
        if p.employee.emp_id==emp_id:
            profiles[i]=profile
            return profile
    raise HTTPException(404,"Profile not found")

@app.delete("/telecom/profiles/{emp_id}")
def delete_one(emp_id:int):
    for p in profiles:
        if p.employee.emp_id==emp_id:
            profiles.remove(p)
            return {"detail":"Profile deleted"}
    raise HTTPException(404,"Profile not found")

@app.get("/telecom/profiles/search",response_model=list[EmployeeTelecomProfile])
def search(department:Optional[str]=None,provider:Optional[str]=None):
    result=profiles
    if department:
        result=[p for p in result if p.employee.department==department]
    if provider:
        result=[p for p in result if p.sim.provider==provider]
    return result