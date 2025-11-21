from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI(title="Student crud")

class Student(BaseModel):
    name:str
    age:int
    grade:str="unknown"
    
students:List[Student]=[] 

@app.post("/students")
def add_student(student:Student):
    students.append(student)
    return {"student created":student}

@app.get("/students")
def getallstudents():
    return students

@app.get("/students/{index}")
def getbyindex(index:int):
    try:
        return students[index]
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found ")

@app.put("/students/{index}")
def update(index:int,updated_student:Student):
    try:
        students[index]=updated_student
        return updated_student
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found")
   
@app.delete("/students/{index}") 
def delete(index:int):
    try:
        removed=students.pop(index)
        return removed
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found")

        