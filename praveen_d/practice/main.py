# Q1) Build a FastAPI CRUD App (20 Marks)

# Create a FastAPI application to manage Employee Records.

# Each employee has:

# id: int

# name: str

# email: str

# department: str

# salary: float

# You must implement these endpoints:

# 

# 



#

# 
# # Store data in an in-memory list.
from pydantic import BaseModel,Field
from fastapi import FastAPI,HTTPException
from typing import List

app=FastAPI(description="Practice 1")

class Employee(BaseModel):
    id: int
    name: str
    email: str
    department: str
    salary: float
employee_list:List[Employee]=[]
# POST /employees
# Add a new employee
# Return the created employee
# If ID already exists → return HTTP 400

@app.post("/employee")
def create_employee(employee:Employee):
    try:
        for emp in employee_list:
            if emp.id==employee.id:
                raise HTTPException
        employee_list.append(employee)# or use employee.model_dump()
        return employee
    except HTTPException:
        raise HTTPException(status_code=400,detail="Already exist")
    
# GET /employees
# Return all employees
@app.get("/employee")
def display_all_emp():
    return employee_list

# GET /employees/{id}
# Return employee with matching ID
# If not found → 404
@app.get("/employee/{id}")
def deiplay_specfic_employee(id:int):
    try:
        for emp in employee_list:
            if emp["id"]==id:
                return emp
    except HTTPException:
        raise HTTPException(status_code=404,detail="Employee ID not found")

#  PUT /employees/{id}
# Update an employee’s details
# If not found → 404
@app.put("/employee/{id}")
def update_employee(id:int,employee:Employee):
    try:
        for index,emp in enumerate (employee_list):
            if emp["id"]==id:
                employee_list[index]=employee.dict()
                return employee
    except HTTPException:
        raise HTTPException(status_code=404,detail="Erroe not found")

# DELETE /employees/{id}
# Remove employee
# If not found → 404
# Return {"message": "Deleted"}

@app.delete("/employee/{id}")
def delete_employee(id:int):
    try:
        for i in range(0,len(employee_list)):
            if id==employee_list[i].id:
                employee_list.pop(i)
    except HTTPException:
        raise HTTPException(status_code=404,detail="Not found")
                    
            
    