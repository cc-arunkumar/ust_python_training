from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional, List

# -----------------------------
# FastAPI Application
# -----------------------------
app = FastAPI(title="UST Employee Telecom Management")

# -----------------------------
# Pydantic Model Schemas
# -----------------------------

class EmployeeBasic(BaseModel):
    """
    Basic employee details schema:
    - emp_id: must be between 1000 and 999999
    - name: minimum 2 characters
    - official_email: must match format name@ust.com
    - department: optional, defaults to "Telecom"
    - location: optional, defaults to "Bengaluru"
    """
    emp_id: int = Field(..., ge=1000, le=999999, description="Employee ID must be between 1000 and 999999")
    name: str = Field(..., min_length=2, description="Employee name must have at least 2 characters")
    official_email: str = Field(
        ..., 
        pattern=r"^[a-zA-Z0-9._%+-]+@ust\.com$", 
        description="Email must follow the format: name@ust.com"
    )
    department: Optional[str] = Field("Telecom", description="Employee department")
    location: Optional[str] = Field("Bengaluru", description="Employee location")


class SimCard(BaseModel):
    """
    SIM card schema:
    - sim_number: must be 10 digits
    - provider: optional, defaults to "Jio"
    - is_esim: optional, defaults to False
    - activation_year: must be between 2020 and 2025
    """
    sim_number: str = Field(..., pattern=r"^\d{10}$", description="SIM number must be a 10-digit number")
    provider: Optional[str] = Field("Jio", description="Network provider name")
    is_esim: Optional[bool] = Field(False, description="Whether SIM is eSIM")
    activation_year: int = Field(..., ge=2020, le=2025, description="Activation year must be between 2020 and 2025")


class DataPlan(BaseModel):
    """
    Data plan schema:
    - name: plan name (3–50 chars)
    - monthly_gb: monthly data limit (1–1000 GB)
    - speed_mbps: optional, defaults to 50 Mbps
    - is_roaming_included: optional, defaults to False
    """
    name: str = Field(..., min_length=3, max_length=50, description="Data plan name")
    monthly_gb: int = Field(..., gt=0, le=1000, description="Monthly data limit in GB")
    speed_mbps: Optional[int] = Field(50, ge=1, le=1000, description="Internet speed in Mbps")
    is_roaming_included: Optional[bool] = Field(False, description="Roaming included or not")


class VoicePlan(BaseModel):
    """
    Voice plan schema:
    - name: plan name (min 3 chars)
    - monthly_minutes: 0–10000 minutes
    - has_isd: optional, defaults to False
    - per_minute_charge_paise: optional, defaults to 0
    """
    name: str = Field(..., min_length=3, description="Voice plan name")
    monthly_minutes: int = Field(..., ge=0, le=10000, description="Monthly voice minutes")
    has_isd: Optional[bool] = Field(False, description="ISD facility included or not")
    per_minute_charge_paise: Optional[int] = Field(0, ge=0, le=1000, description="Charge per minute in paise")


class EmergencyContact(BaseModel):
    """
    Emergency contact schema:
    - name: minimum 2 characters
    - relation: optional, defaults to "Family"
    - phone: must be 10 digits starting with 6–9
    """
    name: str = Field(..., min_length=2, description="Emergency contact name")
    relation: Optional[str] = Field("Family", description="Relation with employee")
    phone: str = Field(..., pattern=r"^[6-9]\d{9}$", description="10-digit phone number starting with 6–9")


class EmployeeTelecomProfile(BaseModel):
    """
    Composite schema for employee telecom profile:
    - employee: EmployeeBasic
    - sim: SimCard
    - data_plan: optional DataPlan
    - voice_plan: optional VoicePlan
    - emergency_contact: optional EmergencyContact
    """
    employee: EmployeeBasic = Field(..., description="Employee full basic details")
    sim: SimCard = Field(..., description="SIM card details")
    data_plan: Optional[DataPlan] = Field(None, description="Assigned data plan")
    voice_plan: Optional[VoicePlan] = Field(None, description="Assigned voice plan")
    emergency_contact: Optional[EmergencyContact] = Field(None, description="Emergency contact details")


# -----------------------------
# In-Memory Database
# -----------------------------
employee_tele_li: List[EmployeeTelecomProfile] = []


# -----------------------------
# CRUD API Endpoints
# -----------------------------

@app.post("/telecom/profiles", response_model=EmployeeTelecomProfile)
def create(new_telecom: EmployeeTelecomProfile):
    """
    Create a new telecom profile.
    Prevents duplicate employee IDs.

    Sample Output:
    POST /telecom/profiles
    Request:
    {
      "employee": {"emp_id":1234,"name":"Ravi","official_email":"ravi@ust.com","department":"Telecom","location":"Bengaluru"},
      "sim": {"sim_number":"9876543210","provider":"Airtel","is_esim":false,"activation_year":2023}
    }
    Response:
    {
      "employee":{"emp_id":1234,"name":"Ravi","official_email":"ravi@ust.com","department":"Telecom","location":"Bengaluru"},
      "sim":{"sim_number":"9876543210","provider":"Airtel","is_esim":false,"activation_year":2023},
      "data_plan":null,"voice_plan":null,"emergency_contact":null
    }
    """
    for emp in employee_tele_li:
        if emp.employee.emp_id == new_telecom.employee.emp_id:
            raise HTTPException(status_code=409, detail="Employee ID already exists")

    employee_tele_li.append(new_telecom)
    return new_telecom


@app.get("/telecom/profiles", response_model=List[EmployeeTelecomProfile])
def display_all():
    """
    Retrieve all telecom profiles.

    Sample Output:
    GET /telecom/profiles
    [
      {
        "employee":{"emp_id":1234,"name":"Ravi","official_email":"ravi@ust.com","department":"Telecom","location":"Bengaluru"},
        "sim":{"sim_number":"9876543210","provider":"Airtel","is_esim":false,"activation_year":2023},
        "data_plan":null,"voice_plan":null,"emergency_contact":null
      }
    ]
    """
    return employee_tele_li


@app.get("/telecom/profiles/search", response_model=List[EmployeeTelecomProfile])
def search_by_category(
    department: Optional[str] = Query(default=None),
    provider: Optional[str] = Query(default=None)
):
    """
    Search employees using department and/or SIM provider.
    Both filters are optional.

    Sample Output:
    GET /telecom/profiles/search?department=Telecom&provider=Airtel
    [
      {
        "employee":{"emp_id":1234,"name":"Ravi","official_email":"ravi@ust.com","department":"Telecom","location":"Bengaluru"},
        "sim":{"sim_number":"9876543210","provider":"Airtel","is_esim":false,"activation_year":2023}
      }
    ]
    """
    results = []
    for emp in employee_tele_li:
        if (department is None or emp.employee.department == department) and \
           (provider is None or emp.sim.provider == provider):
            results.append(emp)
    return results


@app.get("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def search_byid(emp_id: int):
    """
    Search a profile by employee ID.

    Sample Output:
    GET /telecom/profiles/1234
    {
      "employee":{"emp_id":1234,"name":"Ravi","official_email":"ravi@ust.com","department":"Telecom","location":"Bengaluru"},
      "sim":{"sim_number":"9876543210","provider":"Airtel","is_esim":false,"activation_year":2023}
    }
    """
    for emp in employee_tele_li:
        if emp.employee.emp_id == emp_id:
            return emp
    raise HTTPException(status_code=404, detail="Profile not found")

# -----------------------------
# Update a profile by employee ID
# -----------------------------
@app.put("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def update_byid(emp_id: int, new_emp: EmployeeTelecomProfile):
    """
    Update an existing telecom profile by employee ID.
    - Ensures path ID matches the request body ID.
    - Updates employee, SIM, data plan, voice plan, and emergency contact.
    - Raises 404 if profile not found.

    Sample Output:
    PUT /telecom/profiles/1234
    Request:
    {
      "employee": {
        "emp_id": 1234,
        "name": "Ravi",
        "official_email": "ravi@ust.com",
        "department": "Telecom",
        "location": "Bengaluru"
      },
      "sim": {
        "sim_number": "9876543210",
        "provider": "Airtel",
        "is_esim": false,
        "activation_year": 2023
      },
      "data_plan": {
        "name": "Premium Data",
        "monthly_gb": 200,
        "speed_mbps": 100,
        "is_roaming_included": true
      },
      "voice_plan": {
        "name": "Unlimited Voice",
        "monthly_minutes": 5000,
        "has_isd": true,
        "per_minute_charge_paise": 10
      },
      "emergency_contact": {
        "name": "Anita",
        "relation": "Spouse",
        "phone": "9876543210"
      }
    }

    Response:
    {
      "employee": {"emp_id":1234,"name":"Ravi","official_email":"ravi@ust.com","department":"Telecom","location":"Bengaluru"},
      "sim": {"sim_number":"9876543210","provider":"Airtel","is_esim":false,"activation_year":2023},
      "data_plan": {"name":"Premium Data","monthly_gb":200,"speed_mbps":100,"is_roaming_included":true},
      "voice_plan": {"name":"Unlimited Voice","monthly_minutes":5000,"has_isd":true,"per_minute_charge_paise":10},
      "emergency_contact": {"name":"Anita","relation":"Spouse","phone":"9876543210"}
    }

    Error Case:
    PUT /telecom/profiles/9999
    Response: 404 {"detail":"Profile not found"}
    """
    # Ensure path ID matches request body ID
    if emp_id != new_emp.employee.emp_id:
        raise HTTPException(status_code=400, detail="Employee ID does not match")

    for emp in employee_tele_li:
        if emp.employee.emp_id == emp_id:
            emp.employee = new_emp.employee
            emp.sim = new_emp.sim
            emp.data_plan = new_emp.data_plan
            emp.voice_plan = new_emp.voice_plan
            emp.emergency_contact = new_emp.emergency_contact
            return emp

    raise HTTPException(status_code=404, detail="Profile not found")


# -----------------------------
# Delete a profile by employee ID
# -----------------------------
@app.delete("/telecom/profiles/{emp_id}")
def delete(emp_id: int):
    """
    Delete a telecom profile by employee ID.
    - Removes the profile from the in-memory list.
    - Raises 404 if profile not found.

    Sample Output:
    DELETE /telecom/profiles/1234
    Response:
    {"detail":"Record removed successfully"}

    Error Case:
    DELETE /telecom/profiles/9999
    Response: 404 {"detail":"Profile not found"}
    """
    for emp in employee_tele_li:
        if emp.employee.emp_id == emp_id:
            employee_tele_li.remove(emp)
            return {"detail": "Record removed successfully"}
    raise HTTPException(status_code=404, detail="Profile not found")
