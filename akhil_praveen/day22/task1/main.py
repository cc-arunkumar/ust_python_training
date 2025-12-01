from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel,Field,model_validator
from typing import Optional,Literal
import re
from datetime import datetime,date,timedelta
import os
from dotenv import load_dotenv
from auth import create_access_token,get_current_user,User,Token,LoginRequest
import pymysql

load_dotenv()

app = FastAPI(title="UST Employee Training Request Management")

class StatusValidation(BaseModel):
    status : str = Literal["PENDING","APPROVED","REJECTED"]
   

class TrainingRequest(BaseModel):
    employee_id : str = Field(...,pattern=r"^UST[0-9]+$")
    employee_name :  str = Field(...,pattern=r"^[A-Za-z ]+$")
    training_title : str = Field(...,min_length=5)
    training_description : str = Field(...,min_length=10)
    requested_date : date
    status : str = Literal["PENDING","APPROVED","REJECTED"]
    manager_id :  str = Field(...,pattern=r"^UST[0-9]+$") 
    @model_validator(mode="after")
    def validation(self):
        if self.requested_date>date.today():
            raise HTTPException(status_code=404,detail="Requested date cannot be a future date!")
        return self
        

DEMO_USERNAME = os.getenv("DEMO_USERNAME")
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD")

# Token lifetime in minutes (as string in env, converted to int when used).
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
BASE_URL= "/api/v1/training-requests/"


# Function to establish and return a connection to the MySQL database
def get_connection():
    conn = pymysql.connect(
        host="localhost",           # The host where the MySQL server is running (localhost for local connection)
        user=os.getenv("db_username"),                # The MySQL username
        password=os.getenv("db_password"),  
        database="ust_training_db",
        cursorclass=pymysql.cursors.DictCursor  # Use DictCursor to get results as dictionaries

    )
    return conn
def close_connection(conn,cursor):
    if conn.open:
        conn.close()
        cursor.close()
        print("connection closed!")


@app.post("/login",response_model=Token)
def login(data:LoginRequest,):
    if data.username!= DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(status_code=401,detail="Incorrect username or password!")
    
    expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    token =  create_access_token(subject=data.username,expire_delta=expires)
    
    return Token(access_token=token,token_type="bearer")

@app.post(BASE_URL)
def create_request(data:TrainingRequest,current : User = Depends(get_current_user)):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO ust_training_db.training_requests ( 
employee_id, employee_name, training_title , 
training_description, requested_date,status ,manager_id,last_updated) 
VALUES (%s,%s,%s,%s,
%s,%s,%s,%s)
"""
        values = tuple(data.__dict__.values()) + (datetime.now(),)
        cursor.execute(query,values)
        conn.commit()
        return {"id":cursor.lastrowid}
    except Exception as e:
        return HTTPException(status_code=400,detail=str(e))
    finally:
        close_connection(conn,cursor)

@app.get(BASE_URL)
def get_all_requests(current:User = Depends(get_current_user)):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """select * from ust_training_db.training_requests"""
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    except Exception as e:
        return HTTPException(status_code=400,detail=str(e))
    finally:
        close_connection(conn,cursor)
    
@app.get(BASE_URL+"{id}")
def get_requests_by_id(id:int,current:User = Depends(get_current_user)):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """select * from ust_training_db.training_requests where id = %s"""
        cursor.execute(query,(id,))
        data = cursor.fetchone()
        if data:
            return data
        else:
            return None
    except Exception as e:
        return HTTPException(status_code=400,detail=str(e))
    finally:
        close_connection(conn,cursor)

@app.put(BASE_URL+"{id}")
def update_request(id:int,data :TrainingRequest,current:User = Depends(get_current_user)):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        row =  get_requests_by_id(id)
        if row:
            query = """update ust_training_db.training_requests set 
    employee_id = %s, employee_name =%s, training_title =%s , 
    training_description = %s, requested_date = %s,status = %s ,manager_id = %s,last_updated = %s """
            values = tuple(data.__dict__.values()) + (datetime.now(),)
            cursor.execute(query,values)
            conn.commit()
            return data
        else:
            raise HTTPException(status_code=400,detail="ID not found!")
    
    except Exception as e:
        return HTTPException(status_code=400,detail=str(e))
    finally:
        close_connection(conn,cursor)

@app.patch(BASE_URL+"{id}")
def update_status(id:int,status:str,current:User = Depends(get_current_user)):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        row =  get_requests_by_id(id)
        if row:
            query = """update ust_training_db.training_requests set status = %s where id = %s"""
            values = (status,id)
            cursor.execute(query,values)
            conn.commit()
            return {"detail":"status updated"}
        else:
            raise HTTPException(status_code=400,detail="ID not found!")
    except Exception as e:
        return HTTPException(status_code=400,detail=str(e))
    finally:
        close_connection(conn,cursor)
        
@app.delete(BASE_URL+"{id}")
def delete_request(id:int,current:User = Depends(get_current_user)):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        row =  get_requests_by_id(id)
        if row:
            query = """delete from ust_training_db.training_requests  where id = %s"""
            values = (id,)
            cursor.execute(query,values)
            conn.commit()
            return {"detail":"Deleted successfully"}
        else:
            raise HTTPException(status_code=400,detail="ID not found!")
    except Exception as e:
        return HTTPException(status_code=400,detail=str(e))
    finally:
        close_connection(conn,cursor)