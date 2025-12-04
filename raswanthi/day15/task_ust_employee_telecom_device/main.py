from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
import re

# Initialize the FastAPI application with a title
app = FastAPI(title="UST Employee Telecom Management API")

# In-memory storage for employee profiles (acts like a temporary database)
profiles: List[dict] = []

# -----------------------------
# Pydantic Models for Validation
# -----------------------------

# Employee basic details
class EmployeeBasic(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)  # Employee ID must be between 1000–999999
    name: str = Field(..., min_length=2)          # Name must have at least 2 characters
    official_email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@example\.com$")  # Must end with @ust.com
    department: str = Field("Telecom")            # Default department is Telecom
    location: str = Field("Bengaluru")            # Default location is Bengaluru

# SIM card details
class SimCard(BaseModel):
    sim_number: str = Field(..., pattern=r"^\d{10}$")  # Must be exactly 10 digits
    provider: str = Field("Jio")                       # Default provider is Jio
    is_esim: bool = Field(False)                       # Default is physical SIM
    activation_year: int = Field(..., ge=2020, le=2025) # Valid years: 2020–2025

# Data plan details
class DataPlan(BaseModel):
    name: str = Field(..., min_length=3, max_length=50) # Plan name between 3–50 chars
    monthly_gb: int = Field(..., gt=0, le=1000)         # Monthly data between 1–1000 GB
    speed_mbps: int = Field(50, ge=1, le=1000)          # Default speed 50 Mbps
    is_roaming_included: bool = Field(False)            # Roaming not included by default

# Voice plan details
class VoicePlan(BaseModel):
    name: str = Field(..., min_length=3)                # Plan name at least 3 chars
    monthly_minutes: int = Field(..., ge=0, le=10000)   # Minutes between 0–10000
    has_isd: bool = Field(False)                        # ISD not included by default
    per_minute_charge_paise: int = Field(0, ge=0, le=1000) # Charge per minute in paise

# Emergency contact details
class EmergencyContact(BaseModel):
    name: str = Field(..., min_length=2)                # Contact name at least 2 chars
    relation: str = Field("Family")                     # Default relation is Family
    phone: str = Field(..., pattern=r"^[6-9]\d{9}$")    # Must be valid Indian mobile number

# Main Employee Telecom Profile (combines all above models)
class EmployeeTelecomProfile(BaseModel):
    employee: EmployeeBasic
    sim: SimCard
    data_plan: Optional[DataPlan] = None
    voice_plan: Optional[VoicePlan] = None
    emergency_contact: Optional[EmergencyContact] = None


# -----------------------------
# API Endpoints
# -----------------------------

# Create a new employee telecom profile
@app.post("/telecom/profiles", status_code=201)
async def create_profile(profile: EmployeeTelecomProfile):
    # Prevent duplicate employee IDs
    for existing_profile in profiles:
        if existing_profile['employee']['emp_id'] == profile.employee.emp_id:
            raise HTTPException(status_code=409, detail="Employee ID already exists")
    
    # Save profile to in-memory list
    profiles.append(profile.dict())
    return profile

# Create a profile with minimal input (defaults applied)
@app.post("/telecom/profiles/minimal", status_code=201)
async def create_minimal_profile(profile: EmployeeTelecomProfile):
    return await create_profile(profile)

# List all employee profiles
@app.get("/telecom/profiles", response_model=List[EmployeeTelecomProfile])
async def list_profiles():
    return profiles

# Get a specific employee profile by ID
@app.get("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
async def get_profile(emp_id: int):
    for profile in profiles:
        if profile['employee']['emp_id'] == emp_id:
            return profile
    raise HTTPException(status_code=404, detail="Profile not found")

# Update an existing employee profile
@app.put("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
async def update_profile(emp_id: int, profile: EmployeeTelecomProfile):
    for index, existing_profile in enumerate(profiles):
        if existing_profile['employee']['emp_id'] == emp_id:
            # Ensure path ID matches body ID
            if existing_profile['employee']['emp_id'] != profile.employee.emp_id:
                raise HTTPException(status_code=400, detail="Path id does not match body id")
            profiles[index] = profile.dict()
            return profile
    raise HTTPException(status_code=404, detail="Profile not found")

# Delete an employee profile
@app.delete("/telecom/profiles/{emp_id}")
async def delete_profile(emp_id: int):
    global profiles
    profiles = [profile for profile in profiles if profile['employee']['emp_id'] != emp_id]
    return {"detail": "Profile deleted"}

# Search profiles by department or provider
@app.get("/telecom/profiles/search", response_model=List[EmployeeTelecomProfile])
async def search_profiles(department: Optional[str] = None, provider: Optional[str] = None):
    filtered_profiles = profiles
    if department:
        filtered_profiles = [profile for profile in filtered_profiles if profile['employee']['department'] == department]
    if provider:
        filtered_profiles = [profile for profile in filtered_profiles if profile['sim']['provider'] == provider]
    return filtered_profiles


# -----------------------------
# Validation Endpoints
# -----------------------------

@app.get("/validate/emp_id")
async def validate_emp_id(emp_id: int):
    if not (1000 <= emp_id <= 999999):
        raise HTTPException(status_code=422, detail="emp_id must be between 1000 and 999999")
    return {"emp_id": emp_id}

@app.get("/validate/name")
async def validate_name(name: str):
    if len(name) < 2:
        raise HTTPException(status_code=422, detail="Name must have at least 2 characters")
    return {"name": name}

@app.get("/validate/email")
async def validate_email(email: str):
    if not re.match(r"^[a-zA-Z0-9._%+-]+@example\.com$", email):
        raise HTTPException(status_code=422, detail="Email must end with @example.com")
    return {"email": email}

@app.get("/validate/sim_number")
async def validate_sim_number(sim_number: str):
    if not re.match(r"^\d{10}$", sim_number):
        raise HTTPException(status_code=422, detail="SIM number must be exactly 10 digits")
    return {"sim_number": sim_number}

@app.get("/validate/activation_year")
async def validate_activation_year(year: int):
    if not (2020 <= year <= 2025):
        raise HTTPException(status_code=422, detail="Activation year must be between 2020 and 2025")
    return {"activation_year": year}

@app.get("/validate/phone")
async def validate_phone(phone: str):
    if not re.match(r"^[6-9]\d{9}$", phone):
        raise HTTPException(status_code=422, detail="Phone number must be an Indian mobile number starting with 6, 7, 8, or 9")
    return {"phone": phone}
