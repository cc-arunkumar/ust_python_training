import re
from typing import Literal
from pydantic import BaseModel, Field, field_validator
from datetime import date,datetime

class Training(BaseModel):
   id:int=0
   employee_id:str=Field(...,min_length=1,max_length=20,pattern=r"^UST\d+$")
   employee_name:str=Field(...,min_length=1,max_length=100,pattern=r"^[A-Za-z ]+$")
   training_title:str=Field(...,min_length=1,max_length=200)
   training_description:str=Field(...)
   requested_date:date=Field(...)
   status:Literal["Pending","Approved","Rejected"]
   manager_id:str=Field(...,min_length=1,max_length=20,pattern=r"^UST\d+$")
   last_updated: datetime 
   
   @field_validator("requested_date")
   def requested_Date(cls,v):
       if v > date.today():
           raise ValueError("Requested date cannot be future date")
       return v



       


   
    