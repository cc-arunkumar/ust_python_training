from fastapi import FastAPI,HTTPException,APIRouter
from typing import Optional
from ..models.maintenancelog import MaintenanceLog,StatusValidate
from ..crud.maintenance_crud import MaintenanceCrud

maintenance_reader = MaintenanceCrud()
maintenance_router = APIRouter(prefix="/maintenance")

@maintenance_router.post("/create")
def create_maintenance(maintenance:MaintenanceLog):
    try:
        return maintenance_reader.create_maintenance(maintenance)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404,detail="Not Found")

@maintenance_router.get("/list")
def get_all_maintenance(status:Optional[str] = "ALL"):
    try:
        return maintenance_reader.get_all_maintenance(status)
    except Exception:
        raise HTTPException(status_code=404,detail="Not Found")

@maintenance_router.get("/{id}")
def get_maintenance_by_id(id:int):
    try:
        return maintenance_reader.get_maintenance_by_id(id)
    except Exception:
        raise HTTPException(status_code=404,detail="Not Found")

@maintenance_router.put("/{id}")
def update_maintenance(id:int,data:MaintenanceLog):
    try:
        return maintenance_reader.update_maintenance(id,data)
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404,detail="Not Found")

@maintenance_router.patch("/{id}/status")
def update_maintenance_status(id:int,status:StatusValidate):
    try:
        print(status)
        return maintenance_reader.update_maintenance_status(id,status.status)
    except Exception:
        raise HTTPException(status_code=404,detail="Not Found")

@maintenance_router.delete("/{id}")
def delete_maintenance(id:int):
    try:
        return maintenance_reader.delete_maintenance(id)
    except Exception:
        raise HTTPException(status_code=404,detail="Not Found")

@maintenance_router.get("/search/keyword")
def get_maintenance_by_keyword(keyword:str,value:str):
    try:
        return maintenance_reader.get_maintenance_by_keyword(keyword,value)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404,detail="Not Found")

@maintenance_router.get("/list/count")
def get_count():
    try:
        return maintenance_reader.get_all_maintenance_count()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404,detail="Not Found")
