from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel, Field

class Employee_Basic(BaseModel):
    emp_id : int = Field(..., ge=1000, le=99999, description="Employee ID.")
    name : str = Field(...,min_length=2, description="Full Name.")
    official_email : str = Field(...,pattern=r"^[a-zA-Z0-9._%+-]+@ust\.com$", description="Must be a ust email.")
    department : str = Field("Telecom")
    location : str = Field("Bengaluru")
    
class SimCard(BaseModel):
    sim_number : str = Field(...,pattern=r"^\d{10}$", description="10 digit phone number.")
    provider : str = Field("Jio")
    is_esim : bool = False
    activation_year : int = Field(...,ge=2020, le=2025, description="Year of activation.")
    
class DataPlan(BaseModel):
    name : str = Field(..., min_length=3, max_length=50)
    monthly_gb : int = Field(..., gt=0, le=1000)
    speed_mbps : int = Field(50, ge=1, le=1000)
    is_roaming_included : bool = False

class VoicePlan(BaseModel):
    name : str = Field(..., min_length=3)
    monthly_minutes : int = Field(..., ge=0, le=10000)
    has_isd : bool = False
    per_minute_charge_paise : int = Field(0, ge=0, le=1000)

class EmergencyContact(BaseModel):
    name : str = Field(..., min_length=2)
    relation : str = Field("Family")
    phone : str = Field(..., pattern=r"^[6-9]\d{9}$")

class EmployeeTelecomProfile(BaseModel):
    employee : Employee_Basic
    sim : SimCard
    data_plan : Optional[DataPlan] = Field(None)
    voice_plan : Optional[VoicePlan] = Field(None)
    emergency_contact : Optional[EmergencyContact] = Field(None)

app = FastAPI(title="UST_Telecon_Management.")

profiles : List[EmployeeTelecomProfile] = []

@app.post("/telecom/profiles", status_code=201)
def create_employee_profile(profile : EmployeeTelecomProfile):
    for p in profiles:
        if p.employee.emp_id == profile.employee.emp_id:
            raise HTTPException(status_code=409, detail="Employee id already exists.")
    profiles.append(profile)
    return profile
    
    

@app.get("/telecom/profiles", status_code=200)
def get_profiles():
    return profiles

@app.get("/telecom/profiles/{emp_id}", status_code=200)
def get_employee_by_id(emp_id : int):
    for p in profiles:
        if p.employee.emp_id == emp_id:
            return p
    raise HTTPException(status_code=404, detail="Profile not found")

@app.put("/telecom/profiles/{emp_id}", status_code=200)
def update_profile(emp_id : int, new_profile : EmployeeTelecomProfile):
    if new_profile.employee.emp_id != emp_id:
        raise HTTPException(status_code=400, detail="pathid vs bodyid doesnot match.")
    for p in profiles:
        if p.employee.emp_id == emp_id:
            profiles.remove(p)
            profiles.append(new_profile)
            return new_profile
    
    raise HTTPException(status_code=404, detail="no existing profile.")

@app.delete("/telecom/profiles/{emp_id}", status_code=200)
def delete_profile(emp_id : int):
    for index, p in enumerate(profiles):
        if p.employee.emp_id == emp_id:
            profiles.pop(index)
            return p
    raise HTTPException(status_code=404, detail="profile not found.")

@app.get("/telecom/profiles/search", status_code=200)
def get_profiles_by_dept_provider(dept : Optional[str], provider : Optional[str]):
    result = profiles
    if dept:
        result = [p for p in profiles if p.employee.department == dept]
    if provider:
        result = [p for p in profiles if p.sim.provider == provider]
    return result

