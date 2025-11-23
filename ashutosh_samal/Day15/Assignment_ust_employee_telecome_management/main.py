from typing import Optional, List
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

# Employee basic info model
class EmployeeBasic(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999, description="Employee numeric id")
    name: str = Field(..., min_length=2, description="Full name")
    official_email: str = Field(
        ...,
        pattern=r"^[a-zA-Z0-9._%+-]+@ust\.com$",
        description="Must be a UST email"
    )
    department: str = Field("Telecom", description="Default department")
    location: str = Field("Bengaluru", description="Default location")

# SIM card info model
class SimCard(BaseModel):
    sim_number: str = Field(..., pattern=r"^\d{10}$", description="10-digit mobile number")
    provider: str = Field("Jio", description="Default provider")
    is_esim: bool = Field(False, description="Default False")
    activation_year: int = Field(..., ge=2020, le=2025, description="Activation year")

# Data plan model
class DataPlan(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    monthly_gb: int = Field(..., gt=0, le=1000)
    speed_mbps: int = Field(50, ge=1, le=1000, description="Default 50 Mbps")
    is_roaming_included: bool = Field(False, description="Default False")

# Voice plan model
class VoicePlan(BaseModel):
    name: str = Field(..., min_length=3)
    monthly_minutes: int = Field(..., ge=0, le=10000)
    has_isd: bool = Field(False)
    per_minute_charge_paise: int = Field(0, ge=0, le=1000)

# Emergency contact model
class EmergencyContact(BaseModel):
    name: str = Field(..., min_length=2)
    relation: str = Field("Family")
    phone: str = Field(..., pattern=r"^[6-9]\d{9}$", description="Indian mobile")

# Top-level telecom profile model
class EmployeeTelecomProfile(BaseModel):
    employee: EmployeeBasic
    sim: SimCard
    data_plan: Optional[DataPlan] = None
    voice_plan: Optional[VoicePlan] = None
    emergency_contact: Optional[EmergencyContact] = None

# FastAPI app
app = FastAPI(title="UST Employee Telecom Management")

# In-memory storage
profiles: List[EmployeeTelecomProfile] = []

# Helper: find profile index by emp_id
def find_profile_index(emp_id: int) -> int:
    for idx, p in enumerate(profiles):
        if p.employee.emp_id == emp_id:
            return idx
    return -1

# Create profile
@app.post("/telecom/profiles", response_model=EmployeeTelecomProfile, status_code=201)
def create_profile(profile: EmployeeTelecomProfile):
    emp_id = profile.employee.emp_id
    if find_profile_index(emp_id) != -1:
        raise HTTPException(status_code=409, detail="Profile with emp_id already exists")
    profiles.append(profile)
    return profile

# List all profiles
@app.get("/telecom/profiles", response_model=List[EmployeeTelecomProfile])
def list_profiles():
    return profiles

# Search profiles by department/provider
@app.get("/telecom/profiles/search", response_model=List[EmployeeTelecomProfile])
def search_profiles(
    department: Optional[str] = Query(None),
    provider: Optional[str] = Query(None),
):
    results = profiles
    if department is not None:
        results = [p for p in results if p.employee.department == department]
    if provider is not None:
        results = [p for p in results if p.sim.provider == provider]
    return results

# Get profile by emp_id
@app.get("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def get_profile(emp_id: int):
    idx = find_profile_index(emp_id)
    if idx == -1:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profiles[idx]

# Update profile
@app.put("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def update_profile(emp_id: int, profile: EmployeeTelecomProfile):
    if profile.employee.emp_id != emp_id:
        raise HTTPException(status_code=400, detail="Path emp_id and body employee.emp_id must match")
    idx = find_profile_index(emp_id)
    if idx == -1:
        raise HTTPException(status_code=404, detail="Profile not found")
    profiles[idx] = profile
    return profile

# Delete profile
@app.delete("/telecom/profiles/{emp_id}")
def delete_profile(emp_id: int):
    idx = find_profile_index(emp_id)
    if idx == -1:
        raise HTTPException(status_code=404, detail="Profile not found")
    profiles.pop(idx)
    return {"detail": "Profile deleted"}
