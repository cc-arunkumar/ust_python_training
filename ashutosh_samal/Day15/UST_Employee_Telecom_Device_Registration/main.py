from pydantic import BaseModel, Field

# Define the Employee model using Pydantic
class Employee(BaseModel):
    # Employee ID: must be an integer between 1000 and 999999
    emp_id: int = Field(..., ge=1000, le=999999, description="Employee ID must be >= 1000 and <= 999999")
    name: str = Field(..., min_length=2, description="Name must be at least 2 characters")
    department: str = "General"

# Define the SIM model using Pydantic
class SIM(BaseModel):
    
    number: str = Field(..., pattern=r"^\d{10}$", description="Number must be 10 digits")
    provider: str = "jio"  
    activation_year: int = Field(..., ge=2020, le=2025, description="Activation year must be in the range 2020 to 2025")

# Define the Registration model, which contains an Employee and SIM object
class Registration(BaseModel):
    employee: Employee
    sim: SIM

# Data to be passed for the Registration model
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

# Create the Registration object using the provided data
reg = Registration(**data)  
print(reg)  



# Sample Output
# employee=Employee(emp_id=12345, name='Asha', department='Engineering') 
# sim=SIM(number='9876543210', provider='Airtel', activation_year=2023)