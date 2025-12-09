# UST Employee Telecom
# Management
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
# 2. Pydantic Models – Requirements
# You must create the following models. Use BaseModel and Field(...) for constraints.
# Use standard types such as int , str , bool , and Optional[...] .
# 2.1 EmployeeBasic
# Represents the minimal employee information for telecom provisioning.

# Fields
# UST Employee Telecom Management 1
# Field Type Required Rules
# emp_id int Yes
# Employee numeric id; ge=1000 ,
# le=999999
# name str Yes Full name; min_length=2
# official_email str Yes
# Must be a UST email: regex ^[a-zAZ0-9._%+-]+@ust\.com$
# department str No Default "Telecom"
# location str No Default "Bengaluru"
# You may annotate official_email with Field(..., pattern=...) .
# 2.2 SimCard
# Represents a company SIM card issued to the employee.
# Fields
# Field Type Required Rules
# sim_number str Yes
# 10-digit mobile number; regex
# ^\d{10}$
# provider str No Default "Jio"
# is_esim bool No Default False
# activation_year int Yes
# Year of activation; ge=2020 ,
# le=2025
# 2.3 DataPlan
# Represents mobile data plan details.
# Fields
# Field Type Required Rules
# name str Yes min_length=3 , max_length=50
# monthly_gb int Yes
# Data volume in GB; gt=0 ,
# le=1000
# speed_mbps int No Default 50 ; ge=1 , le=1000
# is_roaming_included bool No Default False
# UST Employee Telecom Management 2
# 2.4 VoicePlan
# Represents voice pack details.
# Fields
# Field Type Required Rules
# name str Yes min_length=3
# monthly_minutes int Yes
# Allowed minutes; ge=0 ,
# le=10000
# has_isd bool No Default False
# per_minute_charge_paise int No Default 0 ; ge=0 , le=1000
# 2.5 EmergencyContact
# Represents the emergency contact for telecom-related alerts.
# Fields
# Field Type Required Rules
# name str Yes min_length=2
# relation str No Default "Family"
# phone str Yes
# Indian mobile; regex ^[6-9]\d{9}$ (10
# digits, starting with 6–9)
# 2.6 EmployeeTelecomProfile
# Top-level model used in the API for telecom registration/profile.
# Fields
# Field Type Required
# employee EmployeeBasic Yes
# sim SimCard Yes
# data_plan Optional[DataPlan] No
# voice_plan Optional[VoicePlan] No
# emergency_contact Optional[EmergencyContact] No
# UST Employee Telecom Management 3
# Defaults for data_plan , voice_plan , and emergency_contact should be None .
# 3. FastAPI Service Requirements
# You will build a FastAPI application that manages EmployeeTelecomProfile entries using
# in-memory storage (such as a list).
# Use from fastapi import FastAPI, HTTPException
# No database; use Python lists/dicts in memory.
# Use the Pydantic models defined above for request bodies and responses.
# Assume emp_id is unique per employee. You can treat emp_id as the primary lookup
# key for profiles.
# 4. Endpoints Specification
# Design and implement the following endpoints.

# 4.1 Create telecom profile
# POST /telecom/profiles
# Request body: EmployeeTelecomProfile
# Example JSON:
# {
#  "employee": {
#  "emp_id": 12345,
#  "name": "Asha",
#  "official_email": "asha@ust.com",
#  "department": "Engineering",
#  "location": "Pune"
#  },
#  "sim": {
#  "sim_number": "9876543210",
#  "provider": "Airtel",
#  "is_esim": true,
#  "activation_year": 2023
# UST Employee Telecom Management 4
#  },
#  "data_plan": {
#  "name": "Standard 50GB",
#  "monthly_gb": 50,
#  "speed_mbps": 100,
#  "is_roaming_included": true
#  },
#  "voice_plan": {
#  "name": "Office Calls Pack",
#  "monthly_minutes": 1000,
#  "has_isd": false,
#  "per_minute_charge_paise": 0
#  },
#  "emergency_contact": {
#  "name": "Ravi",
#  "relation": "Friend",
#  "phone": "9876543210"
#  }
# }
# Behavior:
# Validate entire payload via Pydantic.
# If a profile with the same employee.emp_id already exists, return HTTP 409
# (Conflict).
# On success, add profile to in-memory storage and return the created profile.
# Responses:
# 201 Created – body: created EmployeeTelecomProfile
# 400 Bad Request – for invalid data (Pydantic validation errors, automatically
# handled)
# 409 Conflict – if emp_id already exists
# 4.2 Create minimal telecom profile
# UST Employee Telecom Management 5
# (same endpoint as 4.1, different test case)
# Test that the API accepts a profile containing only required fields:
# Example JSON:
# {
#  "employee": {
#  "emp_id": 11111,
#  "name": "Arun",
#  "official_email": "arun@ust.com"
#  },
#  "sim": {
#  "sim_number": "9123456789",
#  "activation_year": 2023
#  }
# }
# Expected behavior:
# department defaults to "Telecom"
# location defaults to "Bengaluru"
# provider defaults to "Jio"
# is_esim defaults to false
# data_plan , voice_plan , emergency_contact are null (or not present depending on
# serialization)
# 4.3 List all profiles
# GET /telecom/profiles
# Behavior:
# Return a list of all saved EmployeeTelecomProfile objects.
# Response:
# 200 OK – JSON array of profiles (possibly empty)
# UST Employee Telecom Management 6
# 4.4 Get profile by employee id
# GET /telecom/profiles/{emp_id}
# Behavior:
# Search in-memory storage for a profile with matching employee.emp_id .
# If found, return it.
# If not found, return HTTP 404.
# Responses:
# 200 OK – EmployeeTelecomProfile
# 404 Not Found – {"detail": "Profile not found"}
# Example:
# GET /telecom/profiles/12345
# Returns: matching profile as JSON.
# 4.5 Update full telecom profile
# PUT /telecom/profiles/{emp_id}
# Request body: EmployeeTelecomProfile
# Behavior:
# If profile for emp_id does not exist → 404.
# If employee.emp_id inside body does not match path {emp_id} → 400 (to enforce
# consistency).
# Replace the stored profile with the new one.
# Responses:
# 200 OK – updated EmployeeTelecomProfile
# 400 Bad Request – path id vs body id mismatch
# 404 Not Found – no existing profile
# 4.6 Delete profile
# DELETE /telecom/profiles/{emp_id}
# UST Employee Telecom Management 7
# Behavior:
# Remove the profile with the matching employee.emp_id from memory.
# Return a confirmation message.
# Responses:
# 200 OK – e.g. {"detail": "Profile deleted"}
# 404 Not Found – if not found, return {"detail": "Profile not found"}
# 4.7 Filter profiles by department and provider

from fastapi import FastAPI, HTTPException  # FastAPI for building the API, HTTPException for handling errors
from pydantic import validator, Field, BaseModel  # Pydantic for data validation and definition of models
from typing import List, Optional  # List for array-like fields and Optional for optional fields


# Define data models using Pydantic
# Model for basic employee information
class EmployeeBasic(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)  # Employee ID must be between 1000 and 999999
    name: str = Field(..., min_length=2)  # Employee name must have at least 2 characters
    official_email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@ust\.com$")  # Email must match the pattern for UST emails
    department: Optional[str] = "Telecom"  # Default department is "Telecom" if not provided
    location: Optional[str] = "Bengaluru"  # Default location is "Bengaluru" if not provided


# Model for SIM card details
class SimCard(BaseModel):
    sim_number: str = Field(..., pattern=r"\d{10}$")  # SIM number must be exactly 10 digits
    provider: Optional[str] = "Jio"  # Default provider is "Jio" if not provided
    is_esim: Optional[bool] = False  # Default is eSIM False if not provided
    activation_year: int = Field(..., ge=2020, le=2025)  # Activation year must be between 2020 and 2025


# Model for data plan details
class DataPlan(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)  # Data plan name must be between 3 and 50 characters
    monthly_gb: int = Field(..., gt=0, le=1000)  # Monthly data must be greater than 0 and less than or equal to 1000
    speed_mbps: Optional[int] = Field(50, ge=1, le=1000)  # Default speed is 50 Mbps, with a range of 1 to 1000 Mbps
    is_roaming_included: Optional[bool] = Field(False)  # Default roaming status is False


# Model for voice plan details
class VoicePlan(BaseModel):
    name: str = Field(..., min_length=3)  # Voice plan name must be at least 3 characters
    monthly_minutes: int = Field(..., ge=0, le=10000)  # Monthly minutes must be between 0 and 10000
    has_isd: Optional[bool] = Field(False)  # Default ISD availability is False
    per_minute_charge_paise: Optional[int] = Field(0, ge=0, le=1000)  # Default per-minute charge is 0, within range 0 to 1000


# Model for emergency contact information
class EmergencyContact(BaseModel):
    name: str = Field(..., min_length=3)  # Emergency contact name must be at least 3 characters
    relation: Optional[str] = "Family"  # Default relation is "Family" if not provided
    phone: str = Field(..., pattern=r"^[6-9]\d{9}$")  # Phone number must match the Indian mobile number format


# Complete employee telecom profile combining all models
class EmployeeTelecomProfile(BaseModel):
    employee: EmployeeBasic = Field(...)  # Embed the EmployeeBasic model
    sim: SimCard = Field(...)  # Embed the SimCard model
    data_plan: Optional[DataPlan] = None  # Data plan is optional, can be None
    voice_plan: Optional[VoicePlan] = None  # Voice plan is optional, can be None
    emergency_contact: Optional[EmergencyContact] = None  # Emergency contact is optional, can be None


# Initialize FastAPI application
app = FastAPI()  # Create a FastAPI instance to define the API

# In-memory storage for profiles
Profiles: List[EmployeeTelecomProfile] = []  # List to store profiles in memory


# CREATE: Add a new telecom profile
@app.post("/telecom/profiles")
def create_telecom_profile(profile: EmployeeTelecomProfile):
    # Check if employee ID already exists in the profiles list
    for existing_profile in Profiles:
        if existing_profile.employee.emp_id == profile.employee.emp_id:
            raise HTTPException(status_code=409, detail="Employee id already exists")  # Conflict if emp_id already exists
    Profiles.append(profile)  # Add new profile to the list
    return profile  # Return the created profile


# READ: Get all profiles
@app.get("/telecom/profiles")
def get_all_profiles():
    return Profiles  # Return the list of all profiles


# SEARCH: Filter profiles by department and/or provider
@app.get("/telecom/profiles/search")
def get_profile_params(department: str = "", provider: str = ""):
    # If no filters provided, return all profiles
    if department == "" and provider == "":
        return Profiles
    
    # If both department and provider filters provided
    if department != "" and provider != "":
        newdepartmentlist = []
        for profile in Profiles:
            if profile.employee.department == department:
                newdepartmentlist.append(profile)
        return newdepartmentlist
    
    # If only provider filter provided
    elif department == "" and provider != "":
        newproviderlist = []
        for profile in Profiles:
            if profile.sim.provider == provider:
                newproviderlist.append(profile)
        return newproviderlist
    
    # If only department filter provided
    else:
        newcombined = []
        for profile in Profiles:
            if profile.employee.department == department and profile.sim.provider == provider:
                newcombined.append(profile)
        return newcombined


# READ: Get specific profile by employee ID
@app.get("/telecom/profiles/{emp_id}")
def get_profile(emp_id: int):
    for profile in Profiles:
        if profile.employee.emp_id == emp_id:
            return profile  # Return the profile if emp_id matches
    raise HTTPException(status_code=404, detail="Profile not found")  # 404 if no profile is found


# UPDATE: Modify an existing profile
@app.put("/telecom/profiles/{emp_id}")
def update_profile(emp_id: int, updated_profile: EmployeeTelecomProfile):
    for i, profile in enumerate(Profiles):
        if profile.employee.emp_id == emp_id:
            Profiles[i] = updated_profile  # Replace the existing profile with the updated profile
            return updated_profile  # Return the updated profile
    raise HTTPException(status_code=404, detail="Employee id does not exist")  # 404 if profile does not exist


# DELETE: Remove a profile by employee ID
@app.delete("/telecom/profiles/{emp_id}")
def delete_profile(emp_id: int):
    for i, profile in enumerate(Profiles):
        if profile.employee.emp_id == emp_id:
            Profiles.pop(i)  # Remove the profile from the list
            return {"detail": "Profile deleted"}  # Return confirmation of deletion
    return {"detail": "Profile Not Found"}  # Return if profile was not found


#outputs

# 1. POST /telecom/profiles - Create Telecom Profile
# request body:
#     {
#   "employee": {
#     "emp_id": 12345,
#     "name": "Asha",
#     "official_email": "asha@ust.com",
#     "department": "Engineering",
#     "location": "Pune"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "provider": "Airtel",
#     "is_esim": true,
#     "activation_year": 2023
#   },
#   "data_plan": {
#     "name": "Standard 50GB",
#     "monthly_gb": 50,
#     "speed_mbps": 100,
#     "is_roaming_included": true
#   },
#   "voice_plan": {
#     "name": "Office Calls Pack",
#     "monthly_minutes": 1000,
#     "has_isd": false,
#     "per_minute_charge_paise": 0
#   },
#   "emergency_contact": {
#     "name": "Ravi",
#     "relation": "Friend",
#     "phone": "9876543210"
#   }
# }
# output:
#     {
#   "employee": {
#     "emp_id": 12345,
#     "name": "Asha",
#     "official_email": "asha@ust.com",
#     "department": "Engineering",
#     "location": "Pune"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "provider": "Airtel",
#     "is_esim": true,
#     "activation_year": 2023
#   },
#   "data_plan": {
#     "name": "Standard 50GB",
#     "monthly_gb": 50,
#     "speed_mbps": 100,
#     "is_roaming_included": true
#   },
#   "voice_plan": {
#     "name": "Office Calls Pack",
#     "monthly_minutes": 1000,
#     "has_isd": false,
#     "per_minute_charge_paise": 0
#   },
#   "emergency_contact": {
#     "name": "Ravi",
#     "relation": "Friend",
#     "phone": "9876543210"
#   }
# }

# 2. POST /telecom/profiles - Create Minimal Telecom Profile (Only Required Fields)
# request body:
#     {
#   "employee": {
#     "emp_id": 11111,
#     "name": "Arun",
#     "official_email": "arun@ust.com"
#   },
#   "sim": {
#     "sim_number": "9123456789",
#     "activation_year": 2023
#   }
# }
# output:
#     {
#   "employee": {
#     "emp_id": 11111,
#     "name": "Arun",
#     "official_email": "arun@ust.com",
#     "department": "Telecom",
#     "location": "Bengaluru"
#   },
#   "sim": {
#     "sim_number": "9123456789",
#     "provider": "Jio",
#     "is_esim": false,
#     "activation_year": 2023
#   },
#   "data_plan": null,
#   "voice_plan": null,
#   "emergency_contact": null
# }

# 3. GET /telecom/profiles - Get All Profiles
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
#   },
#   {
#     "employee": {
#       "emp_id": 11111,
#       "name": "Arun",
#       "official_email": "arun@ust.com",
#       "department": "Telecom",
#       "location": "Bengaluru"
#     },
#     "sim": {
#       "sim_number": "9123456789",
#       "provider": "Jio",
#       "is_esim": false,
#       "activation_year": 2023
#     },
#     "data_plan": null,
#     "voice_plan": null,
#     "emergency_contact": null
#   }
# ]

# 4. GET /telecom/profiles/{emp_id} - Get Profile by Employee ID
# Example Request: GET /telecom/profiles/12345
# output:
#     {
#   "employee": {
#     "emp_id": 12345,
#     "name": "Asha",
#     "official_email": "asha@ust.com",
#     "department": "Engineering",
#     "location": "Pune"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "provider": "Airtel",
#     "is_esim": true,
#     "activation_year": 2023
#   },
#   "data_plan": {
#     "name": "Standard 50GB",
#     "monthly_gb": 50,
#     "speed_mbps": 100,
#     "is_roaming_included": true
#   },
#   "voice_plan": {
#     "name": "Office Calls Pack",
#     "monthly_minutes": 1000,
#     "has_isd": false,
#     "per_minute_charge_paise": 0
#   },
#   "emergency_contact": {
#     "name": "Ravi",
#     "relation": "Friend",
#     "phone": "9876543210"
#   }
# }


# 5. PUT /telecom/profiles/{emp_id} - Update Full Telecom Pr

# Request body:
#     {
#   "employee": {
#     "emp_id": 12345,
#     "name": "Asha",
#     "official_email": "asha_updated@ust.com",
#     "department": "Engineering",
#     "location": "Pune"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "provider": "Airtel",
#     "is_esim": true,
#     "activation_year": 2023
#   },
#   "data_plan": {
#     "name": "Premium Plan",
#     "monthly_gb": 100,
#     "speed_mbps": 200,
#     "is_roaming_included": true
#   },
#   "voice_plan": {
#     "name": "Office Calls Pack",
#     "monthly_minutes": 1000,
#     "has_isd": false,
#     "per_minute_charge_paise": 0
#   },
#   "emergency_contact": {
#     "name": "Ravi",
#     "relation": "Friend",
#     "phone": "9876543210"
#   }
# }

# output:
#     {
#   "employee": {
#     "emp_id": 12345,
#     "name": "Asha",
#     "official_email": "asha_updated@ust.com",
#     "department": "Engineering",
#     "location": "Pune"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "provider": "Airtel",
#     "is_esim": true,
#     "activation_year": 2023
#   },
#   "data_plan": {
#     "name": "Premium Plan",
#     "monthly_gb": 100,
#     "speed_mbps": 200,
#     "is_roaming_included": true
#   },
#   "voice_plan": {
#     "name": "Office Calls Pack",
#     "monthly_minutes": 1000,
#     "has_isd": false,
#     "per_minute_charge_paise": 0
#   },
#   "emergency_contact": {
#     "name": "Ravi",
#     "relation": "Friend",
#     "phone": "9876543210"
#   }
# }

# 6. DELETE /telecom/profiles/{emp_id} - Delete Profile
# Request: DELETE /telecom/profiles/12345
# #output:
# {
#   "detail": "Profile deleted"
# }
# error:
# {
#   "detail": "Profile Not Found"
# }


# 7. GET /telecom/profiles/search - Search Profiles by Department and Provider
#  Request: GET /telecom/profiles/search?department=Engineering&provider=Airtel
# output:
#     [
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
