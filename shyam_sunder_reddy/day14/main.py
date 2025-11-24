from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# -----------------------------
# FastAPI Application
# -----------------------------
application = FastAPI(title="Student CRUD (In memory)")

# -----------------------------
# Data Model
# -----------------------------
class Student(BaseModel):
    """
    Student schema:
    - name: required string
    - age: required integer
    - grade: optional string, defaults to "unknown"
    """
    name: str
    age: int
    grade: str = "unknown"

# -----------------------------
# In-Memory Storage
# -----------------------------
students: List[Student] = []


# -----------------------------
# CRUD Endpoints
# -----------------------------

@application.post("/students")
def create_student(student: Student):
    """
    Create a new student and add to the list.

    Sample Output:
    POST /students
    Request Body:
    {
      "name": "Alice",
      "age": 20,
      "grade": "A"
    }

    Response:
    {
      "student created": {
        "name": "Alice",
        "age": 20,
        "grade": "A"
      }
    }
    """
    students.append(student)
    return {"student created": student}


@application.get("/students", response_model=List[Student])
def display_all_students():
    """
    Get all students.

    Sample Output:
    GET /students
    [
      {"name":"Alice","age":20,"grade":"A"},
      {"name":"Bob","age":22,"grade":"unknown"}
    ]
    """
    return students


@application.get("/students/{index}", response_model=Student)
def display_by_id(index: int):
    """
    Get a student by index in the list.

    Sample Output:
    GET /students/0
    {"name":"Alice","age":20,"grade":"A"}

    Error Case:
    GET /students/99
    Response: 404 {"detail":"Student not found"}
    """
    try:
        return students[index]
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")


@application.put("/students/{index}", response_model=Student)
def update_byid(index: int, updated: Student):
    """
    Update a student by index.

    Sample Output:
    PUT /students/0
    Request Body:
    {"name":"Alice","age":21,"grade":"B"}

    Response:
    {"name":"Alice","age":21,"grade":"B"}

    Error Case:
    PUT /students/99
    Response: 404 {"detail":"Student not found"}
    """
    try:
        students[index] = updated
        return updated
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")


@application.delete("/students/{index}", response_model=Student)
def delete_byid(index: int):
    """
    Delete a student by index.

    Sample Output:
    DELETE /students/0
    Response:
    {"name":"Alice","age":20,"grade":"A"}

    Error Case:
    DELETE /students/99
    Response: 404 {"detail":"Student not found"}
    """
    try:
        removed = students.pop(index)
        return removed
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")
