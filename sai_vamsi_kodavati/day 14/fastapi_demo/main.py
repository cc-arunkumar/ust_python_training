from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize the FastAPI app with a custom title
app = FastAPI(title="Students CRUD (In-Memory)")

# Define the Student model with Pydantic (used for request and response validation)
class Student(BaseModel):
    name: str         # Name of the student
    age: int          # Age of the student
    grade: str = "unknown"  # Default value for grade if not provided

# In-memory "database" to store students. This will be used to simulate the student data storage.
students: List[Student] = []

# Create a new student and add it to the "database"
@app.post("/students", response_model=Student)
def create_student(student: Student):
    # Append the new student to the students list
    students.append(student)
    # Return the student object
    return student

# Retrieve all students from the "database"
@app.get("/students", response_model=List[Student])
def get_students():
    # Return the list of all students
    return students

# Retrieve a specific student by their index in the list
@app.get("/students/{index}", response_model=Student)
def get_student(index: int):
    try:
        # Return the student at the specified index
        return students[index]
    except IndexError:
        # Raise a 404 HTTPException if the student is not found
        raise HTTPException(status_code=404, detail="Student not found")

# Update the details of an existing student based on their index
@app.put("/students/{index}", response_model=Student)
def update_student(index: int, updated_student: Student):
    try:
        # Replace the student at the specified index with the updated student
        students[index] = updated_student
        # Return the updated student object
        return updated_student
    except IndexError:
        # Raise a 404 HTTPException if the student is not found
        raise HTTPException(status_code=404, detail="Student not found")

# Delete a student by their index
@app.delete("/students/{index}", response_model=Student)
def delete_student(index: int):
    try:
        # Remove and return the student at the specified index
        removed_student = students.pop(index)
        return removed_student
    except IndexError:
        # Raise a 404 HTTPException if the student is not found
        raise HTTPException(status_code=404, detail="Student not found")


# -----------------------------------------------------------------------------------------

# Sample Output

# 1. POST /students - Create a new student

# Request:

# POST /students
# Content-Type: application/json

# {
#   "name": "John Doe",
#   "age": 20,
#   "grade": "A"
# }
# Response:

# {
#   "name": "John Doe",
#   "age": 20,
#   "grade": "A"
# }

# 2. GET /students - Retrieve all students

# Request:

# GET /students
# Response:

# [
#   {
#     "name": "John Doe",
#     "age": 20,
#     "grade": "A"
#   }
# ]

# 3. GET /students/{index} - Retrieve a student by index

# Request:

# GET /students/0

# Response:
# {
#   "name": "John Doe",
#   "age": 20,
#   "grade": "A"
# }

# 4. GET /students/{index} - Retrieve a student by index (non-existent index)
# Request:

# GET /students/1
# Response:

# {
#   "detail": "Student not found"
# }

# 5. PUT /students/{index} - Update an existing student

# Request:

# PUT /students/0
# Content-Type: application/json

# {
#   "name": "Jane Doe",
#   "age": 21,
#   "grade": "B"
# }
# Response:

# {
#   "name": "Jane Doe",
#   "age": 21,
#   "grade": "B"
# }

# 6. PUT /students/{index} - Update a student (non-existent index)
# Request:

# PUT /students/1
# Content-Type: application/json

# {
#   "name": "Mary Jane",
#   "age": 22,
#   "grade": "A"
# }
# Response:
# {
#   "detail": "Student not found"
# }

# 7. DELETE /students/{index} - Delete a student by index

# Request:
# DELETE /students/0
# Response:
# {
#   "name": "Jane Doe",
#   "age": 21,
#   "grade": "B"
# }

# 8. DELETE /students/{index} - Delete a student by index (non-existent index)
# Request:
# DELETE /students/1
# Response:

# {
#   "detail": "Student not found"
# }
