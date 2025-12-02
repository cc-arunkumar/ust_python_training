from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel,Field,model_validator
from datetime import datetime,date
from typing import Literal
from auth import get_current_user,auth_router,User
import pymysql


def get_connection():
    # Establish connection to MySQL database
    conn = pymysql.connect(
        host="localhost",      # Database host
        user="root",           # Database username
        password="pass@word1", # Database password
        database="ust_db", # Database name
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Connection Established")  # Confirmation message
    return conn  # Return connection object

class StatusValidater(BaseModel):
    status : Literal["PENDING","APPROVED","REJECTED"]

class TrainingRequest(BaseModel):
    employee_id : str = Field(...,pattern=r"^UST\d+$",max_length=20)
    employee_name : str = Field(...,max_length=100,pattern=r"^[A-Za-z ]+$")
    training_title : str = Field(...,max_length=200,min_length=5)
    training_description : str = Field(...,min_length=10)
    requested_date : date = Field(...,)
    status : Literal["PENDING","APPROVED","REJECTED"]
    manager_id : str = Field(...,pattern=r"^UST\d+$",max_length=20)

    @model_validator(mode="after")
    def validate(self):
        if self.requested_date > date.today() :
            raise HTTPException(status_code=422,detail="Cannot be a future date")
        return self
        
app = FastAPI(title="UST TRAINING REQUEST")

app.include_router(auth_router)


@app.get("/api/v1/training-requests/")
def get_all(current_user : User = Depends(get_current_user)):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("Select * from ust_db.training_requests")
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("Connection Closed")

@app.get("/api/v1/training-requests/{id}")
def get_by_id(id:int,current_user : User = Depends(get_current_user)):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("Select * from ust_db.training_requests where id=%s",(id,))
        rows = cursor.fetchone()
        if rows:
            return rows
        else:
            raise HTTPException(status_code=404,detail="Id not Found")
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("Connection Closed")


@app.post("/api/v1/training-requests/")
def create(data:TrainingRequest,current_user : User = Depends(get_current_user)):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
insert into ust_db.training_requests (employee_id,employee_name,training_title,
training_description,requested_date,status,manager_id,last_updated) values
(%s,%s,%s,%s,%s,%s,%s,%s)
"""
        tup = tuple(data.__dict__.values())+(datetime.now(),)
        cursor.execute(query,tup)
        conn.commit()
        return {"id":cursor.lastrowid}
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("Connection Closed")


@app.put("/api/v1/training-requests/{id}")
def update(id:int,data:TrainingRequest,current_user : User = Depends(get_current_user)):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        row = get_by_id(id)
        if row:
            query = """
    update ust_db.training_requests set employee_id=%s,employee_name=%s,training_title=%s,
    training_description=%s,requested_date=%s,status=%s,manager_id=%s,last_updated=%s 
    where id=%s
    """
            tup = tuple(data.__dict__.values())+(datetime.now(),id)
            cursor.execute(query,tup)
            conn.commit()
            return get_by_id(id)      
        else:
            raise HTTPException(status_code=404,detail="Id not Found")    
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("Connection Closed")


@app.delete("/api/v1/training-requests/{id}")
def delete(id:int,current_user : User = Depends(get_current_user)):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        row = get_by_id(id)
        if row:
            cursor.execute("delete from ust_db.training_requests where id=%s",(id,))
            conn.commit()
            return {"message":"Deleted Successfully"}
        else:
            raise HTTPException(status_code=404,detail="Id not Found")
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("Connection Closed")


@app.patch("/api/v1/training-requests/{id}")
def update_status(id:int,status:StatusValidater,current_user : User = Depends(get_current_user)):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        row = get_by_id(id)
        if row:
            cursor.execute("update ust_db.training_requests set status=%s where id=%s",(status.status,id))
            conn.commit()
            return {"message":"Status Updated Successfully"}
        else:
            raise HTTPException(status_code=404,detail="Id not Found")
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("Connection Closed")