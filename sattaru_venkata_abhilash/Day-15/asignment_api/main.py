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

from typing import Dict, List, Optional, Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# Initialize FastAPI application with a custom title
app = FastAPI(title="Employee Telecom Management")

# Define the Pydantic model for basic employee details
class EmployeeBasic(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)
    name: str = Field(..., min_length=2)
    official_email: str = Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@ust\.com$')
    department: str = "Telecom"
    location: str = "Bengaluru"

# Define the Pydantic model for SIM card details
class SIMCard(BaseModel):
    sim_number: str = Field(..., min_length=10, max_length=10, pattern=r'^\d{10}$')
    provider: str = "Jio"
    is_esim: bool = False
    activation_year: int = Field(..., ge=2020, le=2025)

# Define the Pydantic model for data plan details
class DataPlan(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    monthly_gb: int = Field(..., gt=0, le=1000)
    speed_mbps: int = Field(50, ge=1, le=1000)
    is_roaming_included: bool = False

# Define the Pydantic model for voice plan details
class VoicePlan(BaseModel):
    name: str = Field(..., min_length=3)
    monthly_minutes: int = Field(..., ge=0, le=10000)
    has_isd: bool = False
    per_minute_charge_paise: int = Field(0, ge=0, le=1000)

# Define the Pydantic model for emergency contact details
class EmergencyContact(BaseModel):
    name: str = Field(..., min_length=2)
    relation: str = "Family"
    phone: str = Field(..., pattern=r'^[6-9]\d{9}$')

# Define the main profile combining employee details, SIM, data plan, voice plan, and emergency contact
class EmployeeTelecomProfile(BaseModel):
    employee: EmployeeBasic = Field(...)
    sim: SIMCard = Field(...)
    data_plan: Optional[DataPlan] = None
    voice_plan: Optional[VoicePlan] = None
    emergency_contact: Optional[EmergencyContact] = None

# Dictionary to hold employee telecom profiles by employee ID
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

telecom_data: Dict[int, EmployeeTelecomProfile] = {}

given_data = EmployeeTelecomProfile(**data)

# Store the profile in the telecom_data dictionary
telecom_data[given_data.employee.emp_id] = given_data

# POST endpoint to create a new telecom profile
@app.post("/telecom/profiles", response_model=EmployeeTelecomProfile)
def create_data(profile: EmployeeTelecomProfile):
    employee_id = profile.employee.emp_id
    if employee_id in telecom_data:
        raise HTTPException(status_code=409, detail="emp_id already exists")
    
    telecom_data[employee_id] = profile
    return profile

# GET endpoint to retrieve all telecom profiles
@app.get("/telecom/profiles")
def get_details():
    return list(telecom_data.values())

# GET endpoint to retrieve a telecom profile by employee ID
@app.get("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def get_by_emp_id(emp_id: int):
    if emp_id in telecom_data:
        return telecom_data[emp_id]
    else:
        raise HTTPException(status_code=404, detail="Profile not found")

# PUT endpoint to update an existing telecom profile
@app.put("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def update_data(emp_id: int, emp: EmployeeTelecomProfile):

    if emp_id not in telecom_data:
        raise HTTPException(status_code=404, detail="No existing profile")
    
    if emp_id != emp.employee.emp_id:
        raise HTTPException(status_code=400, detail="Path ID vs body ID mismatch")
    

    telecom_data[emp_id] = emp
    return emp

# DELETE endpoint to delete a telecom profile by employee ID
@app.delete("/telecom/profiles/{emp_id}")
def delete_emp(emp_id: int):

    if emp_id in telecom_data:
        del telecom_data[emp_id]
        return {"detail": "Profile deleted"}
    else:
        raise HTTPException(status_code=404, detail="Profile not found")

# GET endpoint to search for telecom profiles by department or provider
@app.get("/telecom/profiles/search", response_model=List[EmployeeTelecomProfile])
def search_profiles(department: Optional[str] = None, provider: Optional[str] = None):
    results = list(telecom_data.values())
    
    # Filter by department if provided
    if department:
        results = [p for p in results if p.employee.department == department]
    
    if provider:
        results = [p for p in results if p.sim.provider == provider]
    
    # Return the filtered list of profiles
    return results


# Sample output
# Get Details:

# Code	
# 200	
# Response body

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

# Put method:
# input:

# Edit Value
# Schema
# {
#   "employee": {
#     "emp_id": 1000,
#     "name": "string",
#     "official_email": "o4Uu_Y2WeR4lvGlDPXCOsqFxAGnDg-PJEpy3xURG.H%7h_t%gtKFemvnaOVPaSNkr_9aSId-RlM@ust.com",
#     "department": "Telecom",
#     "location": "Bengaluru"
#   },
#   "sim": {
#     "sim_number": "9700760957",
#     "provider": "Jio",
#     "is_esim": false,
#     "activation_year": 2020
#   },
#   "data_plan": {
#     "name": "string",
#     "monthly_gb": 1,
#     "speed_mbps": 50,
#     "is_roaming_included": false
#   },
#   "voice_plan": {
#     "name": "string",
#     "monthly_minutes": 10000,
#     "has_isd": false,
#     "per_minute_charge_paise": 0
#   },
#   "emergency_contact": {
#     "name": "string",
#     "relation": "Family",
#     "phone": "7112876333"
#   }
# }

# Ouput:
# Code	Details
# 200	
# Response body
# Download
# {
#   "employee": {
#     "emp_id": 1000,
#     "name": "string",
#     "official_email": "o4Uu_Y2WeR4lvGlDPXCOsqFxAGnDg-PJEpy3xURG.H%7h_t%gtKFemvnaOVPaSNkr_9aSId-RlM@ust.com",
#     "department": "Telecom",
#     "location": "Bengaluru"
#   },
#   "sim": {
#     "sim_number": "9700760957",
#     "provider": "Jio",
#     "is_esim": false,
#     "activation_year": 2020
#   },
#   "data_plan": {
#     "name": "string",
#     "monthly_gb": 1,
#     "speed_mbps": 50,
#     "is_roaming_included": false
#   },
#   "voice_plan": {
#     "name": "string",
#     "monthly_minutes": 10000,
#     "has_isd": false,
#     "per_minute_charge_paise": 0
#   },
#   "emergency_contact": {
#     "name": "string",
#     "relation": "Family",
#     "phone": "7112876333"
#   }
# }
