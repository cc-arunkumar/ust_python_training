# UST Employee Telecom Management API
# This API manages telecom services for UST employees.

# Key features include:
# 1. Employee registration with personal and telecom details.
# 2. Management of SIM card details and plans (data, voice).
# 3. Optional emergency contact details.
# 4. In-memory storage of employee profiles (data lost on server restart).
# 5. Profile validation using Pydantic models (e.g., valid email, phone numbers, SIM details).
# 6. API endpoints for CRUD operations on employee profiles.
# 7. Profile filtering by department and telecom provider.
# 8. Error handling for invalid inputs (e.g., incorrect phone numbers, missing fields).
# 9. Allows for adding, updating, retrieving, and deleting profiles.
# 10. Testing of various validation scenarios like incorrect employee ID or SIM card number.



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional

# Define Pydantic data models for employee and telecom-related details
# EmployeeBasic Model - Contains basic employee details

class EmployeeBasic(BaseModel):
    
# Model for employee basic details like ID, name, email, department, and location.
# Employee ID, must be between 1000 and 999999
# Employee's full name
# Employee's official email address (must end with '@ust.com')
# Employee's department (default is 'Telecom')
# Employee's location (default is 'Bengaluru')

    emp_id: int  
    name: str  
    official_email: str  
    department: Optional[str] = "Telecom"  
    location: Optional[str] = "Bengaluru"  

# Validator to ensure emp_id is within a specific range (1000 to 999999)

    @field_validator('emp_id')
    def validate_emp_id(cls, v):
        if not (1000 <= v <= 999999):
            raise ValueError('emp_id must be between 1000 and 999999')
        return v

# Validator to ensure official email is valid (must end with '@ust.com')
    
    @field_validator('official_email')
    def validate_email(cls, v):
        if not v.endswith('@ust.com'):
            raise ValueError('Email must be a UST email address.')
        return v

# Validator to ensure name is at least 2 characters long

    @field_validator('name')
    def validate_name(cls, v):
        if len(v) < 2:
            raise ValueError('Name must be at least 2 characters long.')
        return v

# SimCard Model - Contains details of the employee's SIM card

class SimCard(BaseModel):
    
# Model for SIM card details associated with the employee.
# SIM card number (must be a 10-digit number)
# Telecom provider (default is 'Jio')
# Whether it's an eSIM (default is False)
# The year the SIM was activated (must be between 2020 and 2025)

    sim_number: str  
    provider: Optional[str] = "Jio"  
    is_esim: Optional[bool] = False  
    activation_year: int  

# Validator to ensure SIM number is a valid 10-digit number

    @field_validator('sim_number')
    def validate_sim_number(cls, v):
        if not v.isdigit() or len(v) != 10:
            raise ValueError('sim_number must be a 10-digit number.')
        return v

# Validator to ensure activation year is within the specified range (2020 to 2025)
    @field_validator('activation_year')
    def validate_activation_year(cls, v):
        if not (2020 <= v <= 2025):
            raise ValueError('activation_year must be between 2020 and 2025')
        return v

# DataPlan Model - Contains details of the employee's data plan

class DataPlan(BaseModel):
    
# Model for data plan details associated with the employee.
# Name of the data plan
# Monthly data allocation in GB
# Data speed in Mbps (default is 50)
# Whether roaming is included (default is False)

    name: str  
    monthly_gb: int  
    speed_mbps: Optional[int] = 50  
    is_roaming_included: Optional[bool] = False 
     
# Validator to ensure monthly GB is within the range of 1 to 1000 GB
    
    @field_validator('monthly_gb')
    def validate_monthly_gb(cls, v):
        if not (1 <= v <= 1000):
            raise ValueError('monthly_gb must be between 1 and 1000')
        return v

# VoicePlan Model - Contains details of the employee's voice plan

class VoicePlan(BaseModel):
    
# Model for voice plan details associated with the employee.
# Name of the voice plan
# Monthly allotted minutes
# Whether ISD calls are included (default is False)
# Per-minute charge in paise (default is 0)
    
    name: str  
    monthly_minutes: int  
    has_isd: Optional[bool] = False  
    per_minute_charge_paise: Optional[int] = 0  

# Validator to ensure monthly minutes are within the range of 0 to 10,000 minutes
    
    @field_validator('monthly_minutes')
    def validate_monthly_minutes(cls, v):
        if not (0 <= v <= 10000):
            raise ValueError('monthly_minutes must be between 0 and 10000')
        return v

# Validator to ensure per-minute charge is between 0 and 1000 paise

    @field_validator('per_minute_charge_paise')
    def validate_per_minute_charge_paise(cls, v):
        if not (0 <= v <= 1000):
            raise ValueError('per_minute_charge_paise must be between 0 and 1000')
        return v

# EmergencyContact Model - Contains details of an emergency contact for the employee

class EmergencyContact(BaseModel):
    
# Model for emergency contact details associated with the employee.
# Name of the emergency contact
# Relation to the employee (default is 'Family')
# Emergency contact's phone number

    name: str  
    relation: Optional[str] = "Family"  
    phone: str  

# Validator to ensure phone number is a valid Indian mobile number
   
    @field_validator('phone')
    def validate_phone(cls, v):
        if not (v.isdigit() and len(v) == 10 and v[0] in '6789'):
            raise ValueError('phone must be a valid Indian mobile number (starting with 6-9)')
        return v

# EmployeeTelecomProfile Model - Combines employee information with telecom services

class EmployeeTelecomProfile(BaseModel):
    
# Model combining employee basic information with telecom services like SIM, data plan, voice plan, and emergency contact.
# Employee basic information
# Employee's SIM card details
# Optional data plan associated with the employee
# Optional voice plan associated with the employee
# Optional emergency contact details

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
    
# Create a new telecom profile for an employee.
# Check if the employee ID already exists in the profiles list
    
    for existing_profile in Profiles:
        if existing_profile.employee.emp_id == profile.employee.emp_id:
            raise HTTPException(status_code=409, detail="Employee id already exists")
    Profiles.append(profile)  # Add the profile to the list
    return profile  

# READ: Retrieve all telecom profiles

@app.get("/telecom/profiles")
def get_all_profiles():
    
# Retrieve all employee telecom profiles.
    
    return Profiles

# SEARCH: Filter profiles by department and/or provider

@app.get("/telecom/profiles/search")
def get_profile_params(department: str = "", provider: str = ""):

# Search telecom profiles by department and/or provider.
# If no filters provided, return all profiles
    
    if department == "" and provider == "":
        return Profiles
    
# Filter by department and/or provider
    
    filtered_profiles = [
        profile for profile in Profiles
        if (department == "" or profile.employee.department == department) and
           (provider == "" or profile.sim.provider == provider)
    ]
    return filtered_profiles

# READ: Get a specific profile by employee ID

@app.get("/telecom/profiles/{emp_id}")
def get_profile(emp_id: int):

# Retrieve a specific telecom profile by employee ID.
# Loop through profiles to find the one with the matching employee ID
  
    for profile in Profiles:
        if profile.employee.emp_id == emp_id:
            return profile
    raise HTTPException(status_code=404, detail="Profile not found")

# UPDATE: Modify an existing profile by employee ID

@app.put("/telecom/profiles/{emp_id}")
def update_profile(emp_id: int, updated_profile: EmployeeTelecomProfile):

# Update an existing telecom profile by employee ID.
# Check if the employee ID exists and update the profile
    
    for idx, profile in enumerate(Profiles):
        if profile.employee.emp_id == emp_id:
            Profiles[idx] = updated_profile  # Update the profile
            return updated_profile
    raise HTTPException(status_code=404, detail="Employee id does not exist")

# DELETE: Remove a profile by employee ID

@app.delete("/telecom/profiles/{emp_id}")
def delete_profile(emp_id: int):

# Delete a telecom profile by employee ID.
# Check if the profile exists and remove it from the list

    for idx, profile in enumerate(Profiles):
        if profile.employee.emp_id == emp_id:
            Profiles.pop(idx)  # Remove the profile from the list
            return {"detail": "Profile deleted"}
    return {"detail": "Profile Not Found"}



# 1. POST /telecom/profiles - Create a new telecom profile
# Request:
# {
#     "employee": {
#         "emp_id": 1001,
#         "name": "John Doe",
#         "official_email": "john.doe@ust.com",
#         "department": "IT",
#         "location": "Chennai"
#     },
#     "sim": {
#         "sim_number": "9876543210",
#         "provider": "Airtel",
#         "is_esim": false,
#         "activation_year": 2023
#     },
#     "data_plan": {
#         "name": "Unlimited Data",
#         "monthly_gb": 100,
#         "speed_mbps": 100,
#         "is_roaming_included": true
#     },
#     "voice_plan": {
#         "name": "Unlimited Voice",
#         "monthly_minutes": 1000,
#         "has_isd": true,
#         "per_minute_charge_paise": 10
#     },
#     "emergency_contact": {
#         "name": "Jane Doe",
#         "relation": "Spouse",
#         "phone": "9876543211"
#     }
# }

# Response (201 Created):
# {
#     "employee": {
#         "emp_id": 1001,
#         "name": "John Doe",
#         "official_email": "john.doe@ust.com",
#         "department": "IT",
#         "location": "Chennai"
#     },
#     "sim": {
#         "sim_number": "9876543210",
#         "provider": "Airtel",
#         "is_esim": false,
#         "activation_year": 2023
#     },
#     "data_plan": {
#         "name": "Unlimited Data",
#         "monthly_gb": 100,
#         "speed_mbps": 100,
#         "is_roaming_included": true
#     },
#     "voice_plan": {
#         "name": "Unlimited Voice",
#         "monthly_minutes": 1000,
#         "has_isd": true,
#         "per_minute_charge_paise": 10
#     },
#     "emergency_contact": {
#         "name": "Jane Doe",
#         "relation": "Spouse",
#         "phone": "9876543211"
#     }
# }

# 2. GET /telecom/profiles - Retrieve all telecom profiles
# Response (200 OK):
# [
#     {
#         "employee": {
#             "emp_id": 1001,
#             "name": "John Doe",
#             "official_email": "john.doe@ust.com",
#             "department": "IT",
#             "location": "Chennai"
#         },
#         "sim": {
#             "sim_number": "9876543210",
#             "provider": "Airtel",
#             "is_esim": false,
#             "activation_year": 2023
#         },
#         "data_plan": {
#             "name": "Unlimited Data",
#             "monthly_gb": 100,
#             "speed_mbps": 100,
#             "is_roaming_included": true
#         },
#         "voice_plan": {
#             "name": "Unlimited Voice",
#             "monthly_minutes": 1000,
#             "has_isd": true,
#             "per_minute_charge_paise": 10
#         },
#         "emergency_contact": {
#             "name": "Jane Doe",
#             "relation": "Spouse",
#             "phone": "9876543211"
#         }
#     }
# ]

# 3. GET /telecom/profiles/search - Filter profiles by department and/or provider
# Request: GET /telecom/profiles/search?department=IT&provider=Airtel
# Response (200 OK):
# [
#     {
#         "employee": {
#             "emp_id": 1001,
#             "name": "John Doe",
#             "official_email": "john.doe@ust.com",
#             "department": "IT",
#             "location": "Chennai"
#         },
#         "sim": {
#             "sim_number": "9876543210",
#             "provider": "Airtel",
#             "is_esim": false,
#             "activation_year": 2023
#         },
#         "data_plan": {
#             "name": "Unlimited Data",
#             "monthly_gb": 100,
#             "speed_mbps": 100,
#             "is_roaming_included": true
#         },
#         "voice_plan": {
#             "name": "Unlimited Voice",
#             "monthly_minutes": 1000,
#             "has_isd": true,
#             "per_minute_charge_paise": 10
#         },
#         "emergency_contact": {
#             "name": "Jane Doe",
#             "relation": "Spouse",
#             "phone": "9876543211"
#         }
#     }
# ]

# 4. GET /telecom/profiles/{emp_id} - Get a specific profile by employee ID
# Request: GET /telecom/profiles/1001
# Response (200 OK):
# {
#     "employee": {
#         "emp_id": 1001,
#         "name": "John Doe",
#         "official_email": "john.doe@ust.com",
#         "department": "IT",
#         "location": "Chennai"
#     },
#     "sim": {
#         "sim_number": "9876543210",
#         "provider": "Airtel",
#         "is_esim": false,
#         "activation_year": 2023
#     },
#     "data_plan": {
#         "name": "Unlimited Data",
#         "monthly_gb": 100,
#         "speed_mbps": 100,
#         "is_roaming_included": true
#     },
#     "voice_plan": {
#         "name": "Unlimited Voice",
#         "monthly_minutes": 1000,
#         "has_isd": true,
#         "per_minute_charge_paise": 10
#     },
#     "emergency_contact": {
#         "name": "Jane Doe",
#         "relation": "Spouse",
#         "phone": "9876543211"
#     }
# }

# 5. PUT /telecom/profiles/{emp_id} - Update an existing profile by employee ID
# Request: PUT /telecom/profiles/1001
# {
#     "employee": {
#         "emp_id": 1001,
#         "name": "John Doe Updated",
#         "official_email": "john.doe.updated@ust.com",
#         "department": "HR",
#         "location": "Mumbai"
#     },
#     "sim": {
#         "sim_number": "9876543210",
#         "provider": "Airtel",
#         "is_esim": true,
#         "activation_year": 2023
#     },
#     "data_plan": {
#         "name": "Unlimited Data",
#         "monthly_gb": 100,
#         "speed_mbps": 100,
#         "is_roaming_included": true
#     },
#     "voice_plan": {
#         "name": "Unlimited Voice",
#         "monthly_minutes": 1000,
#         "has_isd": true,
#         "per_minute_charge_paise": 10
#     },
#     "emergency_contact": {
#         "name": "Jane Doe Updated",
#         "relation": "Spouse",
#         "phone": "9876543211"
#     }
# }

# Response (200 OK):
# {
#     "employee": {
#         "emp_id": 1001,
#         "name": "John Doe Updated",
#         "official_email": "john.doe.updated@ust.com",
#         "department": "HR",
#         "location": "Mumbai"
#     },
#     "sim": {
#         "sim_number": "9876543210",
#         "provider": "Airtel",
#         "is_esim": true,
#         "activation_year": 2023
#     },
#     "data_plan": {
#         "name": "Unlimited Data",
#         "monthly_gb": 100,
#         "speed_mbps": 100,
#         "is_roaming_included": true
#     },
#     "voice_plan": {
#         "name": "Unlimited Voice",
#         "monthly_minutes": 1000,
#         "has_isd": true,
#         "per_minute_charge_paise": 10
#     },
#     "emergency_contact": {
#         "name": "Jane Doe Updated",
#         "relation": "Spouse",
#         "phone": "9876543211"
#     }
# }

# 6. DELETE /telecom/profiles/{emp_id} - Delete a profile by employee ID
# Request: DELETE /telecom/profiles/1001
# Response (200 OK):
# {
#     "detail": "Profile deleted"
# }

# 7. GET /telecom/profiles/search - Search profiles by department and/or provider
# Request: GET /telecom/profiles/search?department=IT&provider=Airtel
# Response (200 OK):
# [
#     {
#         "employee": {
#             "emp_id": 1001,
#             "name": "John Doe",
#             "official_email": "john.doe@ust.com",
#             "department": "IT",
#             "location": "Chennai"
#         },
#         "sim": {
#             "sim_number": "9876543210",
#             "provider": "Airtel",
#             "is_esim": false,
#             "activation_year": 2023
#         },
#         "data_plan": {
#             "name": "Unlimited Data",
#             "monthly_gb": 100,
#             "speed_mbps": 100,
#             "is_roaming_included": true
#         },
#         "voice_plan": {
#             "name": "Unlimited Voice",
#             "monthly_minutes": 1000,
#             "has_isd": true,
#             "per_minute_charge_paise": 10
#         },
#         "emergency_contact": {
#             "name": "Jane Doe",
#             "relation": "Spouse",
#             "phone": "9876543211"
#         }
#     }
# ]