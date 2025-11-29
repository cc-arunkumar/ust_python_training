from fastapi import APIRouter, Query,Depends
from typing import Optional
from models.vendor_model import VendorCreate, VendorUpdate, VendorStatusUpdate
from auth.auth_jwt_token import get_current_user
from crud.vendor_crud import (
    create_vendor,
    list_vendors,
    get_vendor_by_id,
    update_vendor,
    update_vendor_status,
    delete_vendor,
    search_vendor,
    count_vendors,
    bulk_upload_vendors_from_csv,
)

router = APIRouter(prefix="/vendors", tags=["Vendors"])


def success(message: str, data=None):
    return {"status": "success", "message": message, "data": data}


@router.post("/create")
def create_vendor_api(payload: VendorCreate,current_user: dict = Depends(get_current_user)):
    return success("Vendor created successfully", create_vendor(payload))


@router.get("/list")
def list_vendors_api(status: Optional[str] = Query(default=None),current_user: dict = Depends(get_current_user)):
    return success("Vendors fetched successfully", list_vendors(status))


@router.get("/{vendor_id}")
def get_vendor_api(vendor_id: int,current_user: dict = Depends(get_current_user)):
    return success("Vendor fetched successfully", get_vendor_by_id(vendor_id))


@router.put("/{vendor_id}")
def update_vendor_api(vendor_id: int, payload: VendorUpdate,current_user: dict = Depends(get_current_user)):
    return success("Vendor updated successfully", update_vendor(vendor_id, payload))


@router.patch("/{vendor_id}/status")
def update_vendor_status_api(vendor_id: int, payload: VendorStatusUpdate,current_user: dict = Depends(get_current_user)):
    return success("Vendor status updated successfully", update_vendor_status(vendor_id, payload.active_status))


@router.delete("/{vendor_id}")
def delete_vendor_api(vendor_id: int,current_user: dict = Depends(get_current_user)):
    delete_vendor(vendor_id)
    return success("Vendor deleted successfully", None)


@router.get("/search/")
def search_vendor_api(keyword: str = Query(...),current_user: dict = Depends(get_current_user)):
    return success("Vendors search result", search_vendor(keyword))


@router.get("/count")
def count_vendors_api(current_user: dict = Depends(get_current_user)):
    return success("Total vendors counted successfully", {"count": count_vendors()})


@router.post("/bulk-upload")
def bulk_upload_vendors_api(current_user: dict = Depends(get_current_user)):
    bulk_upload_vendors_from_csv()
    return success("Vendors bulk uploaded successfully", None)
