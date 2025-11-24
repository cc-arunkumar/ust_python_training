from typing import Dict, List, Optional, Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# Initialize the FastAPI application
app = FastAPI()

# Class for employee basic details using Pydantic for data validation
class EmployeeBasic(BaseModel):
    # Employee ID with a range constraint (between 1000 and 999999)
    emp_id: int = Field(..., ge=1000, le=999999)  
    # Employee name with a minimum length of 2 characters
    name: str = Field(..., min_length=2)  
    # Official email with a specific pattern (ust.com domain)
    official_email: str = Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@ust\.com$')
    # Default department is Telecom, can be modified
    department: str = "Telecom"
    # Default location is Bengaluru, can be modified
    location: str = "Bengaluru"

# Class for SIM card details with basic validation
class SIMCard(BaseModel):
    # SIM number must be exactly 10 digits
    sim_number: str = Field(..., min_length=10, max_length=10, pattern=r'^\d{10}$')
    # Default provider is Jio
    provider: str = "Jio"  
    # Default is not an eSIM
    is_esim: bool = False
    # SIM card activation year between 2020 and 2025
    activation_year: int = Field(..., ge=2020, le=2025)

# Class for data plan details
class DataPlan(BaseModel):
    # Plan name with constraints on length
    name: str = Field(..., min_length=3, max_length=50)
    # Monthly data allowance in GB (must be between 1 and 1000)
    monthly_gb: int = Field(..., gt=0, le=1000)
    # Internet speed in Mbps (between 1 and 1000)
    speed_mbps: int = Field(50, ge=1, le=1000)
    # Whether roaming is included by default is False
    is_roaming_included: bool = False

# Class for voice plan details
class VoicePlan(BaseModel):
    # Plan name with a minimum length of 3 characters
    name: str = Field(..., min_length=3)
    # Monthly minutes (can range from 0 to 10000)
    monthly_minutes: int = Field(..., ge=0, le=10000)
    # Whether ISD is included in the plan
    has_isd: bool = False
    # Per minute charge for calls in paise (0 by default)
    per_minute_charge_paise: int = Field(0, ge=0, le=1000)

# Class for emergency contact details
class EmergencyContact(BaseModel):
    # Name of the emergency contact with a minimum length of 2 characters
    name: str = Field(..., min_length=2)
    # Default relation is "Family", but it can be changed
    relation: str = "Family"
    # Emergency contact phone number must match a specific pattern (Indian phone numbers)
    phone: str = Field(..., pattern=r'^[6-9]\d{9}$')

# Class to combine all the individual components for an employee's telecom profile
class EmployeeTelecomProfile(BaseModel):
    # Embedding the EmployeeBasic model to include employee details
    employee: EmployeeBasic = Field(...)  
    # Embedding the SIMCard model to include SIM details
    sim: SIMCard = Field(...)  
    # Optionally including a data plan (it might not be set)
    data_plan: Optional[DataPlan] = None
    # Optionally including a voice plan (it might not be set)
    voice_plan: Optional[VoicePlan] = None
    # Optionally including an emergency contact (it might not be set)
    emergency_contact: Optional[EmergencyContact] = None

# A dictionary to store telecom profiles, using employee ID as the key
telecom_data: Dict[int, EmployeeTelecomProfile] = {}

# Sample data to initialize the telecom profiles
data = {
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

# Initialize telecom_data dictionary with one employee's profile
given_data = EmployeeTelecomProfile(**data)
telecom_data[given_data.employee.emp_id] = given_data

# POST endpoint to create a new telecom profile for an employee
@app.post("/telecom/profiles", response_model=EmployeeTelecomProfile)
def create_data(profile: EmployeeTelecomProfile):
    employee_id = profile.employee.emp_id
    # Check if profile for this employee already exists
    if employee_id in telecom_data:
        raise HTTPException(status_code=409, detail="emp_id already exists")
    # Add the new profile to telecom_data
    telecom_data[employee_id] = profile
    return profile

# GET endpoint to retrieve all telecom profiles
@app.get("/telecom/profiles")
def get_details():
    return list(telecom_data.values())

# GET endpoint to retrieve a specific telecom profile by employee ID
@app.get("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def get_by_emp_id(emp_id: int):
    # If the profile exists, return it; otherwise, raise an HTTPException
    if emp_id in telecom_data:
        return telecom_data[emp_id]
    else:
        raise HTTPException(status_code=404, detail="Profile not found")

# PUT endpoint to update a telecom profile based on employee ID
@app.put("/telecom/profiles/{emp_id}", response_model=EmployeeTelecomProfile)
def update_data(emp_id: int, emp: EmployeeTelecomProfile):
    # Check if the profile exists
    if emp_id not in telecom_data:
        raise HTTPException(status_code=404, detail="no existing profile")
    
    # Ensure that the employee ID in the URL matches the employee ID in the body
    if emp_id != emp.employee.emp_id:
        raise HTTPException(status_code=400, detail="path id vs body id mismatch")
    
    # Update the telecom profile
    telecom_data[emp_id] = emp
    return emp

# DELETE endpoint to remove an employee's telecom profile
@app.delete("/telecom/profiles/{emp_id}")
def delete_emp(emp_id: int):
    # Check if the profile exists
    if emp_id in telecom_data:
        del telecom_data[emp_id]
        return {"detail": "Profile deleted"}
    else:
        raise HTTPException(status_code=404, detail="Profile not found")

# GET endpoint to search profiles by department or provider
@app.get("/telecom/profiles/search", response_model=List[EmployeeTelecomProfile])
def search_profiles(department: Optional[str] = None, provider: Optional[str] = None):
    # Start by returning all profiles
    results = list(telecom_data.values())
    
    # Filter by department if provided
    if department:
        results = [p for p in results if p.employee.department == department]
    
    # Filter by provider if provided
    if provider:
        results = [p for p in results if p.sim.provider == provider]
    
    return results



#POST
#Sample Input (Request Body)
# {
#   "employee": {
#     "emp_id": 12346,
#     "name": "John Doe",
#     "official_email": "john.doe@ust.com",
#     "department": "HR",
#     "location": "Hyderabad"
#   },
#   "sim": {
#     "sim_number": "9876543211",
#     "provider": "Vodafone",
#     "is_esim": true,
#     "activation_year": 2024
#   },
#   "data_plan": {
#     "name": "Unlimited 100GB",
#     "monthly_gb": 100,
#     "speed_mbps": 200,
#     "is_roaming_included": true
#   },
#   "voice_plan": {
#     "name": "Office Calls Pack",
#     "monthly_minutes": 1500,
#     "has_isd": false,
#     "per_minute_charge_paise": 0
#   },
#   "emergency_contact": {
#     "name": "Jane Doe",
#     "relation": "Spouse",
#     "phone": "9876543212"
#   }
# }

Sample Output (Response)
{
  "employee": {
    "emp_id": 12346,
    "name": "John Doe",
    "official_email": "john.doe@ust.com",
    "department": "HR",
    "location": "Hyderabad"
  },
  "sim": {
    "sim_number": "9876543211",
    "provider": "Vodafone",
    "is_esim": true,
    "activation_year": 2024
  },
  "data_plan": {
    "name": "Unlimited 100GB",
    "monthly_gb": 100,
    "speed_mbps": 200,
    "is_roaming_included": true
  },
  "voice_plan": {
    "name": "Office Calls Pack",
    "monthly_minutes": 1500,
    "has_isd": false,
    "per_minute_charge_paise": 0
  },
  "emergency_contact": {
    "name": "Jane Doe",
    "relation": "Spouse",
    "phone": "9876543212"
  }
}

#GET
# Sample Output (Response)
# [
#   {
#     "employee": {
#       "emp_id": 12345,
#       "name": "Asha",
#       "official_email": "asha@ust.com",
#       "department": "Engineering",
#       "location": "Pune"
#     },
#     "sim": {
#       "sim_number": "9876543210",
#       "provider": "Airtel",
#       "is_esim": true,
#       "activation_year": 2023
#     },
#     "data_plan": {
#       "name": "Standard 50GB",
#       "monthly_gb": 50,
#       "speed_mbps": 100,
#       "is_roaming_included": true
#     },
#     "voice_plan": {
#       "name": "Office Calls Pack",
#       "monthly_minutes": 1000,
#       "has_isd": false,
#       "per_minute_charge_paise": 0
#     },
#     "emergency_contact": {
#       "name": "Ravi",
#       "relation": "Friend",
#       "phone": "9876543210"
#     }
#   },
#   {
#     "employee": {
#       "emp_id": 12346,
#       "name": "John Doe",
#       "official_email": "john.doe@ust.com",
#       "department": "HR",
#       "location": "Hyderabad"
#     },
#     "sim": {
#       "sim_number": "9876543211",
#       "provider": "Vodafone",
#       "is_esim": true,
#       "activation_year": 2024
#     },
#     "data_plan": {
#       "name": "Unlimited 100GB",
#       "monthly_gb": 100,
#       "speed_mbps": 200,
#       "is_roaming_included": true
#     },
#     "voice_plan": {
#       "name": "Office Calls Pack",
#       "monthly_minutes": 1500,
#       "has_isd": false,
#       "per_minute_charge_paise": 0
#     },
#     "emergency_contact": {
#       "name": "Jane Doe",
#       "relation": "Spouse",
#       "phone": "9876543212"
#     }
#   }
# ]

# Get telecom profile by employee ID

# Sample Input (Request URL)
# GET /telecom/profiles/12345

# {
#   "employee": {
#     "emp_id": 12345,
#     "name": "Asha",
#     "official_email": "asha@ust.com",
#     "department": "Engineering",
#     "location": "Pune"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "provider": "Airtel",
#     "is_esim": true,
#     "activation_year": 2023
#   },
#   "data_plan": {
#     "name": "Standard 50GB",
#     "monthly_gb": 50,
#     "speed_mbps": 100,
#     "is_roaming_included": true
#   },
#   "voice_plan": {
#     "name": "Office Calls Pack",
#     "monthly_minutes": 1000,
#     "has_isd": false,
#     "per_minute_charge_paise": 0
#   },
#   "emergency_contact": {
#     "name": "Ravi",
#     "relation": "Friend",
#     "phone": "9876543210"
#   }
# }
# 4. PUT /telecom/profiles/{emp_id}: Update an existing telecom profile
# Sample Input (Request URL and Body)
# PUT /telecom/profiles/12345

# Sample Input (Request Body)
# {
#   "employee": {
#     "emp_id": 12345,
#     "name": "Asha",
#     "official_email": "asha@ust.com",
#     "department": "Engineering",
#     "location": "Pune"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "provider": "Airtel",
#     "is_esim": true,
#     "activation_year": 2023
#   },
#   "data_plan": {
#     "name": "Standard 50GB",
#     "monthly_gb": 50,
#     "speed_mbps": 100,
#     "is_roaming_included": false
#   },
#   "voice_plan": {
#     "name": "Office Calls Pack",
#     "monthly_minutes": 1200,
#     "has_isd": false,
#     "per_minute_charge_paise": 0
#   },
#   "emergency_contact": {
#     "name": "Ravi",
#     "relation": "Friend",
#     "phone": "9876543210"
#   }
# }

# Sample Output (Response)
# {
#   "employee": {
#     "emp_id": 12345,
#     "name": "Asha",
#     "official_email": "asha@ust.com",
#     "department": "Engineering",
#     "location": "Pune"
#   },
#   "sim": {
#     "sim_number": "9876543210",
#     "provider": "Airtel",
#     "is_esim": true,
#     "activation_year": 2023
#   },
#   "data_plan": {
#     "name": "Standard 50GB",
#     "monthly_gb": 50,
#     "speed_mbps": 100,
#     "is_roaming_included": false
#   },
#   "voice_plan": {
#     "name": "Office Calls Pack",
#     "monthly_minutes": 1200,
#     "has_isd": false,
#     "per_minute_charge_paise": 0
#   },
#   "emergency_contact": {
#     "name": "Ravi",
#     "relation": "Friend",
#     "phone": "9876543210"
#   }
# }


# 5. DELETE /telecom/profiles/{emp_id}: Delete an employee's telecom profile
# Sample Input (Request URL)
# DELETE /telecom/profiles/12345

# Sample Output (Response)
# {
#   "detail": "Profile deleted"
# }


# GET /telecom/profiles/search: Search profiles by department or provider
# Sample Input (Request URL with query parameters)
# GET /telecom/profiles/search?department=Engineering&provider=Airtel

# Sample Output (Response)
# [
#   {
#     "employee": {
#       "emp_id": 12345,
#       "name": "Asha",
#       "official_email": "asha@ust.com",
#       "department": "Engineering",
#       "location": "Pune"
#     },
#     "sim": {
#       "sim_number": "9876543210",
#       "provider": "Airtel",
#       "is_esim": true,
#       "activation_year": 2023
#     },
#     "data_plan": {
#       "name": "Standard 50GB",
#       "monthly_gb": 50,
#       "speed_mbps": 100

