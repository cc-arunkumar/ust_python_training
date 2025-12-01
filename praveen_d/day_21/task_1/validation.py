
from pydantic import BaseModel,Field,field_validator,EmailStr
from typing import Optional,List
import re
from datetime import datetime
class Validation(BaseModel):
    first_name:str = Field(...,min_length=1,pattern=r"^[A-Za-z ]+$")
    last_name:str
    email: EmailStr = Field(...,max_length=100)
    position:Optional[str]=None
    salary: Optional[float]=Field(...,gt=0)
    hire_date: str
    


    # @field_validator('first_name')
    # def validate_first_name(cls,v):
    #     try:
    #         if v.strip()=="":
    #             raise ValueError("The first name cannot be empty")
    #         if not re.match(r"^[A-Za-z ]+$",v):
    #             raise ValueError("The first name should contain only alphabets")
    #         return v
    #     except ValueError as e:
    #         print(e)
            


        
    @field_validator('last_name')
    def validate_last_name(cls,v):
        try:
            if v.strip()=="":
                raise ValueError
            if not re.match(r"^[A-Za-z]+$",v):
                raise ValueError
            return v
        except ValueError:
            print("The last name should contain only alphabets")
        

            
    @field_validator('position')
    def validate_field(cls,v):
        try:
            if re.search(r"^@#%&$",v):
                return ValueError
            return v
        except ValueError:
            print("The position should not contain special symbols")
   
    @field_validator('hire_date')
    def validate_date(cls, v):
        try:
            # Check if the hire_date is in the future
            hire_date = datetime.strptime(v, "%Y-%m-%d")
            if hire_date > datetime.now():
                raise ValueError("The hire_date cannot be in the future.")
            
            # Validate the format (yyyy-mm-dd)
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", v):
                raise ValueError("The hire_date should be in the format yyyy-mm-dd.")
            
            # Optionally, you can check if the date is valid (e.g., month > 12 or day > 31)
            datetime.strptime(v, "%Y-%m-%d")  # Will raise an error if the date is invalid

        except ValueError as e:
            print(f"Invalid hire_date: {e}")
            return None  # Return None or handle the error as needed
        return v 

        
            
            
            
  
