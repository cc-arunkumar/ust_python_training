# UST Employee Telecom Device
# Registration
# Scenario
# UST provides company SIM cards to employees for official communication.
# When a SIM is issued, an employee must register their details and SIM details.
# You will create Pydantic models to validate the registration input.

# Model Requirements
# Employee Model
# Field Type Required Rules
# emp_id int YES ge=1000 , le=999999
# name str YES min_length=2
# department str NO default: "General"


# SIM Model
# Field Type Required Rules
# number str YES must be exactly 10 digits
# provider str NO default: "Jio"
# activation_year int YES ge=2020 , le=2025
# Regex for SIM number:
# pattern=r"^\d{10}$"

# Registration Model
# (Nesting practice — model inside model)
# UST Employee Telecom Device Registration 1
# Field Type Required
# employee Employee YES
# sim SIM YES

# Deliverables from participants
# They need to submit:
# 1. All 3 model class definitions
# 2. Output of valid registration object printed
# 3. Output of default-field test printed
# 4. Validation error outputs for each failed case


from fastapi import FastAPI, HTTPException  # Importing necessary modules from FastAPI
from pydantic import BaseModel, Field  # Importing Pydantic's BaseModel and Field for data validation
from typing import Optional, List  # Importing Optional for optional fields and List for lists of items

# Initialize FastAPI app with a custom title
app = FastAPI(title="UST Employee Telecom Device Registration")

# Define the EmployeeModel using Pydantic for employee data validation
class EmployeeModel(BaseModel):
    # Employee ID should be an integer between 1000 and 999999
    emp_id: int = Field(..., ge=1000, le=999999, description="id in between 1000 and 999999")
    
    # Name of the employee (must have a minimum length of 2 characters)
    name: str = Field(..., min_length=2)
    
    # Department of the employee (optional, defaults to "General")
    department: Optional[str] = Field(default="General")

# Define the SimModel using Pydantic for SIM card data validation
class SimModel(BaseModel):
    # SIM card number must be exactly 10 characters long
    number: str = Field(..., max_length=10, min_length=10)
    
    # Provider for the SIM card (optional, defaults to "Jio")
    provider: Optional[str] = Field(default="Jio")
    
    # Activation year for the SIM card (must be between 2020 and 2025)
    activation_year: int = Field(..., ge=2020, le=2025)

# Define the RegistrationModel which includes both Employee and Sim information
class RegistrationModel(BaseModel):
    # Employee details are stored here (using EmployeeModel)
    employee: EmployeeModel
    
    # SIM details are stored here (using SimModel)
    sim: SimModel

# Example data for employee and SIM registration
data = {
    "employee": {
        "emp_id": 12345,
        "name": "Asha",
        "department": "Engineering"
    },
    "sim": {
        "number": "9876543210",
        "provider": "Airtel",
        "activation_year": 2023
    }
}

# Create an instance of RegistrationModel using the provided data
obj = RegistrationModel(
    employee=data["employee"],  # Assigning employee data to the employee field
    sim=data["sim"]  # Assigning SIM data to the sim field
)

# Print the dictionary representation of the RegistrationModel instance
# This will print all the data that was used to create the object
print(obj.__dict__)


# case 2:

# # Example data for employee and SIM registration (without providing department and provider)
# data_with_defaults = {
#     "employee": {
#         "emp_id": 67890,
#         "name": "John"
#     },
#     "sim": {
#         "number": "1234567890",
#         "activation_year": 2023
#     }
# }

# # Create an instance of RegistrationModel using the data with defaults
# obj_with_defaults = RegistrationModel(
#     employee=data_with_defaults["employee"],  # Assigning employee data
#     sim=data_with_defaults["sim"]  # Assigning SIM data
# )

# # Print the dictionary representation of the RegistrationModel instance with defaults
# print(obj_with_defaults.__dict__)



#case 3:
# Validation error outputs for each failed case
# try:
#     invalid_data_1 = {
#         "employee": {
#             "emp_id": 999,  # Invalid ID
#             "name": "Alice",
#             "department": "HR"
#         },
#         "sim": {
#             "number": "1234567890",
#             "activation_year": 2023
#         }
#     }
#     invalid_obj_1 = RegistrationModel(
#         employee=invalid_data_1["employee"], 
#         sim=invalid_data_1["sim"]
#     )
# except Exception as e:
#     print("Validation Error 1:", e)




# sample output case 1:
# {'employee': EmployeeModel(emp_id=12345, name='Asha', department='Engineering'), 
# 'sim': SimModel(number='9876543210', provider='Airtel', activation_year=2023)}


# #sample output case 2:
# Output for Default-Field Test:
#{'employee': EmployeeModel(emp_id=67890, name='John', department='General'),
#'sim': SimModel(number='1234567890', provider='Jio', activation_year=2023)}


#sample output case 3:
# Validation Error 1: 1 validation error for RegistrationModel
# employee -> emp_id
#   ensure this value is greater than or equal to 1000 (type=value_error.number.not_ge; limit_value=1000)

