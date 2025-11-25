from typing import Optional
from pydantic import BaseModel, Field


class  TaskModel(BaseModel):
    id:int 
    title:str 
    description:str
    completed:bool

class TaskModelCreate(BaseModel):
    title:str 
    description:str
    
tasks = []
