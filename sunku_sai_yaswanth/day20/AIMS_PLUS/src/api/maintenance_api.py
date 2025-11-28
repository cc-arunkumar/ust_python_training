from fastapi import FastAPI, HTTPException, status,APIRouter,Depends
from typing import List, Optional
from auth.auth_jwt_token import User, get_current_user
from models.maintenance_model import MaintenanceLogModel
from crud.maintenance_crud import get_all, get_by_id, insert_maintenance_log, update_maintenance_log_by_id, delete_maintenance_log, search_maintenance_log

# app = FastAPI()
maintenance_router=APIRouter(prefix="/maintenance")
# Get all maintenance logs with an optional status filter
@maintenance_router.get("/lists", response_model=List[MaintenanceLogModel])
def get_logs(status_filter: Optional[str] = "",current_user: User = Depends(get_current_user)):
    try:
        rows = get_all(status_filter)
        log_list = []
        for row in rows:
            log_list.append(MaintenanceLogModel(**row))
        return log_list
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching maintenance logs: {e}")

# Search maintenance logs by a field type and keyword (e.g., vendor_name or technician_name)
@maintenance_router.get("/search")
def search_logs(field_type: str, keyword: str,current_user: User = Depends(get_current_user)):
    try:
        data = search_maintenance_log(field_type, keyword)
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to search maintenance logs: {e}")

# Get count of all maintenance logs
@maintenance_router.get("/count")
def count_logs(current_user: User = Depends(get_current_user)):
    try:
        data = get_all()
        if data is None:
            raise HTTPException(status_code=404, detail="No maintenance logs found.")
        return {"count": len(data)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error counting maintenance logs: {str(e)}")

# Get a specific maintenance log by log_id
@maintenance_router.get("/{log_id}", response_model=MaintenanceLogModel)
def get_log_by_id(log_id: int,current_user: User = Depends(get_current_user)):
    try:
        rows = get_by_id(log_id)
        if not rows:
            raise HTTPException(status_code=404, detail="Maintenance log not found")
        return MaintenanceLogModel(**rows)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error fetching maintenance log")

# Create a new maintenance log entry
@maintenance_router.post("/create", response_model=MaintenanceLogModel)
def create_maintenance_log(new_log: MaintenanceLogModel,current_user: User = Depends(get_current_user)):
    try:
        insert_maintenance_log(new_log)
        return new_log
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error: {e}")

# Update an existing maintenance log entry by log_id
@maintenance_router.put("/{log_id}", response_model=MaintenanceLogModel)
def update_maintenance_log(log_id: int, updated_log: MaintenanceLogModel,current_user: User = Depends(get_current_user)):
    try:
        update_maintenance_log_by_id(log_id, updated_log)
        return updated_log
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Update failed: {str(e)}")

# Delete a maintenance log entry by log_id
@maintenance_router.delete("/{log_id}")
def delete_maintenance_log_by_id(log_id: int,current_user: User = Depends(get_current_user)):
    try:
        if delete_maintenance_log(log_id):
            return {"detail": "Maintenance log deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting maintenance log: {str(e)}")

@maintenance_router.patch("/{log_id}/status")
def update_status(log_id: int, status: str):
    try:
        # Fetch the existing maintenance log by log_id
        data = get_by_id(log_id)
        
        if not data:
            raise HTTPException(status_code=404, detail="Maintenance log not found")
        
        # Update the status field of the maintenance log
        data['status'] = status
        
        # Update the maintenance log in the database
        update_maintenance_log_by_id(log_id, MaintenanceLogModel(**data))
        
        return {"message": "Maintenance log status updated successfully", "log_id": log_id, "new_status": status}
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating maintenance log status: {str(e)}")
