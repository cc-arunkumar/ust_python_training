from fastapi import APIRouter, Query, Depends
from src.models.vendor_model import VendorCreate, VendorUpdate
from src.crud.vendor_crud import *
from src.auth.auth import get_curr_user
from src.models.login_model import User

vendor_router = APIRouter(prefix="/vendors", tags=["Vendors"])

@vendor_router.post("/create")
def create(vendor: VendorCreate, current_user: User = Depends(get_curr_user)):
    return create_vendor(
        vendor.vendor_name,
        vendor.contact_person,
        vendor.contact_phone,
        vendor.gst_number,
        vendor.email,
        vendor.address,
        vendor.city,
        vendor.active_status
    )

@vendor_router.get("/list")
def list_all(status: str = "ALL", current_user: User = Depends(get_curr_user)):
    return get_all_vendors(status)

@vendor_router.get("/count")
def count(current_user: User = Depends(get_curr_user)):
    return count_vendors()

@vendor_router.get("/search")
def search(keyword: str = Query(...), current_user: User = Depends(get_curr_user)):
    return search_vendors(keyword)

@vendor_router.patch("/{id}/status")
def patch_status(id: int, status: str = Query(...), current_user: User = Depends(get_curr_user)):
    return update_status_only(id, status)

@vendor_router.put("/{id}")
def update(id: int, vendor: VendorUpdate, current_user: User = Depends(get_curr_user)):
    return update_vendor(
        id, vendor.vendor_name, vendor.contact_person,
        vendor.contact_phone, vendor.gst_number, vendor.email,
        vendor.address, vendor.city, vendor.active_status
    )

@vendor_router.delete("/{id}")
def delete(id: int, current_user: User = Depends(get_curr_user)):
    return delete_vendor(id)

@vendor_router.get("/{id}")
def get_one(id: int, current_user: User = Depends(get_curr_user)):
    return get_vendor_by_id(id)
