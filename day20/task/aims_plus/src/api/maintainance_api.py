from fastapi import APIRouter, Query, Depends
from typing import Optional
from models.maintainance_model import MaintenanceCreate, MaintenanceUpdate, MaintenanceStatusUpdate
from auth.auth_jwt_token import get_current_user
from crud.maintainance_crud import (
    create_maintenance,
    list_maintenance,
    get_maintenance_by_id,
    update_maintenance,
    update_maintenance_status,
    delete_maintenance,
    search_maintenance,
    count_maintenance,
    bulk_upload_maintenance_from_csv,
)

router = APIRouter(prefix="/maintenance", tags=["Maintenance"])


def success(message: str, data=None):
    return {"status": "success", "message": message, "data": data}


@router.post("/create")
def create_maintenance_api(payload: MaintenanceCreate,current_user: dict = Depends(get_current_user)):
    return success("Maintenance record created", create_maintenance(payload))


@router.get("/list")
def list_maintenance_api(status: Optional[str] = Query(default=None),current_user: dict = Depends(get_current_user)):
    return success("Maintenance records fetched", list_maintenance(status))


@router.get("/{log_id}")
def get_maintenance_api(log_id: int,current_user: dict = Depends(get_current_user)):
    return success("Maintenance record fetched", get_maintenance_by_id(log_id))


@router.put("/{log_id}")
def update_maintenance_api(log_id: int, payload: MaintenanceUpdate,current_user: dict = Depends(get_current_user)):
    return success("Maintenance record updated", update_maintenance(log_id, payload))


@router.patch("/{log_id}/status")
def update_maintenance_status_api(log_id: int, payload: MaintenanceStatusUpdate,current_user: dict = Depends(get_current_user)):
    return success("Maintenance status updated", update_maintenance_status(log_id, payload.status))


@router.delete("/{log_id}")
def delete_maintenance_api(log_id: int,current_user: dict = Depends(get_current_user)):
    delete_maintenance(log_id)
    return success("Maintenance record deleted", None)


@router.get("/search/")
def search_maintenance_api(keyword: str = Query(...),current_user: dict = Depends(get_current_user)):
    return success("Maintenance search result", search_maintenance(keyword))


@router.get("/count")
def count_maintenance_api(current_user: dict = Depends(get_current_user)):
    return success("Total maintenance records counted", {"count": count_maintenance()})


@router.post("/bulk-upload")
def bulk_upload_maintenance_api(current_user: dict = Depends(get_current_user)):
    bulk_upload_maintenance_from_csv()
    return success("Maintenance bulk upload completed", None)
