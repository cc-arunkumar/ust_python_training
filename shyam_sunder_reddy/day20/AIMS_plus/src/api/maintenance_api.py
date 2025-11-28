from fastapi import FastAPI, HTTPException, APIRouter,Depends
from src.auth.jwt_auth import get_current_user,User
from src.models import maintenance_model
from src.crud import maintenance_crud
from typing import List, Optional

# Router for maintenance-related endpoints, all prefixed with "/maintenance"
maintenance_router = APIRouter(prefix="/maintenance")


# -------------------------------
# Endpoint: Search maintenance logs by field
# -------------------------------
@maintenance_router.get("/search", response_model=List[maintenance_model.MaintenanceLog])
def search(field: str, val: str,current_user: User = Depends(get_current_user)):
    """
    Search maintenance logs by a given field and value.
    Example: /maintenance/search?field=asset_id&val=123
    """
    if maintenance_crud.search_by_tag_log(field, val):
        return maintenance_crud.search_by_tag_log(field, val)
    raise HTTPException(status_code=404, detail="Not found")


# -------------------------------
# Endpoint: Create a new maintenance log
# -------------------------------
@maintenance_router.post("/create", response_model=maintenance_model.MaintenanceLog)
def create_log(new_log: maintenance_model.MaintenanceLog,current_user: User = Depends(get_current_user)):
    """
    Create a new maintenance log record.
    Validates log data before inserting into DB.
    """
    if maintenance_model.validate_maintenance(new_log):
        pass
    else:
        raise HTTPException(status_code=409, detail="Validation failed")
    if not maintenance_crud.create_log(new_log):
        raise HTTPException(status_code=400, detail="Failed to create the Log")
    return new_log


# -------------------------------
# Endpoint: List all maintenance logs / List all By Status
# -------------------------------
@maintenance_router.get("/list", response_model=List[maintenance_model.MaintenanceLog])
def get_all(status: Optional[str] = "",current_user: User = Depends(get_current_user)):
    """
    Retrieve all maintenance logs, optionally filtered by status.
    Example: /maintenance/list?status=completed
    """
    data = maintenance_crud.get_all_logs(status)
    new_li = []
    for row in list(data):
        x = maintenance_model.MaintenanceLog(**row)  # Convert dict to MaintenanceLog model
        new_li.append(x)
    return new_li


# -------------------------------
# Endpoint: Count all maintenance logs
# -------------------------------
@maintenance_router.get("/count")
def count_all(current_user: User = Depends(get_current_user)):
    """
    Return the total count of maintenance logs in the system.
    """
    data = maintenance_crud.get_all_logs()
    return {"detail": f"Count of records: {len(data)}"}


# -------------------------------
# Endpoint: Get maintenance log by ID
# -------------------------------
@maintenance_router.get("/{id}", response_model=maintenance_model.MaintenanceLog)
def get_by_id(id: int,current_user: User = Depends(get_current_user)):
    """
    Retrieve a single maintenance log by its ID.
    """
    data = maintenance_crud.get_log_by_id(id)
    if data:
        return maintenance_model.MaintenanceLog(**data)
    raise HTTPException(status_code=404, detail="Log id not found")


# -------------------------------
# Endpoint: Update maintenance log by ID
# -------------------------------
@maintenance_router.put("/{id}", response_model=maintenance_model.MaintenanceLog)
def update_by_id(id: int, new_log: maintenance_model.MaintenanceLog,current_user: User = Depends(get_current_user)):
    """
    Update an existing maintenance log by ID.
    Validates log data before updating.
    """
    if maintenance_model.validate_maintenance(new_log):
        pass
    else:
        raise HTTPException(status_code=409, detail="Validation failed")
    if maintenance_crud.update_log_by_id(id, new_log):
        return new_log
    raise HTTPException(status_code=400, detail="Unable to update Log")


# -------------------------------
# Endpoint: Patch maintenance log status
# -------------------------------
@maintenance_router.patch("/{id}/status", response_model=maintenance_model.MaintenanceLog)
def patch_by_id(id: int, status: str,current_user: User = Depends(get_current_user)):
    """
    Update only the status field of a maintenance log by ID.
    """
    data = get_by_id(id)
    if data:
        data.status = status
        return update_by_id(id, data)
    raise HTTPException(status_code=404, detail="ID not found")


# -------------------------------
# Endpoint: Delete maintenance log by ID
# -------------------------------
@maintenance_router.delete("/{id}")
def delete_log_id(id: int,current_user: User = Depends(get_current_user)):
    """
    Delete a maintenance log record by ID.
    """
    if maintenance_crud.delete_log_by_id(id):
        return {"detail": "Record deleted successfully"}
    raise HTTPException(status_code=404, detail="Log Id Doesnt Exist")
