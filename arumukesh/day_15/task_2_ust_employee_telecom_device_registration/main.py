from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field, field_validator
from typing import Optional
import re

app = FastAPI(title="UST Employee Telecom Device Registration")

"""
Pydantic Models Section
"""


# -------------------- Employee Model --------------------
class EmployeeModel(BaseModel):
    # Employee ID: must be a number between 1000 and 999999
    emp_id: int = Field(..., ge=1000, le=999999, description="ID must be between 1000 and 999999")

    # Name: minimum length 2 characters
    name: str = Field(..., min_length=2, description="Name length should be minimum 2")

    # Official email: validated using custom regex validator below
    official_email: str

    # Optional fields with default values
    department: Optional[str] = Field(default="Telecom")
    location: Optional[str] = Field(default="Bamgaluru")

    # Custom email validator for ust.com domain
    @field_validator('official_email')
    @classmethod
    def email_regex(cls, v):
        if not re.match(r'^[a-zA-Z0-9._%+-]+@ust\.com$', v):
            raise ValueError("Email must belong to ust.com domain")
        return v


# -------------------- SIM Model --------------------
class SimModel(BaseModel):
    number: str = Field(..., max_length=10, min_length=10, description="Invalid phone number")
    provider: Optional[str] = Field(default="Jio")
    is_esim: Optional[bool] = Field(default=False)

    # Activation year must be within valid range
    activation_year: int = Field(..., ge=2020, le=2025, description="Invalid activation year")


# -------------------- Data Plan Model --------------------
class DataPlan(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Name length 3–50")
    monthly_gb: int = Field(..., gt=0, le=1000, description="Monthly GB must be between 1 and 1000")
    speed_mbps: Optional[int] = Field(default=50, ge=1, le=1000)
    is_roaming_included: Optional[bool] = Field(default=False)


# -------------------- Voice Plan Model --------------------
class VoicePlan(BaseModel):
    name: str = Field(..., min_length=3, description="Name length minimum 3")
    monthly_minutes: int = Field(..., ge=0, le=1000, description="Monthly minutes 0–1000")
    has_isd: Optional[bool] = Field(default=False)
    per_minute_charge_paise: Optional[int] = Field(default=0, ge=0, le=1000)


# -------------------- Emergency Contact Model --------------------
class EmergencyContact(BaseModel):
    name: str = Field(..., min_length=2)
    relation: str = Field(default="Family")

    # Phone must start with 6–9 and be 10 digits, corrected regex
    phone: str = Field(..., pattern=r"^[6-9]\d{9}$", description="Invalid phone number")

    per_minute_charge_paise: Optional[int] = Field(default=0, ge=0, le=1000)


# -------------------- Composite Model --------------------
class EmployeeTelecomProfile(BaseModel):
    # Mandatory nested models
    employee: EmployeeModel = Field(..., description="Employee details required")
    sim: SimModel = Field(..., description="SIM details required")

    # Optional plans and contacts
    data_plan: Optional[DataPlan]
    voice_plan: Optional[VoicePlan]
    emergency_contact: Optional[EmergencyContact]



# Temporary storage for employee profiles
data = []


"""
API Endpoints Section
"""


# -------------------- Create New Profile --------------------
@app.post("/telecom/profiles")
def profile(employees: EmployeeTelecomProfile):
    """
    Add a new employee telecom profile.
    Ensures employee ID is unique.
    """
    for i in data:
        if employees.employee.emp_id == i.employee.emp_id:
            raise HTTPException(status_code=409, detail="Employee ID already exists")

    data.append(employees)
    return {"Employee added successfully": employees.__dict__}




# -------------------- List All Profiles --------------------
@app.get("/telecom/profiles")
def list_of_profiles():
    """
    Returns all saved telecom profiles.
    """
    return data


# -------------------- Get Profile By ID --------------------
@app.get("/telecom/profiles/{id}")
def profile_by_id(id: int):
    """
    Fetch a profile using employee ID.
    """
    for i in data:
        if i.employee.emp_id == id:
            return i

    raise HTTPException(status_code=404, detail="Profile not found")


# -------------------- Update Profile --------------------
@app.put("/telecom/profiles/{emp_id}")
def update_profile(emp_id: int, profile_data: EmployeeTelecomProfile):
    """
    Update the entire profile of an employee.
    """
    for i in range(len(data)):
        if data[i].employee.emp_id == emp_id:
            data[i] = profile_data
            return {"Employee updated": profile_data}

    raise HTTPException(status_code=404, detail="No data found")


# -------------------- Delete Profile --------------------
@app.delete("/telecom/profiles/{emp_id}")
def delete_profile(emp_id: int):
    """
    Delete an employee's telecom profile using employee ID.
    """
    for i in range(len(data)):
        if data[i].employee.emp_id == emp_id:
            return {"Profile deleted": data.pop(i)}

    raise HTTPException(status_code=404, detail="No data found")


# -------------------- Filter By Department or Provider --------------------
@app.get("/telecom/profiles_search")
async def filter_by_department_and_provider(
    department: Optional[str] = Query(None),
    provider: Optional[str] = Query(None)
):
    """
    Filter profiles by:
    - department
    - SIM provider
    - both
    """
    emp = []

    # Filter for both department and provider
    if department and provider:
        for i in data:
            if i.employee.department == department and i.sim.provider == provider:
                emp.append(i)

    # Filter only by department
    elif department:
        for i in data:
            if i.employee.department == department:
                emp.append(i)

    # Filter only by provider
    elif provider:
        for i in data:
            if i.sim.provider == provider:
                emp.append(i)

    # If no filters provided → return all data
    else:
        return data

    # Return matched records or error
    if emp:
        return emp

    raise HTTPException(status_code=404, detail="No data found")


# =========outputs==============
    # """
#     Add a new employee telecom profile.
#     Ensures employee ID is unique.
    
#     Sample Input:
#     {
#         "employee": {
#             "emp_id": 1001,
#             "name": "John Doe",
#             "official_email": "john.doe@ust.com",
#             "department": "Engineering",
#             "location": "Bangalore"
#         },
#         "sim": {
#             "number": "9876543210",
#             "provider": "Airtel",
#             "is_esim": false,
#             "activation_year": 2023
#         },
#         "data_plan": {
#             "name": "Unlimited Data",
#             "monthly_gb": 100,
#             "speed_mbps": 100,
#             "is_roaming_included": true
#         },
#         "voice_plan": {
#             "name": "Unlimited Voice",
#             "monthly_minutes": 500,
#             "has_isd": true,
#             "per_minute_charge_paise": 100
#         },
#         "emergency_contact": {
#             "name": "Jane Doe",
#             "relation": "Spouse",
#             "phone": "9876543210",
#             "per_minute_charge_paise": 50
#         }
#     }

#     Sample Output:
#     {
#         "Employee added successfully": {
#             "employee": {
#                 "emp_id": 1001,
#                 "name": "John Doe",
#                 "official_email": "john.doe@ust.com",
#                 "department": "Engineering",
#                 "location": "Bangalore"
#             },
#             "sim": {
#                 "number": "9876543210",
#                 "provider": "Airtel",
#                 "is_esim": false,
#                 "activation_year": 2023
#             },
#             "data_plan": {
#                 "name": "Unlimited Data",
#                 "monthly_gb": 100,
#                 "speed_mbps": 100,
#                 "is_roaming_included": true
#             },
#             "voice_plan": {
#                 "name": "Unlimited Voice",
#                 "monthly_minutes": 500,
#                 "has_isd": true,
#                 "per_minute_charge_paise": 100
#             },
#             "emergency_contact": {
#                 "name": "Jane Doe",
#                 "relation": "Spouse",
#                 "phone": "9876543210",
#                 "per_minute_charge_paise": 50
#             }
#         }
#     }
#     """
#     for i in data:
#         if employees.employee.emp_id == i.employee.emp_id:
#             raise HTTPException(status_code=409, detail="Employee ID already exists")

#     data.append(employees)
#     return {"Employee added successfully": employees.dict()}


# # -------------------- List All Profiles --------------------

#     Returns all saved telecom profiles.
    
#     Sample Output:
#     [
#         {
#             "employee": {
#                 "emp_id": 1001,
#                 "name": "John Doe",
#                 "official_email": "john.doe@ust.com",
#                 "department": "Engineering",
#                 "location": "Bangalore"
#             },
#             "sim": {
#                 "number": "9876543210",
#                 "provider": "Airtel",
#                 "is_esim": false,
#                 "activation_year": 2023
#             },
#             "data_plan": {
#                 "name": "Unlimited Data",
#                 "monthly_gb": 100,
#                 "speed_mbps": 100,
#                 "is_roaming_included": true
#             },
#             "voice_plan": {
#                 "name": "Unlimited Voice",
#                 "monthly_minutes": 500,
#                 "has_isd": true,
#                 "per_minute_charge_paise": 100
#             },
#             "emergency_contact": {
#                 "name": "Jane Doe",
#                 "relation": "Spouse",
#                 "phone": "9876543210",
#                 "per_minute_charge_paise": 50
#             }
#         }
#     ]
#     """
#     return data


# # -------------------- Get Profile By ID --------------------
# @app.get("/telecom/profiles/{id}")
# def profile_by_id(id: int):
#     """
#     Fetch a profile using employee ID.
    
#     Sample Input: /telecom/profiles/1001
    
#     Sample Output (for emp_id 1001):
#     {
#         "employee": {
#             "emp_id": 1001,
#             "name": "John Doe",
#             "official_email": "john.doe@ust.com",
#             "department": "Engineering",
#             "location": "Bangalore"
#         },
#         "sim": {
#             "number": "9876543210",
#             "provider": "Airtel",
#             "is_esim": false,
#             "activation_year": 2023
#         },
#         "data_plan": {
#             "name": "Unlimited Data",
#             "monthly_gb": 100,
#             "speed_mbps": 100,
#             "is_roaming_included": true
#         },
#         "voice_plan": {
#             "name": "Unlimited Voice",
#             "monthly_minutes": 500,
#             "has_isd": true,
#             "per_minute_charge_paise": 100
#         },
#         "emergency_contact": {
#             "name": "Jane Doe",
#             "relation": "Spouse",
#             "phone": "9876543210",
#             "per_minute_charge_paise": 50
#         }
#     }
    
#     If the employee ID is not found:
#     Sample Output:
#     {
#         "detail": "Profile not found"
#     }
#     """