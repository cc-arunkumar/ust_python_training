from fastapi import FastAPI,HTTPException,Query
from pydantic import BaseModel,Field
from typing import Optional,List

sample_data={
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

class EmployeeBasic(BaseModel):
    emp_id:int=Field(...,ge=1000,le=999999,description="Employee numeric ID")
    name:str=Field(...,min_length=2,description="Give the valid full name")
    official_email:str=Field(...,pattern=r"^[a-zA-Z0-9._%+-]+@ust\.com$",description="UST email address only")
    department:str=Field(default="Telecom",description="Department name")
    location:str=Field(default="Bangaluru",description="location name")
    
class SimCard(BaseModel):
    sim_number:str=Field(...,pattern=r"^\d{10}$",description="give the valid 10 digit number")
    provider:str=Field(default="Jio",description="Provider name")
    is_esim:bool=Field(default=False,description="esim")
    activation_year:int=Field(...,ge=2020,l2=2025,description="year of activation")

class DataPlan(BaseModel):
    name:str=Field(...,min_length=3,max_length=50,description="name of the plan")
    monthly_gb:int=Field(...,gt=0,le=1000,description="data plan in GB")
    speed_mbps:int=Field(default=50,ge=1,le=1000,description="data Speed in mbps")
    is_roaming_include:bool=Field(default=False,description="roaming include flag")

class VoicePlan(BaseModel):
    name:str=Field(...,min_length=3,description="name of the plan")
    monthly_minutes:int=Field(...,ge=0,le=10000,description="allowed minutes per month")
    has_isd:bool=Field(default=False,description="ISD enabled")
    per_minute_charge_paise:int=Field(default=0,ge=0,le=1000,description="per minutes charge in paise")
    
class EmergencyContact(BaseModel):
    name: str = Field(..., min_length=2, description="Contact name")
    relation: str = Field(default="Family", description="Relationship")
    phone: str = Field(..., pattern=r"^[6-9]\d{9}$",description="Indian mobile number starting with 6 or 9")


class EmployeeTelecomProfile(BaseModel):
    employee: EmployeeBasic
    sim: SimCard
    data_plan: Optional[DataPlan] = None
    voice_plan: Optional[VoicePlan] = None
    emergency_contact: Optional[EmergencyContact] = None


app = FastAPI(title="UST Employee Telecom Management API")

# In-memory storage
telecom_profiles: List[EmployeeTelecomProfile] = []
@app.post("/telecom/profiles",response_model=EmployeeTelecomProfile,status_code=201)
async def create_telecom_profile(profile: EmployeeTelecomProfile):
    # Check if profile already exists
    for existing_profile in telecom_profiles:
        if existing_profile.employee.emp_id == profile.employee.emp_id:
            raise HTTPException(
                status_code=409,
                detail=f"Profile with emp_id {profile.employee.emp_id} already exists"
            )
    # Add to storage
    telecom_profiles.append(profile)
    return profile


@app.get("/telecom/profiles",response_model=List[EmployeeTelecomProfile])
async def list_all_profiles():
    return telecom_profiles


@app.get("/telecom/profiles/{emp_id}",response_model=EmployeeTelecomProfile)
async def get_profile_by_id(emp_id: int):
    for profile in telecom_profiles:
        if profile.employee.emp_id == emp_id:
            return profile
    raise HTTPException(
        status_code=404,
        detail="Profile not found"
    )


@app.put("/telecom/profiles/{emp_id}",response_model=EmployeeTelecomProfile)
async def update_telecom_profile(emp_id: int, profile: EmployeeTelecomProfile):
    
    # Validate emp_id consistency
    if profile.employee.emp_id != emp_id:
        raise HTTPException(
            status_code=400,
            detail="Employee ID in path does not match employee ID in request body"
        )
    
    # Check if profile exists and update
    for idx, existing_profile in enumerate(telecom_profiles):
        if existing_profile.employee.emp_id == emp_id:
            telecom_profiles[idx] = profile
            return profile
    raise HTTPException(
        status_code=404,
        detail="Profile not found"
    )


@app.delete("/telecom/profiles/{emp_id}")
async def delete_profile(emp_id: int):
    for idx, profile in enumerate(telecom_profiles):
        if profile.employee.emp_id == emp_id:
            telecom_profiles.pop(idx)
            return {"detail": "Profile deleted"}
    
    raise HTTPException(
        status_code=404,
        detail="Profile not found"
    )


@app.get("/telecom/profiles/search",response_model=List[EmployeeTelecomProfile])
async def search_profiles(
    department: Optional[str] = Query(None, description="Filter by department"),
    provider: Optional[str] = Query(None, description="Filter by SIM provider")
):
    
    results = telecom_profiles
    # Filter by department if provided
    if department:
        results = [p for p in results if p.employee.department == department]
    
    # Filter by provider if provided
    if provider:
        results = [p for p in results if p.sim.provider == provider]
    return results
    
      