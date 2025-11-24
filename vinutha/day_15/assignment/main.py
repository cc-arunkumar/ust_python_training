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


# Import required libraries
from fastapi import FastAPI,HTTPException
from pydantic import validator,Field,BaseModel
from typing import List,Optional
 

# Define data models using Pydantic
# Model for basic employee information
class EmployeeBasic(BaseModel):
    emp_id:int=Field(...,ge=1000,le=999999)
    name:str=Field(...,min_length=2)
    official_email:str=Field(...,pattern=r"^[a-zA-Z0-9._%+-]+@ust\.com$")
    department:Optional[str]="Telecom"
    location:Optional[str]="Bengaluru"

# Model for SIM card details
class SimCard(BaseModel):
    sim_number:str=Field(...,pattern=r"\d{10}$")
    provider:Optional[str]="Jio"
    is_esim:Optional[bool]=False
    activation_year:int=Field(...,ge=2020,le=2025)
    
# Model for data plan details
class DataPlan(BaseModel):
    name:str=Field(...,min_length=3,max_length=50)
    monthly_gb:int=Field(...,gt=0,le=1000)
    speed_mbps:Optional[int]=Field("50",ge=1,le=1000)
    is_roaming_included:Optional[bool]=Field(False)

# Model for voice plan details
class VoicePlan(BaseModel):
    name:str=Field(...,min_length=3)
    monthly_minutes:int=Field(...,ge=0,le=1000)
    has_isd:Optional[bool]=Field(False)
    per_minute_charge_paise:Optional[int]=Field(0,ge=0,le=1000) 
    
# Model for emergency contact information
class EmergencyContact(BaseModel):
    name:str=Field(...,min_length=3)
    relation:Optional[str]="Family"
    phone:str=Field(...,pattern=r"^[6-9]\d{9}$")  
    
# Complete employee telecom profile combining all models
class EmployeeTelecomProfile(BaseModel):
    employee: EmployeeBasic=Field(...)
    sim: SimCard=Field(...)
    data_plan: Optional[DataPlan]=None
    VoicePlan:Optional[VoicePlan]=None
    emergency_contact:Optional[EmergencyContact]=None
    
# Initialize FastAPI application
app=FastAPI()

# In-memory storage for profiles
Profiles: List[EmployeeTelecomProfile]=[]
       

# CREATE: Add a new telecom profile
@app.post("/telecom/profiles")
def create_telecom_profile(profile:EmployeeTelecomProfile):
    # Check if employee ID already exists
    for existing_profile in Profiles:
        if existing_profile.employee.emp_id == profile.employee.emp_id:
            raise HTTPException(status_code=409, detail="Employee id already exists")
    Profiles.append(profile)
    return profile  

# READ: Get all profiles
@app.get("/telecom/profiles")
def get_all_profiles():
    return Profiles

# SEARCH: Filter profiles by department and/or provider
@app.get("/telecom/profiles/search")
def get_profile_params(department:str="",provider:str=""):
    # If no filters provided, return all profiles
    if department=="" and provider=="":
        return Profiles
    # If both department and provider provided
    if department!="" and provider!="":
        newdepartmentlist=[]
        for K in Profiles:
            if K.employee.department==department:
                newdepartmentlist.append(K)
        return newdepartmentlist
    # If only provider provided
    elif department=="" and provider!="":
        newproviderlist=[]
        for K in Profiles:
            if K.sim.provider==provider:
                newproviderlist.append(K)
        return newproviderlist
    # If only department provided
    else:
        newcombined=[]
        for K in Profiles:
            if K.employee.department==department and K.sim.provider==provider:
                newcombined.append(K)
        return newcombined

# READ: Get specific profile by employee ID
@app.get("/telecom/profiles/{emp_id}")
def get_profile(emp_id: int):
    for profile in Profiles:
        if profile.employee.emp_id == emp_id:
            return profile
    raise HTTPException(status_code=404, detail="Profile not found")

# UPDATE: Modify an existing profile
@app.put("/telecom/profiles/{emp_id}")
def update_profile(emp_id: int, updated_profile: EmployeeTelecomProfile):
    for i, profile in enumerate(Profiles):
        if profile.employee.emp_id == emp_id:
            Profiles[i] = updated_profile
            return updated_profile
    raise HTTPException(status_code=404, detail="Employee id does not exist")
 

# DELETE: Remove a profile by employee ID
@app.delete("/telecom/profiles/{emp_id}")
def delete_profile(emp_id:int):
    for i,K in enumerate(Profiles):
        if K.employee.emp_id==emp_id:
            Profiles.pop(i)
            return {"detail":"Profile deleted"}
    return {"detail":"Profile Not Found"}


# sample output:
# 1. Add a New Telecom Profile (CREATE)
# Request:
# POST /telecom/profiles
# Body:
# {
#     "employee": {
#         "emp_id": 12345,
#         "name": "John Doe",
#         "official_email": "john.doe@ust.com",
#         "department": "Engineering",
#         "location": "Bengaluru"
#     },
#     "sim": {
#         "sim_number": "9876543210",
#         "provider": "Jio",
#         "is_esim": false,
#         "activation_year": 2023
#     },
#     "data_plan": {
#         "name": "Unlimited Plan",
#         "monthly_gb": 50,
#         "speed_mbps": 100,
#         "is_roaming_included": true
#     },
#     "voice_plan": {
#         "name": "Voice Plus",
#         "monthly_minutes": 500,
#         "has_isd": true,
#         "per_minute_charge_paise": 60
#     },
#     "emergency_contact": {
#         "name": "Jane Doe",
#         "relation": "Spouse",
#         "phone": "9876543210"
#     }
# }
# Response:
# {
#     "employee": {
#         "emp_id": 12345,
#         "name": "John Doe",
#         "official_email": "john.doe@ust.com",
#         "department": "Engineering",
#         "location": "Bengaluru"
#     },
#     "sim": {
#         "sim_number": "9876543210",
#         "provider": "Jio",
#         "is_esim": false,
#         "activation_year": 2023
#     },
#     "data_plan": {
#         "name": "Unlimited Plan",
#         "monthly_gb": 50,
#         "speed_mbps": 100,
#         "is_roaming_included": true
#     },
#     "voice_plan": {
#         "name": "Voice Plus",
#         "monthly_minutes": 500,
#         "has_isd": true,
#         "per_minute_charge_paise": 60
#     },
#     "emergency_contact": {
#         "name": "Jane Doe",
#         "relation": "Spouse",
#         "phone": "9876543210"
#     }
# }

# 2. Get All Telecom Profiles (READ)
# Request:
# GET /telecom/profiles
# Response:
# [
#     {
#         "employee": {
#             "emp_id": 12345,
#             "name": "John Doe",
#             "official_email": "john.doe@ust.com",
#             "department": "Engineering",
#             "location": "Bengaluru"
#         },
#         "sim": {
#             "sim_number": "9876543210",
#             "provider": "Jio",
#             "is_esim": false,
#             "activation_year": 2023
#         },
#         "data_plan": {
#             "name": "Unlimited Plan",
#             "monthly_gb": 50,
#             "speed_mbps": 100,
#             "is_roaming_included": true
#         },
#         "voice_plan": {
#             "name": "Voice Plus",
#             "monthly_minutes": 500,
#             "has_isd": true,
#             "per_minute_charge_paise": 60
#         },
#         "emergency_contact": {
#             "name": "Jane Doe",
#             "relation": "Spouse",
#             "phone": "9876543210"
#         }
#     }
# ]

# 3. Search Telecom Profiles by Department and/or Provider (SEARCH)
# Request:
# GET /telecom/profiles/search?department=Engineering&provider=Jio
# Response:
# [
#     {
#         "employee": {
#             "emp_id": 12345,
#             "name": "John Doe",
#             "official_email": "john.doe@ust.com",
#             "department": "Engineering",
#             "location": "Bengaluru"
#         },
#         "sim": {
#             "sim_number": "9876543210",
#             "provider": "Jio",
#             "is_esim": false,
#             "activation_year": 2023
#         },
#         "data_plan": {
#             "name": "Unlimited Plan",
#             "monthly_gb": 50,
#             "speed_mbps": 100,
#             "is_roaming_included": true
#         },
#         "voice_plan": {
#             "name": "Voice Plus",
#             "monthly_minutes": 500,
#             "has_isd": true,
#             "per_minute_charge_paise": 60
#         },
#         "emergency_contact": {
#             "name": "Jane Doe",
#             "relation": "Spouse",
#             "phone": "9876543210"
#         }
#     }
# ]

# 4. Get Profile by Employee ID (READ)
# Request:
# GET /telecom/profiles/12345
# Response:
# {
#     "employee": {
#         "emp_id": 12345,
#         "name": "John Doe",
#         "official_email": "john.doe@ust.com",
#         "department": "Engineering",
#         "location": "Bengaluru"
#     },
#     "sim": {
#         "sim_number": "9876543210",
#         "provider": "Jio",
#         "is_esim": false,
#         "activation_year": 2023
#     },
#     "data_plan": {
#         "name": "Unlimited Plan",
#         "monthly_gb": 50,
#         "speed_mbps": 100,
#         "is_roaming_included": true
#     },
#     "voice_plan": {
#         "name": "Voice Plus",
#         "monthly_minutes": 500,
#         "has_isd": true,
#         "per_minute_charge_paise": 60
#     },
#     "emergency_contact": {
#         "name": "Jane Doe",
#         "relation": "Spouse",
#         "phone": "9876543210"
#     }
# }

# 5. Update Telecom Profile by Employee ID (UPDATE)
# Request:
# PUT /telecom/profiles/12345
# Body:
# {
#     "employee": {
#         "emp_id": 12345,
#         "name": "John Doe Updated",
#         "official_email": "john.doe.updated@ust.com",
#         "department": "Engineering",
#         "location": "Mumbai"
#     },
#     "sim": {
#         "sim_number": "9876543210",
#         "provider": "Jio",
#         "is_esim": true,
#         "activation_year": 2023
#     },
#     "data_plan": {
#         "name": "Updated Plan",
#         "monthly_gb": 100,
#         "speed_mbps": 200,
#         "is_roaming_included": true
#     },
#     "voice_plan": {
#         "name": "Updated Voice Plan",
#         "monthly_minutes": 1000,
#         "has_isd": true,
#         "per_minute_charge_paise": 40
#     },
#     "emergency_contact": {
#         "name": "Jane Doe Updated",
#         "relation": "Spouse",
#         "phone": "9876543210"
#     }
# }
# Response:
# {
#     "employee": {
#         "emp_id": 12345,
#         "name": "John Doe Updated",
#         "official_email": "john.doe.updated@ust.com",
#         "department": "Engineering",
#         "location": "Mumbai"
#     },
#     "sim": {
#         "sim_number": "9876543210",
#         "provider": "Jio",
#         "is_esim": true,
#         "activation_year": 2023
#     },
#     "data_plan": {
#         "name": "Updated Plan",
#         "monthly_gb": 100,
#         "speed_mbps": 200,
#         "is_roaming_included": true
#     },
#     "voice_plan": {
#         "name": "Updated Voice Plan",
#         "monthly_minutes": 1000,
#         "has_isd": true,
#         "per_minute_charge_paise": 40
#     },
#     "emergency_contact": {
#         "name": "Jane Doe Updated",
#         "relation": "Spouse",
#         "phone": "9876543210"
#     }
# }

# 6. Delete Telecom Profile by Employee ID (DELETE)
# Request:
# DELETE /telecom/profiles/12345
# Response:
# {
#     "detail": "Profile deleted"
# }

# 7. Profile Not Found (Error Response)
# Request:
# GET /telecom/profiles/99999
# Response:
# {
#     "detail": "Profile not found"
# }

