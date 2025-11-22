from typing import List
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

application=FastAPI(title="Student CRUD(In memory)")

class Student(BaseModel):
    name:str
    age:int
    grade:str="unknown"

students:List[Student]=[]

@application.post("/students")
def create_student(student:Student):
    students.append(student)
    return{"student created":student}

@application.get("/students",response_model=List[Student])
def display_all_students():
    return students

@application.get("/students/{index}",response_model=Student)
def display_by_id(index:int):
    try:
        return students[index]
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found")
    
@application.put("/students/{index}",response_model=Student)
def update_byid(index:int,updated:Student):
    try:
        students[index]=updated
        return updated
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found")

@application.delete("/students/{index}",response_model=Student)
def delete_byid(index:int):
    try:
        removed=students.pop(index)
        return removed
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found")
