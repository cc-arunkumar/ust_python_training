from pydantic import BaseModel, field_validator, Field
from datetime import date, time,datetime

ALLOWED_STATUS=["PENDING","APPROVED","REJECTED"]

class TrainingModel(BaseModel):
    training_id:str=Field(...,pattern=r"^UST-\d+$")
    training_name:str=Field(...,)
    training_title:str=Field(...,min_length=5)
    training_description:str=Field(...,min_length=10)
    requested_date:date
    status:str
    manager_id:str=Field(...,pattern=r"^UST-\d+$")
    

    @field_validator("training_id")
    def check_training_id(cls,v):
        if not v.startswith("UST-"):
            raise ValueError("Must start with UST-")
        return v
    
    @field_validator("training_name")
    def check_training_name(cls,v):
        if not v or len(v)<5:
            raise ValueError("Please enter a valid training name")
        return v
        
    @field_validator("training_title")
    def check_training_title(cls,v):
        if not v or len(v)<5:
            raise ValueError("Please enter a valid training title")
        return v
        
    @field_validator("training_description")
    def check_training_description(cls,v):
        if not v or len(v)<10:
            raise ValueError("Please enter a valid training description")
        return v
    
    @field_validator("requested_date")
    def check_requested_date(cls,v):
        if not v:
            raise ValueError('Hire Date must be in the format YYYY-MM-DD')
        if v>datetime.today().date():
            raise ValueError('Hire Date cannot be a future date')       
        return v
    
    @field_validator("status")
    def check_status(cls,v):
        if not v or v not in ALLOWED_STATUS:
            raise ValueError("Please enter a valid Status")
        return v
        
        
    @field_validator("manager_id")
    def check_manager_id(cls,v):
        if not v.startswith("UST-"):
            raise ValueError("Manager ID must start with UST-")
        return v

