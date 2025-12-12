from pydantic import BaseModel
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskUpdate(BaseModel):
    title: str
    description: str
    completed: bool

class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False
#--- Orm Models----
class User(Base):
    __table__="users"
    id =Column(Integer,primary_key=True, autoincrement=True)
    username= Column(String(50),unique=True,nullable=False)
    password=Column(String(100), nullable=False)
    task = relationship("Task", back_populates="owner")

class Tasks(Base):
    __tables__="tasks"
    id = Column(Integer,primary_key=True, autoincrement=True)
    title=Column(String(100),nullable=False)
    description=Column(String(200))
    completed = Column(Boolean, default=False)
    user_id= Column(Integer,ForeignKey("user_id"),nullable=False)
    owner=relationship("User",back_populates="tasks")
    
    
    

