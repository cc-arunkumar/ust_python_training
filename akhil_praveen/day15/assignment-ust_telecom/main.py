from typing import List,Optional
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
import re

app = FastAPI(title="Ust Employee Telecom Management")

class EmployeeBasic(BaseModel):
    emp_id : int = Field(...,ge=1000,le=999999,description="Employee id should be in between 1000 and 999999")
    name : str = Field(...,min_length=2,description="Length must be greater than or equal to 2")
    official_email : str = Field(...,pattern=r'^[a-zA-Z0-9._%+-]+@ust\.com$',description="Must match the pattern")
    department : Optional[str] = Field("General")
    location : Optional[str] = Field("Bangaluru")
    
class SimCard(BaseModel):
    sim_number : str = Field(...,pattern = r"^\d{10}$",description="Length should be exactly 10")
    provider : Optional[str] = Field("Jio")
    is_esim : Optional[bool] = Field("False") 
    activation_year : int = Field(...,ge=2020,le=2025,description="Employee id should be in between 2020 and 2025")
    
class DataPlan(BaseModel):
    name : str = Field(...,min_length=3,max_length=50,description="Name should be in between 3 and 50 inclusive")
    monthly_gb : int = Field(...,gt=0,le=5000,description="Data volume should be less than 5000gb")
    speed_mbps :  Optional[int] = Field(...,50,ge=1,le=1000,description="Speed in mps should be less than 1000")
    is_roaming_included : Optional[bool] = Field("False")
    
class VoicePlan(BaseModel):
    name : str = Field(...,min_length=3,description="Length must be greater than or equal to 3")
    monthly_minutes : int = Field(...,ge=0,le=10000,description="Minutes should in between 0 and 10000")
    has_isd : Optional[bool] = Field("False")
    per_minute_charge_paise :  Optional[int] = Field(...,50,ge=1,le=1000,description="charge should be less than 1000")
    
class EmergencyContact(BaseModel):
    name : str = Field(...,min_length=2,description="Length must be greater than or equal to 2")
    relation : Optional[str] = Field("Family")
    phone : str = Field(...,pattern = r"^[6-9]\d{9}$",description="Phone is not valid")
    
class EmployeeTelecomProfile(BaseModel):
    employee : EmployeeBasic
    sim : SimCard
    data_plan : DataPlan
    voice_plan : VoicePlan
    emergency_contact : EmergencyContact
    
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
 }
 }

@app.post("/telecom/profiles")
def create_telecom_profile()