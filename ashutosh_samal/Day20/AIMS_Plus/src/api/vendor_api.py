from fastapi import APIRouter, HTTPException,Depends
from typing import List, Optional
from ..model.vendor_model import VendorCreate
from ..auth.jwt_auth import jwt_router,get_current_user,User
from ..crud.vendor_crud import (
    get_vendors,
    get_vendor_by_id,
    create_vendor,
    update_vendor,
    update_vendor_status,
    delete_vendor,
    search_vendors,
    count_vendors
)

# Router for handling vendor-related API endpoints
vendor_router = APIRouter(prefix="/vendors")

# Endpoint to fetch all vendors, optionally filtered by active status
@vendor_router.get("/list")
async def list_vendors(status: Optional[str] = None,current_user: User = Depends(get_current_user)):
    try:
        vendors = get_vendors(status)
        return vendors
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to fetch a vendor by its ID
@vendor_router.get("/{vendor_id}")
async def get_vendor(vendor_id: int,current_user: User = Depends(get_current_user)):
    try:
        vendor = get_vendor_by_id(vendor_id)
        if not vendor:
            raise HTTPException(status_code=404, detail="Vendor not found")
        return vendor
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to create a new vendor
@vendor_router.post("/create")
async def create_vendor_endpoint(vendor: VendorCreate,current_user: User = Depends(get_current_user)):
    try:
        create_vendor(vendor)
        return vendor
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to update an existing vendor
@vendor_router.put("/{vendor_id}")
async def update_vendor_endpoint(vendor_id: int, vendor: VendorCreate,current_user: User = Depends(get_current_user)):
    try:
        update_vendor(vendor_id, vendor)
        return vendor
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to update a vendor's status (active/inactive)
@vendor_router.patch("/{vendor_id}/status")
async def update_vendor_status_endpoint(vendor_id: int, status: str,current_user: User = Depends(get_current_user)):
    try:
        update_vendor_status(vendor_id, status)
        return {"message": "Vendor status updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to delete a vendor
@vendor_router.delete("/{vendor_id}")
async def delete_vendor_endpoint(vendor_id: int,current_user: User = Depends(get_current_user)):
    try:
        delete_vendor(vendor_id)
        return {"message": "Vendor deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to search vendors by keyword
@vendor_router.get("/search")
async def search_vendors_endpoint(keyword: str,current_user: User = Depends(get_current_user)):
    try:
        vendors = search_vendors(keyword)
        return vendors
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to get the total count of vendors
@vendor_router.get("/count")
async def count_vendors_endpoint(current_user: User = Depends(get_current_user)):
    try:
        count = count_vendors()
        return {"total_vendors": count}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
