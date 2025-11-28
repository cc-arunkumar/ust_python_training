from fastapi import APIRouter, HTTPException,Depends  # Import FastAPI components
from typing import List, Optional  # Import typing components for type hinting
from ..models.vendor_model import VendorCreate  # Import VendorCreate model from vendor_model
from ..crud.vendor_crud import (
    get_vendors,  # Import CRUD operations for vendors
    get_vendor_by_id,
    create_vendor,
    update_vendor,
    update_vendor_status,
    delete_vendor,
    search_vendors,
    count_vendors
)
from ..auth.auth_jwt_token import get_current_user

vendor_router = APIRouter(prefix="/vendors",tags=["Vendor"])  # Create a new router for vendor-related endpoints


# Endpoint to list vendors, optionally filtered by status
@vendor_router.get("/list")
async def list_vendors(status: Optional[str] = None,current_user: dict = Depends(get_current_user)):
    try:
        vendors = get_vendors(status)  # Fetch vendors based on status
        return vendors
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure


# Endpoint to fetch a specific vendor by ID
@vendor_router.get("/{vendor_id}")
async def get_vendor(vendor_id: int,current_user: dict = Depends(get_current_user)):
    try:
        vendor = get_vendor_by_id(vendor_id)  # Fetch vendor by ID
        if not vendor:
            raise HTTPException(status_code=404, detail="Vendor not found")  # Return error if not found
        return vendor
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure



# Endpoint to create a new vendor
@vendor_router.post("/create")
async def create_vendor_endpoint(vendor: VendorCreate,current_user: dict = Depends(get_current_user)):
    try:
        create_vendor(vendor)  # Call CRUD function to create vendor
        return vendor  # Return created vendor
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure


# Endpoint to update an existing vendor by ID
@vendor_router.put("/{vendor_id}")
async def update_vendor_endpoint(vendor_id: int, vendor: VendorCreate,current_user: dict = Depends(get_current_user)):
    try:
        update_vendor(vendor_id, vendor)  # Update vendor using the provided ID and data
        return vendor  # Return updated vendor
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure


# Endpoint to update the status of a vendor
@vendor_router.patch("/{vendor_id}/status")
async def update_vendor_status_endpoint(vendor_id: int, status: str,current_user: dict = Depends(get_current_user)):
    try:
        update_vendor_status(vendor_id, status)  # Update vendor status
        return {"message": "Vendor status updated successfully"}  # Return success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure


# Endpoint to delete a vendor by ID
@vendor_router.delete("/{vendor_id}")
async def delete_vendor_endpoint(vendor_id: int,current_user: dict = Depends(get_current_user)):
    try:
        delete_vendor(vendor_id)  # Delete vendor using the provided ID
        return {"message": "Vendor deleted successfully"}  # Return success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure


# Endpoint to search for vendors based on a keyword
@vendor_router.get("/search")
async def search_vendors_endpoint(keyword: str,current_user: dict = Depends(get_current_user)):
    try:
        vendors = search_vendors(keyword)  # Search for vendors by keyword
        return vendors
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure


# Endpoint to get the count of total vendors
@vendor_router.get("/count")
async def count_vendors_endpoint(current_user: dict = Depends(get_current_user)):
    try:
        count = count_vendors()  # Get total vendor count
        return {"total_vendors": count}  # Return vendor count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure
