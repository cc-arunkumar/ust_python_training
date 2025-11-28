from src.crud.vendors import get_all_data,get_data_by_status,get_data_by_id,create_vendor,update_vendor,count_vendors,get_rows_by_column,delete_vendor,update_vendor_status
from src.auth.jwt_auth import get_current_user
from src.models.login_model import User
from src.models.vendors_pydentic import VendorMaster
import pymysql
from fastapi import FastAPI, HTTPException,Depends,APIRouter

from typing import List
vendor_router= APIRouter(prefix="/vendors")


@vendor_router.get("/list", response_model=List[VendorMaster])
def get_data(current_user: User = Depends(get_current_user)):
    return get_all_data() 


@vendor_router.get("/list/status")
def get_all_status(active_status: str,current_user: User = Depends(get_current_user)):
    return get_data_by_status(active_status)


@vendor_router.get("/list/{id}")
def get_data_id(id:int,current_user: User = Depends(get_current_user)):
    return get_data_by_id(id)


@vendor_router.post("/create")
def create_vendor_api(vendor: VendorMaster,current_user: User = Depends(get_current_user)):
    return create_vendor(vendor)


@vendor_router.put("/{id}")
def update_vendor_api(id: str, vendor: VendorMaster,current_user: User = Depends(get_current_user)):
    return update_vendor(id, vendor)

@vendor_router.patch("/{id}/status")
def update_vendor_status_api(id: str, status: str,current_user: User = Depends(get_current_user)):
    return update_vendor_status(id, status)

@vendor_router.delete("/{id}")
def delete_vendor_api(id: str,current_user: User = Depends(get_current_user)):
    return delete_vendor(id)

@vendor_router.get("/filter")
def filter_vendors(column: str, keyword: str,current_user: User = Depends(get_current_user)):
    return get_rows_by_column(column, keyword)
@vendor_router.get("/count")
def count_vendors_api(current_user: User = Depends(get_current_user)):
    return {"total_vendors": count_vendors()}
