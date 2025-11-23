from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Students CRUD")

class Student(BaseModel):
    name:str
    age:int
    grade:str="unknown"
    
students: List[Student] = []

@app.post("/student")
def create_student(student:Student):
    students.append(student)
    return {"Student Created":student}

@app.get("/student",response_model=List[Student])
def get_students():
    return students

@app.get("/student/{index}",response_model=Student)
def get_students(index:int):
    try:
        return students[index]
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found")

@app.put("/students/{index}",response_model=Student)
def update_student(index:int,updated_student:Student):
    try:
        students[index] = update_student
        return update_student
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found")
    
@app.delete("/student/{index}",response_model=Student)
def delete_students(index:int):
    try:
        removed = students.pop(index)
        return removed
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found")


