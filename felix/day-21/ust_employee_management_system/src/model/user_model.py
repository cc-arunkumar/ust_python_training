from pydantic import BaseModel

class User(BaseModel):
    username:str
    
class UserModel(BaseModel):
    username:str
    password:str
    
class Token(BaseModel):
    token:str
    token_type:str