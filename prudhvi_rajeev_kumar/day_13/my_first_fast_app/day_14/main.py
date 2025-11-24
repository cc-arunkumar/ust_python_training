from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# FastAPI app initialization with the title for the Student Management System.
app = FastAPI(title="Testing CRUD Operations on Student Management System.")

# Student model defining the attributes for a student: name, age, and grade.
# The grade defaults to "unknown" if not provided.
class Student(BaseModel):
    name: str  # Name of the student.
    age: int  # Age of the student.
    grade: str = "unknown"  # Grade of the student, defaults to "unknown".

# List to hold the student records in memory (as a simple mock database).
students: list[Student] = []

# Endpoint to create a new student.
# Takes a Student object as input and appends it to the students list.
@app.post("/students")
def create_student(student: Student):
    # Add the new student to the list.
    students.append(student)
    # Return a confirmation message with the student details.
    return {"Student Created": student}

# Endpoint to retrieve all students.
# Returns a list of all student records.
@app.get("/students", response_model=list[Student])
def get_students():
    return students

# Endpoint to retrieve a specific student by their index in the list.
# If the student does not exist (index out of range), raises a 404 error.
@app.get("/students/{index}", response_model=Student)
def get_student(index: int):
    try:
        # Return the student at the specified index.
        return students[index]
    except IndexError:
        # If the index is out of range, raise an HTTP 404 error.
        raise HTTPException(status_code=404, detail="Student Not Found!")

# Endpoint to update the details of an existing student by their index.
# Takes the updated student data and replaces the student at the specified index.
@app.put("/students/{index}", response_model=Student)
def update_student(index: int, updated_student: Student):
    try:
        # Update the student at the specified index with the new data.
        students[index] = updated_student
        return updated_student
    except IndexError:
        # If the student with the given index is not found, raise an HTTP 404 error.
        raise HTTPException(status_code=404, detail="Student Not Found!")

# Endpoint to delete a student by their index.
# Removes the student from the list and returns the deleted student data.
@app.delete("/students/{index}", response_model=Student)
def delete_student(index: int):
    try:
        # Remove and return the student at the specified index.
        removed = students.pop(index)
        return removed
    except IndexError:
        # If the index is out of range, raise an HTTP 404 error.
        raise HTTPException(status_code=404, detail="Student Not Found!")

# Sample Responses Section:

# 1. Sample response when creating a new student:
# POST /students
# Request Body:
# {
#   "name": "John Doe",
#   "age": 20,
#   "grade": "A"
# }

# Response:
# {
#   "Student Created": {
#     "name": "John Doe",
#     "age": 20,
#     "grade": "A"
#   }
# }

# 2. Sample response when fetching all students:
# GET /students
# Request:
# (No input)
# 
# Response:
# [
#   {
#     "name": "John Doe",
#     "age": 20,
#     "grade": "A"
#   },
#   {
#     "name": "Jane Smith",
#     "age": 22,
#     "grade": "B"
#   }
# ]

# 3. Sample response when fetching a student by index:
# GET /students/{index}
# Request (index = 0):
# {
#   "index": 0
# }

# Response:
# {
#   "name": "John Doe",
#   "age": 20,
#   "grade": "A"
# }

# 4. Sample response when updating a student's details:
# PUT /students/{index}
# Request (index = 0, updated student):
# {
#   "name": "John Doe",
#   "age": 21,
#   "grade": "A+"
# }

# Response:
# {
#   "name": "John Doe",
#   "age": 21,
#   "grade": "A+"
# }

# 5. Sample response when deleting a student by index:
# DELETE /students/{index}
# Request (index = 0):
# {
#   "index": 0
# }

# Response:
# {
#   "name": "John Doe",
#   "age": 20,
#   "grade": "A"
# }

# 6. Sample response for attempting to fetch a student who does not exist (404):
# GET /students/{index}
# Request (index = 10):
# {
#   "index": 10
# }

# Response (404):
# {
#   "detail": "Student Not Found!"
# }

# 7. Sample response for attempting to update a student who does not exist (404):
# PUT /students/{index}
# Request (index = 10, updated student):
# {
#   "name": "John Doe",
#   "age": 21,
#   "grade": "A+"
# }

# Response (404):
# {
#   "detail": "Student Not Found!"
# }

# 8. Sample response for attempting to delete a student who does not exist (404):
# DELETE /students/{index}
# Request (index = 10):
# {
#   "index": 10
# }

# Response (404):
# {
#   "detail": "Student Not Found!"
# }
