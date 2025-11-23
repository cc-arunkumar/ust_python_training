# UST Employee Telecom Management
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
# No database or authentication is required

from typing import Dict, List, Optional, Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
 
app = FastAPI(title="Employee Telecom Management")
class EmployeeBasic(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)  
    name: str = Field(..., min_length=2)  
    official_email:str=Field(...,pattern= r'^[a-zA-Z0-9._%+-]+@ust\.com$')
    department: str = "Telecom"
    location:str="Bengaluru"
 
class SIMCard(BaseModel):
    sim_number: str = Field(..., min_length=10, max_length=10,pattern=r'^\d{10}$')
    provider: str = "Jio"  
    is_esim:bool=False
    activation_year: int = Field(..., ge=2020, le=2025)  
 
class DataPlan(BaseModel):
    name:str=Field(...,min_length=3 ,max_length=50)
    monthly_gb:int=Field(...,gt=0 ,le=1000)
    speed_mbps:int=Field(50,ge=1 , le=1000)
    is_roaming_included:bool=False
 
class VoicePlan(BaseModel):
    name:str=Field(...,min_length=3)
    monthly_minutes:int=Field(...,ge=0,le=10000)
    has_isd:bool=False
    per_minute_charge_paise:int=Field(0,ge=0, le=1000)
 
class EmergencyContact(BaseModel):
    name:str=Field(...,min_length=2)
    relation:str="Family"
    phone:str=Field(...,pattern=r'^[6-9]\d{9}$')
 
class EmployeeTelecomProfile(BaseModel):
    employee: EmployeeBasic = Field(...)  
    sim: SIMCard = Field(...)  
    data_plan:Optional[DataPlan]=None
    voice_plan:Optional[VoicePlan]=None
    emergency_contact:Optional[EmergencyContact]=None
 
data={
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
 
telecom_data:Dict[int,EmployeeTelecomProfile]={}
 
given_data=EmployeeTelecomProfile(**data)
telecom_data[given_data.employee.emp_id]=given_data
 
@app.post("/telecom/profiles",response_model=EmployeeTelecomProfile)
def create_data(profile:EmployeeTelecomProfile):
    employee_id=profile.employee.emp_id
    if employee_id in telecom_data:
        raise HTTPException(status_code=409, detail="emp_id already exists")
   
    telecom_data[employee_id]=profile
 
    return profile
 
 
@app.get("/telecom/profiles")
def get_details():
    return list(telecom_data.values())
 
@app.get("/telecom/profiles/{emp_id}",response_model=EmployeeTelecomProfile)
def get_by_emp_id(emp_id:int):
    if emp_id in telecom_data:
        return telecom_data[emp_id]
    else:
        raise HTTPException(status_code=404, detail= "Profile not found")
 
@app.put("/telecom/profiles/{emp_id}",response_model=EmployeeTelecomProfile)
def update_data(emp_id:int,emp:EmployeeTelecomProfile):
 
    if emp_id not in telecom_data:
        raise HTTPException(status_code=404, detail="no existing profile")
   
    if emp_id !=emp.employee.emp_id:
        raise HTTPException(status_code=400, detail="path id vs body id mismatch")
   
    telecom_data[emp_id]=emp
    return emp
 
@app.delete("/telecom/profiles/{emp_id}")
def delete_emp(emp_id:int):
    if emp_id in telecom_data:
        del telecom_data[emp_id]
        return {"detail": "Profile deleted"}
    else:
        raise HTTPException(status_code=404, detail="profile not found")
   
 
@app.get("/telecom/profiles/search", response_model=List[EmployeeTelecomProfile])
def search_profiles(department: Optional[str] = None, provider: Optional[str] = None):
    results = list(telecom_data.values())
 
    if department:
        results = [p for p in results if p.employee.department == department]
    if provider:
        results = [p for p in results if p.sim.provider == provider]
 
    return results
 
 