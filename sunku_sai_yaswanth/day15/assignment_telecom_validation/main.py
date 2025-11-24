from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional, List

# Sample data dictionary (not used directly in API, but useful for reference/testing)
sample_data = {
    "employee": {
        "emp_id": 12345,
        "name": "Asha",
        "official_email": "asha@ust.com",
        "department": "Engineering",
        "location": "Pune"
    },
    "sim": {
        "sim_number": "9876543210",
        "provider": "Airtel",
        "is_esim": True,
        "activation_year": 2023
    },
    "data_plan": {
        "name": "Standard 50GB",
        "monthly_gb": 50,
        "speed_mbps": 100,
        "is_roaming_included": True
    },
    "voice_plan": {
        "name": "Office Calls Pack",
        "monthly_minutes": 1000,
        "has_isd": False,
        "per_minute_charge_paise": 0
    },
    "emergency_contact": {
        "name": "Ravi",
        "relation": "Friend",
        "phone": "9876543210"
    }
}

# -----------------------------
# Pydantic Models for Validation
# -----------------------------

class EmployeeBasic(BaseModel):
    # Basic employee details
    emp_id: int = Field(..., ge=1000, le=999999, description="Employee numeric ID")
    name: str = Field(..., min_length=2, description="Give the valid full name")
    official_email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@ust\.com$", description="UST email address only")
    department: str = Field(default="Telecom", description="Department name")
    location: str = Field(default="Bangaluru", description="Location name")

class SimCard(BaseModel):
    # SIM card details
    sim_number: str = Field(..., pattern=r"^\d{10}$", description="Valid 10 digit number")
    provider: str = Field(default="Jio", description="Provider name")
    is_esim: bool = Field(default=False, description="Flag for eSIM")
    activation_year: int = Field(..., ge=2020, l2=2025, description="Year of activation")  # NOTE: 'l2' seems like a typo, should be 'le'

class DataPlan(BaseModel):
    # Data plan details
    name: str = Field(..., min_length=3, max_length=50, description="Name of the plan")
    monthly_gb: int = Field(..., gt=0, le=1000, description="Monthly data allowance in GB")
    speed_mbps: int = Field(default=50, ge=1, le=1000, description="Data speed in Mbps")
    is_roaming_include: bool = Field(default=False, description="Roaming inclusion flag")

class VoicePlan(BaseModel):
    # Voice plan details
    name: str = Field(..., min_length=3, description="Name of the plan")
    monthly_minutes: int = Field(..., ge=0, le=10000, description="Allowed minutes per month")
    has_isd: bool = Field(default=False, description="ISD enabled flag")
    per_minute_charge_paise: int = Field(default=0, ge=0, le=1000, description="Per minute charge in paise")

class EmergencyContact(BaseModel):
    # Emergency contact details
    name: str = Field(..., min_length=2, description="Contact name")
    relation: str = Field(default="Family", description="Relationship to employee")
    phone: str = Field(..., pattern=r"^[6-9]\d{9}$", description="Indian mobile number starting with 6–9")

class EmployeeTelecomProfile(BaseModel):
    # Aggregated telecom profile for an employee
    employee: EmployeeBasic
    sim: SimCard
    data_plan: Optional[DataPlan] = None
    voice_plan: Optional[VoicePlan] = None
    emergency_contact: Optional[EmergencyContact] = None

# -----------------------------
# FastAPI Application Setup
# -----------------------------

app = FastAPI(title="UST Employee Telecom Management API")

# In-memory storage for telecom profiles
telecom_profiles: List[EmployeeTelecomProfile] = []

# -----------------------------
# CRUD Endpoints
# -----------------------------

@app.post("/telecom/profiles", response_model=EmployeeTelecomProfile, status_code=201)
async def create_telecom_profile(profile: EmployeeTelecomProfile):
    """
    Create a new telecom profile.
    - Rejects if emp_id already exists (HTTP 409 Conflict).
    - Adds profile to in-memory list.
    """
    for existing_profile in telecom_profiles:
        if existing_profile.employee.emp_id == profile.employee.emp_id:
            raise HTTPException(
                status_code=409,
                detail=f"Profile with emp_id {profile.employee.emp_id} already exists"
            )
    telecom_profiles.append(profile)
    return profile

@app.get("/telecom/profiles", response_model=List[EmployeeTelecomProfile])
async def list_all_profiles():
    """
    Retrieve all telecom profiles.
    """
    return telecom_profiles

@app.get("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
async def get_profile_by_id(emp_id: int):
    """
    Retrieve a single profile by employee ID.
    - Returns 404 if not found.
    """
    for profile in telecom_profiles:
        if profile.employee.emp_id == emp_id:
            return profile
    raise HTTPException(status_code=404, detail="Profile not found")

@app.put("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
async def update_telecom_profile(emp_id: int, profile: EmployeeTelecomProfile):
    """
    Update an existing telecom profile.
    - Validates that emp_id in path matches emp_id in body.
    - Returns 404 if profile not found.
    """
    if profile.employee.emp_id != emp_id:
        raise HTTPException(
            status_code=400,
            detail="Employee ID in path does not match employee ID in request body"
        )
    for idx, existing_profile in enumerate(telecom_profiles):
        if existing_profile.employee.emp_id == emp_id:
            telecom_profiles[idx] = profile
            return profile
    raise HTTPException(status_code=404, detail="Profile not found")

@app.delete("/telecom/profiles/{emp_id}")
async def delete_profile(emp_id: int):
    """
    Delete a telecom profile by employee ID.
    - Returns confirmation message if deleted.
    - Returns 404 if not found.
    """
    for idx, profile in enumerate(telecom_profiles):
        if profile.employee.emp_id == emp_id:
            telecom_profiles.pop(idx)
            return {"detail": "Profile deleted"}
    raise HTTPException(status_code=404, detail="Profile not found")

@app.get("/telecom/profiles/search", response_model=List[EmployeeTelecomProfile])
async def search_profiles(
    department: Optional[str] = Query(None, description="Filter by department"),
    provider: Optional[str] = Query(None, description="Filter by SIM provider")
):
    """
    Search telecom profiles by optional filters:
    - Department
    - SIM provider
    """
    results = telecom_profiles
    if department:
        results = [p for p in results if p.employee.department == department]
    if provider:
        results = [p for p in results if p.sim.provider == provider]
    return results



# GET /telecom/profiles

# [
#   {
#     "employee": {
#       "emp_id": 12345,
#       "name": "Asha",
#       "official_email": "asha@ust.com",
#       "department": "Engineering",
#       "location": "Pune"
#     },
#     "sim": {
#       "sim_number": "9876543210",
#       "provider": "Airtel",
#       "is_esim": true,
#       "activation_year": 2023
#     },
#     "data_plan": {
#       "name": "Standard 50GB",
#       "monthly_gb": 50,
#       "speed_mbps": 100,
#       "is_roaming_include": true
#     },
#     "voice_plan": {
#       "name": "Office Calls Pack",
#       "monthly_minutes": 1000,
#       "has_isd": false,
#       "per_minute_charge_paise": 0
#     },
#     "emergency_contact": {
#       "name": "Ravi",
#       "relation": "Friend",
#       "phone": "9876543210"
#     }
#   }
# ]
# GET /telecom/profiles/search?department=Engineering&provider=Airtel
# [
#   {
#     "employee": {
#       "emp_id": 12345,
#       "name": "Asha",
#       "official_email": "asha@ust.com",
#       "department": "Engineering",
#       "location": "Pune"
#     },
#     "sim": {
#       "sim_number": "9876543210",
#       "provider": "Airtel",
#       "is_esim": true,
#       "activation_year": 2023
#     },
#     "data_plan": {
#       "name": "Standard 50GB",
#       "monthly_gb": 50,
#       "speed_mbps": 100,
#       "is_roaming_include": true
#     },
#     "voice_plan": {
#       "name": "Office Calls Pack",
#       "monthly_minutes": 1000,
#       "has_isd": false,
#       "per_minute_charge_paise": 0
#     },
#     "emergency_contact": {
#       "name": "Ravi",
#       "relation": "Friend",
#       "phone": "9876543210"
#     }
#   }
# ]

