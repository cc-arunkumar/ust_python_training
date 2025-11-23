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
    emp_id:int=Field(...,ge=1000,le=999999)
    name:str=Field(...,min_length=2)
    official_email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@ust\.com$")
    department:str="Telecom"
    location:str="Bengaluru"

class SimCard(BaseModel):
    #using field for validation
    sim_number:str=Field(...,pattern=r"^\d{10}$")
    provider:str="Jio"
    is_esim:bool=False
    activation_year:int=Field(...,ge=2020,le=2025)

class DataPlan(BaseModel):
    #using field for validation
    name:str=Field(...,min_length=3,max_length=50)
    monthly_gb:int=Field(...,gt=0,le=1000)
    speed_mbps:int=Field(50,ge=1,le=1000)
    is_roaming_included:bool=False


class VoicePlan(BaseModel):
    #using field for validation
    name:str=Field(...,min_length=3)
    monthly_minutes:int=Field(...,ge=0,le=10000)
    has_isd:bool=False
    per_minute_charge_paise:int=Field(0,ge=0,le=1000)


class EmergencyContact(BaseModel):
    #using field for validation
    name:str=Field(...,min_length=2)
    relation:str="Family"
    phone:str=Field(...,pattern=r"^[6-9]\d{9}$")


#Top level model used in the API for telecom registration

class EmployeeTelecomProfile(BaseModel):
    employee:EmployeeBasic
    sim:SimCard
    data_plan:Optional[DataPlan]=None
    voice_plan:Optional[VoicePlan]=None
    emergency_contact:Optional[EmergencyContact]=None

 
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
    for pf in telecomprofile:
        if pf['employee']['emp_id']==teleprofile.employee.emp_id:
            raise HTTPException(status_code=409,detail="Employee id already exists")
    
    #appending inside the inmemory
    telecomprofile.append(teleprofile.model_dump())
    return teleprofile



#get all profile details
@app.get("/telecom/profiles",response_model=List[EmployeeTelecomProfile])

def get_all():
    return telecomprofile


#get all profile details by id
@app.get("/telecom/profiles/{emp_id}",response_model=EmployeeTelecomProfile)

def get_by_id(emp_id:int):
    for pf in telecomprofile:
        #iterating through to find the correct id
        if pf['employee']['emp_id']==emp_id:
            return pf
    raise HTTPException(status_code=404,detail="Profile not found")


#edit profile by id
@app.put("/telecom/profile/{emp_id}",response_model=EmployeeTelecomProfile)

#getting id and uodating that alone
def update(emp_id:int,profile:EmployeeTelecomProfile):
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
    telecomprofile.remove(existing)
    telecomprofile.append(profile.model_dump())
          
    return profile


#delete profile by emp_id
@app.delete("/telecom/profiles/{emp_id}")
def delete_prof(emp_id:int):
    for pf in telecomprofile:
        if pf['employee']['emp_id']==emp_id:
            telecomprofile.remove(pf)
            return {"Profile deleted successfully"}
    
    raise HTTPException(status_code=404,detail="Profile not found")


#search api for specific params or any params
@app.get("/telecom/profiles/search",response_model=List[EmployeeTelecomProfile])
async def search_profiles(department:Optional[str]=None,provider:Optional[str]=None):
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

