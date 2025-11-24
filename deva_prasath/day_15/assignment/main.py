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




#imports
from pydantic import BaseModel,Field
from typing import List,Optional
from fastapi import FastAPI,HTTPException

#name of the title
app=FastAPI(title="UST Employee Telecom Management")


#defining classes
class EmployeeBasic(BaseModel):
    #using field for validation
    emp_id:int=Field(...,ge=1000,le=999999)  # Emp ID should be between 1000 and 999999
    name:str=Field(...,min_length=2)  # Name should have at least 2 characters
    official_email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@ust\.com$")  # Email should match the pattern
    department:str="Telecom"  # Default department
    location:str="Bengaluru"  # Default location

class SimCard(BaseModel):
    #using field for validation
    sim_number:str=Field(...,pattern=r"^\d{10}$")  # SIM number should be exactly 10 digits
    provider:str="Jio"  # Default provider
    is_esim:bool=False  # Default is not eSIM
    activation_year:int=Field(...,ge=2020,le=2025)  # Activation year should be between 2020 and 2025

class DataPlan(BaseModel):
    #using field for validation
    name:str=Field(...,min_length=3,max_length=50)  # Plan name should be between 3 and 50 characters
    monthly_gb:int=Field(...,gt=0,le=1000)  # Monthly data should be between 1 and 1000 GB
    speed_mbps:int=Field(50,ge=1,le=1000)  # Speed should be between 1 and 1000 Mbps
    is_roaming_included:bool=False  # Default is no roaming

class VoicePlan(BaseModel):
    #using field for validation
    name:str=Field(...,min_length=3)  # Plan name should have at least 3 characters
    monthly_minutes:int=Field(...,ge=0,le=10000)  # Monthly minutes should be between 0 and 10000
    has_isd:bool=False  # Default is no ISD
    per_minute_charge_paise:int=Field(0,ge=0,le=1000)  # Per minute charge should be between 0 and 1000 paise

class EmergencyContact(BaseModel):
    #using field for validation
    name:str=Field(...,min_length=2)  # Name should have at least 2 characters
    relation:str="Family"  # Default relation is family
    phone:str=Field(...,pattern=r"^[6-9]\d{9}$")  # Phone number should start with 6-9 and be 10 digits


#Top level model used in the API for telecom registration

class EmployeeTelecomProfile(BaseModel):
    employee:EmployeeBasic  # Employee basic information
    sim:SimCard  # SIM card details
    data_plan:Optional[DataPlan]=None  # Optional data plan
    voice_plan:Optional[VoicePlan]=None  # Optional voice plan
    emergency_contact:Optional[EmergencyContact]=None  # Optional emergency contact

 
#using in memory with dict inside list
telecomprofile: List[dict]=[
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
 "monthly_gb":50,
 "speed_mbps":100,
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


#post api for creating profile
@app.post("/telecom/profiles",response_model=EmployeeTelecomProfile)

def add_telecom_profile(teleprofile:EmployeeTelecomProfile):
    """
    API to add a new telecom profile.
    - Checks if the employee ID already exists.
    - Adds the profile to the in-memory list if not found.
    """
    for pf in telecomprofile:
        if pf['employee']['emp_id']==teleprofile.employee.emp_id:
            raise HTTPException(status_code=409,detail="Employee id already exists")
    
    #appending inside the inmemory
    telecomprofile.append(teleprofile.model_dump())  # Adds the new profile to the list
    return teleprofile


#get all profile details
@app.get("/telecom/profiles",response_model=List[EmployeeTelecomProfile])

def get_all():
    """
    API to retrieve all telecom profiles.
    - Returns the list of all telecom profiles.
    """
    return telecomprofile


#get all profile details by id
@app.get("/telecom/profiles/{emp_id}",response_model=EmployeeTelecomProfile)

def get_by_id(emp_id:int):
    """
    API to retrieve a telecom profile by employee ID.
    - Returns the profile of the employee if found.
    """
    for pf in telecomprofile:
        #iterating through to find the correct id
        if pf['employee']['emp_id']==emp_id:
            return pf
    raise HTTPException(status_code=404,detail="Profile not found")


#edit profile by id
@app.put("/telecom/profile/{emp_id}",response_model=EmployeeTelecomProfile)

#getting id and uodating that alone
def update(emp_id:int,profile:EmployeeTelecomProfile):
    """
    API to update a telecom profile by employee ID.
    - Checks if the profile exists, and ensures the path ID matches the body ID.
    - Updates the profile if the checks pass.
    """
    existing=None
    for pf in telecomprofile:
        if pf['employee']['emp_id']==emp_id:
            existing=pf
            break
    
    if existing is None:
        raise HTTPException(status_code=404,detail="No existing profile")
    
    if emp_id!=profile.employee.emp_id:
        raise HTTPException(status_code=400,detail="Path ID and Body ID do not match")
    
    #removing existing
    telecomprofile.remove(existing)  # Removes the old profile
    telecomprofile.append(profile.model_dump())  # Adds the updated profile
          
    return profile


#delete profile by emp_id
@app.delete("/telecom/profiles/{emp_id}")
def delete_prof(emp_id:int):
    """
    API to delete a telecom profile by employee ID.
    - Removes the profile from the list if found.
    """
    for pf in telecomprofile:
        if pf['employee']['emp_id']==emp_id:
            telecomprofile.remove(pf)  # Removes the profile
            return {"Profile deleted successfully"}
    
    raise HTTPException(status_code=404,detail="Profile not found")


#search api for specific params or any params
@app.get("/telecom/profiles/search",response_model=List[EmployeeTelecomProfile])
def search_profiles(department:Optional[str]=None,provider:Optional[str]=None):
    """
    API to search telecom profiles based on department or provider.
    - Filters the profiles based on provided search parameters.
    """
    filtered_profiles=telecomprofile  
    #checking for department
    
    if department:
        filtered_profiles=[pf for pf in filtered_profiles if pf['employee']['department']==department]
    
    #checking for provider
    if provider:
        filtered_profiles =[pf for pf in filtered_profiles if pf['sim']['provider'] == provider]
    
    if not filtered_profiles:
        raise HTTPException(status_code=404,detail="No profiles found matching the criteria")
    
    return filtered_profiles







#Sample output


# -------------------------
# 1. Profile Creation

# Request
# {
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

# Response body
# {
#   "employee": {
#     "emp_id": 89808,
#     "name": "Deva",
#     "official_email": "deva@ust.com",
#     "department": "Engineering",
#     "location": "Salem"
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

# ----------------------------------------------

# 2.Get by id
# http://127.0.0.1:8000/telecom/profiles/89808

# {
#   "employee": {
#     "emp_id": 89808,
#     "name": "Deva",
#     "official_email": "deva@ust.com",
#     "department": "Engineering",
#     "location": "Salem"
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

# -------------------------------------------------

# 3. Update by id

# curl -X 'PUT' \
#   'http://127.0.0.1:8000/telecom/profile/89808' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "employee": {
#     "emp_id": 89808,
#     "name": "Varun",
#     "official_email": "varun@ust.com",
#     "department": "Arts",
#     "location": "Karur"
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
# }'



# -------------------------------------------------

# 4. Delete by id

# curl -X 'DELETE' \
#   'http://127.0.0.1:8000/telecom/profiles/89808' \
#   -H 'accept: application/json'


# "Profile deleted successfully"


# -------------------------------------------------


# 5. Validation checks
# -----------------------------
# 1. emp_id > 1000 or < 999999

# Request

# {
#   "employee": {
#     "emp_id": 999,
#     "name": "Asha",
#     "official_email": "asha@ust.com"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "activation_year": 2023
#   }
# }


# Response

# {
#   "detail": [
#     {
#       "type": "greater_than_equal",
#       "loc": [
#         "body",
#         "employee",
#         "emp_id"
#       ],
#       "msg": "Input should be greater than or equal to 1000",
#       "input": 999,
#       "ctx": {
#         "ge": 1000
#       }
#     }
#   ]
# }

# -------------------------------------------------


# 2.name length=2

# Request

# {
#   "employee": {
#     "emp_id": 12345,
#     "name": "A",
#     "official_email": "asha@ust.com"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "activation_year": 2023
#   }
# }

# Response

# {
#   "detail": [
#     {
#       "type": "string_too_short",
#       "loc": [
#         "body",
#         "employee",
#         "name"
#       ],
#       "msg": "String should have at least 2 characters",
#       "input": "A",
#       "ctx": {
#         "min_length": 2
#       }
#     }
#   ]
# }

# -------------------------------------------------

# 3.official_email not ending with @ust.com

# Request
# {
#   "employee": {
#     "emp_id": 12345,
#     "name": "Asha",
#     "official_email": "asha@gmail.com"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "activation_year": 2023
#   }
# }


# Response

# {
#   "detail": [
#     {
#       "type": "string_pattern_mismatch",
#       "loc": [
#         "body",
#         "employee",
#         "official_email"
#       ],
#       "msg": "String should match pattern '^[a-zA-Z0-9._%+-]+@ust\\.com$'",
#       "input": "asha@gmail.com",
#       "ctx": {
#         "pattern": "^[a-zA-Z0-9._%+-]+@ust\\.com$"
#       }
#     }
#   ]
# }
# -------------------------------------------------


# 4.sim_number not 10 digits


# Request

# {
#   "employee": {
#     "emp_id": 12345,
#     "name": "Asha",
#     "official_email": "asha@ust.com"
#   },
#   "sim": {
#     "sim_number": "98765432",
#     "activation_year": 2023
#   }
# }

# Response

# {
#   "detail": [
#     {
#       "type": "string_pattern_mismatch",
#       "loc": [
#         "body",
#         "sim",
#         "sim_number"
#       ],
#       "msg": "String should match pattern '^\\d{10}$'",
#       "input": "98765432",
#       "ctx": {
#         "pattern": "^\\d{10}$"
#       }
#     }
#   ]

# -------------------------------------------------


# 5.activation_year > 2020 or < 2025
	
# Request

# {
#   "employee": {
#     "emp_id": 12345,
#     "name": "Asha",
#     "official_email": "asha@ust.com"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "activation_year": 2019
#   }
# }


# Response

# {
#   "detail": [
#     {
#       "type": "greater_than_equal",
#       "loc": [
#         "body",
#         "sim",
#         "activation_year"
#       ],
#       "msg": "Input should be greater than or equal to 2020",
#       "input": 2019,
#       "ctx": {
#         "ge": 2020
#       }
#     }
#   ]
# }

# -------------------------------------------------

# 6.monthly_gb >0 or <1000

# Request

# {
#   "employee": {
#     "emp_id": 12345,
#     "name": "Asha",
#     "official_email": "asha@ust.com"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "activation_year": 2023
#   },
#   "data_plan": {
#     "name": "Standard 50GB",
#     "monthly_gb": 0,
#     "speed_mbps": 100,
#     "is_roaming_included": true
#   }
# }

# Response

# {
#   "detail": [
#     {
#       "type": "greater_than",
#       "loc": [
#         "body",
#         "data_plan",
#         "monthly_gb"
#       ],
#       "msg": "Input should be greater than 0",
#       "input": 0,
#       "ctx": {
#         "gt": 0
#       }
#     }
#   ]
# }

# -------------------------------------------------

# 7.monthly_minutes negative

# Request

# {
#   "employee": {
#     "emp_id": 12345,
#     "name": "Asha",
#     "official_email": "asha@ust.com"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "activation_year": 2023
#   },
#   "voice_plan": {
#     "name": "Office Calls Pack",
#     "monthly_minutes": -100,
#     "has_isd": false,
#     "per_minute_charge_paise": 0
#   }
# }

# Response

# {
#   "detail": [
#     {
#       "type": "greater_than_equal",
#       "loc": [
#         "body",
#         "voice_plan",
#         "monthly_minutes"
#       ],
#       "msg": "Input should be greater than or equal to 0",
#       "input": -100,
#       "ctx": {
#         "ge": 0
#       }
#     }
#   ]
# }

# -------------------------------------------------

# 8.per_minute_charge_paise negative or >1000

# Request

# {
#   "employee": {
#     "emp_id": 12345,
#     "name": "Asha",
#     "official_email": "asha@ust.com"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "activation_year": 2023
#   },
#   "voice_plan": {
#     "name": "Office Calls Pack",
#     "monthly_minutes": 500,
#     "has_isd": false,
#     "per_minute_charge_paise": -10
#   }
# }

# Response

# {
#   "detail": [
#     {
#       "type": "greater_than_equal",
#       "loc": [
#         "body",
#         "voice_plan",
#         "per_minute_charge_paise"
#       ],
#       "msg": "Input should be greater than or equal to 0",
#       "input": -10,
#       "ctx": {
#         "ge": 0
#       }
#     }
#   ]
# }

# -------------------------------------------------

# 9. phone in EmergencyContact not matching pattern


# Request

# {
#   "employee": {
#     "emp_id": 12345,
#     "name": "Asha",
#     "official_email": "asha@ust.com"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "activation_year": 2023
#   },
#   "emergency_contact": {
#     "name": "Ravi",
#     "relation": "Friend",
#     "phone": "1234567890"
#   }
# }


# Response

# {
#   "detail": [
#     {
#       "type": "string_pattern_mismatch",
#       "loc": [
#         "body",
#         "emergency_contact",
#         "phone"
#       ],
#       "msg": "String should match pattern '^[6-9]\\d{9}$'",
#       "input": "1234567890",
#       "ctx": {
#         "pattern": "^[6-9]\\d{9}$"
#       }
#     }
#   ]
# }

# -------------------------------------------------
