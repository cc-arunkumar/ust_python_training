from pydantic import BaseModel, EmailStr

class Employee(BaseModel):
    name: str
    email: EmailStr
    designation: str        
    manager_id: int         
