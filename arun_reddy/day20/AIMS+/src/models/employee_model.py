from pydantic import BaseModel,Field
from datetime import datetime,date
from ..exceptions.custom_exceptions import InvalidInputException,ValidationErrorException

# List of valid office locations
valid_location=["bangalore","trivandrum","chennai","hyderabad","kochi","ernakulam","coimbatore","hosur"]

class Employee(BaseModel):
    # Employee code must start with "USTEMP-"
    emp_code:str
    # Full name must contain only alphabets and spaces
    full_name:str=Field(...,pattern=r"^[a-zA-Z ]+$")
    # Email must end with "@ust.com"
    email:str
    # Phone must be numeric and at least 10 digits
    phone:str=Field(...,pattern=r"^[0-9]",min_length=10)
    # Department name
    department:str
    # Location must be one of the valid locations
    location:str
    # Join date cannot be in the future
    join_date:date
    # Status must be Active, Inactive, or Resigned
    status:str

    # Validate employee code format
    def validate_emp_code(self):
        if not self.emp_code.startswith("USTEMP-"):
            raise ValidationErrorException("Should start with USTEMP-")

    # Validate email domain
    def validate_email(self):
        if not self.email.endswith("@ust.com"):
            raise ValidationErrorException("Invalid Email")

    # Validate join date is not in the future
    def validate_join_date(self):
        if self.join_date>datetime.today().date():
            raise ValidationErrorException("Inavalid join_date")

    # Validate status against allowed values
    def validate_status(self):
        if self.status not in ["Active","Inactive","Resigned"]:
            raise InvalidInputException("status is Invalid")

    # Validate location against predefined list
    def validate_location(self):
        if self.location.lower() not in valid_location:
            raise InvalidInputException("not a valid location") 
    
    # Run all custom validations after initialization
    def __init__(self, **data):
        super().__init__(**data)   
        self.validate_email()
        self.validate_join_date()
        self.validate_status()
        self.validate_location()
        self.validate_emp_code()
