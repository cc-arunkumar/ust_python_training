from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import re

app = FastAPI(title="Ust Employee Telecom Management")

# Define Employee data structure
class EmployeeBasic(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999, description="Employee id should be between 1000 and 999999")
    name: str = Field(..., min_length=2, description="Name must be at least 2 characters long")
    official_email: str = Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@ust\.com$', description="Must match ust.com email pattern")
    department: Optional[str] = Field("General")  # Default value is "General"
    location: Optional[str] = Field("Bangaluru")  # Default location "Bangaluru"

# Define SimCard details
class SimCard(BaseModel):
    sim_number: str = Field(..., pattern=r"^\d{10}$", description="SIM number must be 10 digits")
    provider: Optional[str] = Field("Jio")  # Default provider "Jio"
    is_esim: Optional[bool] = Field("False")  # Default value is False, though it should be a boolean
    activation_year: int = Field(..., ge=2020, le=2025, description="Activation year should be between 2020 and 2025")

# Define Data Plan details
class DataPlan(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Data plan name must be between 3 and 50 characters")
    monthly_gb: int = Field(..., gt=0, le=5000, description="Data volume must be between 1GB and 5000GB")
    speed_mbps: Optional[int] = Field(50, ge=1, le=1000, description="Speed must be between 1 Mbps and 1000 Mbps")
    is_roaming_included: Optional[bool] = Field("False")  # Default value is False

# Define Voice Plan details
class VoicePlan(BaseModel):
    name: str = Field(..., min_length=3, description="Voice plan name must be at least 3 characters long")
    monthly_minutes: int = Field(..., ge=0, le=10000, description="Monthly minutes must be between 0 and 10,000")
    has_isd: Optional[bool] = Field("False")  # Default is False for ISD availability
    per_minute_charge_paise: Optional[int] = Field(50, ge=1, le=1000, description="Charge per minute in paise (1 to 1000 paise)")

# Define Emergency Contact details
class EmergencyContact(BaseModel):
    name: str = Field(..., min_length=2, description="Emergency contact name must be at least 2 characters long")
    relation: Optional[str] = Field("Family")  # Default relation is "Family"
    phone: str = Field(..., pattern=r"^[6-9]\d{9}$", description="Phone number must be valid (starts with 6-9 and 10 digits total)")

# Employee telecom profile including all data points
class EmployeeTelecomProfile(BaseModel):
    employee: EmployeeBasic
    sim: SimCard
    data_plan: Optional[DataPlan] = None  # Data plan is optional
    voice_plan: Optional[VoicePlan] = None  # Voice plan is optional
    emergency_contact: Optional[EmergencyContact] = None  # Emergency contact is optional

# Initialize empty lists for storing profiles and employee IDs
data_storage = []
emp_id_list = []

# Route to create a new telecom profile for an employee
@app.post("/telecom/profiles")
def create_telecom_profile(tele_profile: EmployeeTelecomProfile):
    # Check if the employee ID already exists
    if tele_profile.employee.emp_id in emp_id_list:
        raise HTTPException(status_code=409, detail="Employee id already exists")
    # Add profile to storage and track employee ID
    data_storage.append(tele_profile)
    emp_id_list.append(tele_profile.employee.emp_id)
    return tele_profile

# Route to get all telecom profiles
@app.get("/telecom/profiles")
def get_all_profiles():
    return data_storage

# Route to get a telecom profile by employee ID
@app.get("/telecom/profiles/{id}")
def get_profiles_by_id(id: int):
    # Check if employee ID exists
    if id not in emp_id_list:
        raise HTTPException(status_code=404, detail="Profile Not Found")
    # Search for profile matching the ID
    for profile in data_storage:
        if profile.employee.emp_id == id:
            return profile

# Route to update an existing telecom profile by employee ID
@app.put("/telecom/profiles/{id}")
def update_profile(id: int, new_tele_profile: EmployeeTelecomProfile):
    # Check if employee exists
    if id not in emp_id_list:
        raise HTTPException(status_code=409, detail="Employee doesn't exist")
    # Ensure employee ID in profile matches the ID being updated
    for profile in data_storage:
        if profile.employee.emp_id == id:
            if profile.employee.emp_id != new_tele_profile.employee.emp_id:
                raise HTTPException(status_code=400, detail="Employee ID can't be changed!")
            # Update profile details
            profile.employee = new_tele_profile.employee
            profile.sim = new_tele_profile.sim
            profile.data_plan = new_tele_profile.data_plan
            profile.voice_plan = new_tele_profile.voice_plan
            profile.emergency_contact = new_tele_profile.emergency_contact
            return profile

# Route to delete a telecom profile by employee ID
@app.delete("/telecom/profiles/{id}")
def delete_profile(id: int):
    # Check if employee ID exists
    if id not in emp_id_list:
        raise HTTPException(status_code=404, detail="Profile Not Found")
    # Find and remove the profile
    for i in range(len(data_storage)):
        if data_storage[i].employee.emp_id == id:
            removed = data_storage.pop(i)
            emp_id_list.remove(id)
            return removed

# Route to search profiles by department or provider
@app.get("/telecom/search")
def search_dept_or_provider(dept: Optional[str] = None, provider: Optional[str] = None):
    # If no search criteria are provided, return all profiles
    if not (dept or provider):
        return get_all_profiles()

    # Temporary list to hold search results and to avoid duplicate profiles
    temp_list = []
    dupli_id = []
    
    # Search by provider if specified
    if provider:
        for profile in data_storage:
            if profile.sim.provider == provider:
                temp_list.append(profile)
                dupli_id.append(profile.employee.emp_id)

    # Search by department if specified
    if dept:
        for profile in data_storage:
            if profile.employee.department == dept and profile.employee.emp_id not in dupli_id:
                temp_list.append(profile)
                dupli_id.append(profile.employee.emp_id)

    # If no results, raise an error
    if not temp_list:
        raise HTTPException(status_code=404, detail="No profiles found!")
    
    return temp_list
