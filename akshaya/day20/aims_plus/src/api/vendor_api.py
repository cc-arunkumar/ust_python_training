from fastapi import FastAPI, HTTPException, UploadFile, File, Query, APIRouter, Depends
import csv, io
from src.models.vendor_model import VendorModel
from ..auth.jwt_auth import get_current_user
from ..models.user_model import User
from src.crud.vendor_crud import (
    create_vendor_db, get_all_vendors_db, list_vendors_by_status_db,
    get_vendor_by_id_db, update_vendor_db, update_vendor_status_db,
    delete_vendor_db, search_vendors_db, count_vendors_db
)

# Create an instance of APIRouter for vendor-related routes
vendor_router = APIRouter()

# 1. Create vendor endpoint
@vendor_router.post("/vendors/create")
def create_vendor(vendor: VendorModel, current_user: User = Depends(get_current_user)):
    """
    Creates a new vendor record in the database.
    The vendor data is provided in the request body.
    The user must be authenticated via JWT (Depends on `get_current_user`).
    """
    # Attempt to create the vendor in the database
    if not create_vendor_db(vendor):
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "message": "Vendor created successfully"}

# 2. Search vendors endpoint
@vendor_router.get("/vendors/search")
def search_vendors(keyword: str = Query(...), value: str = Query(...), current_user: User = Depends(get_current_user)):
    """
    Searches vendors based on a provided keyword and value.
    The user must be authenticated via JWT.
    """
    # Perform the search based on the provided keyword and value
    result = search_vendors_db(keyword, value)

    # Handle case where the database query fails
    if result is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "data": result}

# 3. Count total vendors endpoint
@vendor_router.get("/vendors/count")
def count_vendors(current_user: User = Depends(get_current_user)):
    """
    Returns the total count of vendors in the database.
    The user must be authenticated via JWT.
    """
    # Fetch the total count of vendors from the database
    total = count_vendors_db()

    # Handle case where the database query fails
    if total is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "count": total}

# 4. Get all vendors or filter by status endpoint
@vendor_router.get("/vendors/list")
def list_vendors(status: str = None, current_user: User = Depends(get_current_user)):
    """
    Returns a list of all vendors, optionally filtered by status.
    The user must be authenticated via JWT.
    """
    # If status is provided, filter vendors by status
    if status:
        result = list_vendors_by_status_db(status)
    else:
        # Otherwise, fetch all vendors
        result = get_all_vendors_db()

    # Handle case where database query fails
    if result is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "data": result}

# 5. Get vendor by ID endpoint
@vendor_router.get("/vendors/{id}")
def get_vendor(id: int, current_user: User = Depends(get_current_user)):
    """
    Fetches a specific vendor by its ID.
    Returns vendor data if found, otherwise raises a 404 error.
    The user must be authenticated via JWT.
    """
    # Fetch the vendor by ID from the database
    vendor = get_vendor_by_id_db(id)

    # If no vendor is found, raise a 404 HTTP exception
    if vendor is None:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return {"status": "success", "data": vendor}

# 6. Update vendor endpoint
@vendor_router.put("/vendors/{id}")
def update_vendor(id: int, vendor: VendorModel, current_user: User = Depends(get_current_user)):
    """
    Updates an existing vendor record with the provided new data.
    The user must be authenticated via JWT.
    """
    # Attempt to update the vendor in the database
    if not update_vendor_db(id, vendor):
        raise HTTPException(status_code=404, detail="Vendor not found")
    return {"status": "success", "message": "Vendor updated successfully"}

# 7. Update vendor status endpoint
@vendor_router.patch("/vendors/{id}/status")
def update_vendor_status(id: int, status: str, current_user: User = Depends(get_current_user)):
    """
    Updates only the status of an existing vendor.
    The user must be authenticated via JWT.
    """
    # Attempt to update the vendor's status in the database
    if not update_vendor_status_db(id, status):
        raise HTTPException(status_code=404, detail="Vendor not found")
    return {"status": "success", "message": "Vendor status updated"}

# 8. Delete vendor endpoint
@vendor_router.delete("/vendors/{id}")
def delete_vendor(id: int, current_user: User = Depends(get_current_user)):
    """
    Deletes a vendor record by its ID.
    The user must be authenticated via JWT.
    """
    # Attempt to delete the vendor from the database
    if not delete_vendor_db(id):
        raise HTTPException(status_code=404, detail="Vendor not found")
    return {"status": "success", "message": f"Vendor {id} deleted"}
