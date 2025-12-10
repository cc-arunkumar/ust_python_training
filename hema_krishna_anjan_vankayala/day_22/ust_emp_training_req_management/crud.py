from db_connection import get_connection 
from models import TrainingRequest, User
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from datetime import timedelta,timezone, datetime
from typing import Optional
from jose import JWTError,jwt
from dotenv import load_dotenv
import os

load_dotenv()

DEMO_USERNAME = os.getenv("DEMO_USER")
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD")
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

def create_request(new_req : TrainingRequest):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO ust_training_db.training_requests
        (employee_id, employee_name, training_title, training_description, requested_date, status, manager_id)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """
        values = (
            new_req.employee_id,
            new_req.employee_name,
            new_req.training_title,
            new_req.training_description,
            new_req.requested_date,
            new_req.status,
            new_req.manager_id
        )
        cursor.execute(query,values)
        conn.commit()
    except Exception as e:
        raise Exception(f'{e}')
    finally:
        if conn.open:
            cursor.close()
            conn.close()

def update_request(id:int,updated_req : TrainingRequest):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if read_req_by_id(id):
            query = """
                    UPDATE ust_training_db.training_requests
                    SET 
                    employee_id = %s,
                    employee_name = %s,
                    training_title = %s,
                    training_description = %s,
                    requested_date = %s,
                    status = %s,
                    manager_id = %s
                    WHERE
                    id = %s

            """
            values = (
                updated_req.employee_id,
                updated_req.employee_name,
                updated_req.training_title,
                updated_req.training_description,
                updated_req.requested_date,
                updated_req.status,
                updated_req.manager_id,
                id
            )
            cursor.execute(query,values)
            conn.commit()
        else:
            raise Exception
    except Exception as e:
        raise Exception(f'{e}')
    finally:
        if conn.open:
            cursor.close()
            conn.close()
    
def read_all_requests():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("Select * from ust_training_db.training_requests")
        data = cursor.fetchall()
        return data
    
    except Exception as e:
        raise Exception(f"{e}")
    
    finally:
        if conn:
            cursor.close()
            conn.close()

def read_req_by_id(id : int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ust_training_db.training_requests WHERE id = %s", (id,))
        row = cursor.fetchone()
        if row:
            return row
        else:
            raise ValueError("Request ID Not Found")
        
    except Exception as e:
        raise ValueError(f"{e}")
        
    finally:
        if conn:
            cursor.close()
            conn.close()

def delete_request_by_id(id: int):

    try:
        conn = get_connection()
        cursor = conn.cursor()
        if read_req_by_id(id):
            cursor.execute(
                "DELETE FROM ust_training_db.training_requests WHERE id=%s",
                (id,)
            )
            conn.commit()
            return True
        else:
            raise ValueError("Request not found")
    except Exception as e:
        raise ValueError(f"{e}")
    finally:
        if conn.open:
            cursor.close()
            conn.close()

def patch_request(id: int,col:str,val:str):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if read_req_by_id(id):
            query = f"UPDATE ust_training_db.training_requests SET {col} = %s WHERE id = %s"
            values = (f'{val}',f'{id}')
            cursor.execute(query,values)
            conn.commit()
            return {'details': 'Updated Successfully'}
        else:
            raise Exception
    except Exception as e:
        raise Exception(f'{e}')
    finally:
        if conn.open:
            cursor.close()
            conn.close()

        
def create_access_token(subject:str,expires_delta : Optional[timedelta] = None ):
    to_encode = {'sub':subject}
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({'exp': expire})
    encoded = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded

security = HTTPBearer()

def get_curr_user(cred : HTTPAuthorizationCredentials = Depends(security)):
    token = cred.credentials 
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
    except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
 
    username = payload.get("sub")
    if username != DEMO_USERNAME:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
 
    return User(username=username)

 