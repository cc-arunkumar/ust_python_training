from fastapi import FastAPI,HTTPException
from pydantic import Field,field_validator,BaseModel
from datetime import date
import re
import pymysql


app=FastAPI(title="UST Employee Training Request Management")
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",  
        password="pass@word1",  
        database="ust_training_db" 
    )

class TrainingRequest(BaseModel):

    employee_id:str
    employee_name:str
    training_title:str=Field(...,min_length=5)
    training_description:str=Field(...,min_length=10)
    requested_date:date
    status:str
    manager_id:str
    
    @field_validator("employee_id")
    def valid_manager_id(cls,v):
        if not re.match(r"^UST\d+$",v):
            raise ValueError("employee_id must be valid")
        return v
    
    @field_validator("manager_id")
    def valid_manager_id(cls,v):
        if not re.match(r"^UST\d+$",v):
            raise ValueError("manager_id must be valid")
        return v
    
    @field_validator("employee_name")
    def valid_employee_name(cls,v):
        if not v.strip():
            raise ValueError("employee_name cannot be empty")
        if any(ch.isdigit()for ch in v):
            raise ValueError("employee_name cannot contain numbers")
        return v
    
    @field_validator("requested_date")
    def valid_requested_date(cls,v:date):
        if v > date.today():
            raise ValueError("requested date cannot be future date")
        
        return v
    
    @field_validator("status")
    def valid_status(cls,v):
        allowed={"PENDING","APPROVED","REJECTED"}
        if v not in allowed:
            raise ValueError("status must be PENDING,APPROVED,REJECTED")
        return v

  
    
@app.post("/training_requests")
def training_request(request:TrainingRequest):
    connection=get_connection()
    cursor=connection.cursor()
    query = """
    INSERT INTO training_requests (employee_id, employee_name, training_title, training_description, requested_date, status, manager_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values=(request.employee_id,request.employee_name,request.training_title,request.training_description,request.requested_date,request.status,request.manager_id)
    
    try:
        cursor.execute(query,values)
        connection.commit()
        cursor.close()
        connection.close()
        return {"message":"Training request added succesfully","employee_details":request}
    
    except Exception as e:
        cursor.close()
        connection.close()
        raise HTTPException(status_code=500,detail=f"Error: {str(e)}")



@app.get("/training_requests")
def get_all_requests():
    connection=get_connection()
    cursor=connection.cursor()
    query="SELECT * FROM training_requests"
    cursor.execute(query)
    result=cursor.fetchall()
    cursor.close()
    connection.close()
    if result:
        return{"training_requests":result}
    else:
        raise HTTPException(status_code=404,detail="No Training request found")


@app.get("/training_request/{id}")
def get_request_by_id(id:int):
    connection=get_connection()
    cursor=connection.cursor()
    query="SELECT * FROM training_requests WHERE id = %s"
    cursor.execute(query,(id))
    result=cursor.fetchone()
    cursor.close()
    connection.close()
    if result:
        return{"training_request":result}
    else:
        raise HTTPException(status_code=404,detail=f'{id} training request not found')
    
    
@app.put("/training_requests/{id}")
def update_training_request(id: int, request: TrainingRequest):
    connection = get_connection()
    cursor = connection.cursor()
    query = """
    UPDATE training_requests 
    SET employee_id = %s, employee_name = %s, training_title = %s, training_description = %s, 
        requested_date = %s, status = %s, manager_id = %s
    WHERE id = %s
    """
    values = (
        request.employee_id, request.employee_name, request.training_title,
        request.training_description, request.requested_date,
        request.status, request.manager_id, id
    )
    try:
        cursor.execute(query, values)
        connection.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail=f"Training request {id} not found")
        return {"message": "Training request updated successfully", "details": request}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
        if connection.open:
            cursor.close()
            connection.close()

            
@app.delete("/training_requests/{id}")
def delete_training_request(id:int):
    connection=get_connection()
    cursor=connection.cursor()
    query="DELETE FROM training_requests WHERE id=%s"
    
    try:
        cursor.execute(query,(id))
        connection.commit()
        return {"message":f"training request id: {id} deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
        if connection.open:
            cursor.close()
            connection.close()


