# src/api/MaintenanceLog_api/main.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'src'))
from fastapi import FastAPI, HTTPException,APIRouter,Depends
from typing import List
from pydantic import BaseModel
from crud.maintainence_crud import (create_maintenance,delete_maintenance,get_all_maintenance,get_maintenance_by_id,get_maintenance_by_status,get_maintenance_count,update_maintenance,update_maintenance_status,search_maintenance_by_keyword) 
from models.maintenance_model import MaintenanceLog  # Import Pydantic model
from src.auth.login_function import get_current_user,User


maintain_router = APIRouter(prefix="/maintainence")

# 1. POST /MaintenanceLog/create - Create a new MaintenanceLog record
@maintain_router.post("/MaintenanceLog/create", response_model=MaintenanceLog)
def create_MaintenanceLog_api(MaintenanceLog: MaintenanceLog,current_user: User = Depends(get_current_user)):
    create_maintenance(MaintenanceLog)
    return MaintenanceLog

# 2. GET /MaintenanceLog/list - Get all MaintenanceLog records
@maintain_router.get("/MaintenanceLog/list", response_model=List[MaintenanceLog],)
def get_MaintenanceLog_list_api(current_user: User = Depends(get_current_user)):
    MaintenanceLog_records = get_all_maintenance()
    return MaintenanceLog_records

# 3. GET /MaintenanceLog/list?status= - Get MaintenanceLog records by status
@maintain_router.get("/MaintenanceLog/list", response_model=List[MaintenanceLog])
def get_MaintenanceLog_by_status_api(status: str,current_user: User = Depends(get_current_user)):
    MaintenanceLog_records = get_maintenance_by_status(status)
    return MaintenanceLog_records

# 4. GET /MaintenanceLog/{id} - Get MaintenanceLog record by ID
@maintain_router.get("/MaintenanceLog/{id}", response_model=MaintenanceLog)
def get_MaintenanceLog_by_id_api(id: int,current_user: User = Depends(get_current_user)):
    MaintenanceLog = get_maintenance_by_id(id)
    if not MaintenanceLog:
        raise HTTPException(status_code=404, detail="MaintenanceLog record not found")
    return MaintenanceLog

# 5. PUT /MaintenanceLog/{id} - Update MaintenanceLog record by ID
@maintain_router.put("/MaintenanceLog/{id}", response_model=MaintenanceLog)
def update_MaintenanceLog_api(id: int, MaintenanceLog: MaintenanceLog,current_user: User = Depends(get_current_user)):
    MaintenanceLog_data = MaintenanceLog
    update_maintenance(id, MaintenanceLog_data)
    return MaintenanceLog

# 6. PATCH /MaintenanceLog/{id}/status - Update only the status of the MaintenanceLog
@maintain_router.patch("/MaintenanceLog/{id}/status")
def update_MaintenanceLog_status_api(id: int, status: str,current_user: User = Depends(get_current_user)):
    update_maintenance_status(id, status)
    return {"message": f"MaintenanceLog {id} status updated to {status}"}

# 7. DELETE /MaintenanceLog/{id} - Delete a MaintenanceLog record by ID
@maintain_router.delete("/MaintenanceLog/{id}")
def delete_MaintenanceLog_api(id: int,current_user: User = Depends(get_current_user)):
    delete_maintenance(id)
    return {"message": f"MaintenanceLog record {id} deleted successfully"}

# 8. GET /MaintenanceLog/search?keyword= - Search MaintenanceLog records by keyword
@maintain_router.get("/MaintenanceLog/search", response_model=List[MaintenanceLog])
def search_MaintenanceLog_api(keyword: str,current_user: User = Depends(get_current_user)):
    MaintenanceLog = search_maintenance_by_keyword(keyword)
    return MaintenanceLog

# 9. GET /MaintenanceLog/count - Get the count of MaintenanceLog records
@maintain_router.get("/MaintenanceLog/count")
def count_MaintenanceLog_api(current_user: User = Depends(get_current_user)):
    count = get_maintenance_count()
    return {"count": count}
