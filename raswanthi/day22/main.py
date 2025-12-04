from validation_model import EmployeeTraining
from fastapi import FastAPI,HTTPException,Depends
from db_connection import get_connection
from typing import Dict,Optional
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os
from pydantic import BaseModel

app=FastAPI(title="UST Employee Training Request Management")
 
class User(BaseModel):
    username: str
 
class Token(BaseModel):
    token: str
    token_type: str

class LoginRequest(BaseModel):
    username: str
    password: str

load_dotenv()
 
SECRECT_KEY = os.getenv("SECRECT_KEY")
ALGORITHM = os.getenv("ALGORITHM")
 
USERNAME = os.getenv("USER_NAME")
 
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    to_encode = {"sub": subject}
    if expires_delta:
        expires = datetime.now(timezone.utc) + expires_delta
    else:
        expires = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expires})
 
    encoded = jwt.encode(to_encode, SECRECT_KEY, algorithm=ALGORITHM)
    return encoded
 
 
security = HTTPBearer()
 
 
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRECT_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
 
    username = payload.get("sub")
    if username != USERNAME:
        raise HTTPException(status_code=401, detail="User not found")

    return User(username=username)
 



@app.post("/api/v1/training-requests/")
def create_training_request(emp:EmployeeTraining):
    conn=get_connection()
    try:
        with conn.cursor() as cursor:
            sql="""INSERT INTO TRAINING_REQUESTS
            (employee_id,employee_name,training_title,training_description,
            requested_date,status,manager_id,last_updated)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            
            """
            cursor.execute(sql,
                (emp.employee_id,emp.employee_name,
                emp.training_title,emp.training_description,
                emp.requested_date,emp.status,
                emp.manager_id,emp.last_updated))
            
            conn.commit()
            return {"message":"Request for training created successfully!"}
    finally:
        conn.close()
    
@app.get("/api/v1/training-requests/")
def get_request():
    conn=get_connection()
    try:
        with conn.cursor() as cursor:
            sql="SELECT * FROM TRAINING_REQUESTS"
            cursor.execute(sql)
            result=cursor.fetchall()
            return {"training requests":result}
    finally:
        conn.close()
        
@app.get("/api/v1/training-requests/{id}")
def get_request_by_id(id:int):
    conn=get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM TRAINING_REQUESTS WHERE ID=%s",(id,))
            emp=cursor.fetchone()
            if not emp:
                raise HTTPException(status_code=404,detail="Request not found")
            return emp 
        
    finally:
        conn.close()
        
@app.put("/api/v1/training-requests/{id}")
def update_request(id:int,emp:EmployeeTraining):
    conn=get_connection()
    try:
        with conn.cursor() as cursor:
            sql="""UPDATE training_requests 
                SET employee_id=%s,employee_name=%s,
                training_title=%s,training_description=%s,
                requested_date=%s,status=%s,
                manager_id=%s,last_updated=%s 
                WHERE id=%s
                """
            cursor.execute(sql,(emp.employee_id,emp.employee_name,
                                emp.training_title,emp.training_description,
                                emp.requested_date,emp.status,
                                emp.manager_id,emp.last_updated,
                                emp.id))
            conn.commit()
            if cursor.rowcount==0:
                raise HTTPException(status_code=404,detail="Request not found")
            return {"message":"Request updated successfully!"}            
    finally:
        conn.close()


@app.patch("/api/v1/training-requests/{id}")
def update_partial_request(id: int, updates: Dict[str, str]):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:

            updates["last_updated"] = datetime.utcnow()

            set_clause_parts = []
            values = []
            for key, value in updates.items():
                set_clause_parts.append(f"{key}=%s")
                values.append(value)

            if not set_clause_parts:
                raise HTTPException(status_code=400, detail="No fields provided for update")

            set_clause = ", ".join(set_clause_parts)
            sql = f"UPDATE TRAINING_REQUESTS SET {set_clause} WHERE id=%s"
            
            values.append(id)
            
            cursor.execute(sql, tuple(values))
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Request not found")

            return {"message": "Request partially updated successfully!"}
    finally:
        conn.close()
        
        
@app.delete("/api/v1/training-requests/{id}")
def delete_request(id:int):
    conn=get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM training_requests WHERE id=%s",(id,))
            if cursor.rowcount==0:
                raise HTTPException(status_code=404,detail="Request not found")
            conn.commit()
            return {"message": "Employee deleted successfully"}
    finally:
        conn.close()
            
