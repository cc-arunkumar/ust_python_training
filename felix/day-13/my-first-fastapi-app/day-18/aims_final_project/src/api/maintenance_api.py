from fastapi import FastAPI, HTTPException, APIRouter,Depends
from typing import Optional
from ..models.maintenancelog import MaintenanceLog, StatusValidate
from ..curd.maintenance_crud import MaintenanceCrud
from ..auth.jwt_auth import get_current_user,User

# Initialize CRUD handler for maintenance operations
maintenance_reader = MaintenanceCrud()

# Create a router instance with a prefix for all maintenance-related endpoints
maintenance_router = APIRouter(prefix="/maintenance")


@maintenance_router.post("/create")
def create_maintenance(maintenance: MaintenanceLog,current_user: User = Depends(get_current_user)):
    """
    Endpoint to create a new maintenance log entry.
    Accepts a MaintenanceLog model as input.
    """
    try:
        return maintenance_reader.create_maintenance(maintenance)
    except Exception as e:
        # Log the error for debugging purposes
        print(e)
        raise HTTPException(status_code=404, detail="Not Found")


@maintenance_router.get("/list")
def get_all_maintenance(status: Optional[str] = "ALL",current_user: User = Depends(get_current_user)):
    """
    Endpoint to retrieve all maintenance logs.
    Optional query parameter 'status' can filter logs by status.
    Defaults to 'ALL' to return every log.
    """
    try:
        return maintenance_reader.get_all_maintenance(status)
    except Exception:
        raise HTTPException(status_code=404, detail="Not Found")


@maintenance_router.get("/{id}")
def get_maintenance_by_id(id: int,current_user: User = Depends(get_current_user)):
    """
    Endpoint to fetch a single maintenance log by its unique ID.
    """
    try:
        return maintenance_reader.get_maintenance_by_id(id)
    except Exception:
        raise HTTPException(status_code=404, detail="Not Found")


@maintenance_router.put("/{id}")
def update_maintenance(id: int, data: MaintenanceLog,current_user: User = Depends(get_current_user)):
    """
    Endpoint to update an existing maintenance log by ID.
    Accepts a MaintenanceLog model with updated data.
    """
    try:
        return maintenance_reader.update_maintenance(id, data)
    except Exception as e:
        # Log the error for debugging purposes
        print(str(e))
        raise HTTPException(status_code=404, detail="Not Found")


@maintenance_router.patch("/{id}/status")
def update_maintenance_status(id: int, status: StatusValidate,current_user: User = Depends(get_current_user)):
    """
    Endpoint to update only the status of a maintenance log.
    Accepts a StatusValidate model containing the new status.
    """
    try:
        print(status)  # Debug print, can be replaced with proper logging
        return maintenance_reader.update_maintenance_status(id, status.status)
    except Exception:
        raise HTTPException(status_code=404, detail="Not Found")


@maintenance_router.delete("/{id}")
def delete_maintenance(id: int,current_user: User = Depends(get_current_user)):
    """
    Endpoint to delete a maintenance log by ID.
    """
    try:
        return maintenance_reader.delete_maintenance(id)
    except Exception:
        raise HTTPException(status_code=404, detail="Not Found")


@maintenance_router.get("/search/keyword")
def get_maintenance_by_keyword(keyword: str, value: str,current_user: User = Depends(get_current_user)):
    """
    Endpoint to search maintenance logs dynamically by a given keyword and value.
    Example: /maintenance/search/keyword?keyword=description&value=Repair
    """
    try:
        return maintenance_reader.get_maintenance_by_keyword(keyword, value)
    except Exception as e:
        print(e)  # Debug print, can be replaced with proper logging
        raise HTTPException(status_code=404, detail="Not Found")


@maintenance_router.get("/list/count")
def get_count(current_user: User = Depends(get_current_user)):
    """
    Endpoint to return the total count of maintenance logs.
    Useful for dashboards or summary views.
    """
    try:
        return maintenance_reader.get_all_maintenance_count()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail="Not Found")