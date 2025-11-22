from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="madhan CRUD (In-Memory)")

class Student(BaseModel):
    name: str
    age: int
    grade: str = "unknown"

students : List[Student] = []

@app.post("/students")
def create_student(student:Student):
    students.append(student)
    return {"Student created":student}

@app.get("/students",response_model=Student)
def get_student(index:int):
    try:
        return students[index]
    except:
        raise HTTPException(status_code=404, detail="student Not Found")
@app.get("/Students/")
def get_student():
    try:
        return students
    except IndexError:
        raise HTTPException(status_code=404, detail="Students not Found")

@app.put("/student/{index}", response_model=Student)
def update_student(index:int,updated_student: Student):
    try:
        students[index] = updated_student
        return update_student
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{index}",response_model=Student)
def delete_student(index:int):
    try:
        removed = students.pop(index)
        return removed
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found")
    