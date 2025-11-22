from typing import List
from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Students CRUD (In-Memory)")


class Student(BaseModel):
    name:str
    age:int
    grade:str="unknown"
students:list[Student]=[]

@app.post("/students")
def create_student(student:Student):
    students.append(student)
    return {"Student Created":student}
@app.get("/students",response_model=List[Student])
def get_student():
    return students

@app.get("/students/{index}",response_model=List[Student])
def get_student(index:int):
    try:
        return students[index]
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found")

@app.put("/students/{index}",response_model=List[Student])
def update_student(index:int,updated_Student:Student):
    try:
        students[index] =updated_Student
        return updated_Student
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found")
    
@app.delete("/students/{index}", response_model=Student)
def delete_student(index:int):
    try:
        removed = students.pop(index)
        return removed
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")
    
