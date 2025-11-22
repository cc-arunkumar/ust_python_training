from fastapi import FastAPI,HTTPException
from typing import List
from pydantic import BaseModel

app=FastAPI(title="Students crud operstions")
class Student(BaseModel):
    name:str
    age:int
    grade:str= "unknown"
    
students:List[Student]=[]

@app.post("/students",response_model=Student)
def create_student(student:Student):
    students.append(student)
    return student

@app.get('/students',response_model=List[Student])
def get_students():
    return students

@app.get('/students/{index}',response_model=Student)
def get_students(index:int):
    try:
        return students[index]
    except IndexError:
        raise HTTPException(status_code=404,detail="student not found")
    
@app.put('/students/{index}',response_model=Student)
def update_student(index:int,update_student:Student):
    try:
        students[index]=update_student
        return update_student
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found")
    
@app.delete('/students/{index}',response_model=Student)
def delete_student(index:int):
    try:
        removed=students.pop(index)
        return removed
    except IndexError:
        raise HTTPException(status_code=404,detail="Student not found")
    