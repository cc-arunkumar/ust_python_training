from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create an instance of FastAPI
app = FastAPI(title="Students CRUD (In-Memory)")

# Pydantic model to represent a student
class Student(BaseModel):
    name: str  # Student's name (required field)
    age: int  # Student's age (required field)
    grade: str = "unknown"  # Student's grade, default value is "unknown"

# In-memory "database" to store the students (a list of Student objects)
students: List[Student] = []

# POST endpoint to create a new student
@app.post("/students", response_model=Student)
def create_student(student: Student):
    students.append(student)  # Add the new student to the list
    return student  # Return the created student

# GET endpoint to fetch all students
@app.get("/students", response_model=List[Student])
def get_students():
    return students  # Return the list of all students

# GET endpoint to fetch a student by index (zero-based)
@app.get("/students/{index}", response_model=Student)
def get_student(index: int):
    try:
        return students[index]  # Return the student at the given index
    except IndexError:
        # If the index is out of range, raise a 404 error
        raise HTTPException(status_code=404, detail="Student not found")

# PUT endpoint to update an existing student by index
@app.put("/students/{index}", response_model=Student)
def update_student(index: int, updated_student: Student):
    try:
        students[index] = updated_student  # Replace the student at the given index with the updated data
        return updated_student  # Return the updated student
    except IndexError:
        # If the index is out of range, raise a 404 error
        raise HTTPException(status_code=404, detail="Student not found")

# DELETE endpoint to delete a student by index
@app.delete("/students/{index}", response_model=Student)
def delete_student(index: int):
    try:
        removed_student = students.pop(index)  # Remove and return the student at the given index
        return removed_student  # Return the removed student
    except IndexError:
        # If the index is out of range, raise a 404 error
        raise HTTPException(status_code=404, detail="Student not found")
