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
# No database or authentication is required

from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# Initialize FastAPI app with a title
app = FastAPI(title="Employee Telecom Management")


# Define Pydantic Models


class EmployeeBasic(BaseModel):
    # Employee basic details with validation rules
    emp_id: int = Field(..., ge=1000, le=999999)   # Employee ID must be between 1000 and 999999
    name: str = Field(..., min_length=2)           # Name must have at least 2 characters
    official_email: str = Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@ust\.com$')  # Must be UST email
    department: str = "Telecom"                    # Default department
    location: str = "Bengaluru"                    # Default location

class SIMCard(BaseModel):
    # SIM card details
    sim_number: str = Field(..., min_length=10, max_length=10, pattern=r'^\d{10}$')  # 10-digit number
    provider: str = "Jio"                         # Default provider
    is_esim: bool = False                         # Default physical SIM
    activation_year: int = Field(..., ge=2020, le=2025)  # Valid activation years

class DataPlan(BaseModel):
    # Internet data plan details
    name: str = Field(..., min_length=3, max_length=50)
    monthly_gb: int = Field(..., gt=0, le=1000)   # Monthly data limit
    speed_mbps: int = Field(50, ge=1, le=1000)    # Default 50 Mbps
    is_roaming_included: bool = False             # Default roaming not included

class VoicePlan(BaseModel):
    # Voice call plan details
    name: str = Field(..., min_length=3)
    monthly_minutes: int = Field(..., ge=0, le=10000)
    has_isd: bool = False
    per_minute_charge_paise: int = Field(0, ge=0, le=1000)

class EmergencyContact(BaseModel):
    # Emergency contact details
    name: str = Field(..., min_length=2)
    relation: str = "Family"
    phone: str = Field(..., pattern=r'^[6-9]\d{9}$')  # Valid Indian mobile number

class EmployeeTelecomProfile(BaseModel):
    # Complete telecom profile combining all models
    employee: EmployeeBasic = Field(...)
    sim: SIMCard = Field(...)
    data_plan: Optional[DataPlan] = None
    voice_plan: Optional[VoicePlan] = None
    emergency_contact: Optional[EmergencyContact] = None

# Sample Data Initialization


data = {
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

# Dictionary to store profiles keyed by employee ID
telecom_data: Dict[int, EmployeeTelecomProfile] = {}

# Load initial data into dictionary
given_data = EmployeeTelecomProfile(**data)
telecom_data[given_data.employee.emp_id] = given_data


# API Endpoints


@app.post("/telecom/profiles", response_model=EmployeeTelecomProfile)
def create_data(profile: EmployeeTelecomProfile):
    """Create a new employee telecom profile"""
    employee_id = profile.employee.emp_id
    if employee_id in telecom_data:
        raise HTTPException(status_code=409, detail="emp_id already exists")
    telecom_data[employee_id] = profile
    return profile

@app.get("/telecom/profiles")
def get_details():
    """Get all employee telecom profiles"""
    return list(telecom_data.values())

@app.get("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def get_by_emp_id(emp_id: int):
    """Get a profile by employee ID"""
    if emp_id in telecom_data:
        return telecom_data[emp_id]
    else:
        raise HTTPException(status_code=404, detail="Profile not found")

@app.put("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def update_data(emp_id: int, emp: EmployeeTelecomProfile):
    """Update an existing profile"""
    if emp_id not in telecom_data:
        raise HTTPException(status_code=404, detail="no existing profile")
    if emp_id != emp.employee.emp_id:
        raise HTTPException(status_code=400, detail="path id vs body id mismatch")
    telecom_data[emp_id] = emp
    return emp

@app.delete("/telecom/profiles/{emp_id}")
def delete_emp(emp_id: int):
    """Delete a profile by employee ID"""
    if emp_id in telecom_data:
        del telecom_data[emp_id]
        return {"detail": "Profile deleted"}
    else:
        raise HTTPException(status_code=404, detail="profile not found")

@app.get("/telecom/profiles/search", response_model=List[EmployeeTelecomProfile])
def search_profiles(department: Optional[str] = None, provider: Optional[str] = None):
    """Search profiles by department or provider"""
    results = list(telecom_data.values())
    if department:
        results = [p for p in results if p.employee.department == department]
    if provider:
        results = [p for p in results if p.sim.provider == provider]
    return results


# -------------------------------------------------------------------------------

# Sample Output
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
#       "is_roaming_included": true
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
