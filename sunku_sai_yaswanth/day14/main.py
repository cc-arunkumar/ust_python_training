# Students CRUD Operations
from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI(title="Students CRUD Operations")

# Pydantic model to define the structure of a Student
class Student(BaseModel):
    name: str
    age: int
    grade: str = "unknown"  # Default value for grade

# In-memory list to store students
students: List[Student] = []

# Create a new student
@app.post("/students", response_model=Student)
def create_student(student: Student):
    """
    Endpoint to create a new student and add it to the in-memory list.
    """
    students.append(student)  # Add the student to the list
    return student  # Return the created student object

# Get the list of all students
@app.get('/students', response_model=List[Student])
def get_students():
    """
    Endpoint to retrieve the list of all students.
    """
    return students  # Return the list of all students

# Get a specific student by index
@app.get('/students/{index}', response_model=Student)
def get_student(index: int):
    """
    Endpoint to retrieve a specific student by index.
    """
    try:
        return students[index]  # Try to return the student at the given index
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")  # Handle index out of range error

# Update a student's details by index
@app.put('/students/{index}', response_model=Student)
def update_student(index: int, update_student: Student):
    """
    Endpoint to update an existing student's details by index.
    """
    try:
        students[index] = update_student  # Replace the student at the given index with the updated details
        return update_student  # Return the updated student
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")  # Handle index out of range error

# Delete a student by index
@app.delete('/students/{index}', response_model=Student)
def delete_student(index: int):
    """
    Endpoint to delete a student by index.
    """
    try:
        removed = students.pop(index)  # Remove the student at the given index
        return removed  # Return the removed student
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")  # Handle index out of range error

# output
# post request
# {
#     "name": "sai",
#     "age": 20,
#     "grade": "A"
# }
# responce
# {
#     "name": "sai",
#     "age": 20,
#     "grade": "A"
# }

