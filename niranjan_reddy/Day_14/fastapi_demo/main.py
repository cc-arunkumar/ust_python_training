from fastapi import FastAPI,HTTPException
from typing import List
from pydantic import BaseModel


app=FastAPI(title="Students CRUD (In-Memory)")

class Student(BaseModel):
    name:str
    age:int
    grade:str="unknown"

students:List[Student]=[]

@app.post("/student")
def create_student(student:Student):
    students.append(student)
    return {"Student created":student}

@app.get("/student",response_model=List[Student])
def get_student():
    return students

@app.get("/student/{index}",response_model=Student)
def det_student(index:int):
    try:
        return students[index]
    except IndexError:
        raise HTTPException(status_code=404,detail="student not found")

@app.put("/student/{index}",response_model=Student)
def update_student(index:int,updated_student:Student):
    try:
        students[index]=updated_student
        return updated_student
    except IndexError:
        raise HTTPException(status_code=404,detail="student not found")

@app.delete("/student/{index}",response_model=Student)
def delete_student(index:int):
    try:
        removed=students.pop(index)
        return removed
    except IndexError:
        raise HTTPException(status_code=404,detail="student not found")
