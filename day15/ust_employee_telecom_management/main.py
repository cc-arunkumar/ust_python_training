from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional

# Define Pydantic data models

# EmployeeBasic Model - Contains basic employee details
class EmployeeBasic(BaseModel):
    emp_id: int
    name: str
    official_email: str
    department: Optional[str] = "Telecom"
    location: Optional[str] = "Bengaluru"

    # Validate emp_id to ensure it's within the specified range
    @field_validator('emp_id')
    def validate_emp_id(cls, v):
        if not (1000 <= v <= 999999):
            raise ValueError('emp_id must be between 1000 and 999999')
        return v

    # Validate official email to ensure it ends with '@ust.com'
    @field_validator('official_email')
    def validate_email(cls, v):
        if not v.endswith('@ust.com'):
            raise ValueError('Email must be a UST email address.')
        return v

    # Validate name length to ensure it has at least 2 characters
    @field_validator('name')
    def validate_name(cls, v):
        if len(v) < 2:
            raise ValueError('Name must be at least 2 characters long.')
        return v

# SimCard Model - Contains details of the employee's SIM card
class SimCard(BaseModel):
    sim_number: str
    provider: Optional[str] = "Jio"
    is_esim: Optional[bool] = False
    activation_year: int

    # Validate sim_number to ensure it's a 10-digit number
    @field_validator('sim_number')
    def validate_sim_number(cls, v):
        if not v.isdigit() or len(v) != 10:
            raise ValueError('sim_number must be a 10-digit number.')
        return v

    # Validate activation year to ensure it's between 2020 and 2025
    @field_validator('activation_year')
    def validate_activation_year(cls, v):
        if not (2020 <= v <= 2025):
            raise ValueError('activation_year must be between 2020 and 2025')
        return v

# DataPlan Model - Contains details of the employee's data plan
class DataPlan(BaseModel):
    name: str
    monthly_gb: int
    speed_mbps: Optional[int] = 50
    is_roaming_included: Optional[bool] = False

    # Validate monthly_gb to ensure it's between 1 and 1000
    @field_validator('monthly_gb')
    def validate_monthly_gb(cls, v):
        if not (1 <= v <= 1000):
            raise ValueError('monthly_gb must be between 1 and 1000')
        return v

# VoicePlan Model - Contains details of the employee's voice plan
class VoicePlan(BaseModel):
    name: str
    monthly_minutes: int
    has_isd: Optional[bool] = False
    per_minute_charge_paise: Optional[int] = 0

    # Validate monthly_minutes to ensure it's between 0 and 10000
    @field_validator('monthly_minutes')
    def validate_monthly_minutes(cls, v):
        if not (0 <= v <= 10000):
            raise ValueError('monthly_minutes must be between 0 and 10000')
        return v

    # Validate per_minute_charge_paise to ensure it's between 0 and 1000
    @field_validator('per_minute_charge_paise')
    def validate_per_minute_charge_paise(cls, v):
        if not (0 <= v <= 1000):
            raise ValueError('per_minute_charge_paise must be between 0 and 1000')
        return v

# EmergencyContact Model - Contains details of an emergency contact for the employee
class EmergencyContact(BaseModel):
    name: str
    relation: Optional[str] = "Family"
    phone: str

    # Validate phone number to ensure it is a valid Indian mobile number
    @field_validator('phone')
    def validate_phone(cls, v):
        if not (v.isdigit() and len(v) == 10 and v[0] in '6789'):
            raise ValueError('phone must be a valid Indian mobile number (starting with 6-9)')
        return v

# EmployeeTelecomProfile Model - Combines employee information with telecom services
class EmployeeTelecomProfile(BaseModel):
    employee: EmployeeBasic
    sim: SimCard
    data_plan: Optional[DataPlan] = None
    voice_plan: Optional[VoicePlan] = None
    emergency_contact: Optional[EmergencyContact] = None


# Initialize FastAPI application
app = FastAPI()

# In-memory storage for employee telecom profiles
Profiles: List[EmployeeTelecomProfile] = []

# CREATE: Add a new telecom profile for an employee
@app.post("/telecom/profiles")
def create_telecom_profile(profile: EmployeeTelecomProfile):
    # Check if the employee ID already exists in the profiles list
    for existing_profile in Profiles:
        if existing_profile.employee.emp_id == profile.employee.emp_id:
            raise HTTPException(status_code=409, detail="Employee id already exists")
    Profiles.append(profile)
    return profile  

# READ: Retrieve all telecom profiles
@app.get("/telecom/profiles")
def get_all_profiles():
    return Profiles

# SEARCH: Filter profiles by department and/or provider
@app.get("/telecom/profiles/search")
def get_profile_params(department: str = "", provider: str = ""):
    # If no filters provided, return all profiles
    if department == "" and provider == "":
        return Profiles
    # If both department and provider provided, filter accordingly
    if department != "" and provider != "":
        filtered_by_department = [profile for profile in Profiles if profile.employee.department == department]
        return filtered_by_department
    # If only provider provided, filter by provider
    elif department == "" and provider != "":
        filtered_by_provider = [profile for profile in Profiles if profile.sim.provider == provider]
        return filtered_by_provider
    # If only department provided, filter by department
    else:
        filtered_by_combined = [profile for profile in Profiles if profile.employee.department == department and profile.sim.provider == provider]
        return filtered_by_combined

# READ: Get a specific profile by employee ID
@app.get("/telecom/profiles/{emp_id}")
def get_profile(emp_id: int):
    for profile in Profiles:
        if profile.employee.emp_id == emp_id:
            return profile
    raise HTTPException(status_code=404, detail="Profile not found")

# UPDATE: Modify an existing profile by employee ID
@app.put("/telecom/profiles/{emp_id}")
def update_profile(emp_id: int, updated_profile: EmployeeTelecomProfile):
    for idx, profile in enumerate(Profiles):
        if profile.employee.emp_id == emp_id:
            Profiles[idx] = updated_profile
            return updated_profile
    raise HTTPException(status_code=404, detail="Employee id does not exist")

# DELETE: Remove a profile by employee ID
@app.delete("/telecom/profiles/{emp_id}")
def delete_profile(emp_id: int):
    for idx, profile in enumerate(Profiles):
        if profile.employee.emp_id == emp_id:
            Profiles.pop(idx)
            return {"detail": "Profile deleted"}
    return {"detail": "Profile Not Found"}
