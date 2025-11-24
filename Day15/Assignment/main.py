
# UST Employee Telecom 
# Management 
# API Specification and Validation Assignment
#  1. Context
#  UST manages telecom services for its employees. For each employee, the system 
# must store:
#  Employee identity and contact information
#  Company SIM details
#  Optional data and voice plan information
#  Optional emergency contact information
#  You are required to design:
#   Pydantic models that validate the structure and constraints of this data.
#   FastAPI endpoints that use these models for request parsing and validation, 
# with in-memory storage (lists) only.
#  The focus is on correct modelling, validation behaviour, and clear API contracts.
#  No database or authentication is required.

from pydantic import BaseModel
from typing import List, Optional
from fastapi import FastAPI, HTTPException

app = FastAPI(title="UST Employee Telecom Management")

# Employee details
class EmployeeBasic(BaseModel):
    emp_id: int
    name: str
    official_email: str
    department: str = "Telecom"
    location: str = "Bengaluru"

# SIM details
class SimCard(BaseModel):
    sim_number: str
    provider: str = "Jio"
    is_esim: bool = False
    activation_year: int

# Data plan details
class DataPlan(BaseModel):
    name: str
    monthly_gb: int
    speed_mbps: int = 50
    is_roaming_included: bool = False

# Voice plan details
class VoicePlan(BaseModel):
    name: str
    monthly_minutes: int
    has_isd: bool = False
    per_minute_charge_paise: int = 0

# Emergency contact details
class EmergencyContact(BaseModel):
    name: str
    relation: str = "Family"
    phone: str

# Complete telecom profile
class EmployeeTelecomProfile(BaseModel):
    employee: EmployeeBasic
    sim: SimCard
    data_plan: Optional[DataPlan] = None
    voice_plan: Optional[VoicePlan] = None
    emergency_contact: Optional[EmergencyContact] = None

# In-memory list with initial data
telecomprofile: List[dict] = [
    {
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
]

# Create new profile
@app.post("/telecom/profiles", response_model=EmployeeTelecomProfile)
def add_telecom_profile(teleprofile: EmployeeTelecomProfile):
    for pf in telecomprofile:
        if pf['employee']['emp_id'] == teleprofile.employee.emp_id:
            raise HTTPException(status_code=409, detail="Employee id already exists")
    telecomprofile.append(teleprofile.dict())
    return teleprofile

# Get all profiles
@app.get("/telecom/profiles", response_model=List[EmployeeTelecomProfile])
def get_all():
    return telecomprofile

# Get profile by ID
@app.get("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def get_by_id(emp_id: int):
    for pf in telecomprofile:
        if pf['employee']['emp_id'] == emp_id:
            return pf
    raise HTTPException(status_code=404, detail="Profile not found")

# Update profile by ID
@app.put("/telecom/profile/{emp_id}", response_model=EmployeeTelecomProfile)
def update(emp_id: int, profile: EmployeeTelecomProfile):
    existing = None
    for pf in telecomprofile:
        if pf['employee']['emp_id'] == emp_id:
            existing = pf
            break
    if existing is None:
        raise HTTPException(status_code=404, detail="No existing profile")
    if emp_id != profile.employee.emp_id:
        raise HTTPException(status_code=400, detail="Path ID and Body ID do not match")
    telecomprofile.remove(existing)
    telecomprofile.append(profile.dict())
    return profile

# Delete profile by ID
@app.delete("/telecom/profiles/{emp_id}")
def delete_prof(emp_id: int):
    for pf in telecomprofile:
        if pf['employee']['emp_id'] == emp_id:
            telecomprofile.remove(pf)
            return {"Profile deleted successfully"}
    raise HTTPException(status_code=404, detail="Profile not found")

# Search profiles by department or provider
@app.get("/telecom/profiles/search", response_model=List[EmployeeTelecomProfile])
async def search_profiles(department: Optional[str] = None, provider: Optional[str] = None):
    filtered_profiles = telecomprofile
    if department:
        filtered_profiles = [pf for pf in filtered_profiles if pf['employee']['department'] == department]
    if provider:
        filtered_profiles = [pf for pf in filtered_profiles if pf['sim']['provider'] == provider]
    if not filtered_profiles:
        raise HTTPException(status_code=404, detail="No profiles found matching the criteria")
    return filtered_profiles

# sample output:
   
# get

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

#post

#  "employee": {
#     "emp_id": 1000,
#     "name": "strerer",
#     "official_email": "KXmx7N1lHZ366+5qGXQ8KJT29%7QI0dRpYQQbFH6sh@ust.com",
#     "department": "Telecom",
#     "location": "Bengaluru"
#   },
#   "sim": {
#     "sim_number": "2488784370",
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
#     "monthly_minutes": 100,
#     "has_isd": false,
#     "per_minute_charge_paise": 0
#   },
#   "emergency_contact": {
#     "name": "madhan",
#     "relation": "Family",
#     "phone": "567433243"
#   }
# }


#get
# #emp_id = 12345
# {
#   "employee": {
#     "emp_id": 12345,
#     "name": "Asha",
#     "official_email": "asha@ust.com",
#     "department": "Engineering",
#     "location": "Pune"
#   }

#put
#sim number changed to 7
#   "employee": {
#     "emp_id": 1000,
#     "name": "string",
#     "official_email": "+jiUCADVL67RqnC+YXvAN.zg.9+6Qlihe69-m2Omb9K-UblL3Xp@ust.com",
#     "department": "Telecom",
#     "location": "Bengaluru"
#   },
#   "sim": {
#     "sim_number": "7",
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
#     "phone": "9259870486"
#   }
# }

#delete
#   {
#     "employee": {
#       "emp_id": 1000,
#       "name": "string",
#       "official_email": "V01JPE5svDVOLLXr7PZjZkeBFoz76i9k5%_cahUiYdEbNmWQqEpgAYlfWQvMNqJM1vTl9fqhQG-1Ch.jt0p@ust.com",
#       "department": "Telecom",
#       "location": "Bengaluru"
#     },
#     "sim": {
#       "sim_number": "0297124986",
#       "provider": "Jio",
#       "is_esim": false,
#       "activation_year": 2020
#     },
#     "data_plan": {
#       "name": "string",
#       "monthly_gb": 1,
#       "speed_mbps": 50,
#       "is_roaming_included": false
#     },
#     "voice_plan": {
#       "name": "string",
#       "monthly_minutes": 10000,
#       "has_isd": false,
#       "per_minute_charge_paise": 0
#     },
#     "emergency_contact": {
#       "name": "string",
#       "relation": "Family",
#       "phone": "6616340170"
#     }
#   }
# ]
