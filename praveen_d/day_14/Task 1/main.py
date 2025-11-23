from fastapi import HTTPException,FastAPI
from typing import List
from pydantic import BaseModel

app=FastAPI(title="Students CRUD Operations(IN-Memory)")

# @app.get("/students")
# def students():
#     return {"HI guys"}

class Student(BaseModel):
    name:str
    age:int
    grade:str="Unknown"
students_list:List[Student]=[]

@app.post("/students")
def create_students(student:Student):
    students_list.append(student)
    return {"Student Created":student}

@app.get("/student",response_model=List[Student])
def display_all_students():
    return students_list

@app.get("/student/{index}")
def get_particular_info(index:int):
    try:
        return students_list[index]
    except IndexError:
        raise HTTPException(status_code=404, detail="Student not found")

@app.put("/student/{index}",response_model=Student)
def update_student(index:int,student:Student):
    try:
        students_list[index]=student
        return student
    except HTTPException:
        raise HTTPException(status_code=404,detail="Student detail was not found")
    
@app.delete("/students/{index}",response_model=Student)
def delete_student(index:int):
    try:
        removed=students_list.pop(index)
        return removed
    except HTTPException:
        raise HTTPException(status_code=404,detail="The student is not present")

