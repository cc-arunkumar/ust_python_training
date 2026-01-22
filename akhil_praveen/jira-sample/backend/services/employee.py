from fastapi import HTTPException
from typing import List
import json

class EmployeeService:
    @staticmethod
    def create(data:dict):
        try:
            with open("../mockdata/employee_data.json","w") as data:
                # emp = json.load(data)
                    
                
        except Exception as e:
            return e

# with open("../mockdata/employee_data.json","r") as data:
#     emp = json.load(data)
#     for i in emp:
#         print(i)