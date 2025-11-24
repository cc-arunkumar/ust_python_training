from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# FastAPI app initialization
app = FastAPI(title="Student CRUD (In-Memory)")

# Student model
class Student(BaseModel):
    name: str
    age: int
    grade: str = "unknown"  # Default grade is "unknown"

# In-memory student data (list to store students)
students: List[Student] = []

# Endpoint to add a new student
@app.post("/add")
def create_student(student: Student):
    students.append(student)
    return {"Student created": student}

# Endpoint to get the list of all students
@app.get("/students", response_model=List[Student])
def get_students():
    return students

# Endpoint to get a student by index
@app.get("/students/{index}", response_model=Student)
def get_student(index: int):
    try:
        return students[index]
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")

# Endpoint to update a student at a specific index
@app.put("/update", response_model=Student)
def update(index: int, update_student: Student):
    try:
        students[index] = update_student
        return update_student
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")

# Endpoint to delete a student by index
@app.delete("/delete", response_model=Student)
def delete_student(index: int):
    try:
        removed = students.pop(index)
        return removed
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")

# Main function to print "Hello from day14!"
def main():
    print("Hello from day14!")

# Start the application when the script is executed
if __name__ == "__main__":
    main()

# Sample Output:

"""
Sample Output for /add (POST):
Input: 
{
    "name": "John Doe",
    "age": 20,
    "grade": "A"
}
Output:
{
    "Student created": {
        "name": "John Doe",
        "age": 20,
        "grade": "A"
    }
}

Sample Output for /students (GET):
Output:
[
    {
        "name": "John Doe",
        "age": 20,
        "grade": "A"
    }
]

Sample Output for /students/0 (GET):
Input: /students/0
Output:
{
    "name": "John Doe",
    "age": 20,
    "grade": "A"
}

Sample Output for /update (PUT):
Input: 
{
    "index": 0, 
    "update_student": {
        "name": "John Smith", 
        "age": 21, 
        "grade": "B"
    }
}
Output:
{
    "name": "John Smith",
    "age": 21,
    "grade": "B"
}

Sample Output for /delete (DELETE):
Input: /delete (index=0)
Output:
{
    "name": "John Smith",
    "age": 21,
    "grade": "B"
}

"""
