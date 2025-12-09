from pydantic import BaseModel,Field,field_validator

from datetime import date
# print(date.today())
# emp_id INT primary key not null,
#     first_name varchar(50) not null,
#     last_name varchar (50) not null,
#     email varchar(50) not null,
#     position varchar(50) ,
#     salary float check(salary>0),
#     hire_date Date not null
class Employee_pydentic(BaseModel):
    emp_id:int=0
    first_name:str=Field(...,max_length=50,pattern=r"^[A-Za-z- ]+$")
    last_name:str=Field(...,max_length=50 , pattern=r"^[A-Za-z ]+$")
    email:str=Field(...,max_length=100,pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    position:str=Field(default=None,max_length=50,pattern=r'[a-zA-Z0-9-]+$')
    salary:float=Field(...,gt=0)
    hire_date:date=Field(...)
    
    
    @field_validator("hire_date")
    def validate_hire_date(cls, v):
        if v > date.today():
            raise ValueError("hire_date cannot be a future date")
        return v
    
    
    