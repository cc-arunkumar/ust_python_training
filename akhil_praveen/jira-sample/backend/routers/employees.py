from fastapi import APIRouter, HTTPException,Depends
from schemas.employee import *
from pydantic import BaseModel

emp_router = APIRouter(prefix="/employees", tags=["Employees"])

@emp_router.post("/", response_model=EmployeeResponse, status_code=201)
def create_employee(payload:EmployeeCreate):

    try:
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"Internal server error: {str(e)}")