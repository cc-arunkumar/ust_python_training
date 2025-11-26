from pydantic import BaseModel,Field


class TaskModel(BaseModel):

    title:str=Field(...,description="Enter detail")
    description:str=Field(...,description="Enter detail")
    completed:bool