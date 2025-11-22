from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Student Management System")

class Student(BaseModel):
    name : str
    age : int
    grade : str = "Not Provided"

students : List[Student] = []

@app.post("/students",response_model=Student)
def add_student(student:Student):
    students.append(student)
    return student

@app.get("/students",response_model=List[Student])
def get_all_students():
    return students

@app.get("/students/{index}",response_model=Student)
def get_student_by_index(index:int):
    try:
        return students[index]
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found")

@app.put("/students/{index}",response_model=Student)
def update_student(index:int,updated_student:Student):
    try:
        students[index]=updated_student
        return updated_student
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found")
    
@app.put("/students/{index}",response_model=Student)
def update_student(index:int,updated_student:Student):
    try:
        students[index]=updated_student
        return updated_student
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found")
    
@app.delete("/students/{index}",response_model=Student)
def delete_student(index:int):
    try:
        deleted = students.pop(index)
        return deleted
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found")
