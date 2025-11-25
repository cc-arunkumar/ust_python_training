# Import typing helpers for optional values and lists
from typing import Optional, List

# Import Pydantic BaseModel and Field for data validation
from pydantic import BaseModel, Field

# Import FastAPI framework and HTTPException for error handling
from fastapi import FastAPI, HTTPException

# Import regex module for pattern matching
import re

# Initialize FastAPI application with a title
app = FastAPI(title="UST Employee Telecom Management")

# -----------------------------
# Regex helpers for validation
# -----------------------------

# Regex to validate UST official email format
UST_EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@ust\.com$")

# Regex to validate any 10-digit mobile number
MOBILE_10_DIGIT_REGEX = re.compile(r"^\d{10}$")

# Regex to validate Indian mobile numbers (must start with 6–9)
INDIAN_MOBILE_REGEX = re.compile(r"^[6-9]\d{9}$")


# -----------------------------
# Pydantic Models (Data Schemas)
# -----------------------------

# Define basic employee details with validation rules
class EmployeeBasic(BaseModel):
    # Employee ID must be between 1000 and 999999
    emp_id: int = Field(..., ge=1000, le=999999)
    # Name must have at least 2 characters
    name: str = Field(..., min_length=2)
    # Must match UST email format
    official_email: str = Field(..., pattern=UST_EMAIL_REGEX.pattern)
    # Default department is Telecom
    department: str = "Telecom"
    # Default location is Bengaluru
    location: str = "Bengaluru"


# Define SIM card details associated with employee
class SimCard(BaseModel):
    # Must be a 10-digit number
    sim_number: str = Field(..., pattern=MOBILE_10_DIGIT_REGEX.pattern)
    # Default provider is Jio
    provider: str = "Jio"
    # Flag to indicate if SIM is eSIM
    is_esim: bool = False
    # Activation year must be between 2020–2025
    activation_year: int = Field(..., ge=2020, le=2025)


# Define data plan details for employee SIM
class DataPlan(BaseModel):
    # Plan name must be 3–50 characters
    name: str = Field(..., min_length=3, max_length=50)
    # Monthly data must be >0 and ≤1000 GB
    monthly_gb: int = Field(..., gt=0, le=1000)
    # Default speed is 50 Mbps, must be between 1–1000
    speed_mbps: int = Field(50, ge=1, le=1000)
    # Flag to indicate roaming inclusion
    is_roaming_included: bool = False


# Define voice plan details for employee SIM
class VoicePlan(BaseModel):
    # Plan name must have at least 3 characters
    name: str = Field(..., min_length=3)
    # Monthly minutes must be between 0–10000
    monthly_minutes: int = Field(..., ge=0, le=10000)
    # Flag to indicate ISD facility
    has_isd: bool = False
    # Per-minute charge in paise (0–1000)
    per_minute_charge_paise: int = Field(0, ge=0, le=1000)


# Define emergency contact details for employee
class EmergencyContact(BaseModel):
    # Contact name must have at least 2 characters
    name: str = Field(..., min_length=2)
    # Default relation is Family
    relation: str = "Family"
    # Must be a valid Indian mobile number
    phone: str = Field(..., pattern=INDIAN_MOBILE_REGEX.pattern)


# Define complete telecom profile for an employee
class EmployeeTelecomProfile(BaseModel):
    employee: EmployeeBasic
    sim: SimCard
    data_plan: Optional[DataPlan] = None
    voice_plan: Optional[VoicePlan] = None
    emergency_contact: Optional[EmergencyContact] = None


# -----------------------------
# In-memory storage (temporary DB substitute)
# -----------------------------

# List to store employee profiles in memory
profiles: List[EmployeeTelecomProfile] = []


# -----------------------------
# Utility function (basic loop)
# -----------------------------

# Return index of employee profile by emp_id, or -1 if not found
def find_profile_index_by_emp_id(emp_id: int) -> int:
    # Loop through all profiles by index
    for i in range(len(profiles)):
        # Check if current profile's emp_id matches
        if profiles[i].employee.emp_id == emp_id:
            # Return index if match found
            return i
    # Return -1 if no match found
    return -1


# -----------------------------
# API Endpoints
# -----------------------------

# Create a new employee telecom profile
@app.post("/telecom/profiles", response_model=EmployeeTelecomProfile, status_code=201)
def create_profile(profile: EmployeeTelecomProfile):
    # Check if profile already exists
    id = find_profile_index_by_emp_id(profile.employee.emp_id)
    # If found, raise conflict error
    if id != -1:
        raise HTTPException(status_code=409, detail="Profile already exists")
    # Add new profile to list
    profiles.append(profile)
    # Return created profile
    return profile


# List all employee telecom profiles
@app.get("/telecom/profiles", response_model=List[EmployeeTelecomProfile])
def list_profiles():
    # Return all profiles
    return profiles


# Retrieve a specific employee telecom profile by emp_id
@app.get("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def get_profile(emp_id: int):
    # Find profile index
    id = find_profile_index_by_emp_id(emp_id)
    # If not found, raise 404 error
    if id == -1:
        raise HTTPException(status_code=404, detail="Profile not found")
    # Return matching profile
    return profiles[id]


# Update an existing employee telecom profile
@app.put("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def update_profile(emp_id: int, profile: EmployeeTelecomProfile):
    # Ensure path emp_id matches body emp_id
    if profile.employee.emp_id != emp_id:
        raise HTTPException(status_code=400, detail="Path emp_id and body emp_id must match")

    # Find profile index
    id = find_profile_index_by_emp_id(emp_id)
    # If not found, raise 404 error
    if id == -1:
        raise HTTPException(status_code=404, detail="Profile not found")

    # Replace old profile with new one
    profiles[id] = profile
    # Return updated profile
    return profile


# Delete an employee telecom profile by emp_id
@app.delete("/telecom/profiles/{emp_id}")
def delete_profile(emp_id: int):
    # Find profile index
    id = find_profile_index_by_emp_id(emp_id)
    # If not found, raise 404 error
    if id == -1:
        raise HTTPException(status_code=404, detail="Profile not found")
    # Remove profile from list
    profiles.pop(id)
    # Return success message
    return {"detail": "Profile deleted"}


# Search employee telecom profiles by department and/or provider
@app.get("/telecom/profiles/search", response_model=List[EmployeeTelecomProfile])
def search_profiles(department: Optional[str] = None, provider: Optional[str] = None):
    # Start with all profiles
    result = profiles
    # If department filter provided
    if department:
        result = [p for p in result if p.employee.department == department]
    # If provider filter provided
    if provider:
        result = [p for p in result if p.sim.provider == provider]
    # Return filtered list
    return result

# Output
# {
#   "create_profile": {
#     "request": {
#       "employee": {
#         "emp_id": 1001,
#         "name": "Ravi Kumar",
#         "official_email": "ravi.kumar@ust.com",
#         "department": "Telecom",
#         "location": "Bengaluru"
#       },
#       "sim": {
#         "sim_number": "9876543210",
#         "provider": "Jio",
#         "is_esim": false,
#         "activation_year": 2023
#       },
#       "data_plan": {
#         "name": "Work Plan",
#         "monthly_gb": 50,
#         "speed_mbps": 100,
#         "is_roaming_included": true
#       },
#       "voice_plan": {
#         "name": "Voice Basic",
#         "monthly_minutes": 500,
#         "has_isd": false,
#         "per_minute_charge_paise": 10
#       },
#       "emergency_contact": {
#         "name": "Anita Kumar",
#         "relation": "Family",
#         "phone": "9123456789"
#       }
#     },
#     "response": {
#       "employee": {
#         "emp_id": 1001,
#         "name": "Ravi Kumar",
#         "official_email": "ravi.kumar@ust.com",
#         "department": "Telecom",
#         "location": "Bengaluru"
#       },
#       "sim": {
#         "sim_number": "9876543210",
#         "provider": "Jio",
#         "is_esim": false,
#         "activation_year": 2023
#       },
#       "data_plan": {
#         "name": "Work Plan",
#         "monthly_gb": 50,
#         "speed_mbps": 100,
#         "is_roaming_included": true
#       },
#       "voice_plan": {
#         "name": "Voice Basic",
#         "monthly_minutes": 500,
#         "has_isd": false,
#         "per_minute_charge_paise": 10
#       },
#       "emergency_contact": {
#         "name": "Anita Kumar",
#         "relation": "Family",
#         "phone": "9123456789"
#       }
#     }
#   },

#   "list_profiles": {
#     "response": [
#       {
#         "employee": {
#           "emp_id": 1001,
#           "name": "Ravi Kumar",
#           "official_email": "ravi.kumar@ust.com",
#           "department": "Telecom",
#           "location": "Bengaluru"
#         },
#         "sim": {
#           "sim_number": "9876543210",
#           "provider": "Jio",
#           "is_esim": false,
#           "activation_year": 2023
#         },
#         "data_plan": {
#           "name": "Work Plan",
#           "monthly_gb": 50,
#           "speed_mbps": 100,
#           "is_roaming_included": true
#         },
#         "voice_plan": {
#           "name": "Voice Basic",
#           "monthly_minutes": 500,
#           "has_isd": false,
#           "per_minute_charge_paise": 10
#         },
#         "emergency_contact": {
#           "name": "Anita Kumar",
#           "relation": "Family",
#           "phone": "9123456789"
#         }
#       }
#     ]
#   },

#   "get_profile_by_id": {
#     "response_success": {
#       "employee": {
#         "emp_id": 1001,
#         "name": "Ravi Kumar",
#         "official_email": "ravi.kumar@ust.com",
#         "department": "Telecom",
#         "location": "Bengaluru"
#       },
#       "sim": {
#         "sim_number": "9876543210",
#         "provider": "Jio",
#         "is_esim": false,
#         "activation_year": 2023
#       }
#     },
#     "response_error": {
#       "detail": "Profile not found"
#     }
#   },

#   "update_profile": {
#     "request": {
#       "employee": {
#         "emp_id": 1001,
#         "name": "Ravi Kumar",
#         "official_email": "ravi.kumar@ust.com",
#         "department": "Telecom",
#         "location": "Bengaluru"
#       },
#       "sim": {
#         "sim_number": "9876543210",
#         "provider": "Airtel",
#         "is_esim": true,
#         "activation_year": 2024
#       }
#     },
#     "response": {
#       "employee": {
#         "emp_id": 1001,
#         "name": "Ravi Kumar",
#         "official_email": "ravi.kumar@ust.com",
#         "department": "Telecom",
#         "location": "Bengaluru"
#       },
#       "sim": {
#         "sim_number": "9876543210",
#         "provider": "Airtel",
#         "is_esim": true,
#         "activation_year": 2024
#       }
#     },
#     "response_error": {
#       "detail": "Profile not found"
#     }
#   },

#   "delete_profile": {
#     "response_success": {
#       "detail": "Profile deleted"
#     },
#     "response_error": {
#       "detail": "Profile not found"
#     }
#   },

#   "search_profiles": {
#     "query": {
#       "department": "Telecom",
#       "provider": "Jio"
#     },
#     "response": [
#       {
#         "employee": {
#           "emp_id": 1001,
#           "name": "Ravi Kumar",
#           "official_email": "ravi.kumar@ust.com",
#           "department": "Telecom",
#           "location": "Bengaluru"
#         },
#         "sim": {
#           "sim_number": "9876543210",
#           "provider": "Jio",
#           "is_esim": false,
#           "activation_year": 2023
#         }
#       }
#     ]
#   }
# }