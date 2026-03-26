# Importing required libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

# Initialize FastAPI app
app = FastAPI(title="UST Telecom")

# -----------------------------
# Employee Basic Information
# -----------------------------
class EmployeeBasic(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)  # Employee ID must be between 1000 and 999999
    name: str = Field(..., min_length=2)          # Name must be at least 2 characters
    official_email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@ust\.com$")  # Only @ust.com emails allowed
    department: str = "Telecom"                   # Default department
    location: str = "Bengaluru"                   # Default location

# -----------------------------
# SIM Card Information
# -----------------------------
class SimCard(BaseModel):
    sim_number: str = Field(..., pattern=r"^\d{10}$")  # Must be exactly 10 digits
    provider: str = "Jio"                              # Default provider
    is_esim: bool = False                              # Default physical SIM
    activation_year: int = Field(..., ge=2020, le=2025)  # Valid years only

# -----------------------------
# Data Plan Information
# -----------------------------
class DataPlan(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    monthly_gb: int = Field(..., gt=0, le=1000)        # Must be >0 GB
    speed_mbps: int = Field(50, ge=1, le=1000)         # Default 50 Mbps
    is_roaming_included: bool = False

# -----------------------------
# Voice Plan Information
# -----------------------------
class VoicePlan(BaseModel):
    name: str = Field(..., min_length=3)
    monthly_minutes: int = Field(..., ge=0, le=10000)
    has_isd: bool = False
    per_minute_charge_paise: int = Field(0, ge=0, le=1000)

# -----------------------------
# Emergency Contact
# -----------------------------
class EmergencyContact(BaseModel):
    name: str = Field(..., min_length=2)
    relation: str = "Family"
    phone: str = Field(..., pattern=r"^[6-9]\d{9}$")  # Must start with 6–9 and be 10 digits

# -----------------------------
# Employee Telecom Profile
# -----------------------------
class EmployeeTelecomProfile(BaseModel):
    employee: EmployeeBasic
    sim: SimCard
    data_plan: Optional[DataPlan] = None
    voice_plan: Optional[VoicePlan] = None
    emergency_contact: Optional[EmergencyContact] = None

# In-memory storage (⚠️ resets when server restarts)
profiles = []

# -----------------------------
# CRUD Endpoints
# -----------------------------

# Create new profile
@app.post("/telecom/profiles", response_model=EmployeeTelecomProfile, status_code=201)
def create_profile(profile: EmployeeTelecomProfile):
    for p in profiles:
        if p.employee.emp_id == profile.employee.emp_id:
            raise HTTPException(409, "Profile already exists")
    profiles.append(profile)
    return profile

# Get all profiles
@app.get("/telecom/profiles", response_model=list[EmployeeTelecomProfile])
def get_all():
    return profiles

# Get single profile by ID
@app.get("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def get_one(emp_id: int):
    for p in profiles:
        if p.employee.emp_id == emp_id:
            return p
    raise HTTPException(404, "Profile not found")

# Update profile by ID
@app.put("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def update_profile(emp_id: int, profile: EmployeeTelecomProfile):
    if emp_id != profile.employee.emp_id:
        raise HTTPException(400, "ID mismatch")
    for i, p in enumerate(profiles):
        if p.employee.emp_id == emp_id:
            profiles[i] = profile
            return profile
    raise HTTPException(404, "Profile not found")

# Delete profile by ID
@app.delete("/telecom/profiles/{emp_id}")
def delete_one(emp_id: int):
    for p in profiles:
        if p.employee.emp_id == emp_id:
            profiles.remove(p)
            return {"detail": "Profile deleted"}
    raise HTTPException(404, "Profile not found")

# Search profiles by department or provider
@app.get("/telecom/profiles/search", response_model=list[EmployeeTelecomProfile])
def search(department: Optional[str] = None, provider: Optional[str] = None):
    result = profiles
    if department:
        result = [p for p in result if p.employee.department == department]
    if provider:
        result = [p for p in result if p.sim.provider == provider]
    return result


"""SAMPLE OUTPUT
1. CREATE PROFILE (POST /telecom/profiles)
{
  "employee": {
    "emp_id": 1001,
    "name": "gowtham",
    "official_email": "gowtham@ust.com",
    "department": "Telecom",
    "location": "Bengaluru"
  },
  "sim": {
    "sim_number": "9876543210",
    "provider": "Jio",
    "is_esim": false,
    "activation_year": 2023
  },
  "data_plan": {
    "name": "SuperFast",
    "monthly_gb": 200,
    "speed_mbps": 100,
    "is_roaming_included": true
  },
  "voice_plan": {
    "name": "TalkMore",
    "monthly_minutes": 500,
    "has_isd": true,
    "per_minute_charge_paise": 50
  },
  "emergency_contact": {
    "name": "Sakthi",
    "relation": "Family",
    "phone": "9876543211"
  }
}


2. GET ALL PROFILES (GET /telecom/profiles)
[
  {
    "employee": {
      "emp_id": 1001,
      "name": "gowtham",
      "official_email": "gowtham@ust.com",
      "department": "Telecom",
      "location": "Bengaluru"
    },
    "sim": {
      "sim_number": "9876543210",
      "provider": "Jio",
      "is_esim": false,
      "activation_year": 2023
    },
    "data_plan": {
      "name": "SuperFast",
      "monthly_gb": 200,
      "speed_mbps": 100,
      "is_roaming_included": true
    },
    "voice_plan": {
      "name": "TalkMore",
      "monthly_minutes": 500,
      "has_isd": true,
      "per_minute_charge_paise": 50
    },
    "emergency_contact": {
      "name": "Sakthi",
      "relation": "Family",
      "phone": "9876543211"
    }
  }
]

3. GET PROFILE BY ID (GET /telecom/profiles/1001)
{
  "employee": {
    "emp_id": 1001,
    "name": "gowtham",
    "official_email": "gowtham@ust.com",
    "department": "Telecom",
    "location": "Bengaluru"
  },
  "sim": {
    "sim_number": "9876543210",
    "provider": "Jio",
    "is_esim": false,
    "activation_year": 2023
  },
  "data_plan": {
    "name": "SuperFast",
    "monthly_gb": 200,
    "speed_mbps": 100,
    "is_roaming_included": true
  },
  "voice_plan": {
    "name": "TalkMore",
    "monthly_minutes": 500,
    "has_isd": true,
    "per_minute_charge_paise": 50
  },
  "emergency_contact": {
    "name": "Sakthi",
    "relation": "Family",
    "phone": "9876543211"
  }
}


4. UPDATE PROFILE (PUT /telecom/profiles/1001)
{
  "employee": {
    "emp_id": 1001,
    "name": "gowtham Updated",
    "official_email": "gowtham21@ust.com",
    "department": "Telecom",
    "location": "Bengaluru"
  },
  "sim": {
    "sim_number": "9876543210",
    "provider": "Jio",
    "is_esim": false,
    "activation_year": 2023
  }
}
5. DELETE PROFILE (DELETE /telecom/profiles/1001)
{
  "detail": "Profile deleted"
}


"""