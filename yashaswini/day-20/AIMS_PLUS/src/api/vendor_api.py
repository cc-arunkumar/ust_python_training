from fastapi import FastAPI, HTTPException, APIRouter,Depends
from typing import Optional
from ..models.vendor_master import VendorMaster, StatusValidate
from ..crud.vendor_crud import VendorCrud
from ..auth.jwt_auth import get_current_user,User

# Initialize CRUD handler for vendor operations
vendor_reader = VendorCrud()

# Create a router instance with a prefix for all vendor-related endpoints
vendor_router = APIRouter(prefix="/vendor")


@vendor_router.post("/create")
def create_vendor(vendor: VendorMaster,current_user: User = Depends(get_current_user)):
    """
    Endpoint to create a new vendor record.
    Accepts a VendorMaster model as input.
    """
    try:
        return vendor_reader.create_vendor(vendor)
    except Exception as e:
        # Log the error for debugging purposes
        print(e)
        raise HTTPException(status_code=404, detail="Not Found")


@vendor_router.get("/list")
def get_all_vendor(status: Optional[str] = "ALL",current_user: User = Depends(get_current_user)):
    """
    Endpoint to retrieve all vendors.
    Optional query parameter 'status' can filter vendors by status.
    Defaults to 'ALL' to return every vendor.
    """
    try:
        return vendor_reader.get_all_vendor(status)
    except Exception:
        raise HTTPException(status_code=404, detail="Not Found")


@vendor_router.get("/{id}")
def get_vendor_by_id(id: int,current_user: User = Depends(get_current_user)):
    """
    Endpoint to fetch a single vendor by their unique ID.
    """
    try:
        return vendor_reader.get_vendor_by_id(id)
    except Exception:
        raise HTTPException(status_code=404, detail="Not Found")


@vendor_router.put("/{id}")
def update_vendor(id: int, data: VendorMaster,current_user: User = Depends(get_current_user)):
    """
    Endpoint to update an existing vendor record by ID.
    Accepts a VendorMaster model with updated data.
    """
    try:
        return vendor_reader.update_vendor(id, data)
    except Exception as e:
        # Log the error for debugging purposes
        print(str(e))
        raise HTTPException(status_code=404, detail="Not Found")


@vendor_router.patch("/{id}/status")
def update_vendor_status(id: int, status: StatusValidate,current_user: User = Depends(get_current_user)):
    """
    Endpoint to update only the status of a vendor.
    Accepts a StatusValidate model containing the new status.
    """
    try:
        print(status)  # Debug print, can be replaced with proper logging
        return vendor_reader.update_vendor_status(id, status.status)
    except Exception:
        raise HTTPException(status_code=404, detail="Not Found")


@vendor_router.delete("/{id}")
def delete_vendor(id: int,current_user: User = Depends(get_current_user)):
    """
    Endpoint to delete a vendor record by ID.
    """
    try:
        return vendor_reader.delete_vendor(id)
    except Exception:
        raise HTTPException(status_code=404, detail="Not Found")


@vendor_router.get("/search/keyword")
def get_vendor_by_keyword(keyword: str, value: str,current_user: User = Depends(get_current_user)):
    """
    Endpoint to search vendors dynamically by a given keyword and value.
    Example: /vendor/search/keyword?keyword=name&value=ABC Corp
    """
    try:
        return vendor_reader.get_vendor_by_keyword(keyword, value)
    except Exception as e:
        print(e)  # Debug print, can be replaced with proper logging
        raise HTTPException(status_code=404, detail="Not Found")


@vendor_router.get("/list/count")
def get_count(current_user: User = Depends(get_current_user)):
    """
    Endpoint to return the total count of vendors.
    Useful for dashboards or summary views.
    """
    try:
        return vendor_reader.get_all_vendor_count()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail="Not Found")