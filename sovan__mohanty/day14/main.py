#Task Students CRUD(IN-Memory)

from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Students CRUD(IN-Memory)")

# Student model
class Student(BaseModel):
    name: str
    age: int
    grade: str = "unknown"

# In-memory list of students
students: List[Student] = []

@app.post("/students")
def create_student(student: Student):
    # Create a new student and add to list
    students.append(student)
    return {"Student Created": student}

@app.get("/students", response_model=List[Student])
def get_students():
    # Return all students
    return students

@app.get("/students/{index}", response_model=Student)
def get_student(index: int):
    # Return student by index; 404 if not found
    try:
        return students[index]
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")

@app.put("/students/{index}", response_model=Student)
def update_student(index: int, updated_student: Student):
    # Update student at given index
    try:
        students[index] = updated_student
        return updated_student
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{index}", response_model=Student)
def delete_student(index: int):
    # Delete student at given index
    try:
        removed = students.pop(index)
        return removed
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")

#Sample Executions
# Create Student
# {
#   "Student Created": {
#     "name": "Asha",
#     "age": 20,
#     "grade": "A"
#   }
# }

# Get All Students
# [
#   {"name":"Asha","age":20,"grade":"A"}
# ]

# Get Student by Index

# {"name":"Asha","age":20,"grade":"A"}

# Update Student

# {"name":"Asha Rao","age":21,"grade":"B"}

# Delete Student

# {"name":"Asha Rao","age":21,"grade":"B"}
