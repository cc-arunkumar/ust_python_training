from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, Field, field_validator
from datetime import datetime, timedelta, date, timezone
from typing import Optional
from jose import jwt, JWTError
from dotenv import load_dotenv
import os

from db_connection import get_connection

# Load environment variables
load_dotenv()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "defaultsecret")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

app = FastAPI(title="UST Employee Training Request Management API")

# ---------------------------
# JWT utilities
# ---------------------------
def create_access_token(subject: str, expires_delta: Optional[timedelta] = None):
    to_encode = {"sub": subject}
    if expires_delta:
        expires = datetime.now(timezone.utc) + expires_delta
    else:
        expires = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expires})
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    username = payload.get("sub")
    if username is None:
        raise HTTPException(status_code=401, detail="User not found")
    return username

# ---------------------------
# Pydantic model
# ---------------------------
class TrainingRequest(BaseModel):
    employee_id: str = Field(..., pattern=r"^UST\d+$")
    employee_name: str = Field(..., min_length=1, pattern=r"^[A-Za-z\s'-]+$")
    training_title: str = Field(..., min_length=5)
    training_description: str = Field(..., min_length=10)
    requested_date: date
    status: str = Field(..., pattern=r"^(PENDING|APPROVED|REJECTED)$")
    manager_id: str = Field(..., pattern=r"^UST\d+$")

    @field_validator("requested_date")
    def validate_requested_date(cls, v: date):
        if v > date.today():
            raise ValueError("requested_date cannot be a future date")
        return v

# ---------------------------
# Auth endpoint
# ---------------------------
@app.post("/auth/login")
def login(username: str, password: str):
    if username == "admin" and password == "password123":
        token = create_access_token(username)
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

# ---------------------------
# CRUD endpoints
# ---------------------------
@app.post("/api/v1/training-requests", status_code=201)
def create_request(request: TrainingRequest, _: str = Depends(get_current_user)):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = """INSERT INTO training_requests 
                 (employee_id, employee_name, training_title, training_description, requested_date, status, manager_id) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        values = (
            request.employee_id,
            request.employee_name,
            request.training_title,
            request.training_description,
            request.requested_date,
            request.status,
            request.manager_id,
        )
        cursor.execute(sql, values)
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return {"message": "Training request created successfully", "id": new_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.get("/api/v1/training-requests")
def get_all_requests(_: str = Depends(get_current_user)):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM training_requests")
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.get("/api/v1/training-requests/{id}")
def get_request(id: int, _: str = Depends(get_current_user)):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM training_requests WHERE id = %s", (id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if not result:
            raise HTTPException(status_code=404, detail="Request not found")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.put("/api/v1/training-requests/{id}")
def update_request(id: int, request: TrainingRequest, _: str = Depends(get_current_user)):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = """UPDATE training_requests 
                 SET employee_id = %s, employee_name = %s, training_title = %s, 
                     training_description = %s, requested_date = %s, status = %s, manager_id = %s 
                 WHERE id = %s"""
        values = (
            request.employee_id,
            request.employee_name,
            request.training_title,
            request.training_description,
            request.requested_date,
            request.status,
            request.manager_id,
            id,
        )
        cursor.execute(sql, values)
        conn.commit()
        affected = cursor.rowcount
        cursor.close()
        conn.close()
        if affected == 0:
            raise HTTPException(status_code=404, detail="Request not found")
        return {"message": "Training request updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.patch("/api/v1/training-requests/{id}")
def partial_update_request(id: int, request: dict, _: str = Depends(get_current_user)):
    if not request:
        raise HTTPException(status_code=400, detail="No fields provided for update")

    allowed_fields = {
        "employee_id",
        "employee_name",
        "training_title",
        "training_description",
        "requested_date",
        "status",
        "manager_id",
    }
    unknown = set(request.keys()) - allowed_fields
    if unknown:
        raise HTTPException(status_code=400, detail=f"Unknown fields: {', '.join(unknown)}")

    try:
        conn = get_connection()
        cursor = conn.cursor()
        fields = ", ".join([f"{k} = %s" for k in request.keys()])
        sql = f"UPDATE training_requests SET {fields} WHERE id = %s"
        values = list(request.values()) + [id]
        cursor.execute(sql, values)
        conn.commit()
        affected = cursor.rowcount
        cursor.close()
        conn.close()
        if affected == 0:
            raise HTTPException(status_code=404, detail="Request not found")
        return {"message": "Training request partially updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@app.delete("/api/v1/training-requests/{id}")
def delete_request(id: int, _: str = Depends(get_current_user)):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM training_requests WHERE id = %s", (id,))
        conn.commit()
        affected = cursor.rowcount
        cursor.close()
        conn.close()
        if affected == 0:
            raise HTTPException(status_code=404, detail="Request not found")
        return {"message": "Training request deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


# {
#   "employee_id": "UST12345",
#   "employee_name": "John Mathew",
#   "training_title": "Advanced Python",
#   "training_description": "Need deep Python knowledge",
#   "requested_date": "2025-02-01",
#   "status": "PENDING",
#   "manager_id": "UST56789"
# }