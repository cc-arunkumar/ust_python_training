from fastapi import FastAPI, HTTPException, UploadFile, File, Query, APIRouter, Depends
import csv, io
from src.models.maintenance_model import MaintenanceModel
from ..auth.jwt_auth import get_current_user
from ..models.user_model import User
from src.crud.maintenance_crud import (
    create_maintenance_db, get_all_maintenance_db, list_maintenance_by_status_db,
    get_maintenance_by_id_db, update_maintenance_db, update_maintenance_status_db,
    delete_maintenance_db, search_maintenance_db, count_maintenance_db
)

# Create an instance of APIRouter for maintenance-related routes
log_router = APIRouter()

# 1. Create maintenance log endpoint
@log_router.post("/maintenance/create")
def create_maintenance(log: MaintenanceModel, current_user: User = Depends(get_current_user)):
    """
    Creates a new maintenance log in the database.
    The maintenance data is provided in the request body.
    The user must be authenticated via JWT (Depends on `get_current_user`).
    """
    # Attempt to create the maintenance log in the database
    if not create_maintenance_db(log):
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "message": "Maintenance log created successfully"}

# 2. Search maintenance logs endpoint
@log_router.get("/maintenance/search")
def search_maintenance(keyword: str = Query(...), value: str = Query(...), current_user: User = Depends(get_current_user)):
    """
    Searches maintenance logs based on a provided keyword and value.
    The user must be authenticated via JWT.
    """
    # Perform the search based on the provided keyword and value
    result = search_maintenance_db(keyword, value)

    # Handle case where the database query fails
    if result is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "data": result}

# 3. Count total maintenance logs endpoint
@log_router.get("/maintenance/count")
def count_maintenance(current_user: User = Depends(get_current_user)):
    """
    Returns the total count of maintenance logs in the database.
    The user must be authenticated via JWT.
    """
    # Fetch the total count of maintenance logs from the database
    total = count_maintenance_db()

    # Handle case where the database query fails
    if total is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "count": total}

# 4. Get all maintenance logs or filter by status endpoint
@log_router.get("/maintenance/list")
def list_maintenance(status: str = None, current_user: User = Depends(get_current_user)):
    """
    Returns a list of all maintenance logs, optionally filtered by status.
    The user must be authenticated via JWT.
    """
    # If status is provided, filter logs by status
    if status:
        result = list_maintenance_by_status_db(status)
    else:
        # Otherwise, fetch all maintenance logs
        result = get_all_maintenance_db()

    # Handle case where database query fails
    if result is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "data": result}

# 5. Get maintenance log by ID endpoint
@log_router.get("/maintenance/{id}")
def get_maintenance(id: int, current_user: User = Depends(get_current_user)):
    """
    Fetches a specific maintenance log by its ID.
    Returns log data if found, otherwise raises a 404 error.
    The user must be authenticated via JWT.
    """
    # Fetch the maintenance log by ID from the database
    log = get_maintenance_by_id_db(id)

    # If no log is found, raise a 404 HTTP exception
    if log is None:
        raise HTTPException(status_code=404, detail="Maintenance log not found")
    return {"status": "success", "data": log}

# 6. Update maintenance log endpoint
@log_router.put("/maintenance/{id}")
def update_maintenance(id: int, log: MaintenanceModel, current_user: User = Depends(get_current_user)):
    """
    Updates an existing maintenance log with the provided new data.
    The user must be authenticated via JWT.
    """
    # Attempt to update the maintenance log in the database
    if not update_maintenance_db(id, log):
        raise HTTPException(status_code=404, detail="Maintenance log not found")
    return {"status": "success", "message": "Maintenance log updated successfully"}

# 7. Update maintenance log status endpoint
@log_router.patch("/maintenance/{id}/status")
def update_maintenance_status(id: int, status: str, current_user: User = Depends(get_current_user)):
    """
    Updates only the status of an existing maintenance log.
    The user must be authenticated via JWT.
    """
    # Attempt to update the maintenance log's status in the database
    if not update_maintenance_status_db(id, status):
        raise HTTPException(status_code=404, detail="Maintenance log not found")
    return {"status": "success", "message": "Maintenance status updated"}

# 8. Delete maintenance log endpoint
@log_router.delete("/maintenance/{id}")
def delete_maintenance(id: int, current_user: User = Depends(get_current_user)):
    """
    Deletes a maintenance log by its ID.
    The user must be authenticated via JWT.
    """
    # Attempt to delete the maintenance log from the database
    if not delete_maintenance_db(id):
        raise HTTPException(status_code=404, detail="Maintenance log not found")
    return {"status": "success", "message": f"Maintenance log {id} deleted"}
