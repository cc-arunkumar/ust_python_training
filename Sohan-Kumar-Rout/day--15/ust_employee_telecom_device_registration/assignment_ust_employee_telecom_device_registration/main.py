from pydantic import BaseModel, Field
from typing import Optional,List
from fastapi import FastAPI,HTTPException

# Initialize FastAPI app
app = FastAPI(title="UST Employee Operation")

# Basic employee model
class EmployeeBasic(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)  
    name: str = Field(..., min_length=2)           
    department: str = "General"  

# SIM card model
class SIMCard(BaseModel):
    number: str = Field(..., pattern=r"^\d{10}$") 
    provider: str = Field(default="Jio")           
    activation_year: int = Field(..., ge=2020, le=2025) 
    
# Data plan model
class DataPlan(BaseModel):
    name : str = Field(...,min_length=3,max_length=50)
    monthly_gb : int = Field(...,gt=0,le=1000)
    speed_mbps : int = Field(deafault=50,ge=1,le=1000)
    is_roaming_included: bool = (False)

# Voice plan model
class VoicePlan(BaseModel):
    name : str = Field(...,min_length=3)
    monthly_minuited : int = Field(...,ge=0,le=1000)
    has_isb : bool = Field(default=False)
    per_minute_charge_paise : int = Field(default=0,ge=0,le=1000)
    
# Emergency contact model
class EmergencyContact(BaseModel):
    name : str = Field(...,min_length=2)
    relation : str = Field(default="Family")
    phone : str = Field(pattern="^[6-9]\d{9}$")
    
# Employee telecom profile model
class EmployeeTelecomProfile(BaseModel):
    employee :  EmployeeBasic= (...)
    sim : SIMCard = (...)
    data_plan : Optional[DataPlan]= Field(default=None)
    voice_plan : Optional[VoicePlan] = Field(default=None)
    Emergency_contact : Optional[EmergencyContact] = Field(default=None)
    
# In-memory list of profiles
profiles: List[EmployeeTelecomProfile]=[]

# Create telecom profile
@app.post("/telecom/profile",status_code=409)
def create_telecom(profile: EmployeeTelecomProfile):
    for check in profiles:
        if check.employee.emp_id==profile.employee.id:
            raise HTTPException(detail="Employee with this id already exits")
    profiles.append(profile)
    return profiles

# Get all profiles
@app.get("/telecom/profiles")
def all_telecom_employees():
    return profiles

# Get profile by employee id
@app.get("/telecom/profiles/{emp_id}")
def get_by_id(emp_id : int):
    for check in profiles:
        if check.employee.emp_id == emp_id:
            return check
    raise HTTPException(status_code=404,detail="profile not found")

# Update profile by employee id
@app.put("/telecom/profiles/{emp_id}")
def update_by_emp_id(emp_id:int, profile: EmployeeTelecomProfile):
    if profile.employee.emp_id !=emp_id:
        raise HTTPException(status_code=404, detail=" employee id doesnot match")
    for c in profiles:
        if c.employee.emp_id==emp_id:
            profiles.remove(c)
            profiles.append(profile)
            return profile
    raise HTTPException(status_code=404,detail="profile not found")

# Delete profile by employee id
@app.delete("/telecom/profiles/{emp_id}")
def delete_by_employee_id(emp_id: int):
    for c in profiles:
        if c.employee.emp_id==emp_id:
            profiles.remove(c)
            return {"detail": "profile deleted"}
        
    raise HTTPException(status_code=404,detail="Profile not found")

# Search profiles by department or provider
@app.get("/telecom/profiles/search")
def profiles_search(department:Optional[str]=None,provider: Optional[str]=None):
    result=profiles
    if department:
        result= [p for p in result if p.employee.department==department]
    if provider:
        result=[p for p in result if p.sim.provider==provider]
    return result


#Output

# POST /telecom/profile
# [
#   {
#     "employee": {
#       "emp_id": 12345,
#       "name": "Asha",
#       "department": "Engineering"
#     },
#     "sim": {
#       "number": "9876543210",
#       "provider": "Airtel",
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

# GET /telecom/profiles
# [
#   {
#     "employee": {
#       "emp_id": 12345,
#       "name": "Asha",
#       "department": "Engineering"
#     },
#     "sim": {
#       "number": "9876543210",
#       "provider": "Airtel",
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

# GET /telecom/profiles/12345
# {
#   "employee": {
#     "emp_id": 12345,
#     "name": "Asha",
#     "department": "Engineering"
#   },
#   "sim": {
#     "number": "9876543210",
#     "provider": "Airtel",
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

# DELETE /telecom/profiles/12345
# {
#   "detail": "profile deleted"
# }

# GET /telecom/profiles/search?department=Engineering
# [
#   {
#     "employee": {
#       "emp_id": 12345,
#       "name": "Asha",
#       "department": "Engineering"
#     },
#     "sim": {
#       "number": "9876543210",
#       "provider": "Airtel",
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
