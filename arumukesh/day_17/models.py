from pydantic import BaseModel,Field


class TaskModel(BaseModel):
    # id:int=Field(...,description="Enter detail")
    title:str=Field(...,description="Enter detail")
    description:str=Field(...,description="Enter detail")
    completed:bool