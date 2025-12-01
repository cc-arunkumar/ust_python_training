from fastapi import APIRouter, HTTPException,Depends  # Import FastAPI components
from typing import List, Optional  # Import typing components for type hinting
from ..models.maientenance_model import MaintenanceCreate  # Import MaintenanceCreate model from maintenance_model
from ..crud.maientenance_crud import (
    get_maintenance_logs,  # Import CRUD operations for maintenance logs
    get_maintenance_by_id,
    create_maintenance,
    update_maintenance,
    update_maintenance_status,
    delete_maintenance,
    search_maintenance,
    count_maintenance
)
from ..auth.auth_jwt_token import get_current_user

maintenance_router = APIRouter(prefix="/maintenance",tags=["Maientenance"])  # Create a new router for maintenance-related endpoints

# Endpoint to list maintenance logs, optionally filtered by status
@maintenance_router.get("/list")
async def list_maintenance(status: Optional[str] = None,current_user: dict = Depends(get_current_user)):
    try:
        logs = get_maintenance_logs(status)  # Fetch maintenance logs based on status
        return logs
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure




# Endpoint to search for maintenance logs based on a keyword
@maintenance_router.get("/search")
async def search_maintenance_endpoint(keyword: str,current_user: dict = Depends(get_current_user)):
    try:
        logs = search_maintenance(keyword)  # Search for maintenance logs by keyword
        return logs
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure



# Endpoint to get the count of total maintenance logs
@maintenance_router.get("/count")
async def count_maintenance_endpoint(current_user: dict = Depends(get_current_user)):
    try:
        count = count_maintenance()  # Get total maintenance log count
        return {"total_maintenance_logs": count}  # Return maintenance log count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure


# Endpoint to fetch a specific maintenance log by ID
@maintenance_router.get("/{maintenance_id}")
async def get_maintenance(maintenance_id: int,current_user: dict = Depends(get_current_user)):
    try:
        log = get_maintenance_by_id(maintenance_id)  # Fetch maintenance log by ID
        if not log:
            raise HTTPException(status_code=404, detail="Maintenance log not found")  # Return error if not found
        return log
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure



# Endpoint to create a new maintenance log
@maintenance_router.post("/create")
async def create_maintenance_endpoint(log: MaintenanceCreate,current_user: dict = Depends(get_current_user)):
    try:
        create_maintenance(log)  # Call CRUD function to create maintenance log
        return log  # Return created maintenance log
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure



# Endpoint to update an existing maintenance log by ID
@maintenance_router.put("/{maintenance_id}")
async def update_maintenance_endpoint(maintenance_id: int, log: MaintenanceCreate,current_user: dict = Depends(get_current_user)):
    try:
        update_maintenance(maintenance_id, log)  # Update maintenance log using the provided ID and data
        return log  # Return updated maintenance log
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure



# Endpoint to update the status of a maintenance log
@maintenance_router.patch("/{maintenance_id}/status")
async def update_maintenance_status_endpoint(maintenance_id: int, status: str,current_user: dict = Depends(get_current_user)):
    try:
        update_maintenance_status(maintenance_id, status)  # Update maintenance log status
        return {"message": "Maintenance status updated successfully"}  # Return success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure


# Endpoint to delete a maintenance log by ID
@maintenance_router.delete("/{maintenance_id}")
async def delete_maintenance_endpoint(maintenance_id: int,current_user: dict = Depends(get_current_user)):
    try:
        delete_maintenance(maintenance_id)  # Delete maintenance log using the provided ID
        return {"message": "Maintenance record deleted successfully"}  # Return success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure
