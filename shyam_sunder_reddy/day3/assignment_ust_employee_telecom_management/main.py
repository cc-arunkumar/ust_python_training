from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional, List

# Initialize FastAPI application
app = FastAPI(title="UST Employee Telecom Management")

# ----------------------------- #
#     Pydantic Model Schemas     #
# ----------------------------- #

# Basic employee details model
class EmployeeBasic(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999, description="Employee ID must be between 1000 and 999999")
    name: str = Field(..., min_length=2, description="Employee name must have at least 2 characters")
    official_email: str = Field(
        ..., 
        pattern=r"^[a-zA-Z0-9._%+-]+@ust\.com$", 
        description="Email must follow the format: name@ust.com"
    )
    department: Optional[str] = Field("Telecom", description="Employee department")
    location: Optional[str] = Field("Bengaluru", description="Employee location")

# SIM card information model
class SimCard(BaseModel):
    sim_number: str = Field(..., pattern=r"^\d{10}$", description="SIM number must be a 10-digit number")
    provider: Optional[str] = Field("Jio", description="Network provider name")
    is_esim: Optional[bool] = Field(False, description="Whether SIM is eSIM")
    activation_year: int = Field(..., ge=2020, le=2025, description="Activation year must be between 2020 and 2025")

# Data plan model
class DataPlan(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Data plan name")
    monthly_gb: int = Field(..., gt=0, le=1000, description="Monthly data limit in GB")
    speed_mbps: Optional[int] = Field(50, ge=1, le=1000, description="Internet speed in Mbps")
    is_roaming_included: Optional[bool] = Field(False, description="Roaming included or not")

# Voice plan model
class VoicePlan(BaseModel):
    name: str = Field(..., min_length=3, description="Voice plan name")
    monthly_minutes: int = Field(..., ge=0, le=10000, description="Monthly voice minutes")
    has_isd: Optional[bool] = Field(False, description="ISD facility included or not")
    per_minute_charge_paise: Optional[int] = Field(0, ge=0, le=1000, description="Charge per minute in paise")

# Emergency contact model
class EmergencyContact(BaseModel):
    name: str = Field(..., min_length=2, description="Emergency contact name")
    relation: Optional[str] = Field("Family", description="Relation with employee")
    phone: str = Field(..., pattern=r"^[6-9]\d{9}$", description="10-digit phone number starting with 6–9")

# Employee Telecom Profile (main composite object)
class EmployeeTelecomProfile(BaseModel):
    employee: EmployeeBasic = Field(..., description="Employee full basic details")
    sim: SimCard = Field(..., description="SIM card details")
    data_plan: Optional[DataPlan] = Field(None, description="Assigned data plan")
    voice_plan: Optional[VoicePlan] = Field(None, description="Assigned voice plan")
    emergency_contact: Optional[EmergencyContact] = Field(None, description="Emergency contact details")

# In-memory database list (for demo purposes)
employee_tele_li: List[EmployeeTelecomProfile] = []

# ------------------------------------- #
#          CRUD API ENDPOINTS            #
# ------------------------------------- #

# Create a new telecom profile
@app.post("/telecom/profiles", response_model=EmployeeTelecomProfile)
def create(new_telecom: EmployeeTelecomProfile):
    # Check if employee ID already exists
    for emp in employee_tele_li:
        if emp.employee.emp_id == new_telecom.employee.emp_id:
            raise HTTPException(status_code=409, detail="Employee ID already exists")

    employee_tele_li.append(new_telecom)
    return new_telecom

# Retrieve all profiles
@app.get("/telecom/profiles", response_model=List[EmployeeTelecomProfile])
def display_all():
    return employee_tele_li

# Search profiles by department or provider
@app.get("/telecom/profiles/search", response_model=List[EmployeeTelecomProfile])
def search_by_category(
    department: Optional[str] = Query(default=None),
    provider: Optional[str] = Query(default=None)
):
    """
    Search employees using department and/or SIM provider.
    Both filters are optional.
    """
    results = []
    for emp in employee_tele_li:
        if (department is None or emp.employee.department == department) and \
           (provider is None or emp.sim.provider == provider):
            results.append(emp)
    return results

# Search a profile by employee ID
@app.get("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def search_byid(emp_id: int):
    for emp in employee_tele_li:
        if emp.employee.emp_id == emp_id:
            return emp
    raise HTTPException(status_code=404, detail="Profile not found")

# Update a profile by employee ID
@app.put("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def update_byid(emp_id: int, new_emp: EmployeeTelecomProfile):
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

# Delete a profile by employee ID
@app.delete("/telecom/profiles/{emp_id}")
def delete(emp_id: int):
    for emp in employee_tele_li:
        if emp.employee.emp_id == emp_id:
            employee_tele_li.remove(emp)
            return {"detail": "Record removed successfully"}
    raise HTTPException(status_code=404, detail="Profile not found")
