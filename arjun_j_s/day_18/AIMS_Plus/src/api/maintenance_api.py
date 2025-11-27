from fastapi import APIRouter,HTTPException
from ..models.maintenance_model import MaintenanceLog
from ..crud.maintenance_crud import Maintain
from typing import List,Optional

log_service = Maintain()

log_router = APIRouter(prefix="/maintenance")


@log_router.get("/list")
def get_all(status:Optional[str]="all"):
    try:
        return log_service.get_all_log(status)
    except Exception as e:
        raise HTTPException(status_code=404,detail =str(e))
    
@log_router.get("/{log_id}")
def get_by_id(log_id:int):
    try:
        return log_service.get_log_by_id(log_id)
    except Exception as e:
        raise HTTPException(status_code=404,detail =str(e))
    
@log_router.put("/{log_id}")
def update_emp(log_id:int,log:MaintenanceLog):
    try:
        if log_service.update_log(log_id,log):
            return {"message" : "Update Successfull"}
        else:
            return {"message" : "Log Not Found"}
    except Exception as e:
        raise HTTPException(status_code=404,detail =str(e))
    
@log_router.patch("/{log_id}/")
def update_log(log_id:int,status:str):
    try:
        if log_service.update_log_status(log_id,status):
            return {"message" : "Update Successfull"}
        else:
            return {"message" : "Log Not Found"}
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404,detail=str(e))
    
@log_router.post("/create")
def create_log(log:MaintenanceLog):
    try:
        if log_service.create_maintenance(log):
            return {"message" : "Added Successfull"}
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404,detail=str(e))
    
@log_router.delete("/{log_id}")
def delete_log(log_id:int):
    try:
        if log_service.delete_log(log_id):
            return {"message" : "Deleted Successfull"}
        else:
            return {"message" : "Log Not Found"}
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404,detail=str(e))
    
@log_router.get("/search/keyword/")
def get_by_keyword(keyword:str,value:str):
    try:
        return log_service.get_log_keyword(keyword,value)
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404,detail =str(e))
    
@log_router.get("/all/count/")
def get_count():
    try:
        return log_service.get_log_count()
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404,detail =str(e))