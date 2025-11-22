from typing import List
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI(title="Student CRUD")

class Student(BaseModel):
    name:str
    age:int
    grade:str="unknown"
    
students:List[Student]=[]

@app.post("/student")
def create_student(student:Student):
    print("--> ",student)
    students.append(student)
    return {"student":student}
    # def create_student(student:Student)
    
    
@app.get("/students/{index}",response_model=Student)
def get_student(index:int):
    try:
        return students[index]
    except IndexError:
        return {"Index value not in file!"}
    
@app.get("/students",response_model=List[Student])
def get_students():
    return students


@app.put("/student/{index}")
def update_students(index:int,updated_student:Student):
    try:
        students[index]=updated_student
        return {"Update completed"}
    except IndexError:
        raise HTTPException("Not valid index")

@app.delete("/student/{index}",response_model=Student)
def student_delete(index:int):
    try:
        students.remove(students[index])
        return {"DELETE DONE !!",students}
    except IndexError:
        raise HTTPException("Not valid index")
          

    
