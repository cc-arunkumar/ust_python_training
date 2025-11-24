# CRUD Task
# Simpler use-case: UST Employee API

from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(title="Students CRUD (In-Memory)")

# Define a Pydantic model for the Student data
class Student(BaseModel):
    name: str
    age: int
    grade: str = "unknown"  # Default grade is "unknown"

# In-memory list to store student data
students: List[Student] = []

# Endpoint to create a new student
@app.post("/student")
def create_student(student: Student):
    students.append(student)  # Append new student to the in-memory list
    return {"Student created": student}

# Endpoint to get all students
@app.get("/student", response_model=List[Student])
def get_student():
    return students  # Return the list of all students


# Endpoint to get a student by index
@app.get("/student/{index}", response_model=Student)
def get_student_by_index(index: int):
    try:
        return students[index]  # Return student at the specified index
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")  # Error if index is out of bounds

# Endpoint to update a student's data
@app.put("/student/{index}", response_model=Student)
def update_student(index: int, updated_student: Student):
    try:
        students[index] = updated_student  # Replace student at specified index
        return updated_student
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")  # Error if index is out of bounds

# Endpoint to delete a student by index
@app.delete("/student/{index}", response_model=Student)
def delete_student(index: int):
    try:
        removed = students.pop(index)  # Remove student at specified index
        return removed
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")  # Error if index is out of bounds


# Sample output


# **Expected Output for POST /student**
# Input:
# {
#     "name": "Alice",
#     "age": 20,
#     "grade": "A"
# }
# Output:
# {"Student created": {"name": "Alice", "age": 20, "grade": "A"}}

# **Expected Output for GET /student**
# If there are 2 students:
# Output:
# [
#     {"name": "Alice", "age": 20, "grade": "A"},
#     {"name": "Bob", "age": 21, "grade": "B"}
# ]
# **Expected Output for GET /student/{index}**
# If index=0 and the student exists:
# Output:
# {"name": "Alice", "age": 20, "grade": "A"}
# If index=3 (nonexistent):
# Output:
# HTTPException: 404 Not Found - Student not found

# **Expected Output for PUT /student/{index}**
# Input:
# {
#     "name": "Alice",
#     "age": 20,
#     "grade": "A+"
# }
# If index=0 (valid student):
# Output:
# {"name": "Alice", "age": 20, "grade": "A+"}
# If index=3 (nonexistent):
# Output:
# HTTPException: 404 Not Found - Student not found

# **Expected Output for DELETE /student/{index}**
# If index=0 (valid student):
# Output:
# {"name": "Alice", "age": 20, "grade": "A"}
# If index=3 (nonexistent):
# Output:
# HTTPException: 404 Not Found - Student not found
