from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Initialize FastAPI application
app = FastAPI(title="Student CRUD")

# -----------------------------
# Data Model
# -----------------------------
class Student(BaseModel):
    name: str
    age: int
    grade: str = "unknown"   # Default grade is "unknown"

# In-memory storage for students
students: List[Student] = []

# -----------------------------
# CRUD Endpoints
# -----------------------------

@app.post("/students")
def add_student(student: Student):
    """
    Create a new student and add to the list.
    """
    students.append(student)
    return {"student created": student}


@app.get("/students")
def get_all_students():
    """
    Get all students.
    """
    return students


@app.get("/students/{index}")
def get_by_index(index: int):
    """
    Get student by index in the list.
    - Returns 404 if index is invalid.
    """
    try:
        return students[index]
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")


@app.put("/students/{index}")
def update(index: int, updated_student: Student):
    """
    Update student details at given index.
    - Returns 404 if index is invalid.
    """
    try:
        students[index] = updated_student
        return updated_student
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")


@app.delete("/students/{index}")
def delete(index: int):
    """
    Delete student at given index.
    - Returns 404 if index is invalid.
    """
    try:
        removed = students.pop(index)
        return removed
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")


# -----------------------------
# SAMPLE INPUT/OUTPUT SUMMARY
# -----------------------------
# 1. Add Student (POST /students)
# Request:
# {
#   "name": "Ravi",
#   "age": 20,
#   "grade": "A"
# }
# Response:
# {
#   "student created": {
#     "name": "Ravi",
#     "age": 20,
#     "grade": "A"
#   }
# }

# 2. Get All Students (GET /students)
# Response:
# [
#   {"name": "Ravi", "age": 20, "grade": "A"},
#   {"name": "Meera", "age": 22, "grade": "B"}
# ]

# 3. Get Student by Index (GET /students/0)
# Response:
# {
#   "name": "Ravi",
#   "age": 20,
#   "grade": "A"
# }

# 4. Update Student (PUT /students/0)
# Request:
# {
#   "name": "Ravi Kumar",
#   "age": 21,
#   "grade": "A+"
# }
# Response:
# {
#   "name": "Ravi Kumar",
#   "age": 21,
#   "grade": "A+"
# }

# 5. Delete Student (DELETE /students/0)
# Response:
# {
#   "name": "Ravi Kumar",
#   "age": 21,
#   "grade": "A+"
# }

