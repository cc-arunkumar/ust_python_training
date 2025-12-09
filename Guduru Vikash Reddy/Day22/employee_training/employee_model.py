from pydantic import BaseModel,Field
from typing import Optional
from datetime import date

class Employee(BaseModel):
    id:Optional[int]=None
    employee_id:str=Field(...,pattern=r"^UST\d+",description="The id must start with UST")
    employee_name:str=Field(...,min_length=5,pattern=r"^[A-Za-z ]+$",description="THE name should be minimum of 5 and conatin only characters")
    training_title:str=Field(...,min_length=5)
    training_description:str=Field(...,min_length=10)
    requested_date:date=Field(...,lt=date.today(),description="Should not be in future")
    status:str=Field(...,pattern=r"^(pending|approved|rejected)$",description="Allowed values: PENDING, APPROVED, REJECTED")
    manager_id:str=Field(...,pattern=r"^UST\d+",description="The id must start with UST") 