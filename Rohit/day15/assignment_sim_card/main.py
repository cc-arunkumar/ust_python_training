from pydantic import BaseModel, Field
from typing import Optional, List
from fastapi import FastAPI, HTTPException

# Create FastAPI app
app = FastAPI(title="UST Employee Operation")

# ------------------ Data Models ------------------

# Basic employee details
class EmployeeBasic(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)   # Employee ID must be between 1000 and 999999
    name: str = Field(..., min_length=2)           # Name must be at least 2 characters
    department: str = "General"                    # Default department is "General"

# SIM card details
class SIMCard(BaseModel):
    number: str = Field(..., pattern=r"^\d{10}$")  # Must be a 10-digit number
    provider: str = Field(default="Jio")           # Default provider is Jio
    activation_year: int = Field(..., ge=2020, le=2025)  # Activation year between 2020–2025

# Data plan details
class DataPlan(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)   # Plan name length between 3–50
    monthly_gb: int = Field(..., gt=0, le=1000)           # Monthly GB >0 and ≤1000
    speed_mbps: int = Field(default=50, ge=1, le=1000)    # Speed default 50 Mbps, range 1–1000
    is_roaming_included: bool = False                     # Roaming default False

# Voice plan details
class VoicePlan(BaseModel):
    name: str = Field(..., min_length=3)                  # Plan name at least 3 chars
    monthly_minutes: int = Field(..., ge=0, le=1000)      # Minutes between 0–1000
    has_isd: bool = Field(default=False)                  # Default no ISD
    per_minute_charge_paise: int = Field(default=0, ge=0, le=1000)  # Charge per minute

# Emergency contact details
class EmergencyContact(BaseModel):
    name: str = Field(..., min_length=2)                  # Name at least 2 chars
    relation: str = Field(default="Family")               # Default relation Family
    phone: str = Field(pattern="^[6-9]\d{9}$")            # Valid Indian mobile number

# Full telecom profile combining all above
class EmployeeTelecomProfile(BaseModel):
    employee: EmployeeBasic = (...)
    sim: SIMCard = (...)
    data_plan: Optional[DataPlan] = Field(default=None)
    voice_plan: Optional[VoicePlan] = Field(default=None)
    emergency_contact: Optional[EmergencyContact] = Field(default=None)

# ------------------ In-memory storage ------------------
profiles: List[EmployeeTelecomProfile] = []   # Store all profiles in memory

# ------------------ Endpoints ------------------

# Create new telecom profile
@app.post("/telecom/profile")
def create_telecom(profile: EmployeeTelecomProfile):
    for check in profiles:
        if check.employee.emp_id == profile.employee.emp_id:
            raise HTTPException(status_code=409, detail="Employee with this id already exists")
    profiles.append(profile)
    return profiles

# Get all profiles
@app.get("/telecom/profiles")
def all_telecom_employees():
    return profiles

# Get profile by employee ID
@app.get("/telecom/profiles/{emp_id}")
def get_by_id(emp_id: int):
    for check in profiles:
        if check.employee.emp_id == emp_id:
            return check
    raise HTTPException(status_code=404, detail="Profile not found")

# Update profile by employee ID
@app.put("/telecom/profiles/{emp_id}")
def update_by_emp_id(emp_id: int, profile: EmployeeTelecomProfile):
    if profile.employee.emp_id != emp_id:
        raise HTTPException(status_code=400, detail="Employee ID does not match")
    for c in profiles:
        if c.employee.emp_id == emp_id:
            profiles.remove(c)
            profiles.append(profile)
            return profile
    raise HTTPException(status_code=404, detail="Profile not found")

# Delete profile by employee ID
@app.delete("/telecom/profiles/{emp_id}")
def delete_by_employee_id(emp_id: int):
    for c in profiles:
        if c.employee.emp_id == emp_id:
            profiles.remove(c)
            return {"detail": "Profile deleted"}
    raise HTTPException(status_code=404, detail="Profile not found")

# Search profiles by department or provider
@app.get("/telecom/profiles/search")
def profiles_search(department: Optional[str] = None, provider: Optional[str] = None):
    result = profiles
    if department:
        result = [p for p in result if p.employee.department == department]
    if provider:
        result = [p for p in result if p.sim.provider == provider]
    return result
