# UST Employee Telecom Management
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
import re

# Initialize the FastAPI application
app = FastAPI(title="UST Employee Telecom Management API")

# In-memory storage for employee profiles
# Note: For production, consider using a persistent database instead of in-memory storage.
profiles: List[dict] = []

# Pydantic Models for Data Validation
# Models ensure the incoming data is validated and conform to the defined structure.

class EmployeeBasic(BaseModel):
    # Employee basic details with validation rules
    emp_id: int = Field(..., ge=1000, le=999999)  # Employee ID should be between 1000 and 999999
    name: str = Field(..., min_length=2)  # Name should be at least 2 characters long
    official_email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@ust\.com$")  # Email should follow a specific format
    department: str = Field("Telecom")  # Default department set to 'Telecom'
    location: str = Field("Bengaluru")  # Default location set to 'Bengaluru'


class SimCard(BaseModel):
    # Sim card details with validation rules
    sim_number: str = Field(..., pattern=r"^\d{10}$")  # SIM number must be exactly 10 digits
    provider: str = Field("Jio")  # Default provider is Jio
    is_esim: bool = Field(False)  # Default is non-ESIM
    activation_year: int = Field(..., ge=2020, le=2025)  # Activation year should be between 2020 and 2025

class DataPlan(BaseModel):
    # Data plan details with validation rules
    name: str = Field(..., min_length=3, max_length=50)  # Plan name should be between 3 and 50 characters
    monthly_gb: int = Field(..., gt=0, le=1000)  # Monthly GB should be between 1 and 1000
    speed_mbps: int = Field(50, ge=1, le=1000)  # Speed should be between 1 and 1000 Mbps
    is_roaming_included: bool = Field(False)  # Default is no roaming

class VoicePlan(BaseModel):
    # Voice plan details with validation rules
    name: str = Field(..., min_length=3)  # Plan name should be at least 3 characters
    monthly_minutes: int = Field(..., ge=0, le=10000)  # Monthly minutes should be between 0 and 10000
    has_isd: bool = Field(False)  # Default is no ISD included
    per_minute_charge_paise: int = Field(0, ge=0, le=1000)  # Charge per minute (in paise), between 0 and 1000

class EmergencyContact(BaseModel):
    # Emergency contact details with validation rules
    name: str = Field(..., min_length=2)  # Contact name should be at least 2 characters
    relation: str = Field("Family")  # Default relation is 'Family'
    phone: str = Field(..., pattern=r"^[6-9]\d{9}$")  # Phone number must follow Indian mobile format

class EmployeeTelecomProfile(BaseModel):
    # Composite model for employee telecom profile
    employee: EmployeeBasic  # Employee basic details
    sim: SimCard  # SIM card details
    data_plan: Optional[DataPlan] = None  # Optional data plan
    voice_plan: Optional[VoicePlan] = None  # Optional voice plan
    emergency_contact: Optional[EmergencyContact] = None  # Optional emergency contact


# API Endpoints

@app.post("/telecom/profiles", status_code=201)
async def create_profile(profile: EmployeeTelecomProfile):
    # Check if the employee already exists
    # Ensures that employee profiles are unique by emp_id
    for existing_profile in profiles:
        if existing_profile['employee']['emp_id'] == profile.employee.emp_id:
            raise HTTPException(status_code=409, detail="Employee ID already exists")
    
    # Add the profile to in-memory storage
    # Note: Replace with database operation for production
    profiles.append(profile.dict())
    return profile

@app.post("/telecom/profiles/minimal", status_code=201)
async def create_minimal_profile(profile: EmployeeTelecomProfile):
    # Create a profile with default values for missing fields
    return await create_profile(profile)

@app.get("/telecom/profiles", response_model=List[EmployeeTelecomProfile])
async def list_profiles():
    # Return the list of all employee telecom profiles
    return profiles

@app.get("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
async def get_profile(emp_id: int):
    # Retrieve a specific employee profile by emp_id
    for profile in profiles:
        if profile['employee']['emp_id'] == emp_id:
            return profile
    raise HTTPException(status_code=404, detail="Profile not found")

@app.put("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
async def update_profile(emp_id: int, profile: EmployeeTelecomProfile):
    # Update an existing employee profile by emp_id
    for index, existing_profile in enumerate(profiles):
        if existing_profile['employee']['emp_id'] == emp_id:
            if existing_profile['employee']['emp_id'] != profile.employee.emp_id:
                raise HTTPException(status_code=400, detail="Path id does not match body id")
            profiles[index] = profile.dict()
            return profile
    raise HTTPException(status_code=404, detail="Profile not found")

@app.delete("/telecom/profiles/{emp_id}")
async def delete_profile(emp_id: int):
    # Delete an employee profile by emp_id
    global profiles
    profiles = [profile for profile in profiles if profile['employee']['emp_id'] != emp_id]
    return {"detail": "Profile deleted"}

@app.get("/telecom/profiles/search", response_model=List[EmployeeTelecomProfile])
async def search_profiles(department: Optional[str] = None, provider: Optional[str] = None):
    # Search profiles by department or provider
    filtered_profiles = profiles
    if department:
        filtered_profiles = [profile for profile in filtered_profiles if profile['employee']['department'] == department]
    if provider:
        filtered_profiles = [profile for profile in filtered_profiles if profile['sim']['provider'] == provider]
    return filtered_profiles


# Validation Errors for Invalid Scenarios
# These endpoints help validate input data before using it in the main application

@app.get("/validate/emp_id")
async def validate_emp_id(emp_id: int):
    # Validate employee ID range
    if not (1000 <= emp_id <= 999999):
        raise HTTPException(status_code=422, detail="emp_id must be between 1000 and 999999")
    return {"emp_id": emp_id}

@app.get("/validate/name")
async def validate_name(name: str):
    # Validate name length
    if len(name) < 2:
        raise HTTPException(status_code=422, detail="Name must have at least 2 characters")
    return {"name": name}

@app.get("/validate/email")
async def validate_email(email: str):
    # Validate email format
    if not re.match(r"^[a-zA-Z0-9._%+-]+@ust\.com$", email):
        raise HTTPException(status_code=422, detail="Email must end with @ust.com")
    return {"email": email}

@app.get("/validate/sim_number")
async def validate_sim_number(sim_number: str):
    # Validate SIM number format
    if not re.match(r"^\d{10}$", sim_number):
        raise HTTPException(status_code=422, detail="SIM number must be exactly 10 digits")
    return {"sim_number": sim_number}

@app.get("/validate/activation_year")
async def validate_activation_year(year: int):
    # Validate SIM activation year range
    if not (2020 <= year <= 2025):
        raise HTTPException(status_code=422, detail="Activation year must be between 2020 and 2025")
    return {"activation_year": year}

@app.get("/validate/phone")
async def validate_phone(phone: str):
    # Validate emergency contact phone format
    if not re.match(r"^[6-9]\d{9}$", phone):
        raise HTTPException(status_code=422, detail="Phone number must be an Indian mobile number starting with 6, 7, 8, or 9")
    return {"phone": phone}


