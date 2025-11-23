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