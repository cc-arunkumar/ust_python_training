from fastapi import FastAPI, HTTPException, status, APIRouter, Depends
from src.crud import vendor_crud
from src.models import vendor_model
from typing import List, Optional
from src.auth.auth_jwt_token import get_current_user
from src.models.login_model import User


# Router for vendor endpoints
vendors_router = APIRouter(prefix="/vendors")

# Search vendors by field and keyword
@vendors_router.get('/search', response_model=List[vendor_model.VendorMaster])
def search_by_word(field_type: str, keyword: str,curr_user: User = Depends(get_current_user)):
    try:
        data = vendor_crud.search_vendors(field_type, keyword)
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to fetch data: {e}")


# Get all vendors (optionally filter by active_status)
@vendors_router.get('/list', response_model=List[vendor_model.VendorMaster])
def get_all(status_filter: Optional[str] = "",curr_user: User = Depends(get_current_user)):
    try:
        data = vendor_crud.get_all_vendors(status_filter)
        new_li = []
        for row in data:
            new_li.append(vendor_model.VendorMaster(**row))
        return new_li
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Failed to Fetch All the Records: {e}")


# Get count of vendors
@vendors_router.get("/count")
def count_all(curr_user: User = Depends(get_current_user)):
    data = vendor_crud.get_all_vendors()
    return {"detail": f"Count of records: {len(data)}"}


# Get vendor by ID
@vendors_router.get('/{id}', response_model=vendor_model.VendorMaster)
def get_by_id(id: int,curr_user: User = Depends(get_current_user)):
    try:
        data = vendor_crud.get_vendor_by_id(id)
        if not data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not Found")
        return vendor_model.VendorMaster(**data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"ID not Found or Unable to fetch the Record : {e}")


# Create a new vendor
@vendors_router.post('/create', response_model=vendor_model.VendorMaster)
def create_asset(new_asset: vendor_model.VendorMaster,curr_user: User = Depends(get_current_user)):
    try:
        vendor_crud.create_vendor(new_asset)
        return new_asset
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error: {e}")


# Delete vendor by ID
@vendors_router.delete("/{id}")
def delete_vendor_id(id: int,curr_user: User = Depends(get_current_user)):
    try:
        if vendor_crud.delete_vendor_by_id(id):
            return {"detail": "Record deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Vendor Doesnt Exist: {e}")


# Update vendor by ID
@vendors_router.put("/{id}", response_model=vendor_model.VendorMaster)
def update_by_id(id: int, new_vendor: vendor_model.VendorMaster,curr_user: User = Depends(get_current_user)):
    if vendor_crud.update_vendor_by_id(id, new_vendor):
        return new_vendor
    raise HTTPException(status_code=400, detail="Unable to update Vendor")


# Patch vendor status by ID
@vendors_router.patch("/{id}/status", response_model=vendor_model.VendorMaster)
def patch_by_id(id: int, status: str,curr_user: User = Depends(get_current_user)):
    data = get_by_id(id)
    try:
        if data:
            data.active_status = status
            return update_by_id(id, data)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error: {e}")
