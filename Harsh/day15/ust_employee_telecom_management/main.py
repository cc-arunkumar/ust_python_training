from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field



class EmployeeBasic(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)
    name: str = Field(..., min_length=2)
    official_email: str = Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@ust\.com$')
    department: str = Field(default="Telecom")
    location: str = Field(default="Bengaluru")

class SimCard(BaseModel):
    sim_number: str = Field(..., pattern=r'^\d{10}$')
    provider: str = Field(default="Jio")
    is_esim: bool = Field(default=False)
    activation_year: int = Field(..., ge=2020, le=2025)

class DataPlan(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    monthly_gb: int = Field(..., gt=0, le=1000)
    speed_mbps: int = Field(default=50, ge=1, le=1000)
    is_roaming_included: bool = Field(default=False)

class VoicePlan(BaseModel):
    name: str = Field(..., min_length=3)
    monthly_minutes: int = Field(..., ge=0, le=10000)
    has_isd: bool = Field(default=False)
    per_minute_charge_paise: int = Field(default=0, ge=0, le=1000)

class EmergencyContact(BaseModel):
    name: str = Field(..., min_length=2)
    relation: str = Field(default="Family")
    phone: str = Field(..., pattern=r'^[6-9]\d{9}$')

class EmployeeTelecomProfile(BaseModel):
    employee: EmployeeBasic
    sim: SimCard
    data_plan: Optional[DataPlan] = None
    voice_plan: Optional[VoicePlan] = None
    emergency_contact: Optional[EmergencyContact] = None



app = FastAPI(title="UST Employee Telecom Management")
profiles: List[EmployeeTelecomProfile] = []

# Create profile
@app.post("/telecom/profiles", status_code=201)
def create_profile(profile: EmployeeTelecomProfile):
    for p in profiles:
        if p.employee.emp_id == profile.employee.emp_id:
            raise HTTPException(status_code=409, detail="Profile with emp_id already exists")
    profiles.append(profile)
    return profile

# List all profiles
@app.get("/telecom/profiles")
def list_profiles():
    return profiles

# Get profile by emp_id
@app.get("/telecom/profiles/{emp_id}")
def get_profile(emp_id: int):
    for p in profiles:
        if p.employee.emp_id == emp_id:
            return p
    raise HTTPException(status_code=404, detail="Profile not found")

# Update profile
@app.put("/telecom/profiles/{emp_id}")
def update_profile(emp_id: int, profile: EmployeeTelecomProfile):
    if profile.employee.emp_id != emp_id:
        raise HTTPException(status_code=400, detail="Path emp_id does not match body employee.emp_id")
    for p in profiles:
        if p.employee.emp_id == emp_id:
            # remove old profile and add new one
            profiles.remove(p)
            profiles.append(profile)
            return profile
    raise HTTPException(status_code=404, detail="Profile not found")

# Delete profile
@app.delete("/telecom/profiles/{emp_id}")
def delete_profile(emp_id: int):
    for p in profiles:
        if p.employee.emp_id == emp_id:
            profiles.remove(p)
            return {"detail": "Profile deleted"}
    raise HTTPException(status_code=404, detail="Profile not found")


# Search profiles
@app.get("/telecom/profiles/search")
def search_profiles(department: Optional[str] = None, provider: Optional[str] = None):
    results = profiles
    if department:
        results = [p for p in results if p.employee.department == department]
    if provider:
        results = [p for p in results if p.sim.provider == provider]
    return results
