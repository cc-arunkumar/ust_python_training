# UST Employee Telecom Management

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
# 2.2 SimCard
# Represents a company SIM card issued to the employee.
# 2.3 DataPlan
# Represents mobile data plan details.
# 2.4 VoicePlan
# Represents voice pack details.
# 2.5 EmergencyContact
# Represents the emergency contact for telecom-related alerts.
# 2.6 EmployeeTelecomProfile
# Top-level model used in the API for telecom registration/profile.
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
# Test that the API accepts a profile containing only required fields
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
# 7 Behavior:
# Remove the profile with the matching employee.emp_id from memory.
# Return a confirmation message.
# Responses:
# 200 OK – e.g. {"detail": "Profile deleted"}
# 404 Not Found – if not found, return {"detail": "Profile not found"}
# 4.7 Filter profiles by department and provider
# GET /telecom/profiles/search
# Query parameters:
# department – optional string
# provider – optional string
# Behavior:
# If no filters provided: return all profiles.
# If department provided: only profiles where employee.department matches exactly.
# If provider provided: only profiles where sim.provider matches exactly.
# If both provided: apply both filters.
# Response:
# 200 OK – list of EmployeeTelecomProfile objects matching filters.
# Example:
# GET /telecom/profiles/search?department=Engineering&provider=Airtel
# 5. Validation Scenarios to Test
# The following requests should produce validation errors (HTTP 422 from
# FastAPI/Pydantic):
# 1. emp_id < 1000 or > 999999
# 2. name length < 2
# UST Employee Telecom Management 8
# 3. official_email not ending with @ust.com
# 4. sim_number not 10 digits
# 5. activation_year < 2020 or > 2025
# 6. monthly_gb ≤ 0 or > 1000
# 7. monthly_minutes negative
# 8. per_minute_charge_paise negative or > 1000
# 9. phone in EmergencyContact not matching pattern ^[6-9]\d{9}$
# In each case, participants should inspect the error response in FastAPI docs
# ( /docs ) and confirm that Pydantic correctly identifies the failing field(s).
# 6. Participant Deliverables
# 1. All Pydantic model definitions:
# EmployeeBasic
# SimCard
# DataPlan
# VoicePlan
# EmergencyContact
# EmployeeTelecomProfile
# 2. FastAPI application with the endpoints:
# POST /telecom/profiles
# GET /telecom/profiles
# GET /telecom/profiles/{emp_id}
# PUT /telecom/profiles/{emp_id}
# DELETE /telecom/profiles/{emp_id}
# GET /telecom/profiles/search
# 3. Screenshots or logs showing:
# 9 Successful profile creation (full and minimal)
# Profile retrieval by emp_id
# Update and delete operations
# Validation errors for the specified invalid scenarios



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional

# -------------------------------
# Define Pydantic Data Models
# -------------------------------

# EmployeeBasic Model - Contains basic employee details
class EmployeeBasic(BaseModel):
    emp_id: int
    name: str
    official_email: str
    department: Optional[str] = "Telecom"   # Default department
    location: Optional[str] = "Bengaluru"   # Default location

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
    provider: Optional[str] = "Jio"         # Default provider
    is_esim: Optional[bool] = False         # Default: physical SIM
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
    speed_mbps: Optional[int] = 50          # Default speed
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
    relation: Optional[str] = "Family"      # Default relation
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


# -------------------------------
# Initialize FastAPI Application
# -------------------------------
app = FastAPI(title="Employee Telecom Profiles API")

# In-memory storage for employee telecom profiles
Profiles: List[EmployeeTelecomProfile] = []


# -------------------------------
# CRUD Endpoints
# -------------------------------

# CREATE: Add a new telecom profile for an employee
@app.post("/telecom/profiles")
def create_telecom_profile(profile: EmployeeTelecomProfile):
    """
    Create a new telecom profile.
    - Ensures employee ID is unique.
    - Adds profile to in-memory list.
    """
    for existing_profile in Profiles:
        if existing_profile.employee.emp_id == profile.employee.emp_id:
            raise HTTPException(status_code=409, detail="Employee id already exists")
    Profiles.append(profile)
    return profile  


# READ: Retrieve all telecom profiles
@app.get("/telecom/profiles")
def get_all_profiles():
    """
    Get all telecom profiles.
    Returns the full list of stored profiles.
    """
    return Profiles


# SEARCH: Filter profiles by department and/or provider
@app.get("/telecom/profiles/search")
def get_profile_params(department: str = "", provider: str = ""):
    """
    Search profiles by department and/or provider.
    - If no filters provided, returns all profiles.
    - If only provider given, filters by provider.
    - If only department given, filters by department.
    - If both provided, filters accordingly.
    """
    if department == "" and provider == "":
        return Profiles
    if department != "" and provider != "":
        filtered_by_department = [profile for profile in Profiles if profile.employee.department == department]
        return filtered_by_department
    elif department == "" and provider != "":
        filtered_by_provider = [profile for profile in Profiles if profile.sim.provider == provider]
        return filtered_by_provider
    else:
        filtered_by_combined = [profile for profile in Profiles if profile.employee.department == department and profile.sim.provider == provider]
        return filtered_by_combined


# READ: Get a specific profile by employee ID
@app.get("/telecom/profiles/{emp_id}")
def get_profile(emp_id: int):
    """
    Retrieve a profile by employee ID.
    Raises 404 if not found.
    """
    for profile in Profiles:
        if profile.employee.emp_id == emp_id:
            return profile
    raise HTTPException(status_code=404, detail="Profile not found")


# UPDATE: Modify an existing profile by employee ID
@app.put("/telecom/profiles/{emp_id}")
def update_profile(emp_id: int, updated_profile: EmployeeTelecomProfile):
    """
    Update an existing profile by employee ID.
    - Replaces old profile with new one.
    - Raises 404 if employee ID does not exist.
    """
    for idx, profile in enumerate(Profiles):
        if profile.employee.emp_id == emp_id:
            Profiles[idx] = updated_profile
            return updated_profile
    raise HTTPException(status_code=404, detail="Employee id does not exist")


# DELETE: Remove a profile by employee ID
@app.delete("/telecom/profiles/{emp_id}")
def delete_profile(emp_id: int):
    """
    Delete a profile by employee ID.
    - Removes profile from list.
    - Returns confirmation message.
    """
    for idx, profile in enumerate(Profiles):
        if profile.employee.emp_id == emp_id:
            Profiles.pop(idx)
            return {"detail": "Profile deleted"}
    return {"detail": "Profile Not Found"}


# Sample Requests and Expected Outputs
# 1. Create a new profile
# Request:
# POST /telecom/profiles
# Body:
# {
#   "employee": {
#     "emp_id": 1234,
#     "name": "Rahul Sharma",
#     "official_email": "rahul.sharma@ust.com",
#     "department": "Telecom",
#     "location": "Bengaluru"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "provider": "Jio",
#     "is_esim": false,
#     "activation_year": 2023
#   },
#   "data_plan": {
#     "name": "Work Unlimited",
#     "monthly_gb": 200,
#     "speed_mbps": 100,
#     "is_roaming_included": true
#   },
#   "voice_plan": {
#     "name": "Corporate Voice",
#     "monthly_minutes": 500,
#     "has_isd": true,
#     "per_minute_charge_paise": 50
#   },
#   "emergency_contact": {
#     "name": "Anita Sharma",
#     "relation": "Family",
#     "phone": "9876543211"
#   }
# }
# Response:
# {
#   "employee": {
#     "emp_id": 1234,
#     "name": "Rahul Sharma",
#     "official_email": "rahul.sharma@ust.com",
#     "department": "Telecom",
#     "location": "Bengaluru"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "provider": "Jio",
#     "is_esim": false,
#     "activation_year": 2023
#   },
#   "data_plan": {
#     "name": "Work Unlimited",
#     "monthly_gb": 200,
#     "speed_mbps": 100,
#     "is_roaming_included": true
#   },
#   "voice_plan": {
#     "name": "Corporate Voice",
#     "monthly_minutes": 500,
#     "has_isd": true,
#     "per_minute_charge_paise": 50
#   },
#   "emergency_contact": {
#     "name": "Anita Sharma",
#     "relation": "Family",
#     "phone": "9876543211"
#   }
# }
# 2. Get all profiles
# Request:
# GET /telecom/profiles
# Response:
# [
#   {
#     "employee": {
#       "emp_id": 1234,
#       "name": "Rahul Sharma",
#       "official_email": "rahul.sharma@ust.com",
#       "department": "Telecom",
#       "location": "Bengaluru"
#     },
#     "sim": {
#       "sim_number": "9876543210",
#       "provider": "Jio",
#       "is_esim": false,
#       "activation_year": 2023
#     },
#     "data_plan": {
#       "name": "Work Unlimited",
#       "monthly_gb": 200,
#       "speed_mbps": 100,
#       "is_roaming_included": true
#     },
#     "voice_plan": {
#       "name": "Corporate Voice",
#       "monthly_minutes": 500,
#       "has_isd": true,
#       "per_minute_charge_paise": 50
#     },
#     "emergency_contact": {
#       "name": "Anita Sharma",
#       "relation": "Family",
#       "phone": "9876543211"
#     }
#   }
# ]
# 3. Search profiles by provider
# Request:
# GET /telecom/profiles/search?provider=Jio
# Response:
# [
#   {
#     "employee": {
#       "emp_id": 1234,
#       "name": "Rahul Sharma",
#       "official_email": "rahul.sharma@ust.com",
#       "department": "Telecom",
#       "location": "Bengaluru"
#     },
#     "sim": {
#       "sim_number": "9876543210",
#       "provider": "Jio",
#       "is_esim": false,
#       "activation_year": 2023
#     },
#     "data_plan": {
#       "name": "Work Unlimited",
#       "monthly_gb": 200,
#       "speed_mbps": 100,
#       "is_roaming_included": true
#     },
#     "voice_plan": {
#       "name": "Corporate Voice",
#       "monthly_minutes": 500,
#       "has_isd": true,
#       "per_minute_charge_paise": 50
#     },
#     "emergency_contact": {
#       "name": "Anita Sharma",
#       "relation": "Family",
#       "phone": "9876543211"
#     }
#   }
# ]
# 4. Get profile by employee ID
# Request:
# GET /telecom/profiles/1234
# Response:
# {
#   "employee": {
#     "emp_id": 1234,
#     "name": "Rahul Sharma",
#     "official_email": "rahul.sharma@ust.com",
#     "department": "Telecom",
#     "location": "Bengaluru"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "provider": "Jio",
#     "is_esim": false,
#     "activation_year": 2023
#   },
#   "data_plan": {
#     "name": "Work Unlimited",
#     "monthly_gb": 200,
#     "speed_mbps": 100,
#     "is_roaming_included": true
#   },
#   "voice_plan": {
#     "name": "Corporate Voice",
#     "monthly_minutes": 500,
#     "has_isd": true,
#     "per_minute_charge_paise": 50
#   },
#   "emergency_contact": {
#     "name": "Anita Sharma",
#     "relation": "Family",
#     "phone": "9876543211"
#   }
# }
# 5. Update profile
# Request:
# PUT /telecom/profiles/1234
# Body:
# {
#   "employee": {
#     "emp_id": 1234,
#     "name": "Rahul Sharma",
#     "official_email": "rahul.sharma@ust.com",
#     "department": "IT",
#     "location": "Chennai"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "provider": "Airtel",
#     "is_esim": true,
#     "activation_year": 2024
#   }
# }
# Response:
# {
#   "employee": {
#     "emp_id": 1234,
#     "name": "Rahul Sharma",
#     "official_email": "rahul.sharma@ust.com",
#     "department": "IT",
#     "location": "Chennai"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "provider": "Airtel",
#     "is_esim": true,
#     "activation_year": 2024
#   }
# }
# 6. Delete profile
# Request:
# DELETE /telecom/profiles/1234
# Response:
# {"detail": "Profile deleted"}