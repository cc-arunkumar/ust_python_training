from fastapi import HTTPException, FastAPI
from typing import List
from pydantic import BaseModel

# Create FastAPI app with a title for the API documentation
app = FastAPI(title="Students CRUD Operations(IN-Memory)")

# Pydantic model to define the structure of a Student object
class Student(BaseModel):
    name: str  # Name of the student (required)
    age: int  # Age of the student (required)
    grade: str = "Unknown"  # Grade of the student (optional, default is "Unknown")

# In-memory list to store students
students_list: List[Student] = []

# Endpoint to create a new student record
@app.post("/students")
def create_students(student: Student):
    # Append the newly created student to the students_list
    students_list.append(student)
    return {"Student Created": student}  # Return the created student data

# Endpoint to get the list of all students
@app.get("/student", response_model=List[Student])
def display_all_students():
    # Return the list of all students
    return students_list

# Endpoint to get a particular student based on the index (position) in the list
@app.get("/student/{index}")
def get_particular_info(index: int):
    try:
        # Return the student at the given index
        return students_list[index]
    except IndexError:
        # Raise an HTTPException if the index is invalid (out of bounds)
        raise HTTPException(status_code=404, detail="Student not found")

# Endpoint to update a student's information based on the index
@app.put("/student/{index}", response_model=Student)
def update_student(index: int, student: Student):
    try:
        # Update the student data at the given index
        students_list[index] = student
        return student  # Return the updated student
    except IndexError:
        # Raise an HTTPException if the student at the given index doesn't exist
        raise HTTPException(status_code=404, detail="Student detail was not found")

# Endpoint to delete a student from the list based on the index
@app.delete("/students/{index}", response_model=Student)
def delete_student(index: int):
    try:
        # Remove and return the student from the list at the given index
        removed = students_list.pop(index)
        return removed
    except IndexError:
        # Raise an HTTPException if the student at the given index doesn't exist
        raise HTTPException(status_code=404, detail="The student is not present")
