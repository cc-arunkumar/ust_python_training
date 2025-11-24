# UST Employee Telecom Management
# API Specification and Validation Assignment
# 1. Context
# UST manages telecom services for its employees. For each employee, the system
# must store:
# Employee identity and contact information
# Company SIM details
# Optional data and voice plan information
# Optional emergency contact information
# You are required to design:
# 1. Pydantic models that validate the structure and constraints of this data.
# 2. FastAPI endpoints that use these models for request parsing and validation,
# with in-memory storage (lists) only.
# The focus is on correct modelling, validation behaviour, and clear API contracts.
# No database or authentication is required.

from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# create FastAPI app instance
app = FastAPI(title="UST Employee Telecom Device Registration")

# Data Models

class EmployeeBasic(BaseModel):
    # employee basic details
    emp_id: int = Field(..., ge=1000, le=999999, description="valid employee id")
    name: str = Field(..., min_length=2, description="min length 2")
    official_mail: str = Field(..., pattern="[a-zA-Z0-9_%+-]+@ust\\.com$")
    department: Optional[str] = Field(default="General")
    location: Optional[str] = Field(default="Bengaluru")

class SimCard(BaseModel):
    # sim card details
    sim_number: str = Field(..., pattern="^\\d{10}$", description="10 digit number")
    provider: str = Field(default="Jio")
    is_esim: Optional[bool] = Field(default=False)
    activation_year: int = Field(..., ge=2000, le=2025)

class DataPlan(BaseModel):
    #  data plan details
    name: str = Field(..., min_length=3, max_length=50)
    monthly_gb: int = Field(..., gt=0, le=1000)
    speed_mbps: Optional[int] = Field(default=50, ge=1, le=1000)
    is_roaming_included: Optional[bool] = Field(default=False)

class VoicePlan(BaseModel):
    # voice plan details
    name: str = Field(..., min_length=3)
    monthly_minutes: int = Field(..., ge=0, le=10000)
    has_isd: Optional[bool] = Field(default=False)
    per_minute_charge_paise: Optional[int] = Field(default=0, ge=0, le=1000)

class EmergencyContact(BaseModel):
    # emergency contact details
    name: str = Field(..., min_length=2)
    relation: Optional[str] = Field(default="Family")
    phone: str = Field(..., pattern='[6-9]\\d{9}$')

class EmployeeTelecomProfile(BaseModel):
    # full telecom profile
    employee: EmployeeBasic
    sim: SimCard
    data_plan: Optional[DataPlan] = Field(default=None)
    voice_plan: Optional[VoicePlan] = Field(default=None)
    emergency_contact: Optional[EmergencyContact] = Field(default=None)


# In-memory storage
employee_profile: List[EmployeeTelecomProfile] = []  # list of profiles

# API Endpoints

# POST: create new telecom profile
@app.post('/telecom/profiles', response_model=EmployeeTelecomProfile)
def create_telecom_profile(new_profile: EmployeeTelecomProfile):
    # add new profile, check duplicate emp_id
    for emp in employee_profile:
        if emp.employee.emp_id == new_profile.employee.emp_id:
            raise HTTPException(status_code=409, detail="Employee Already Exists")
    employee_profile.append(new_profile)
    return new_profile

# GET: fetch all profiles
@app.get('/telecom/profiles', response_model=List[EmployeeTelecomProfile])
def all_profiles():
    # return all profiles
    return employee_profile

# GET: search profiles by department/provider
@app.get('/telecom/profiles/search', response_model=List[EmployeeTelecomProfile])
def filter_profiles(department: str = None, provider: str = None):
    # filter by department or provider
    if department is None and provider is None:
        return employee_profile
    else:
        new_li = []
        for stored in employee_profile:
            stored_department = stored.employee.department if not isinstance(stored, dict) else stored['employee']['department']
            stored_provider = stored.sim.provider if not isinstance(stored, dict) else stored['sim']['provider']

            if department and provider:
                if stored_department == department and stored_provider == provider:
                    new_li.append(stored)
            elif department:
                if stored_department == department:
                    new_li.append(stored)
            elif provider:
                if stored_provider == provider:
                    new_li.append(stored)
        return new_li

# GET: fetch profile by emp_id
@app.get('/telecom/profiles/{emp_id}')
def get_profile_id(emp_id: int):
    # get profile by emp_id
    for emp in employee_profile:
        stored_id = emp.employee.emp_id if not isinstance(emp, dict) else emp['employee']['emp_id']
        if stored_id == emp_id:
            return emp
    raise HTTPException(status_code=404, detail="Profile Not Found")

# PUT: update profile by emp_id
@app.put('/telecom/profiles/{emp_id}', response_model=EmployeeTelecomProfile)
def update_profile(emp_id: int, updated_emp: EmployeeTelecomProfile):
    # update profile by emp_id
    if updated_emp.employee.emp_id != emp_id:
        raise HTTPException(status_code=400, detail="Path emp_id and body employee.emp_id do not match")

    for idx, stored in enumerate(employee_profile):
        stored_id = stored.employee.emp_id if not isinstance(stored, dict) else stored['employee']['emp_id']
        if stored_id == emp_id:
            employee_profile[idx] = updated_emp
            return updated_emp

    raise HTTPException(status_code=404, detail="Profile Not Found")

# Sample Output (GET /telecom/profiles/search?department=IT&provider=Jio):
# [
#   { "employee": {"emp_id": 1001, "name": "Arun", "official_mail": "arun@ust.com", "department": "IT", "location": "Bengaluru"},
#     "sim": {"sim_number": "9876543210", "provider": "Jio", "is_esim": false, "activation_year": 2023}
#   }
# ]

# Sample Output (GET /telecom/profiles/{emp_id}):
# {
#   "employee": {"emp_id": 1001, "name": "ramu", "official_mail": "ramu@ust.com", "department": "IT", "location": "Bengaluru"},
#   "sim": {"sim_number": "9876543210", "provider": "Jio", "is_esim": false, "activation_year": 2023}
# }

# Sample Output (PUT /telecom/profiles/{emp_id}):
# {
#   "employee": {"emp_id": 1001, "name": "Abhi", "official_mail": "abhi@ust.com", "department": "HR", "location": "Chennai"},
#   "sim": {"sim_number": "9876543210", "provider": "Airtel", "is_esim": true, "activation_year": 2024}
# }

# Error Output (POST /telecom/profiles):
# 409 Conflict -> {"detail": "Employee Already Exists"}

# Error Output (GET /telecom/profiles/{emp_id}):
# 404 Not Found -> {"detail": "Profile Not Found"}

# Error Output (PUT /telecom/profiles/{emp_id}):
# 400 Bad Request -> {"detail": "Path emp_id and body employee.emp_id do not match"}
# 404 Not Found -> {"detail": "Profile Not Found"}




