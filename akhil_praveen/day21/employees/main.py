import pymysql
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field,EmailStr,model_validator
from typing import Optional
from datetime import date
 
def get_connection():
    # Establish connection to MySQL database
    conn = pymysql.connect(
        host="localhost",      # Database host
        user="root",           # Database username
        password="pass@word1", # Database password
        database="ust_emp_db", # Database name
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Connection Established")  # Confirmation message
    return conn  # Return connection object
 
app = FastAPI(title="Employee Management")
 
class Employee(BaseModel):
    first_name : str = Field(...,pattern=r"^[A-Za-z -]+$",max_length=50)
    last_name : str = Field(...,pattern=r"^[A-Za-z -]+$",max_length=50)
    email : EmailStr = Field(...,max_length=50)
    position : Optional[str] = Field(max_length=100,pattern=r"^[A-Za-z0-9 -]+$")
    salary : Optional[float] = Field(gt=0)
    hire_date : date
 
    @model_validator(mode="after")
    def check_date(self):
        if self.hire_date > date.today():
            raise HTTPException(status_code=422,detail="Cannot be a future date")
        return self
       
 
@app.post("/employees/")
def create_employee(emp:Employee):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query="""
insert into ust_emp_db.employees (first_name,last_name,email,position,salary,hire_date)
values (%s,%s,%s,%s,%s,%s);
"""    
        cursor.execute(query,tuple(emp.__dict__.values()))
        conn.commit()
        return {"employee_id":cursor.lastrowid}
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))
   
 
@app.get("/employees/{emp_id}")
def get_emp_by_id(emp_id : int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("Select * from ust_emp_db.employees where employee_id=%s",(emp_id,))
        data = cursor.fetchone()
        if data:
            return data
        else:
            raise Exception("Employee Not Found")
    except Exception as e:
        raise HTTPException(status_code=404,detail=str(e))
   
@app.put("/employees/{emp_id}")
def update_emp(emp_id:int,emp:Employee):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if get_emp_by_id(emp_id):
            query="""
    update ust_emp_db.employees set first_name=%s,last_name=%s,email=%s,position=%s,salary=%s,hire_date=%s
    where employee_id=%s;
    """
            tup =tuple(emp.__dict__.values()) + (emp_id,)
            cursor.execute(query,tup)
            conn.commit()
            return get_emp_by_id(emp_id)
        else:
            raise Exception("Employee Not Found")
    except Exception as e:
        raise HTTPException(status_code=404,detail=str(e))
   
@app.delete("/employees/{emp_id}")
def delete_emp(emp_id:int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        data = get_emp_by_id(emp_id)
        if data:
            cursor.execute("delete from ust_emp_db.employees where employee_id=%s",(emp_id,))
            conn.commit()
            return {"message":"Deleted Successfully"}
        else:
            raise Exception("Employee Not Found")
    except Exception as e:
        raise HTTPException(status_code=404,detail=str(e))
 
 
 
 
 
 