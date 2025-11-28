from fastapi import APIRouter, HTTPException,Depends
from ..models.maintenance_model import MaintenanceLog
from ..models.user_model import User
from ..crud.maintenance_crud import Maintain
from typing import List, Optional
from ..auth.jwt_auth import get_current_user

log_service = Maintain()  # Service instance for maintenance CRUD
log_router = APIRouter(prefix="/maintenance")  # Router with /maintenance prefix


@log_router.get("/list")
def get_all(status: Optional[str] = "all",current_user : User =Depends(get_current_user)):  # Get all maintenance logs (optionally filter by status)
    try:
        return log_service.get_all_log(status)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@log_router.get("/{log_id}")
def get_by_id(log_id: int,current_user : User =Depends(get_current_user)):  # Get maintenance log by ID
    try:
        return log_service.get_log_by_id(log_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@log_router.put("/{log_id}")
def update_emp(log_id: int, log: MaintenanceLog,current_user : User =Depends(get_current_user)):  # Update full maintenance log record
    try:
        if log_service.update_log(log_id, log):
            return {"message": "Update Successful"}
        else:
            return {"message": "Log Not Found"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@log_router.patch("/{log_id}/")
def update_log(log_id: int, status: str,current_user : User =Depends(get_current_user)):  # Update only maintenance log status
    try:
        if log_service.update_log_status(log_id, status):
            return {"message": "Update Successful"}
        else:
            return {"message": "Log Not Found"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@log_router.post("/create")
def create_log(log: MaintenanceLog,current_user : User =Depends(get_current_user)):  # Create new maintenance log
    try:
        if log_service.create_maintenance(log):
            return {"message": "Added Successful"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@log_router.delete("/{log_id}")
def delete_log(log_id: int,current_user : User =Depends(get_current_user)):  # Delete maintenance log by ID
    try:
        if log_service.delete_log(log_id):
            return {"message": "Deleted Successful"}
        else:
            return {"message": "Log Not Found"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@log_router.get("/search/keyword/")
def get_by_keyword(keyword: str, value: str,current_user : User =Depends(get_current_user)):  # Search maintenance logs by keyword/value
    try:
        return log_service.get_log_keyword(keyword, value)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@log_router.get("/all/count/")
def get_count(current_user : User =Depends(get_current_user)):  # Get total maintenance log count
    try:
        return log_service.get_log_count()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))