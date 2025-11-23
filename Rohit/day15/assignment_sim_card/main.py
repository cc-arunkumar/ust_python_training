from fastapi import FastAPI,HTTPException
from typing import List,Optional
from pydantic import BaseModel,Field


app= FastAPI()

class Employee_model(BaseModel):
    emp_id:str=Field(...,ge=1000 , le=999999)
    name:str= Field(...,min_length=2)
    department:str= Field(..., default="General")


class Sim_model(BaseModel):
    number:int= Field(...,re=r"^\d{10}$")
    provider:str = Field(default="Jio")
    activation_year:str = Field(...,ge=2020,le=2025)
    


    
        