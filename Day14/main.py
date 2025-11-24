from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Madhan CRUD (In-Memory)")

# Student model
# Defines the structure of a student object with name, age, and grade.
# Default grade is set to "unknown" if not provided.
class Student(BaseModel):
    name: str
    age: int
    grade: str = "unknown"

# In-memory list
# This list will store all student records temporarily while the app runs.
students: List[Student] = []

# Create a new student
# Endpoint: POST /students
# Accepts a Student object in the request body, appends it to the list,
# and returns a confirmation message with the student data.
@app.post("/students")
def create_student(student: Student):
    students.append(student)
    return {"Student created": student}

# Get a student by index
# Endpoint: GET /students?index={number}
# Retrieves a student from the list using its index.
# If the index is invalid, returns a 404 error.
@app.get("/students", response_model=Student)
def get_student(index: int):
    try:
        return students[index]
    except IndexError:
        raise HTTPException(status_code=404, detail="Student Not Found")

# Get all students
# Endpoint: GET /Students/
# Returns the entire list of students.
@app.get("/Students/")
def get_student():
    return students

# Update a student by index
# Endpoint: PUT /student/{index}
# Replaces the student at the given index with new data.
# If the index is invalid, returns a 404 error.
@app.put("/student/{index}", response_model=Student)
def update_student(index: int, updated_student: Student):
    try:
        students[index] = updated_student
        return updated_student
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")

# Delete a student by index
# Endpoint: DELETE /students/{index}
# Removes the student at the given index from the list and returns the deleted record.
# If the index is invalid, returns a 404 error.
@app.delete("/students/{index}", response_model=Student)
def delete_student(index: int):
    try:
        removed = students.pop(index)
        return removed
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")

    
# Sample Output for Madhan CRUD (Important Test Cases)

# Test 1: Create a New Student
## Input:
# POST /students
# {
#   "name": "Arun",
#   "age": 21,
#   "grade": "A"
# }

## Output:
# HTTP Status: 200 OK
# {
#   "Student created": {
#     "name": "Arun",
#     "age": 21,
#     "grade": "A"
#   }
# }


# Test 2: Get Student by Index
## Input:
# GET /students?index=0

## Output:
# HTTP Status: 200 OK
# {
#   "name": "Arun",
#   "age": 21,
#   "grade": "A"
# }



# Test 3: Get All Students
## Input:
# GET /Students/

## Output:
# HTTP Status: 200 OK
# [
#   {
#     "name": "Arun",
#     "age": 21,
#     "grade": "A"
#   }
# ]



# Test 4: Update Student by Index
## Input:
# PUT /student/0
# {
#   "name": "Arun Kumar",
#   "age": 22,
#   "grade": "B"
# }

## Output:
# HTTP Status: 200 OK
# {
#   "name": "Arun Kumar",
#   "age": 22,
#   "grade": "B"
# }


# Test 5: Delete Student by Index
## Input:
# DELETE /students/0

## Output:
# HTTP Status: 200 OK
# {
#   "name": "Arun Kumar",
#   "age": 22,
#   "grade": "B"
# }



# Test 6: Get Student by Invalid Index
## Input:
# GET /students?index=5

## Output:
# HTTP Status: 404 Not Found
# {
#   "detail": "Student Not Found"
# }


# Test 7: Update Student by Invalid Index
## Input:
# PUT /student/10
# {
#   "name": "Madhan",
#   "age": 23,
#   "grade": "C"
# }

## Output:
# HTTP Status: 404 Not Found
# {
#   "detail": "Student not found"
# }


# Test 8: Delete Student by Invalid Index
## Input:
# DELETE /students/10

## Output:
# HTTP Status: 404 Not Found
# {
#   "detail": "Student not found"
# }

