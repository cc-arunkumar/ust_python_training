from pydantic import BaseModel,Field,model_validator
from datetime import date,datetime
from enum import Enum

class StatusEnum(str,Enum):
    pending="PENDING"
    approved="APPROVED"
    rejected="REJECTED"
    

class EmployeeTraining(BaseModel):
    id:int 
    employee_id:str=Field(...,pattern=r'^UST\d+$')
    employee_name:str=Field(...,pattern=r'^[A-Za-z ]+$')
    training_title:str=Field(...,min_length=5)
    training_description:str=Field(...,min_length=10)
    requested_date:date
    status:StatusEnum
    manager_id:str=Field(...,pattern=r'^UST\d+$')
    last_updated:datetime=Field(default_factory=datetime.utcnow)
    
    @model_validator(mode="after")
    def validate_date(self):
        if self.requested_date > date.today():
            raise ValueError("Requested date cannot be a future date")
        self.last_updated=datetime.utcnow()
        return self