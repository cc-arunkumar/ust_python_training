from fastapi import FastAPI, HTTPException, status, APIRouter, Depends
from src.crud import maintenance_crud
from src.models import maintenance_model
from typing import List, Optional
from src.auth.jwt_auth import get_current_user, User


# Router for maintenance endpoints
maintenance_router = APIRouter(prefix="/maintenance")

# Search maintenance logs by field and keyword
@maintenance_router.get('/search', response_model=List[maintenance_model.MaintenanceLog])
def search_by_word(field_type: str, keyword: str,curr_user: User = Depends(get_current_user)):
    try:
        data = maintenance_crud.search_logs(field_type, keyword)
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to fetch data: {e}")


# Get all maintenance logs (optionally filter by status)
@maintenance_router.get('/list', response_model=List[maintenance_model.MaintenanceLog])
def get_all(status_filter: Optional[str] = "",curr_user: User = Depends(get_current_user)):
    try:
        data = maintenance_crud.get_all_logs(status_filter)
        new_li = []
        for row in data:
            new_li.append(maintenance_model.MaintenanceLog(**row))
        return new_li
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Failed to Fetch All the Records: {e}")


# Get count of maintenance logs
@maintenance_router.get("/count")
def count_all(curr_user: User = Depends(get_current_user)):
    data = maintenance_crud.get_all_logs()
    return {"detail": f"Count of records: {len(data)}"}


# Get maintenance log by ID
@maintenance_router.get('/{id}', response_model=maintenance_model.MaintenanceLog)
def get_by_id(id: int,curr_user: User = Depends(get_current_user)):
    try:
        data = maintenance_crud.get_log_by_id(id)
        if not data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not Found")
        return maintenance_model.MaintenanceLog(**data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"ID not Found or Unable to fetch the Record : {e}")


# Create a new maintenance log
@maintenance_router.post('/create', response_model=maintenance_model.MaintenanceLog)
def create_asset(new_asset: maintenance_model.MaintenanceLog,curr_user: User = Depends(get_current_user)):
    try:
        maintenance_crud.create_log(new_asset)
        return new_asset
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error: {e}")


# Delete maintenance log by ID
@maintenance_router.delete("/{id}")
def delete_asset_id(id: int,curr_user: User = Depends(get_current_user)):
    try:
        if maintenance_crud.delete_log_by_id(id):
            return {"detail": "Record deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Log Id Doesnt Exist: {e}")


# Update maintenance log by ID
@maintenance_router.put("/{id}", response_model=maintenance_model.MaintenanceLog)
def update_by_id(id: int, new_asset: maintenance_model.MaintenanceLog,curr_user: User = Depends(get_current_user)):
    try:
        maintenance_crud.update_log_by_id(id, new_asset)
        data = maintenance_crud.get_log_by_id(id)
        return maintenance_model.MaintenanceLog(**data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to update Log: {e}")


# Patch maintenance log status by ID
@maintenance_router.patch("/{id}/status", response_model=maintenance_model.MaintenanceLog)
def patch_by_id(id: int, status: str,curr_user: User = Depends(get_current_user)):
    data = get_by_id(id)
    try:
        if data:
            data.status = status
            return update_by_id(id, data)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error: {e}")
