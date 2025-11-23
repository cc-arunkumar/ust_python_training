from pydantic import BaseModel, Field
from typing import Optional,List
from fastapi import FastAPI,HTTPException

app = FastAPI(title="UST Employee Operation")






class EmployeeBasic(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)  
    name: str = Field(..., min_length=2)           
    department: str = "General"  

# e = EmployeeBasic(emp_id=1234, name="Asha", department="Information Technology")
# print(e)

class SIMCard(BaseModel):
    number: str = Field(..., pattern=r"^\d{10}$") 
    provider: str = Field(default="Jio")           
    activation_year: int = Field(..., ge=2020, le=2025) 
    
class DataPlan(BaseModel):
    name : str = Field(...,min_length=3,max_length=50)
    monthly_gb : int = Field(...,gt=0,le=1000)
    speed_mbps : int = Field(deafault=50,ge=1,le=1000)
    is_roaming_included: bool = (False)

class VoicePlan(BaseModel):
    name : str = Field(...,min_length=3)
    monthly_minuited : int = Field(...,ge=0,le=1000)
    has_isb : bool = Field(default=False)
    per_minute_charge_paise : int = Field(default=0,ge=0,le=1000)
    
class EmergencyContact(BaseModel):
    name : str = Field(...,min_length=2)
    relation : str = Field(default="Family")
    phone : str = Field(pattern="^[6-9]\d{9}$")
    
class EmployeeTelecomProfile(BaseModel):
    employee :  EmployeeBasic= (...)
    sim : SIMCard = (...)
    data_plan : Optional[DataPlan]= Field(default=None)
    voice_plan : Optional[VoicePlan] = Field(default=None)
    Emergency_contact : Optional[EmergencyContact] = Field(default=None)
    
    
profiles: List[EmployeeTelecomProfile]=[]
# class Registration(BaseModel):
#     employee: EmployeeBasic
#     sim: SIMCard

data = {
    "employee": {
        "emp_id": 12345,
        "name": "Asha",
        "department": "Engineering"
    },
    "sim": {
        "number": "9876543210",
        "provider": "Airtel",
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
@app.post("/telecom/profile",status_code=409)
def create_telecom(profile: EmployeeTelecomProfile):
    for check in profiles:
        if check.employee.emp_id==profile.employee.id:
            raise HTTPException(detail="Employee with this id already exits")
    profiles.append(profile)
    return profiles

@app.get("/telecom/profiles")
def all_telecom_employees():
    return profiles

@app.get("/telecom/profiles/{emp_id}")
def get_by_id(emp_id : int):
    for check in profiles:
        if check.employee.emp_id == emp_id:
            return check
    raise HTTPException(status_code=404,detail="profile not found")

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

@app.delete("/telecom/profiles/{emp_id}")
def delete_by_employee_id(emp_id: int):
    for c in profiles:
        if c.employee.emp_id==emp_id:
            profiles.remove(c)
            return {"detail": "profile deleted"}
        
    raise HTTPException(status_code=404,detail="Profile not found")

@app.get("/telecom/profiles/search")
def profiles_search(department:Optional[str]=None,provider: Optional[str]=None):
    result=profiles
    if department:
        result= [p for p in result if p.employee.department==department]
    if provider:
        result=[p for p in result if p.sim.provider==provider]
    return result