from src.auth.jwt_auth import get_current_user
from src.models.login_model import User
from src.crud.maintenance_inventory import get_maintenance_by_id,list_maintenance,list_maintenance_by_status,update_maintenance,update_maintenance_status,delete_maintenance,create_maintenance
import pymysql
from fastapi import FastAPI, HTTPException,Depends,APIRouter
from src.models.maintenance_pydentic import MaintenanceLog


maintenance_router = APIRouter(prefix="/maintenance")





@maintenance_router.post("/create")
def create_maintenance_api(log: MaintenanceLog,current_user: User = Depends(get_current_user)):
    return create_maintenance(log)

@maintenance_router.get("/list")
def list_maintenance_api(current_user: User = Depends(get_current_user)):
    return list_maintenance()

@maintenance_router.get("/list/status")
def list_maintenance_status_api(status: str,current_user: User = Depends(get_current_user)):
    return list_maintenance_by_status(status)

@maintenance_router.get("/{id}")
def get_maintenance_api(id: int,current_user: User = Depends(get_current_user)):
    return get_maintenance_by_id(id)

@maintenance_router.put("/{id}")
def update_maintenance_api(id: int, row: dict,current_user: User = Depends(get_current_user)):
    return update_maintenance(id, row)

@maintenance_router.patch("/{id}/status")
def update_maintenance_status_api(id: int, status: str,current_user: User = Depends(get_current_user)):
    return update_maintenance_status(id, status)

@maintenance_router.delete("/{id}")
def delete_maintenance_api(id: int,current_user: User = Depends(get_current_user)):
    return delete_maintenance(id)
