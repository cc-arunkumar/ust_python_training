from typing import List
from pydantic import BaseModel
from fastapi import FastAPI,HTTPException


app = FastAPI(title="Students CRUD(I-memory)")


class Student(BaseModel):
    name:str
    age:int
    grade:str="unknown"
    
student : List[Student] = []

@app.get("/students",response_model=Student)
def getStudent():
    return student

@app.get("/students/{index}",response_model=List[Student])
def get_students_by_id(index:int):
    try:
        
        return student[index]
    except IndexError:
        raise HTTPException(status_code=404,detail="student not found")
    
@app.post("/students",response_model=Student)
def add_student(student:Student):
    student.append(student)
    return student
    
@app.put("/students/{index}", response_model=Student)
def update_delete(index:int,update_student=Student):
    try:
        
        student[index] = student
    except HTTPException:
        raise HTTPException(status_code=404,detail="student not found")
    
@app.delete("/students/{index}", response_model=Student)
def delete_student(index:int):
    try:
        removed = student.pop(index)
        return removed
    except IndexError:
        HTTPException(status_code=404,detail="studet not found")
        
    
        
