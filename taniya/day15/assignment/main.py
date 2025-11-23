from typing import Optional, List
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException
import re

app = FastAPI(title="UST Employee Telecom Management ")
# Regex helpers

UST_EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@ust\.com$")
MOBILE_10_DIGIT_REGEX = re.compile(r"^\d{10}$")
INDIAN_MOBILE_REGEX = re.compile(r"^[6-9]\d{9}$")


# Pydantic Models

class EmployeeBasic(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)
    name: str = Field(..., min_length=2)
    official_email: str = Field(..., pattern=UST_EMAIL_REGEX.pattern)
    department: str = "Telecom"
    location: str = "Bengaluru"


class SimCard(BaseModel):
    sim_number: str = Field(..., pattern=MOBILE_10_DIGIT_REGEX.pattern)
    provider: str = "Jio"
    is_esim: bool = False
    activation_year: int = Field(..., ge=2020, le=2025)


class DataPlan(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    monthly_gb: int = Field(..., gt=0, le=1000)
    speed_mbps: int = Field(50, ge=1, le=1000)
    is_roaming_included: bool = False


class VoicePlan(BaseModel):
    name: str = Field(..., min_length=3)
    monthly_minutes: int = Field(..., ge=0, le=10000)
    has_isd: bool = False
    per_minute_charge_paise: int = Field(0, ge=0, le=1000)


class EmergencyContact(BaseModel):
    name: str = Field(..., min_length=2)
    relation: str = "Family"
    phone: str = Field(..., pattern=INDIAN_MOBILE_REGEX.pattern)


class EmployeeTelecomProfile(BaseModel):
    employee: EmployeeBasic
    sim: SimCard
    data_plan: Optional[DataPlan] = None
    voice_plan: Optional[VoicePlan] = None
    emergency_contact: Optional[EmergencyContact] = None

# FastAPI App

app = FastAPI(title="UST Employee Telecom Management")

# In-memory storage
profiles: List[EmployeeTelecomProfile] = []


def find_profile_index_by_emp_id(emp_id: int) -> int:
    for i, p in enumerate(profiles):
        if p.employee.emp_id == emp_id:
            return i
    return -1


@app.post("/telecom/profiles", response_model=EmployeeTelecomProfile, status_code=201)
def create_profile(profile: EmployeeTelecomProfile):
    id = find_profile_index_by_emp_id(profile.employee.emp_id)
    if id != -1:
        raise HTTPException(status_code=409, detail="Profile already exists")
    profiles.append(profile)
    return profile


@app.get("/telecom/profiles", response_model=List[EmployeeTelecomProfile])
def list_profiles():
    return profiles


@app.get("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def get_profile(emp_id: int):
    id = find_profile_index_by_emp_id(emp_id)
    if id == -1:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profiles[id]


@app.put("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def update_profile(emp_id: int, profile: EmployeeTelecomProfile):
    if profile.employee.emp_id != emp_id:
        raise HTTPException(status_code=400, detail="Path emp_id and body emp_id must match")

    id = find_profile_index_by_emp_id(emp_id)
    if id == -1:
        raise HTTPException(status_code=404, detail="Profile not found")

    profiles[id] = profile
    return profile


@app.delete("/telecom/profiles/{emp_id}")
def delete_profile(emp_id: int):
    id = find_profile_index_by_emp_id(emp_id)
    if id == -1:
        raise HTTPException(status_code=404, detail="Profile not found")
    profiles.pop(id)
    return {"detail": "Profile deleted"}


@app.get("/telecom/profiles/search", response_model=List[EmployeeTelecomProfile])
def search_profiles(department: Optional[str] = None, provider: Optional[str] = None):
    result = profiles
    if department:
        result = [p for p in result if p.employee.department == department]
    if provider:
        result = [p for p in result if p.sim.provider == provider]
    return result