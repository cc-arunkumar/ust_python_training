from typing import List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

# Create FastAPI app
app = FastAPI(title="Students CRUD (In-memory)")

# Define Student model
class Student(BaseModel):
    name: str
    age: int
    grade: str = "unknown"

# In-memory list to store students
students: List[Student] = []

# Get all students
@app.get("/students", response_model=List[Student])
def get_students():
    return students

# Get student by index
@app.get("/students/{index}", response_model=Student)
def get_student_by_id(index: int):
    try:
        return students[index]
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")

# Add new student
@app.post("/students", response_model=Student)
def add_student(new_student: Student):
    students.append(new_student)
    return new_student

# Update student by index
@app.put("/students/{index}", response_model=Student)
def update_student(index: int, update_student: Student):
    try:
        students[index] = update_student
        return update_student
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")

# Delete student by index
@app.delete("/students/{index}", response_model=Student)
def delete_student(index: int):
    try:
        removed = students.pop(index)
        return removed
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")


# ================sample output=======================
# {
#   "students": [
#     {
#       "name": "Rohit",
#       "age": 22,
#       "grade": "A"
#     },
#     {
#       "name": "Meera",
#       "age": 20,
#       "grade": "B"
#     }
#   ],
#   "get_student_by_index": {
#     "name": "Rohit",
#     "age": 22,
#     "grade": "A"
#   },
#   "add_student": {
#     "name": "Arjun",
#     "age": 21,
#     "grade": "unknown"
#   },
#   "update_student": {
#     "name": "Rohit Sharma",
#     "age": 23,
#     "grade": "A+"
#   },
#   "delete_student": {
#     "name": "Meera",
#     "age": 20,
#     "grade": "B"
#   }
# }
