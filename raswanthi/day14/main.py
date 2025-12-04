from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

# Initialize FastAPI application with a title
app = FastAPI(title="Students CRUD (In-memory)")

# -----------------------------
# Pydantic Model (Schema)
# -----------------------------
class Student(BaseModel):
    # Define the structure of a Student object
    name: str
    age: int
    grade: str = "unknown"   # Default grade is "unknown" if not provided

# -----------------------------
# In-memory "Database"
# -----------------------------
# This list will hold all student records in memory
students: List[Student] = []

# -----------------------------
# CRUD Endpoints
# -----------------------------

@app.post("/students")
def create_student(student: Student):
    """
    Create a new student and add to the list.
    Request body: Student object
    Response: Confirmation message with created student
    """
    students.append(student)
    return {"Student Created": student}

@app.get("/students", response_model=List[Student])
def get_students():
    """
    Get all students.
    Response: List of Student objects
    """
    return students

@app.get("/students/{index}", response_model=Student)
def get_student(index: int):
    """
    Get a student by index (position in the list).
    Path parameter: index (int)
    Response: Student object if found, else 404 error
    """
    try:
        return students[index]
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")

@app.put("/students/{index}", response_model=Student)
def update_student(index: int, updated_student: Student):
    """
    Update a student at a given index.
    Path parameter: index (int)
    Request body: Updated Student object
    Response: Updated Student object if found, else 404 error
    """
    try:
        students[index] = updated_student
        return updated_student
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{index}", response_model=Student)
def delete_student(index: int):
    """
    Delete a student at a given index.
    Path parameter: index (int)
    Response: Deleted Student object if found, else 404 error
    """
    try:
        removed = students.pop(index)
        return removed
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")
