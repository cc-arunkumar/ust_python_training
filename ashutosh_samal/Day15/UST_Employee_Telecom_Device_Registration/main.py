from pydantic import BaseModel, Field

class Employee(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999, description="Employee ID must be >= 1000 and <= 999999")
    name: str = Field(..., min_length=2, description="Name must be at least 2 characters")
    department: str = "General"

class SIM(BaseModel):
    number: str = Field(..., pattern=r"^\d{10}$", description="Number must be 10 digits")
    provider: str = "jio"  
    activation_year: int = Field(..., ge=2020, le=2025, description="Activation year must be in the range 2020 to 2025")

class Registration(BaseModel):
    employee: Employee
    sim: SIM


data = {
    "employee": {
        "emp_id":12345,
        "name":"Asha",
        "department":"Engineering"
    },
    "sim": {
        "number":"9876543210",
        "provider":"Airtel",
        "activation_year":2023
    }
 }


reg = Registration(**data)
print(reg)
