from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import re

# Pydantic model for login request (username and password)
class LoginRequest(BaseModel):
    username: str  
    password: str  

# Pydantic model for JWT token response (access_token and token_type)
class Token(BaseModel):
    access_token: str
    token_type: str    

# Pydantic model for the user (username)
class User(BaseModel):
    username: str

# Task model for creating and updating tasks
class TaskModel(BaseModel):
    id: int 
    title: str
    description: str  
    completed: bool = False  

# Model used for updating tasks
class UpdateTask(BaseModel):
    title: str  
    description: str  
    completed: bool = False 

# Model used for creating new tasks
class CreateTask(BaseModel):
    title: str  
    description: str  

# In-memory list of tasks to simulate a simple task database
tasks = []

# List of task IDs to ensure each task has a unique ID
id_list = []

