from pydantic import BaseModel, Field
from typing import Optional

class EmployeeCreate(BaseModel):
    
    employee_name : str = Field(..., description="Full name of the employee")
    designation: Optional[str] = None
    manager_id : Optional[int] = Field(None, description="Employee ID of the manager")
    email : Optional[str] = Field(None, description="Email address of the employee")
    status : Optional[str] = Field(None, description="Current status of the employee (e.g., active, inactive)")

class EmployeeUpdate(BaseModel):
    
    employee_name : Optional[str] = Field(None, description="Full name of the employee")
    designation: Optional[str] = None
    manager_id : Optional[int] = Field(None, description="Employee ID of the manager")
    email : Optional[str] = Field(None, description="Email address of the employee")
    status : Optional[str] = Field(None, description="Current status of the employee (e.g., active, inactive)")

class EmployeeResponse(EmployeeCreate):
    employee_id : int = Field(..., description="Unique identifier for the employee")

    class Config:
        from_attributes = True