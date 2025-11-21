from typing import List
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI(title="Student CRUD (In-Memory)")

class Student(BaseModel):
    name: str
    age: int
    grade: str = "unknown"

students : List[Student] = []

@app.post("/add")
def create_student(student:Student):
    students.append(student)    
    return {"Student created" : student}
    
@app.get("/students",response_model=List[Student])
def get_students():
    return students
        

@app.get("/students/{index}",response_model=Student)
def get_student(index:int):
    try:
        return students[index]
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found")
    
@app.put("/update",response_model=Student)
def update(index:int,update_student:Student):
    try:
        students[index]=update_student
        return update_student
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found")
    
@app.delete("/delete",response_model=Student)
def delete_student(index:int):
    try:
        removed = students.pop(index)
        return removed
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found")
        


def main():
    print("Hello from day14!")


if __name__ == "__main__":
    main()
