#Easy
#task1

from pydantic import BaseModel
from enum import Enum
from typing import List
from datetime import date
class BandEnum(str, Enum):
    B1 = "B1"
    B2 = "B2"
    B3 = "B3"
    M1 = "M1"

class EmployeeTask(BaseModel):
 # Employee Info
 employee_id: int
 employee_name: str
 email: str
 mobile: str
 band: BandEnum
 
 # Task Info
 task_id: int
 task_title: str
 task_description: str
 hours_spent: int
 completed: bool = False
 
 