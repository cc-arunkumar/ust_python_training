from fastapi import APIRouter,HTTPException
from ..models.vendor_model import VendorMaster
from ..crud.vendor_crud import Vendor
from typing import List,Optional

vendor_service = Vendor()

vendor_router = APIRouter(prefix="/vendor")


@vendor_router.get("/list")
def get_all(status:Optional[str]="all"):
    try:
        return vendor_service.get_all_vendor(status)
    except Exception as e:
        raise HTTPException(status_code=404,detail =str(e))
    
@vendor_router.get("/{vendor_id}")
def get_by_id(vendor_id:int):
    try:
        return vendor_service.get_vendor_by_id(vendor_id)
    except Exception as e:
        raise HTTPException(status_code=404,detail =str(e))
    
@vendor_router.put("/{vendor_id}")
def update_vendor(vendor_id:int,vendor:VendorMaster):
    try:
        if vendor_service.update_vendor(vendor_id,vendor):
            return {"message" : "Update Successfull"}
        else:
            return {"message" : "Vendor Not Found"}
    except Exception as e:
        raise HTTPException(status_code=404,detail =str(e))
    
@vendor_router.patch("/{vendor_id}/")
def update_vendor(vendor_id:int,status:str):
    try:
        if vendor_service.update_vendor_status(vendor_id,status):
            return {"message" : "Update Successfull"}
        else:
            return {"message" : "Vendor Not Found"}
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404,detail=str(e))
    
@vendor_router.post("/create")
def create_vendor(vendor:VendorMaster):
    try:
        if vendor_service.create_vendor(vendor):
            return {"message" : "Added Successfull"}
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404,detail=str(e))
    
@vendor_router.delete("/{vendor_id}")
def delete_vendor(vendor_id:int):
    try:
        if vendor_service.delete_vendor(vendor_id):
            return {"message" : "Deleted Successfull"}
        else:
            return {"message" : "Log Not Found"}
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404,detail=str(e))
    
@vendor_router.get("/search/keyword/")
def get_by_keyword(keyword:str,value:str):
    try:
        return vendor_service.get_vendor_keyword(keyword,value)
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404,detail =str(e))
    
@vendor_router.get("/all/count/")
def get_count():
    try:
        return vendor_service.get_vendor_count()
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404,detail =str(e))