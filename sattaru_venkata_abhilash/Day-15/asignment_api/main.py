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

app = FastAPI(title="Employee Telecom Management")

# Pydantic model for Employee's basic information
class EmployeeBasic(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)  # Employee ID should be between 1000 and 999999
    name: str = Field(..., min_length=2)  # Employee name should have at least 2 characters
    official_email: str = Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@ust\.com$')  # Email should be a valid UST email
    department: str = "Telecom"  # Default department value is "Telecom"
    location: str = "Bengaluru"  # Default location value is "Bengaluru"

# Pydantic model for SIM card details
class SIMCard(BaseModel):
    sim_number: str = Field(..., min_length=10, max_length=10, pattern=r'^\d{10}$')  # SIM number must be a 10-digit number
    provider: str = "Jio"  # Default provider is "Jio"
    is_esim: bool = False  # Default is false, assuming the SIM is not an eSIM
    activation_year: int = Field(..., ge=2020, le=2025)  # SIM activation year should be between 2020 and 2025

# Pydantic model for Data Plan details
class DataPlan(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)  # Data plan name should be between 3 and 50 characters
    monthly_gb: int = Field(..., gt=0, le=1000)  # Monthly GB usage must be between 1 and 1000
    speed_mbps: int = Field(50, ge=1, le=1000)  # Speed in Mbps must be between 1 and 1000 (default is 50)
    is_roaming_included: bool = False  # Default is false, assuming roaming is not included

# Pydantic model for Voice Plan details
class VoicePlan(BaseModel):
    name: str = Field(..., min_length=3)  # Voice plan name should have at least 3 characters
    monthly_minutes: int = Field(..., ge=0, le=10000)  # Monthly minutes must be between 0 and 10000
    has_isd: bool = False  # Default is false, assuming no ISD feature
    per_minute_charge_paise: int = Field(0, ge=0, le=1000)  # Per-minute charge must be between 0 and 1000 paise

# Pydantic model for Emergency Contact details
class EmergencyContact(BaseModel):
    name: str = Field(..., min_length=2)  # Emergency contact name should have at least 2 characters
    relation: str = "Family"  # Default relation is "Family"
    phone: str = Field(..., pattern=r'^[6-9]\d{9}$')  # Phone number must be a valid Indian phone number (starting with 6-9)

# Main model that combines Employee, SIM, Data Plan, Voice Plan, and Emergency Contact
class EmployeeTelecomProfile(BaseModel):
    employee: EmployeeBasic = Field(...)  # Employee details
    sim: SIMCard = Field(...)  # SIM card details
    data_plan: Optional[DataPlan] = None  # Data plan details (optional)
    voice_plan: Optional[VoicePlan] = None  # Voice plan details (optional)
    emergency_contact: Optional[EmergencyContact] = None  # Emergency contact details (optional)

# In-memory storage to hold employee telecom profiles
telecom_data: Dict[int, EmployeeTelecomProfile] = {}

# Sample data for a telecom profile
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

# Creating a new telecom profile and storing it in the dictionary
given_data = EmployeeTelecomProfile(**data)
telecom_data[given_data.employee.emp_id] = given_data

# POST endpoint to create a new telecom profile
@app.post("/telecom/profiles", response_model=EmployeeTelecomProfile)
def create_data(profile: EmployeeTelecomProfile):
    employee_id = profile.employee.emp_id
    if employee_id in telecom_data:  # Check if profile with the same emp_id already exists
        raise HTTPException(status_code=409, detail="emp_id already exists")  # Conflict error
    telecom_data[employee_id] = profile  # Add the profile to the in-memory data store
    return profile  # Return the created profile

# GET endpoint to fetch all telecom profiles
@app.get("/telecom/profiles")
def get_details():
    return list(telecom_data.values())  # Return all profiles in the dictionary

# GET endpoint to fetch a telecom profile by employee ID
@app.get("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def get_by_emp_id(emp_id: int):
    if emp_id in telecom_data:
        return telecom_data[emp_id]  # Return the profile with the given emp_id
    else:
        raise HTTPException(status_code=404, detail="Profile not found")  # Not found error

# PUT endpoint to update a telecom profile
@app.put("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def update_data(emp_id: int, emp: EmployeeTelecomProfile):
    if emp_id not in telecom_data:  # Check if the profile exists
        raise HTTPException(status_code=404, detail="No existing profile")  # Not found error
    if emp_id != emp.employee.emp_id:  # Check if the emp_id in the URL matches the emp_id in the body
        raise HTTPException(status_code=400, detail="Path ID vs Body ID mismatch")  # Bad request error
    telecom_data[emp_id] = emp  # Update the profile with the new data
    return emp  # Return the updated profile

# DELETE endpoint to delete a telecom profile
@app.delete("/telecom/profiles/{emp_id}")
def delete_emp(emp_id: int):
    if emp_id in telecom_data:
        del telecom_data[emp_id]  # Delete the profile from the data store
        return {"detail": "Profile deleted"}  # Success response
    else:
        raise HTTPException(status_code=404, detail="Profile not found")  # Not found error

# GET endpoint to search for telecom profiles based on department or provider
@app.get("/telecom/profiles/search", response_model=List[EmployeeTelecomProfile])
def search_profiles(department: Optional[str] = None, provider: Optional[str] = None):
    results = list(telecom_data.values())  # Start with all profiles
    if department:  # Filter by department if provided
        results = [p for p in results if p.employee.department == department]
    if provider:  # Filter by provider if provided
        results = [p for p in results if p.sim.provider == provider]
    return results  # Return the filtered list of profiles
