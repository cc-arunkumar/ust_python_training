from fastapi import FastAPI, HTTPException, APIRouter,Depends
from src.models.login_model import User
from src.auth.jwt_auth import get_current_user
from src.models import vendor_model
from src.crud import vendor_crud
from typing import List, Optional

# Router for vendor-related endpoints, all prefixed with "/vendors"
vendor_router = APIRouter(prefix="/vendors")


# -------------------------------
# Endpoint: Search vendors by field
# -------------------------------
@vendor_router.get("/search", response_model=List[vendor_model.VendorMaster])
def search(field: str, val: str,current_user: User = Depends(get_current_user)):
    """
    Search vendors by a given field and value.
    Example: /vendors/search?field=name&val=ABC Corp
    """
    if vendor_crud.search_by_tag_vendor(field, val):
        return vendor_crud.search_by_tag_vendor(field, val)
    raise HTTPException(status_code=404, detail="Not found")


# -------------------------------
# Endpoint: Create a new vendor
# -------------------------------
@vendor_router.post("/create", response_model=vendor_model.VendorMaster)
def create_vendor(new_vendor: vendor_model.VendorMaster,current_user: User = Depends(get_current_user)):
    """
    Create a new vendor record.
    Validates vendor data before inserting into DB.
    """
    if not vendor_model.validate(new_vendor):
        raise HTTPException(status_code=409, detail="Validation failed")
    if not vendor_crud.create_vendor(new_vendor):
        raise HTTPException(status_code=400, detail="Failed to create the Vendor")
    return new_vendor


# -------------------------------
# Endpoint: List all vendors / List all By Status
# -------------------------------
@vendor_router.get("/list", response_model=List[vendor_model.VendorMaster])
def get_all(status: Optional[str] = "",current_user: User = Depends(get_current_user)):
    """
    Retrieve all vendors, optionally filtered by status.
    Example: /vendors/list?status=active
    """
    data = vendor_crud.get_all_vendors(status)
    new_li = []
    for row in list(data):
        x = vendor_model.VendorMaster(**row)  # Convert dict to VendorMaster model
        new_li.append(x)
    return new_li


# -------------------------------
# Endpoint: Count all vendors
# -------------------------------
@vendor_router.get("/count")
def count_all(current_user: User = Depends(get_current_user)):
    """
    Return the total count of vendors in the system.
    """
    data = vendor_crud.get_all_vendors()
    return {"detail": f"Count of records: {len(data)}"}


# -------------------------------
# Endpoint: Get vendor by ID
# -------------------------------
@vendor_router.get("/{id}", response_model=vendor_model.VendorMaster)
def get_by_id(id: int,current_user: User = Depends(get_current_user)):
    """
    Retrieve a single vendor by its ID.
    """
    data = vendor_crud.get_vendor_by_id(id)
    if data:
        return vendor_model.VendorMaster(**data)
    raise HTTPException(status_code=404, detail="Vendor id not found")


# -------------------------------
# Endpoint: Update vendor by ID
# -------------------------------
@vendor_router.put("/{id}", response_model=vendor_model.VendorMaster)
def update_by_id(id: int, new_vendor: vendor_model.VendorMaster,current_user: User = Depends(get_current_user)):
    """
    Update an existing vendor by ID.
    Validates vendor data before updating.
    """
    if vendor_model.validate(new_vendor):
        pass
    else:
        raise HTTPException(status_code=409, detail="Validation failed")
    if vendor_crud.update_vendor_by_id(id, new_vendor):
        return new_vendor
    raise HTTPException(status_code=400, detail="Unable to update Vendor")


# -------------------------------
# Endpoint: Patch vendor status
# -------------------------------
@vendor_router.patch("/{id}/status", response_model=vendor_model.VendorMaster)
def patch_by_id(id: int, status: str,current_user: User = Depends(get_current_user)):
    """
    Update only the active_status field of a vendor by ID.
    """
    data = get_by_id(id)
    if data:
        data.active_status = status
        return update_by_id(id, data)
    raise HTTPException(status_code=404, detail="ID not found")


# -------------------------------
# Endpoint: Delete vendor by ID
# -------------------------------
@vendor_router.delete("/{id}")
def delete_vendor_id(id: int,current_user: User = Depends(get_current_user)):
    """
    Delete a vendor record by ID.
    """
    if vendor_crud.delete_vendor_by_id(id):
        return {"detail": "Record deleted successfully"}
    raise HTTPException(status_code=404, detail="Vendor Id Doesnt Exist")
