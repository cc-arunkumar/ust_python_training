from fastapi import FastAPI,HTTPException,APIRouter
from typing import Optional
from ..models.vendormaster import VendorMaster,StatusValidate
from ..crud.vendor_crud import VendorCrud

vendor_reader = VendorCrud()
vendor_router = APIRouter(prefix="/vendor")

@vendor_router.post("/create")
def create_vendor(vendor:VendorMaster):
    try:
        return vendor_reader.create_vendor(vendor)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404,detail="Not Found")

@vendor_router.get("/list")
def get_all_vendor(status:Optional[str] = "ALL"):
    try:
        return vendor_reader.get_all_vendor(status)
    except Exception:
        raise HTTPException(status_code=404,detail="Not Found")

@vendor_router.get("/{id}")
def get_vendor_by_id(id:int):
    try:
        return vendor_reader.get_vendor_by_id(id)
    except Exception:
        raise HTTPException(status_code=404,detail="Not Found")

@vendor_router.put("/{id}")
def update_vendor(id:int,data:VendorMaster):
    try:
        return vendor_reader.update_vendor(id,data)
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404,detail="Not Found")

@vendor_router.patch("/{id}/status")
def update_vendor_status(id:int,status:StatusValidate):
    try:
        print(status)
        return vendor_reader.update_vendor_status(id,status.status)
    except Exception:
        raise HTTPException(status_code=404,detail="Not Found")

@vendor_router.delete("/{id}")
def delete_vendor(id:int):
    try:
        return vendor_reader.delete_vendor(id)
    except Exception:
        raise HTTPException(status_code=404,detail="Not Found")

@vendor_router.get("/search/keyword")
def get_vendor_by_keyword(keyword:str,value:str):
    try:
        return vendor_reader.get_vendor_by_keyword(keyword,value)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404,detail="Not Found")

@vendor_router.get("/list/count")
def get_count():
    try:
        return vendor_reader.get_all_vendor_count()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404,detail="Not Found")
