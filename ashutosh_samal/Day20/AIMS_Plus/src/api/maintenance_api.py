from fastapi import APIRouter, HTTPException,Depends
from typing import List, Optional
from ..model.maintenance_model import MaintenanceCreate
from ..auth.jwt_auth import jwt_router,get_current_user,User
from ..crud.maintenance_crud import (
    fetch_maintenance_logs,
    fetch_maintenance_by_id,
    create_new_maintenance_log,
    modify_maintenance_log,
    modify_maintenance_status,
    remove_maintenance_log,
    search_maintenance_logs,
    get_total_maintenance_count
)

maintenance_router = APIRouter(prefix="/maintenance")

# Fetch the list of maintenance logs, with an optional filter by status
@maintenance_router.get("/list")
async def list_maintenance(status: Optional[str] = None,current_user: User = Depends(get_current_user)):
    try:
        logs = fetch_maintenance_logs(status)  # Call the CRUD function to get logs
        return logs
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Search maintenance logs based on a keyword (in description, vendor name, or technician name)
@maintenance_router.get("/search")
async def search_maintenance_endpoint(keyword: str,current_user: User = Depends(get_current_user)):
    try:
        logs = search_maintenance_logs(keyword)  # Call the CRUD function to search for logs
        return logs
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Get the total count of maintenance logs
@maintenance_router.get("/count")
async def count_maintenance_endpoint(current_user: User = Depends(get_current_user)):
    try:
        count = get_total_maintenance_count()  # Call the CRUD function to get count of logs
        return {"total_maintenance_logs": count}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Fetch a specific maintenance log by its ID
@maintenance_router.get("/{maintenance_id}")
async def get_maintenance(maintenance_id: int,current_user: User = Depends(get_current_user)):
    try:
        log = fetch_maintenance_by_id(maintenance_id)  # Call the CRUD function to get log by ID
        if not log:
            raise HTTPException(status_code=404, detail="Maintenance log not found")
        return log
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Create a new maintenance log
@maintenance_router.post("/create")
async def create_maintenance_endpoint(log: MaintenanceCreate,current_user: User = Depends(get_current_user)):
    try:
        create_new_maintenance_log(log)  # Call the CRUD function to create a new log
        return log
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Update an existing maintenance log by ID
@maintenance_router.put("/{maintenance_id}")
async def update_maintenance_endpoint(maintenance_id: int, log: MaintenanceCreate,current_user: User = Depends(get_current_user)):
    try:
        modify_maintenance_log(maintenance_id, log)  # Call the CRUD function to update the log
        return log
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Update the status of a specific maintenance log
@maintenance_router.patch("/{maintenance_id}/status")
async def update_maintenance_status_endpoint(maintenance_id: int, status: str,current_user: User = Depends(get_current_user)):
    try:
        modify_maintenance_status(maintenance_id, status)  # Call the CRUD function to modify status
        return {"message": "Maintenance status updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Delete a maintenance log by ID
@maintenance_router.delete("/{maintenance_id}")
async def delete_maintenance_endpoint(maintenance_id: int,current_user: User = Depends(get_current_user)):
    try:
        remove_maintenance_log(maintenance_id)  # Call the CRUD function to delete the log
        return {"message": "Maintenance record deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
