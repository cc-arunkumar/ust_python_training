from fastapi import FastAPI, HTTPException, Query, APIRouter, Depends
from ..auth.auth_jwt_token import get_current_user   # Dependency to get the currently logged-in user
from ..models.user_model import User                 # User model for authentication
from src.models.maintenance_model import MaintenanceLog  # Maintenance log model definition
from src.crud.maintenance_crud import (
    create_maintenance_db, get_all_maintenance_db, list_maintenance_by_status_db,
    get_maintenance_by_id_db, update_maintenance_db, update_maintenance_status_db,
    delete_maintenance_db, search_maintenance_db, count_maintenance_db
)

# Create a router for maintenance-related endpoints with a common prefix
maintenance_router = APIRouter(prefix="/maintenance")


# ------------------- CREATE -------------------
@maintenance_router.post("/maintenance/create")
def create_maintenance(log: MaintenanceLog, current_user: User = Depends(get_current_user)):
    """
    Create a new maintenance log entry.
    - Requires authentication (current_user).
    - Accepts MaintenanceLog object as input.
    - Returns success message if created, else raises HTTP 500.
    """
    if not create_maintenance_db(log):
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "message": "Maintenance log created successfully"}


# ------------------- SEARCH -------------------
@maintenance_router.get("/maintenance/search")
def search_maintenance(keyword: str = Query(...), value: str = Query(...), current_user: User = Depends(get_current_user)):
    """
    Search maintenance logs by keyword and value.
    - Example: /maintenance/search?keyword=type&value=electrical
    - Returns matching logs.
    - Raises HTTP 500 if database connection fails.
    """
    result = search_maintenance_db(keyword, value)
    if result is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "data": result}


# ------------------- COUNT -------------------
@maintenance_router.get("/maintenance/count")
def count_maintenance(current_user: User = Depends(get_current_user)):
    """
    Count total number of maintenance logs.
    - Returns integer count.
    - Raises HTTP 500 if database connection fails.
    """
    total = count_maintenance_db()
    if total is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "count": total}


# ------------------- LIST -------------------
@maintenance_router.get("/maintenance/list")
def list_maintenance(status: str = None, current_user: User = Depends(get_current_user)):
    """
    List all maintenance logs.
    - Optional query parameter 'status' to filter logs by status.
    - Returns all logs if no status is provided.
    - Raises HTTP 500 if database connection fails.
    """
    if status:
        result = list_maintenance_by_status_db(status)
    else:
        result = get_all_maintenance_db()
    if result is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "data": result}


# ------------------- GET BY ID -------------------
@maintenance_router.get("/maintenance/{id}")
def get_maintenance(id: int, current_user: User = Depends(get_current_user)):
    """
    Retrieve a single maintenance log by ID.
    - Returns log details if found.
    - Raises HTTP 404 if log not found.
    """
    log = get_maintenance_by_id_db(id)
    if log is None:
        raise HTTPException(status_code=404, detail="Maintenance log not found")
    return {"status": "success", "data": log}


# ------------------- UPDATE -------------------
@maintenance_router.put("/maintenance/{id}")
def update_maintenance(id: int, log: MaintenanceLog, current_user: User = Depends(get_current_user)):
    """
    Update an existing maintenance log by ID.
    - Accepts MaintenanceLog object with updated fields.
    - Returns success message if updated.
    - Raises HTTP 404 if log not found.
    """
    if not update_maintenance_db(id, log):
        raise HTTPException(status_code=404, detail="Maintenance log not found")
    return {"status": "success", "message": "Maintenance log updated successfully"}


# ------------------- UPDATE STATUS -------------------
@maintenance_router.patch("/maintenance/{id}/status")
def update_maintenance_status(id: int, status: str, current_user: User = Depends(get_current_user)):
    """
    Update only the status of a maintenance log.
    - Example: PATCH /maintenance/1/status?status=completed
    - Returns success message if updated.
    - Raises HTTP 404 if log not found.
    """
    if not update_maintenance_status_db(id, status):
        raise HTTPException(status_code=404, detail="Maintenance log not found")
    return {"status": "success", "message": "Maintenance status updated"}


# ------------------- DELETE -------------------
@maintenance_router.delete("/maintenance/{id}")
def delete_maintenance(id: int, current_user: User = Depends(get_current_user)):
    """
    Delete a maintenance log by ID.
    - Returns success message if deleted.
    - Raises HTTP 404 if log not found.
    """
    if not delete_maintenance_db(id):
        raise HTTPException(status_code=404, detail="Maintenance log not found")
    return {"status": "success", "message": f"Maintenance log {id} deleted"}
