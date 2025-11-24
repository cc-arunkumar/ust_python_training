# def main():
#     print("Hello from day14!")


# if __name__ == "__main__":
#     main()

from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(title="Students CRUD(In-memory)")

# Pydantic model for Student data validation
class Student(BaseModel):
    name: str  # Student name (mandatory)
    age: int  # Student age (mandatory)
    grade: str = "unknown"  # Student grade (optional, defaults to "unknown")
    
# In-memory data storage for students
# Note: For production, replace this with a persistent database solution.
students: List[Student] = []

# Create a new student record
@app.post("/students")
def create_student(student: Student):
    students.append(student)  # Append the student to the list
    return {"Student Created": student}  # Return created student details

# Get all students
@app.get("/students", response_model=List[Student])
def get_students():
    # Return the list of all students
    return students

# Get a specific student by index
@app.get("/students/{index}", response_model=Student)
def get_student(index: int):
    try:
        return students[index]  # Return student at specified index
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")  # Raise error if index is out of range
    
# Update a specific student by index
@app.put("/students/{index}", response_model=Student)
def update_student(index: int, updated_student: Student):
    try:
        students[index] = updated_student  # Update student details at specified index
        return updated_student  # Return updated student details
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")  # Raise error if index is out of range
    
# Delete a student by index
@app.delete("/students/{index}", response_model=Student)
def delete_student(index: int):
    try:
        removed = students.pop(index)  # Remove student at specified index
        return removed  # Return the removed student details
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")  # Raise error if index is out of range
