from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(title="Students CRUD")

# Define the Student model using Pydantic
class Student(BaseModel):
    name: str  # Name of the student (string)
    age: int   # Age of the student (integer)
    grade: str = "unknown"  # Grade of the student (default is "unknown")

# List to store students
students: List[Student] = []  # Empty list to store student data

# POST endpoint to create a new student
@app.post("/student")
def create_student(student: Student):
    students.append(student)  
    return {"Student Created": student}  

# GET endpoint to retrieve all students
@app.get("/student", response_model=List[Student])
def get_students():
    return students  # Return the list of all students

# GET endpoint to retrieve a specific student by index
@app.get("/student/{index}", response_model=Student)
def get_students(index: int):
    try:
        return students[index]  
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")  # If student not found, raise 404 error

# PUT endpoint to update a student's information by index
@app.put("/students/{index}", response_model=Student)
def update_student(index: int, updated_student: Student):
    try:
        students[index] = updated_student  
        return updated_student 
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")  # If student not found, raise 404 error

# DELETE endpoint to remove a student by index
@app.delete("/student/{index}", response_model=Student)
def delete_students(index: int):
    try:
        removed = students.pop(index)  
        return removed  
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")  # If student not found, raise 404 error


