from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Initialize FastAPI application with metadata
app = FastAPI(title="Student Management System")

# ==============================
# Data Model
# ==============================
class Student(BaseModel):
    name: str
    age: int
    grade: str = "Not Provided"  # Default value if grade is not given

# In-memory storage (not persistent, resets when server restarts)
students: List[Student] = []

# ==============================
# API Endpoints
# ==============================

# Create a new student
@app.post("/students", response_model=Student)
def add_student(student: Student):
    """
    Add a new student to the system.
    - Input: Student object (name, age, grade)
    - Output: The created student record
    """
    students.append(student)
    return student


# Get all students
@app.get("/students", response_model=List[Student])
def get_all_students():
    """
    Retrieve all students currently stored.
    - Output: List of student records
    """
    return students


# Get a student by index
@app.get("/students/{index}", response_model=Student)
def get_student_by_index(index: int):
    """
    Retrieve a student by their index in the list.
    - Input: Index (int)
    - Output: Student record if found, else 404 error
    """
    try:
        return students[index]
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")


# Update a student by index
@app.put("/students/{index}", response_model=Student)
def update_student(index: int, updated_student: Student):
    """
    Update an existing student record by index.
    - Input: Index (int), Updated Student object
    - Output: Updated student record
    """
    try:
        students[index] = updated_student
        return updated_student
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")


# Delete a student by index
@app.delete("/students/{index}", response_model=Student)
def delete_student(index: int):
    """
    Delete a student record by index.
    - Input: Index (int)
    - Output: Deleted student record
    """
    try:
        deleted = students.pop(index)
        return deleted
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")


# ==============================
# Sample Input/Output
# ==============================
"""
Sample Input (POST /students):
{
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

Sample Output:
{
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

--------------------------------

Sample Input (GET /students):
No input required

Sample Output:
[
    {
        "name": "Alice",
        "age": 20,
        "grade": "A"
    }
]

--------------------------------

Sample Input (PUT /students/0):
{
    "name": "Alice Johnson",
    "age": 21,
    "grade": "A+"
}

Sample Output:
{
    "name": "Alice Johnson",
    "age": 21,
    "grade": "A+"
}

--------------------------------

Sample Input (DELETE /students/0):
No input required

Sample Output:
{
    "name": "Alice Johnson",
    "age": 21,
    "grade": "A+"
}
"""