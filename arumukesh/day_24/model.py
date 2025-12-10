from pydantic import BaseModel
from typing import Optional, List, Dict


class Project(BaseModel):
    name: str
    status: str


class Address(BaseModel):
    city: str
    state: str


class Employee(BaseModel):
    emp_id:int
    name: str
    age: int
    department: str
    skills: Optional[List[str]]
    address: Optional[Address]  # <-- Updated
    projects: Optional[List[Project]]
    experience_years: Optional[int]
