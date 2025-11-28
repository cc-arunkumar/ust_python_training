from fastapi import APIRouter, Query, Depends
from src.models.maintanance_model import MaintenanceCreate, MaintenanceUpdate
from src.crud.maintenance_crud import *
from src.auth.auth import get_curr_user
from src.models.login_model import User

main_router = APIRouter(prefix="/maintenance", tags=["Maintenance"])

@main_router.post("/create")
def create_maintenance(maintenance: MaintenanceCreate, current_user: User = Depends(get_curr_user)):
    try:
        return {"status": "success", "message": "Maintenance record created successfully"}
    except Exception as e:
        return {"status": "fail", "message": str(e)}

@main_router.get("/list")
def list_all(status: str = None, current_user: User = Depends(get_curr_user)):
    return get_all_maintenance(status)

@main_router.get("/count")
def count(current_user: User = Depends(get_curr_user)):
    return count_maintenance()

@main_router.get("/search")
def search(keyword: str = Query(...), current_user: User = Depends(get_curr_user)):
    return search_maintenance(keyword)

@main_router.patch("/{id}/status")
def patch_status(id: int, status: str = Query(...), current_user: User = Depends(get_curr_user)):
    return update_status_only(id, status)

@main_router.get("/{id}")
def get_one(id: int, current_user: User = Depends(get_curr_user)):
    return get_maintenance_by_id(id)

@main_router.put("/{id}")
def update(id: int, maint: MaintenanceUpdate, current_user: User = Depends(get_curr_user)):
    return update_maintenance(id, maint)

@main_router.delete("/{id}")
def delete(id: int, current_user: User = Depends(get_curr_user)):
    return delete_maintenance(id)
