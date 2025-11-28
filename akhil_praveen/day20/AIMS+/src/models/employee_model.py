from pydantic import BaseModel, Field, EmailStr, model_validator  # Import necessary classes for validation and modeling
from datetime import date  # Import date to handle date fields
from typing import Literal  # Import Literal for specifying fixed values for certain fields

# StatusValidate model for validating the 'status' field of employee (can only be 'Active', 'Inactive', or 'Resigned')
class StatusValidate(BaseModel):
    # The 'status' field must be one of the specified literal values
    status: Literal['Active', 'Inactive', 'Resigned']

# EmployeeDirectory model to define the structure of an employee's data
class EmployeeDirectory(BaseModel):
    # 'emp_code' field must follow the given pattern (e.g., USTEMP12345)
    emp_code: str = Field(..., pattern=r"^USTEMP[A-Za-z0-9-]+$")
    
    # 'full_name' field must only contain letters and spaces
    full_name: str = Field(..., pattern=r"^[A-Za-z ]+$")
    
    # 'email' field must be a valid email address as per the EmailStr type from Pydantic
    email: EmailStr
    
    # 'phone' field must follow a specific pattern for valid Indian phone numbers (starting with 6-9 and followed by 9 digits)
    phone: str = Field(..., pattern=r"^[6-9][0-9]{9}$")
    
    # 'department' field must be one of the predefined departments
    department: Literal['HR', 'IT', 'Admin', 'Finance', 'Support']
    
    # 'location' field must be one of the specified locations
    location: Literal['Trivandrum', 'Bangalore', 'Chennai', 'Hyderabad', 'Mumbai', 'Delhi', 'Pune']
    
    # 'join_date' must be a valid date field (the date when the employee joined)
    join_date: date
    
    # 'status' field must be one of the specified literal values (Active, Inactive, or Resigned)
    status: Literal['Active', 'Inactive', 'Resigned']
    
    # Custom validation logic to check additional business rules after the initial validation
    @model_validator(mode="after")
    def validate(self):
        # Check if the email ends with '@ust.com' domain
        if not self.email.endswith("@ust.com"):
            raise ValueError("Email must belong to @ust.com domain")
        
        # Ensure the join_date is not in the future
        if self.join_date > date.today():
            raise ValueError("join_date cannot be in the future")
        
        return self
