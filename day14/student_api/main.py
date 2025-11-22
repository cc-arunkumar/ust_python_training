from fastapi import FastAPI, HTTPException  # Import FastAPI and HTTPException for error handling
from pydantic import BaseModel  # Import BaseModel from Pydantic for data validation
from typing import List  # Import List from typing to specify that we are using a list

# Initialize the FastAPI app with the title "Student Management System"
app = FastAPI(title="Student Management System")

# Define the Student model with name, age, and grade
class Student(BaseModel):
    name: str  # Student name
    age: int  # Student age
    grade: str = "Not Provided"  # Default grade is "Not Provided"

# In-memory list to store students
students: List[Student] = []

# ---------------------- ENDPOINTS ----------------------

# Add a new student to the list
@app.post("/students", response_model=Student)
def add_student(student: Student):
    students.append(student)  # Append the new student to the list
    return student  # Return the added student

# Get the list of all students
@app.get("/students", response_model=List[Student])
def get_all_students():
    return students  # Return the full list of students

# Get a student by their index in the list
@app.get("/students/{index}", response_model=Student)
def get_student_by_index(index: int):
    try:
        return students[index]  # Return the student at the given index
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")  # Handle case where index is out of range

# Update a student by their index
@app.put("/students/{index}", response_model=Student)  # Fixed the typo here ("syudents" -> "students")
def update_student(index: int, updated_student: Student):
    try:
        students[index] = updated_student  # Replace the student at the given index with the updated student
        return updated_student  # Return the updated student
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")  # Handle case where index is out of range

# Delete a student by their index
@app.delete("/students/{index}", response_model=Student)
def delete_student(index: int):
    try:
        removed = students.pop(index)  # Remove the student at the given index
        return removed  # Return the student that was removed
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")  # Handle case where index is out of range
