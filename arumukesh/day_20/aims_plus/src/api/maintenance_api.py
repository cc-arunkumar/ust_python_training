from fastapi import Depends,APIRouter, HTTPException
from src.model.model_maintenance_log import MaintenanceLog
from src.auth.jwt_authentication import get_current_user,User
from src.crud.maintenance_cruf import (
    create,
    get_all,
    get_by_id,
    update,
    delete,
    get_count,
    find,
    set_status
)

router = APIRouter(prefix="/maintenance", tags=["Maintenance Logs"])


@router.post("/")
def create(data: MaintenanceLog,current_user:User=Depends(get_current_user)):
    return create(data)


@router.get("/")
def list_all(current_user:User=Depends(get_current_user)):
    return get_all()


@router.get("/status/{status}")
def filter_by_status(status: str,current_user:User=Depends(get_current_user)):
    return get_all(status)


@router.get("/search/{column}/{value}")
def search(column: str, value: str,current_user:User=Depends(get_current_user)):
    return find(column, value)


@router.get("/count")
def count_data(current_user:User=Depends(get_current_user)):
    return get_count()


@router.get("/{log_id}")
def get(log_id: int,current_user:User=Depends(get_current_user)):
    result = get_by_id(log_id)
    if not result:
        raise HTTPException(404, "Record not found")
    return result


@router.put("/{log_id}")
def modify(log_id: int, data: MaintenanceLog,current_user:User=Depends(get_current_user)):
    return update(log_id, data)


@router.patch("/{log_id}/status/{status}")
def update_status(log_id: int, status: str,current_user:User=Depends(get_current_user)):
    return set_status(log_id, status)


@router.delete("/{log_id}")
def remove(log_id: int,current_user:User=Depends(get_current_user)):
    return delete(log_id)
