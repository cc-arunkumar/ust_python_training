from pydantic import BaseModel

class LoginData(BaseModel):
    username: str
    password: str

class TaskBase(BaseModel):
    title: str
    description: str

class TaskNew(TaskBase):
    pass

class TaskEdit(TaskBase):
    completed: bool

class Task(TaskBase):
    id: int
    completed: bool