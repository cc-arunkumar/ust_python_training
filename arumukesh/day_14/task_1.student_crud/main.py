from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize FastAPI app with a title "Student CRUD"
app = FastAPI(title="Student CRUD")

# Define the Student model, which will be used for creating, updating, and returning student data
class Student(BaseModel):
    name: str        # The name of the student (string)
    age: int         # The age of the student (integer)
    grade: str = "unknown"  # The grade of the student (string, default value is "unknown")

# List to hold student records, initially empty
students: List[Student] = []

# POST endpoint to create a new student
@app.post("/student")
def create_student(student: Student):
    # Print the student data for debugging purposes
    print("--> ", student)
    # Append the new student to the students list
    students.append(student)
    # Return the created student in the response body
    return {"student": student}

# GET endpoint to retrieve a specific student by index in the list
@app.get("/students/{index}", response_model=Student)
def get_student(index: int):
    try:
        # Return the student at the specified index
        return students[index]
    except IndexError:
        # If the index is invalid (out of bounds), return an error message
        return {"detail": "Index value not found!"}

# GET endpoint to retrieve all students
@app.get("/students", response_model=List[Student])
def get_students():
    # Return the entire list of students
    return students

# PUT endpoint to update an existing student by index
@app.put("/student/{index}")
def update_students(index: int, updated_student: Student):
    try:
        # Update the student at the specified index with the new data
        students[index] = updated_student
        # Return a success message
        return {"message": "Update completed"}
    except IndexError:
        # If the index is invalid (out of bounds), raise an HTTP error
        raise HTTPException(status_code=404, detail="Not a valid index")

# DELETE endpoint to remove a student by index
@app.delete("/student/{index}", response_model=Student)
def student_delete(index: int):
    try:
        # Remove the student at the specified index
        deleted_student = students.pop(index)
        # Return a success message with the remaining students in the list
        return {"message": "DELETE DONE!!", "remaining_students": students}
    except IndexError:
        # If the index is invalid (out of bounds), raise an HTTP error
        raise HTTPException(status_code=404, detail="Not a valid index")
