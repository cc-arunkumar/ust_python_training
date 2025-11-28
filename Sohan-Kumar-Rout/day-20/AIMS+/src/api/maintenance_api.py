from fastapi import APIRouter, Depends
from auth.jwt_auth import User, get_curr_user
from crud.maintenance_crud import (
    create_maintenance,
    list_maintenance,
    list_maintenance_by_status,
    get_maintenance_by_id,
    update_maintenance,
    update_maintenance_status,
    delete_maintenance,count_maintenance,search_maintenance
)
from models.maintenance import MaintenanceBase

router = APIRouter(prefix="/maintenance", tags=["Maintenance"])

@router.get("/count")
def api_count_maintenance(current_user: User = Depends(get_curr_user)):
    return count_maintenance()

@router.post("/create")
def api_create_maintenance(log: MaintenanceBase, current_user: User = Depends(get_curr_user)):
    return create_maintenance(log)

@router.get("/")
def api_list_maintenance(current_user: User = Depends(get_curr_user)):
    return list_maintenance()

@router.get("/status/{status}")
def api_list_maintenance_by_status(status: str, current_user: User = Depends(get_curr_user)):
    return list_maintenance_by_status(status)

@router.get("/{log_id}")
def api_get_maintenance_by_id(log_id: int, current_user: User = Depends(get_curr_user)):
    return get_maintenance_by_id(log_id)

@router.put("/{log_id}")
def api_update_maintenance(log_id: int, row: dict, current_user: User = Depends(get_curr_user)):
    return update_maintenance(log_id, row)

@router.patch("/{log_id}/status")
def api_update_maintenance_status(log_id: int, status: str, current_user: User = Depends(get_curr_user)):
    return update_maintenance_status(log_id, status)

@router.delete("/{log_id}")
def api_delete_maintenance(log_id: int, current_user: User = Depends(get_curr_user)):
    return delete_maintenance(log_id)



@router.get("/search")
def api_search_maintenance(column_name: str, keyword: str, current_user: User = Depends(get_curr_user)):
    
    return search_maintenance(column_name, keyword)
   