from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title= "Testing CRUD Operations on Student Management Syatem.")

class Student(BaseModel):
    name : str
    age : int
    grade : str = "unknown"

students: list[Student] = []

@app.post("/students")
def create_student(student : Student):
    students.append(student)
    return {"Student Created" : student}

@app.get("/students", response_model=list[Student])
def get_students():
    return students

@app.get("/students/{index}", response_model=Student)
def get_student(index : int):
    try:
        return students[index]
    except IndexError:
        raise HTTPException(status_code=404, detail="Student Not Found!")

@app.put("/students/{index}", response_model=Student)
def update_student(index: int, updated_student: Student):
    try:
        students[index] = update_student
        return updated_student
    except IndexError:
        raise HTTPException(status_code=404, detail="Student Not Found!")

@app.delete("/students/{index}", response_model=Student)
def delete_student(index : int):
    try:
        removed = students.pop(index)
        return removed
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not Found!")

