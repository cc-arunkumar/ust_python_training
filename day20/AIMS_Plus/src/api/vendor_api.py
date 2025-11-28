from fastapi import APIRouter, HTTPException,Depends
from ..models.vendor_model import VendorMaster
from ..models.user_model import User
from ..crud.vendor_crud import Vendor
from typing import List, Optional
from ..auth.jwt_auth import get_current_user

vendor_service = Vendor()  # Service instance for vendor CRUD
vendor_router = APIRouter(prefix="/vendor")  # Router with /vendor prefix


@vendor_router.get("/list")
def get_all(status: Optional[str] = "all",current_user : User =Depends(get_current_user)):  # Get all vendors (optionally filter by status)
    try:
        return vendor_service.get_all_vendor(status)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@vendor_router.get("/{vendor_id}")
def get_by_id(vendor_id: int,current_user : User =Depends(get_current_user)):  # Get vendor by ID
    try:
        return vendor_service.get_vendor_by_id(vendor_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@vendor_router.put("/{vendor_id}")
def update_vendor(vendor_id: int, vendor: VendorMaster,current_user : User =Depends(get_current_user)):  # Update full vendor record
    try:
        if vendor_service.update_vendor(vendor_id, vendor):
            return {"message": "Update Successful"}
        else:
            return {"message": "Vendor Not Found"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@vendor_router.patch("/{vendor_id}/")
def update_vendor(vendor_id: int, status: str,current_user : User =Depends(get_current_user)):  # Update only vendor status
    try:
        if vendor_service.update_vendor_status(vendor_id, status):
            return {"message": "Update Successful"}
        else:
            return {"message": "Vendor Not Found"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@vendor_router.post("/create")
def create_vendor(vendor: VendorMaster,current_user : User =Depends(get_current_user)):  # Create new vendor
    try:
        if vendor_service.create_vendor(vendor):
            return {"message": "Added Successful"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@vendor_router.delete("/{vendor_id}")
def delete_vendor(vendor_id: int,current_user : User =Depends(get_current_user)):  # Delete vendor by ID
    try:
        if vendor_service.delete_vendor(vendor_id):
            return {"message": "Deleted Successful"}
        else:
            return {"message": "Vendor Not Found"}  # Fixed message (was "Log Not Found")
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@vendor_router.get("/search/keyword/")
def get_by_keyword(keyword: str, value: str,current_user : User =Depends(get_current_user)):  # Search vendor by keyword/value
    try:
        return vendor_service.get_vendor_keyword(keyword, value)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@vendor_router.get("/all/count/")
def get_count(current_user : User =Depends(get_current_user)):  # Get total vendor count
    try:
        return vendor_service.get_vendor_count()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))