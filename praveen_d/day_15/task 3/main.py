from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

# In-memory storage for profiles
profiles = []
next_emp_id = 10000  # Starting emp_id for new profiles

# Pydantic Models
class EmployeeBasic(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)
    name: str = Field(..., min_length=2)
    official_email: str = Field(..., regex=r"^[a-zA-Z0-9._%+-]+@ust\.com$")
    department: str = Field(default="Telecom")
    location: str = Field(default="Bengaluru")

class SimCard(BaseModel):
    sim_number: str = Field(..., regex=r"^\d{10}$")
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
    phone: str = Field(..., regex=r"^[6-9]\d{9}$")

class EmployeeTelecomProfile(BaseModel):
    employee: EmployeeBasic
    sim: SimCard
    data_plan: Optional[DataPlan] = None
    voice_plan: Optional[VoicePlan] = None
    emergency_contact: Optional[EmergencyContact] = None

# Helper function to check if emp_id already exists
def get_profile_by_emp_id(emp_id: int):
    for profile in profiles:
        if profile.employee.emp_id == emp_id:
            return profile
    return None

# Endpoints
@app.post("/telecom/profiles", status_code=201)
def create_telecom_profile(profile: EmployeeTelecomProfile):
    # Check if emp_id already exists
    if get_profile_by_emp_id(profile.employee.emp_id):
        raise HTTPException(status_code=409, detail="Profile with this emp_id already exists")
    
    # Add profile to in-memory storage
    profiles.append(profile)
    return profile

@app.post("/telecom/profiles/minimal", status_code=201)
def create_minimal_telecom_profile(profile: EmployeeTelecomProfile):
    # Ensure minimal fields are passed, defaults will be set for others
    if not profile.employee.department:
        profile.employee.department = "Telecom"
    if not profile.employee.location:
        profile.employee.location = "Bengaluru"
    if not profile.sim.provider:
        profile.sim.provider = "Jio"
    if not profile.sim.is_esim:
        profile.sim.is_esim = False

    # Add profile to in-memory storage
    profiles.append(profile)
    return profile

@app.get("/telecom/profiles", response_model=List[EmployeeTelecomProfile])
def get_all_profiles():
    return profiles

@app.get("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def get_profile_by_id(emp_id: int):
    profile = get_profile_by_emp_id(emp_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@app.put("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def update_profile(emp_id: int, updated_profile: EmployeeTelecomProfile):
    profile = get_profile_by_emp_id(emp_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    # Check if emp_id in the body matches the URL parameter
    if updated_profile.employee.emp_id != emp_id:
        raise HTTPException(status_code=400, detail="emp_id in body does not match path parameter")

    # Update the profile
    profiles.remove(profile)
    profiles.append(updated_profile)
    return updated_profile

@app.delete("/telecom/profiles/{emp_id}", status_code=200)
def delete_profile(emp_id: int):
    profile = get_profile_by_emp_id(emp_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    # Delete the profile
    profiles.remove(profile)
    return {"detail": "Profile deleted"}

@app.get("/telecom/profiles/search", response_model=List[EmployeeTelecomProfile])
def search_profiles(department: Optional[str] = None, provider: Optional[str] = None):
    filtered_profiles = []

    # Filter by department
    if department:
        for profile in profiles:
            if profile.employee.department == department:
                filtered_profiles.append(profile)

    # Filter by provider
    if provider:
        result = []
        for profile in filtered_profiles if filtered_profiles else profiles:
            if profile.sim.provider == provider:
                result.append(profile)
        filtered_profiles = result

    return filtered_profiles

