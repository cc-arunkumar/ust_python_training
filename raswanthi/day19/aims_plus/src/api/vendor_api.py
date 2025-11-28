from fastapi import FastAPI, HTTPException, Query, APIRouter, Depends
from ..auth.auth_jwt_token import get_current_user   # Dependency to get the currently logged-in user
from ..models.user_model import User                 # User model for authentication
from src.models.vendor_model import VendorModel      # Vendor model definition
from src.crud.vendor_crud import (
    create_vendor_db, get_all_vendors_db, list_vendors_by_status_db,
    get_vendor_by_id_db, update_vendor_db, update_vendor_status_db,
    delete_vendor_db, search_vendors_db, count_vendors_db
)

# Create a router for vendor-related endpoints with a common prefix
vendor_router = APIRouter(prefix="/vendors")


# ------------------- CREATE -------------------
@vendor_router.post("/vendors/create")
def create_vendor(vendor: VendorModel, current_user: User = Depends(get_current_user)):
    """
    Create a new vendor record.
    - Requires authentication (current_user).
    - Accepts VendorModel object as input.
    - Returns success message if created, else raises HTTP 500.
    """
    if not create_vendor_db(vendor):
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "message": "Vendor created successfully"}


# ------------------- SEARCH -------------------
@vendor_router.get("/vendors/search")
def search_vendors(keyword: str = Query(...), value: str = Query(...), current_user: User = Depends(get_current_user)):
    """
    Search vendors by keyword and value.
    - Example: /vendors/search?keyword=name&value=ABC Corp
    - Returns matching vendors.
    - Raises HTTP 500 if database connection fails.
    """
    result = search_vendors_db(keyword, value)
    if result is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "data": result}


# ------------------- COUNT -------------------
@vendor_router.get("/vendors/count")
def count_vendors(current_user: User = Depends(get_current_user)):
    """
    Count total number of vendors.
    - Returns integer count.
    - Raises HTTP 500 if database connection fails.
    """
    total = count_vendors_db()
    if total is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "count": total}


# ------------------- LIST -------------------
@vendor_router.get("/vendors/list")
def list_vendors(status: str = None, current_user: User = Depends(get_current_user)):
    """
    List all vendors.
    - Optional query parameter 'status' to filter vendors by status.
    - Returns all vendors if no status is provided.
    - Raises HTTP 500 if database connection fails.
    """
    if status:
        result = list_vendors_by_status_db(status)
    else:
        result = get_all_vendors_db()
    if result is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "data": result}


# ------------------- GET BY ID -------------------
@vendor_router.get("/vendors/{id}")
def get_vendor(id: int, current_user: User = Depends(get_current_user)):
    """
    Retrieve a single vendor by ID.
    - Returns vendor details if found.
    - Raises HTTP 404 if vendor not found.
    """
    vendor = get_vendor_by_id_db(id)
    if vendor is None:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return {"status": "success", "data": vendor}


# ------------------- UPDATE -------------------
@vendor_router.put("/vendors/{id}")
def update_vendor(id: int, vendor: VendorModel, current_user: User = Depends(get_current_user)):
    """
    Update an existing vendor by ID.
    - Accepts VendorModel object with updated fields.
    - Returns success message if updated.
    - Raises HTTP 404 if vendor not found.
    """
    if not update_vendor_db(id, vendor):
        raise HTTPException(status_code=404, detail="Vendor not found")
    return {"status": "success", "message": "Vendor updated successfully"}


# ------------------- UPDATE STATUS -------------------
@vendor_router.patch("/vendors/{id}/status")
def update_vendor_status(id: int, status: str, current_user: User = Depends(get_current_user)):
    """
    Update only the status of a vendor.
    - Example: PATCH /vendors/1/status?status=inactive
    - Returns success message if updated.
    - Raises HTTP 404 if vendor not found.
    """
    if not update_vendor_status_db(id, status):
        raise HTTPException(status_code=404, detail="Vendor not found")
    return {"status": "success", "message": "Vendor status updated"}


# ------------------- DELETE -------------------
@vendor_router.delete("/vendors/{id}")
def delete_vendor(id: int, current_user: User = Depends(get_current_user)):
    """
    Delete a vendor by ID.
    - Returns success message if deleted.
    - Raises HTTP 404 if vendor not found.
    """
    if not delete_vendor_db(id):
        raise HTTPException(status_code=404, detail="Vendor not found")
    return {"status": "success", "message": f"Vendor {id} deleted"}
