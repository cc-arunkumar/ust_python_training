# ! Importing Required Libraries
# FastAPI -> framework for building APIs quickly
# HTTPException -> used to raise API errors with status codes
# BaseModel, Field -> Pydantic models for data validation
# Optional -> allows nullable fields
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

# ! FastAPI Application Initialization
# Creating the FastAPI app instance with a custom title
app = FastAPI(title="UST Telecom")

# ! Employee Basic Information Model
class EmployeeBasic(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)
    name: str = Field(..., min_length=2)
    official_email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@ust\.com$")
    department: str = "Telecom"
    location: str = "Bengaluru"

# ! SIM Card Model
class SimCard(BaseModel):
    sim_number: str = Field(..., pattern=r"^\d{10}$")
    provider: str = "Jio"
    is_esim: bool = False
    activation_year: int = Field(..., ge=2020, le=2025)

# ! Data Plan Model
class DataPlan(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    monthly_gb: int = Field(..., gt=0, le=1000)
    speed_mbps: int = Field(50, ge=1, le=1000)
    is_roaming_included: bool = False

# ! Voice Plan Model
class VoicePlan(BaseModel):
    name: str = Field(..., min_length=3)
    monthly_minutes: int = Field(..., ge=0, le=10000)
    has_isd: bool = False
    per_minute_charge_paise: int = Field(0, ge=0, le=1000)

# ! Emergency Contact Model
class EmergencyContact(BaseModel):
    name: str = Field(..., min_length=2)
    relation: str = "Family"
    phone: str = Field(..., pattern=r"^[6-9]\d{9}$")

# ! Employee Telecom Profile Model
class EmployeeTelecomProfile(BaseModel):
    employee: EmployeeBasic
    sim: SimCard
    data_plan: Optional[DataPlan] = None
    voice_plan: Optional[VoicePlan] = None
    emergency_contact: Optional[EmergencyContact] = None

# ! In-Memory Storage
profiles = []

# ! Create Profile Endpoint (POST)
@app.post("/telecom/profiles", response_model=EmployeeTelecomProfile, status_code=201)
def create_profile(profile: EmployeeTelecomProfile):
    for p in profiles:
        if p.employee.emp_id == profile.employee.emp_id:
            raise HTTPException(409, "Profile already exists")
    profiles.append(profile)
    return profile

# ! Get All Profiles Endpoint (GET)
@app.get("/telecom/profiles", response_model=list[EmployeeTelecomProfile])
def get_all():
    return profiles

# ! Get One Profile by ID Endpoint (GET)
@app.get("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def get_one(emp_id: int):
    for p in profiles:
        if p.employee.emp_id == emp_id:
            return p
    raise HTTPException(404, "Profile not found")

# ! Update Profile Endpoint (PUT)
@app.put("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def update_profile(emp_id: int, profile: EmployeeTelecomProfile):
    # Ensure path ID matches body ID
    if emp_id != profile.employee.emp_id:
        raise HTTPException(400, "ID mismatch")
    for i, p in enumerate(profiles):
        if p.employee.emp_id == emp_id:
            profiles[i] = profile
            return profile
    raise HTTPException(404, "Profile not found")

# ! Delete Profile Endpoint (DELETE)
@app.delete("/telecom/profiles/{emp_id}")
def delete_one(emp_id: int):
    for p in profiles:
        if p.employee.emp_id == emp_id:
            profiles.remove(p)
            return {"detail": "Profile deleted"}
    raise HTTPException(404, "Profile not found")

# ! Search Profiles Endpoint (GET)
@app.get("/telecom/profiles/search", response_model=list[EmployeeTelecomProfile])
def search(department: Optional[str] = None, provider: Optional[str] = None):
    result = profiles
    if department:
        result = [p for p in result if p.employee.department.lower() == department.lower()]
    if provider:
        result = [p for p in result if p.sim.provider.lower() == provider.lower()]
    return result


"""SAMPLE OUTPUT
1. Get All
[
  {
    "employee": {
      "emp_id": 1000,
      "name": "string",
      "official_email": "hhhKFqb%CXa5uXbJhoJiQM25cy06ePb8B1VSY4P7I3zraO.ZaImaKMrjWh7xo5MrkEy8toHOzZMc3DAYjvlmAyhW_ZFxb5UCh__b0@ust.com",
      "department": "Telecom",
      "location": "Bengaluru"
    },
    "sim": {
      "sim_number": "3444508306",
      "provider": "Jio",
      "is_esim": false,
      "activation_year": 2020
    },
    "data_plan": {
      "name": "string",
      "monthly_gb": 1,
      "speed_mbps": 50,
      "is_roaming_included": false
    },
    "voice_plan": {
      "name": "string",
      "monthly_minutes": 10000,
      "has_isd": false,
      "per_minute_charge_paise": 0
    },
    "emergency_contact": {
      "name": "string",
      "relation": "Family",
      "phone": "8368593814"
    }
  }
]

2. Create Profile
{
  "employee": {
    "emp_id": 1001,
    "name": "Gowtham",
    "official_email": "gowtham@ust.com",
    "department": "Telecom",
    "location": "Trivandrum"
  },
  "sim": {
    "sim_number": "1234567890",
    "provider": "Jio",
    "is_esim": false,
    "activation_year": 2023
  },
  "data_plan": {
    "name": "Yearly",
    "monthly_gb": 1,
    "speed_mbps": 50,
    "is_roaming_included": false
  },
  "voice_plan": {
    "name": "string",
    "monthly_minutes": 10000,
    "has_isd": false,
    "per_minute_charge_paise": 0
  },
  "emergency_contact": {
    "name": "string",
    "relation": "Family",
    "phone": "8277052853"
  }
}

3. Get BY ID
{
  "employee": {
    "emp_id": 1000,
    "name": "string",
    "official_email": "h-4@ust.com",
    "department": "Telecom",
    "location": "Bengaluru"
  },
  "sim": {
    "sim_number": "8760714111",
    "provider": "Jio",
    "is_esim": false,
    "activation_year": 2020
  },
  "data_plan": {
    "name": "string",
    "monthly_gb": 1,
    "speed_mbps": 50,
    "is_roaming_included": false
  },
  "voice_plan": {
    "name": "string",
    "monthly_minutes": 10000,
    "has_isd": false,
    "per_minute_charge_paise": 0
  },
  "emergency_contact": {
    "name": "string",
    "relation": "Family",
    "phone": "9863722826"
  }
}

4. Update

{
  "employee": {
    "emp_id": 3000,
    "name": "Varun",
    "official_email": "IAH4LS1D5sqUeI7CirWTOJjeZffFjtbeF.LwVznni31H3JFi2ELsJ6LV3ItJgB8tN59T0mVm+0eQ9c0UR0Z30O@ust.com",
    "department": "Telecom",
    "location": "Bengaluru"
  },
  "sim": {
    "sim_number": "7199239584",
    "provider": "Jio",
    "is_esim": false,
    "activation_year": 2020
  },
  "data_plan": {
    "name": "string",
    "monthly_gb": 1,
    "speed_mbps": 50,
    "is_roaming_included": false
  },
  "voice_plan": {
    "name": "string",
    "monthly_minutes": 10000,
    "has_isd": false,
    "per_minute_charge_paise": 0
  },
  "emergency_contact": {
    "name": "string",
    "relation": "Family",
    "phone": "6882547507"
  }
}
5. Delete 

Code	Description	
200	 Successful Response



6. SEARCH by Department
[
  {
    "employee": {
      "emp_id": 1000,
      "name": "string",
      "official_email": "HW3ZWAjfk-98s%ahm_M%7k%RmZs-Z+9.u3oWgGjjLI1MJ9rkz47G0H85t_VtcQGonouB@ust.com",
      "department": "Telecom",
      "location": "Bengaluru"
    },
    "sim": {
      "sim_number": "2153173302",
      "provider": "Jio",
      "is_esim": false,
      "activation_year": 2020
    },
    "data_plan": {
      "name": "string",
      "monthly_gb": 1,
      "speed_mbps": 50,
      "is_roaming_included": false
    },
    "voice_plan": {
      "name": "string",
      "monthly_minutes": 10000,
      "has_isd": false,
      "per_minute_charge_paise": 0
    },
    "emergency_contact": {
      "name": "string",
      "relation": "Family",
      "phone": "8875349454"
    }
  }
]

"""