from pydantic import BaseModel,validator,Field
from typing import List,Optional 


# Request body model for login endpoint
class LoginRequest(BaseModel):
    username: str
    password: str

# Response model for token
class Token(BaseModel):
    access_token: str
    token_type: str

# User model (used for protected endpoints)
class User(BaseModel):
    username: str

class Taskmodelcreate(BaseModel):
    title:str
    description:str
   
    
class TaskModel(BaseModel):
    title:str
    description:str
    completed:Optional[bool]=False
    
