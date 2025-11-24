from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel, Field

# Employee data model to represent basic employee details.
class Employee_Basic(BaseModel):
    emp_id: int = Field(..., ge=1000, le=99999, description="Employee ID. Must be a unique integer between 1000 and 99999.")
    name: str = Field(..., min_length=2, description="Full Name of the employee.")
    official_email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@ust\.com$", description="Must be a UST company email (ust.com domain).")
    department: str = Field("Telecom", description="Department where the employee works.")
    location: str = Field("Bengaluru", description="Location of the employee's office.")

# Data model for the employee's sim card details.
class SimCard(BaseModel):
    sim_number: str = Field(..., pattern=r"^\d{10}$", description="10-digit phone number.")
    provider: str = Field("Jio", description="Provider name of the SIM card.")
    is_esim: bool = Field(False, description="Indicates whether the SIM card is an eSIM.")
    activation_year: int = Field(..., ge=2020, le=2025, description="Year of SIM card activation (must be between 2020 and 2025).")

# Data model for the employee's data plan details.
class DataPlan(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Name of the data plan.")
    monthly_gb: int = Field(..., gt=0, le=1000, description="Amount of data (in GB) per month.")
    speed_mbps: int = Field(50, ge=1, le=1000, description="Speed of the data plan in Mbps.")
    is_roaming_included: bool = Field(False, description="Indicates whether roaming is included in the plan.")

# Data model for the employee's voice plan details.
class VoicePlan(BaseModel):
    name: str = Field(..., min_length=3, description="Name of the voice plan.")
    monthly_minutes: int = Field(..., ge=0, le=10000, description="Amount of voice minutes included per month.")
    has_isd: bool = Field(False, description="Indicates whether the plan includes ISD (International dialing).")
    per_minute_charge_paise: int = Field(0, ge=0, le=1000, description="Charge (in paise) per minute for calls.")

# Data model for the employee's emergency contact.
class EmergencyContact(BaseModel):
    name: str = Field(..., min_length=2, description="Name of the emergency contact.")
    relation: str = Field("Family", description="Relation of the emergency contact with the employee.")
    phone: str = Field(..., pattern=r"^[6-9]\d{9}$", description="Phone number of the emergency contact.")

# Main profile data model, combining employee, sim card, data plan, voice plan, and emergency contact.
class EmployeeTelecomProfile(BaseModel):
    employee: Employee_Basic
    sim: SimCard
    data_plan: Optional[DataPlan] = None
    voice_plan: Optional[VoicePlan] = None
    emergency_contact: Optional[EmergencyContact] = None

# FastAPI app initialization with the title of the application.
app = FastAPI(title="UST_Telecom_Management")

# In-memory list to store the profiles. In production, consider using a database.
profiles: List[EmployeeTelecomProfile] = []

# Endpoint to create a new telecom profile for an employee.
@app.post("/telecom/profiles", status_code=201)
def create_employee_profile(profile: EmployeeTelecomProfile):
    # Check if an employee profile with the same emp_id already exists.
    for p in profiles:
        if p.employee.emp_id == profile.employee.emp_id:
            raise HTTPException(status_code=409, detail="Employee id already exists.")
    # Add the new profile to the list.
    profiles.append(profile)
    return profile

# Endpoint to get a list of all employee telecom profiles.
@app.get("/telecom/profiles", status_code=200)
def get_profiles():
    return profiles

# Endpoint to get a specific employee's telecom profile by employee ID.
@app.get("/telecom/profiles/{emp_id}", status_code=200)
def get_employee_by_id(emp_id: int):
    for p in profiles:
        if p.employee.emp_id == emp_id:
            return p
    # If profile is not found, raise an error.
    raise HTTPException(status_code=404, detail="Profile not found")

# Endpoint to update an existing employee profile based on employee ID.
@app.put("/telecom/profiles/{emp_id}", status_code=200)
def update_profile(emp_id: int, new_profile: EmployeeTelecomProfile):
    # Ensure that the path parameter (emp_id) matches the body data's emp_id.
    if new_profile.employee.emp_id != emp_id:
        raise HTTPException(status_code=400, detail="pathid vs bodyid does not match.")
    # Check if the profile exists, then update it.
    for p in profiles:
        if p.employee.emp_id == emp_id:
            profiles.remove(p)
            profiles.append(new_profile)
            return new_profile
    # If profile is not found, raise an error.
    raise HTTPException(status_code=404, detail="No existing profile.")

# Endpoint to delete an employee's telecom profile by employee ID.
@app.delete("/telecom/profiles/{emp_id}", status_code=200)
def delete_profile(emp_id: int):
    for index, p in enumerate(profiles):
        if p.employee.emp_id == emp_id:
            profiles.pop(index)
            return p
    # If profile is not found, raise an error.
    raise HTTPException(status_code=404, detail="Profile not found.")

# Endpoint to search employee profiles based on department and provider.
@app.get("/telecom/profiles/search", status_code=200)
def get_profiles_by_dept_provider(dept: Optional[str] = None, provider: Optional[str] = None):
    result = profiles
    # Filter by department if provided.
    if dept:
        result = [p for p in profiles if p.employee.department == dept]
    # Filter by provider if provided.
    if provider:
        result = [p for p in profiles if p.sim.provider == provider]
    return result


# Sample Output Section:

# Sample POST request to create a new employee profile:
# Request Body:
# {
#   "employee": {
#     "emp_id": 12345,
#     "name": "John Doe",
#     "official_email": "john.doe@ust.com",
#     "department": "Telecom",
#     "location": "Bengaluru"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "provider": "Jio",
#     "is_esim": false,
#     "activation_year": 2023
#   },
#   "data_plan": {
#     "name": "Unlimited 4G",
#     "monthly_gb": 50,
#     "speed_mbps": 100,
#     "is_roaming_included": true
#   },
#   "voice_plan": {
#     "name": "Unlimited Voice",
#     "monthly_minutes": 1000,
#     "has_isd": true,
#     "per_minute_charge_paise": 50
#   },
#   "emergency_contact": {
#     "name": "Jane Doe",
#     "relation": "Spouse",
#     "phone": "9876543211"
#   }
# }

# Sample Response:
# {
#   "employee": {
#     "emp_id": 12345,
#     "name": "John Doe",
#     "official_email": "john.doe@ust.com",
#     "department": "Telecom",
#     "location": "Bengaluru"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "provider": "Jio",
#     "is_esim": false,
#     "activation_year": 2023
#   },
#   "data_plan": {
#     "name": "Unlimited 4G",
#     "monthly_gb": 50,
#     "speed_mbps": 100,
#     "is_roaming_included": true
#   },
#   "voice_plan": {
#     "name": "Unlimited Voice",
#     "monthly_minutes": 1000,
#     "has_isd": true,
#     "per_minute_charge_paise": 50
#   },
#   "emergency_contact": {
#     "name": "Jane Doe",
#     "relation": "Spouse",
#     "phone": "9876543211"
#   }
# }

# Sample GET request to fetch all profiles:
# Response:
# [
#   {
#     "employee": {
#       "emp_id": 12345,
#       "name": "John Doe",
#       "official_email": "john.doe@ust.com",
#       "department": "Telecom",
#       "location": "Bengaluru"
#     },
#     "sim": {
#       "sim_number": "9876543210",
#       "provider": "Jio",
#       "is_esim": false,
#       "activation_year": 2023
#     },
#     "data_plan": {
#       "name": "Unlimited 4G",
#       "monthly_gb": 50,
#       "speed_mbps": 100,
#       "is_roaming_included": true
#     },
#     "voice_plan": {
#       "name": "Unlimited Voice",
#       "monthly_minutes": 1000,
#       "has_isd": true,
#       "per_minute_charge_paise": 50
#     },
#     "emergency_contact": {
#       "name": "Jane Doe",
#       "relation": "Spouse",
#       "phone": "9876543211"
#     }
#   }
# ]
