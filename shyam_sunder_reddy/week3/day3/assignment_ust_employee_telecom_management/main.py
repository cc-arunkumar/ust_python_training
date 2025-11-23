from fastapi import FastAPI,HTTPException,Query
from pydantic import BaseModel,Field
from typing import Optional,List


app=FastAPI(title="UST Employee Telecome Management")

class EmployeeBasic(BaseModel):
    emp_id:int=Field(...,ge=1000,le=999999,description="Employee id must be in the valid range")
    name:str=Field(...,min_length=2,description="Name should be of minimum length 2")
    official_email:str=Field(...,pattern=r"^[a-zA-Z0-9._%+-]+@ust\.com$",description="Email is not in proper format")
    department:Optional[str]=Field("Telecom",description="Proper department not given")
    location:Optional[str]=Field("Bengaluru",description="Proper Location")

class SimCard(BaseModel):
    sim_number:str=Field(...,pattern=r"^\d{10}$",description="Proper number format not given")
    provider:Optional[str]=Field("Jio",description="Proper provider not given")
    is_esim:Optional[bool]=Field(False,description="Given data not in format")
    activation_year:int=Field(...,ge=2020,le=2025,description="The year must be in between 2020 and 2025")
    
class DataPlan(BaseModel):
    name:str=Field(...,min_length=3,max_length=50,description="The name length should be between 3 to 50")
    monthly_gb:int=Field(...,gt=0,le=1000,description="Monthly gb should be 0 to 1000 GB")
    speed_mbps:Optional[int]=Field(50,ge=1,le=1000,description="speed should be in beetween 1 to 1000")
    is_roaming_included:Optional[bool]=Field(False,description="Specify the proper roaming is true or false")

class VoicePlan(BaseModel):
    name:str=Field(...,min_length=3,description="The voice plan length should be at least 3")
    monthly_minutes:int=Field(...,ge=0,le=10000,description="The minutes should be in between o to 10000")
    has_isd:Optional[bool]=Field(False,description="The proper Format True or False")
    per_minute_charge_paise:Optional[int]=Field(0,ge=0,le=1000,description="The input must be between 0 and 1000")

class EmergencyContact(BaseModel):
    name:str=Field(...,min_length=2,description="The name length should be greater than 2")
    relation:Optional[str]=Field("Family",description="Proper Format not given")
    phone:str=Field(...,pattern=r"^[6-9]\d{9}$",description="The phone number length must be 10 and start with 6 to 9 digits")

class EmployeeTelecomProfile(BaseModel):
    employee:EmployeeBasic=Field(...,description="This should be Employee Basic object")
    sim:SimCard=Field(...,description="This should be sim card object")
    data_plan:Optional[DataPlan]=Field(None,description="Enter the proper format of Data plan")
    voice_plan:Optional[VoicePlan]=Field(None,description="Enter the proper format of Voice plan")
    emergency_contact:Optional[EmergencyContact]=Field(None,description="Enter the format of Emergency contact")

#Testing the validation
# data={
#  "employee": { "emp_id": 12345, "name": "Asha", "official_email": "asha@ust.com", "department": "Engineering", "location": "Pune" },
#  "sim": { "sim_number": "9876543210", "provider": "Airtel", "is_esim": True, "activation_year": 2023 },
#  "data_plan": { "name": "Standard 50GB", "monthly_gb": 50, "speed_mbps": 100, "is_roaming_included": True },
#  "voice_plan": {"name": "Office Calls Pack", "monthly_minutes": 1000, "has_isd": False, "per_minute_charge_paise": 0 },
#  "emergency_contact": { "name": "Ravi", "relation": "Friend", "phone": "9876543210" }
# }

# obj=EmployeeTelecomProfile(**data)
# print(obj)
employee_tele_li:List[EmployeeTelecomProfile]=[]

@app.post("/telecom/profiles",response_model=EmployeeTelecomProfile)
def create(new_telecom:EmployeeTelecomProfile):
    for emp in employee_tele_li:
        if emp.employee.emp_id==new_telecom.employee.emp_id:
            raise HTTPException(status_code=409,detail="Employee id already Exist")
    
    employee_tele_li.append(new_telecom)
    return new_telecom

@app.get("/telecom/profiles",response_model=List[EmployeeTelecomProfile])
def display_all():
    return employee_tele_li


@app.get("/telecom/profiles/search", response_model=List[EmployeeTelecomProfile])
def search_by_category(department: Optional[str] = Query(default=None),provider: Optional[str] = Query(default=None)):
    results = []
    for emp in employee_tele_li:
        if (department is None or emp.employee.department == department) and \
           (provider is None or emp.sim.provider == provider):
            results.append(emp)
    return results  

@app.get("/telecom/profiles/{emp_id}",response_model=EmployeeTelecomProfile)
def search_byid(emp_id:int):
    for emp in employee_tele_li:
        if emp.employee.emp_id==emp_id:
            return emp
    raise HTTPException(status_code=404,detail="Profile Not found")

@app.put("/telecom/profiles/{emp_id}",response_model=EmployeeTelecomProfile)
def update_byid(emp_id:int,new_emp:EmployeeTelecomProfile):
    if emp_id!=new_emp.employee.emp_id:
        raise HTTPException(status_code=400,detail="Employee ID doesnt match")
    for emp in employee_tele_li:
        if emp.employee.emp_id==emp_id:
            emp.employee=new_emp.employee
            emp.sim=new_emp.sim
            emp.data_plan=new_emp.data_plan
            emp.voice_plan=new_emp.voice_plan
            emp.emergency_contact=new_emp.emergency_contact
            return emp
    raise HTTPException(status_code=404,detail="Profile Not Found")

@app.delete("/telecom/profiles/{emp_id}")
def delete(emp_id:int):
    for emp in employee_tele_li:
        if emp.employee.emp_id==emp_id:
            employee_tele_li.remove(emp)
            return {"detail":"Record Removed Successfully"}
    raise HTTPException(status_code=404,detail="Profile Not Found")

# @app.get("/telecom/profiles/search",response_model=List[EmployeeTelecomProfile])
# def search_by_category(department:str=None,provider:str=None):
#     if department is None and provider is None:
#         return employee_tele_li
#     elif provider is None: 
#         new_li=[]
#         for emp in employee_tele_li:
#             if emp.employee.department==department:
#                 new_li.append(emp)
#         return new_li
#     elif department is None:
#         new_li=[]
#         for emp in employee_tele_li:
#             if emp.sim.provider==provider:
#                 new_li.append(emp)
#         return new_li
#     else:
#         new_li=[]
#         for emp in employee_tele_li:
#             if emp.employee.department==department and emp.sim.provider==provider:
#                 new_li.append(emp)
#         return new_li

 
            
    
