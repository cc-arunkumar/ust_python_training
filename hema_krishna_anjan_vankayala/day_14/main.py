from typing import List
from fastapi import FastAPI , HTTPException
from pydantic import BaseModel 

# Initialize FastAPI app with title
app = FastAPI(title="Student CRUD")

#  DATA MODEL
class Student(BaseModel):
    # Represents a student record
    name: str          # Student's name
    age: int           # Student's age
    grade: str = "unknown"  # Default grade if not provided

# In-memory list to store students
students: List[Student] = []

# API ENDPOINTS

# POST /students → Create a new student
@app.post("/students")
def create_student(student: Student):
    # Append new student to the list
    students.append(student)
    return {"Student Created": student}

# SAMPLE OUTPUT:
# Request Body:
# { "name": "Rahul Sharma", "age": 20, "grade": "A" }
# Response:
# { "Student Created": { "name": "Rahul Sharma", "age": 20, "grade": "A" } }

# GET /students → Retrieve all students
@app.get("/students", response_model=List[Student])
def get_students():
    # Return the full list of students
    return students

# SAMPLE OUTPUT:
# [
#   { "name": "Rahul Sharma", "age": 20, "grade": "A" },
#   { "name": "Priya Singh", "age": 22, "grade": "B" }
# ]

# GET /students/{index} → Retrieve student by index
@app.get("/students/{index}", response_model=Student)
def get_student(index: int):
    try:
        # Return student at given index
        return students[index]
    except IndexError:
        # If index is invalid, raise 404 error
        raise HTTPException(status_code=404, detail="Student Not Found")

# SAMPLE OUTPUT:
# Request: GET /students/0
# Response: { "name": "Rahul Sharma", "age": 20, "grade": "A" }
# Error Example: GET /students/10 → { "detail": "Student Not Found" }

# PUT /students/{index} → Update student at given index
@app.put("/students/{index}", response_model=Student)
def update_statement(index: int, updated_student: Student):
    try:
        # Replace student at given index with new data
        students[index] = updated_student
        return updated_student
    except IndexError:
        # If index is invalid, raise 404 error
        raise HTTPException(status_code=404, detail="Student Not Found")

# SAMPLE OUTPUT:
# Request Body:
# { "name": "Anjali Verma", "age": 21, "grade": "A+" }
# Response:
# { "name": "Anjali Verma", "age": 21, "grade": "A+" }

# DELETE /students/{index} → Delete student at given index
@app.delete('/students/{index}', response_model=Student)
def delete_student(index: int):
    try:
        # Remove student at given index and return deleted record
        removed = students.pop(index)
        return removed
    except IndexError:
        # If index is invalid, raise 404 error
        raise HTTPException(status_code=404, detail="Student Not Found")

# SAMPLE OUTPUT:
# Request: DELETE /students/1
# Response: { "name": "Priya Singh", "age": 22, "grade": "B" }
# Error Example: DELETE /students/10 → { "detail": "Student Not Found" }
