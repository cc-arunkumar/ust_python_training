from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create FastAPI app instance with a title
app = FastAPI(title="Students CRUD (In-Memory)")

# -------------------------------
# Student model using Pydantic
# -------------------------------
class Student(BaseModel):
    name: str
    age: int
    grade: str = "unknown"   # Default grade if not provided

# In-memory list to store students
students: list[Student] = []

# -------------------------------
# Create student (POST)
# -------------------------------
@app.post("/students")
def create_student(student: Student):
    """
    Add a new student to the list.
    """
    students.append(student)
    return {"Student Created": student}

# -------------------------------
# Get all students (GET)
# -------------------------------
@app.get("/students", response_model=List[Student])
def get_students():
    """
    Return all students.
    """
    return students

# -------------------------------
# Get student by index (GET)
# -------------------------------
@app.get("/students/{index}", response_model=Student)
def get_student(index: int):
    """
    Return a student by index.
    """
    try:
        return students[index]
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")

# -------------------------------
# Update student by index (PUT)
# -------------------------------
@app.put("/students/{index}", response_model=Student)
def update_student(index: int, updated_student: Student):
    """
    Update a student at a given index.
    """
    try:
        students[index] = updated_student
        return updated_student
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")

# -------------------------------
# Delete student by index (DELETE)
# -------------------------------
@app.delete("/students/{index}", response_model=Student)
def delete_student(index: int):
    """
    Delete a student at a given index.
    """
    try:
        removed = students.pop(index)
        return removed
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")
    
# output
# {
#   "create_student": {
#     "request": {
#       "name": "Alice",
#       "age": 20,
#       "grade": "A"
#     },
#     "response": {
#       "Student Created": {
#         "name": "Alice",
#         "age": 20,
#         "grade": "A"
#       }
#     }
#   },

#   "get_all_students": {
#     "response": [
#       {
#         "name": "Alice",
#         "age": 20,
#         "grade": "A"
#       }
#     ]
#   },

#   "get_student_by_index": {
#     "response_success": {
#       "name": "Alice",
#       "age": 20,
#       "grade": "A"
#     },
#     "response_error": {
#       "detail": "Student not found"
#     }
#   },

#   "update_student": {
#     "request": {
#       "name": "Alice",
#       "age": 21,
#       "grade": "B"
#     },
#     "response": {
#       "name": "Alice",
#       "age": 21,
#       "grade": "B"
#     },
#     "response_error": {
#       "detail": "Student not found"
#     }
#   },

#   "delete_student": {
#     "response_success": {
#       "name": "Alice",
#       "age": 21,
#       "grade": "B"
#     },
#     "response_error": {
#       "detail": "Student not found"
#     }
#   }
# }