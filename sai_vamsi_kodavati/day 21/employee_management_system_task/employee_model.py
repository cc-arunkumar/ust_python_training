from pydantic import BaseModel, Field
from typing import Optional
from datetime import date,datetime
# Pydantic model representing an employee record and its validations
class Employee(BaseModel):
    employee_id : Optional[int] 
    first_name : str= Field(...,max_length=50,pattern=r'^[A-Za-z- ]+$')
    last_name : str = Field(...,max_length=50,pattern=r'^[A-Za-z- ]+$')
    email : str = Field(...,max_length=100,pattern=r'^[A-Za-z0-9._%+-]+@ust.com$')
    position : str= Field(max_length=50,pattern=r'^[A-Za-z0-9- ]$')
    salary : float = Field(gt=0)
    hire_date : date = Field(lt=date.today())
    
