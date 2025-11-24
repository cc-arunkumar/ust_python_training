from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(title="Student CRUD Operation")

# Student model
class Student(BaseModel):
    name: str
    age: int
    grade: str = "unknown"

# In-memory list to store students
students: List[Student] = []

# Create student
@app.post("/students")
def create_student(student: Student):
    students.append(student)
    return {"Student Created": student}

# Get all students
@app.get("/students", response_model=List[Student])
def get_student():
    return students

# Get student by index
@app.get("/students/{index}", response_model=Student)
def get_student(index: int):
    try:
        return students[index]
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")

# Update student by index (currently returns existing student)
@app.put("/students/{index}", response_model=Student)
def update_student(index : int):
    try:
        return students[index]
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")
    
# Delete student by index
@app.delete("/students/{index}",response_model=Student)
def delete_student(index : int):
    try:
        removed = students.pop(index)
        return removed
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found")

#Output

# POST /students
# {
#   "Student Created": {
#     "name": "Alice",
#     "age": 20,
#     "grade": "A"
#   }
# }

# GET /students
# [
#   {
#     "name": "Alice",
#     "age": 20,
#     "grade": "A"
#   },
#   {
#     "name": "Bob",
#     "age": 22,
#     "grade": "B"
#   }
# ]

# GET /students/0
# {
#   "name": "Alice",
#   "age": 20,
#   "grade": "A"
# }

# PUT /students/1
# {
#   "name": "Bob",
#   "age": 22,
#   "grade": "B"
# }

# DELETE /students/0
# {
#   "name": "Alice",
#   "age": 20,
#   "grade": "A"
# }

# Error Example (GET /students/10)
# {
#   "detail": "Student not found"
# }
