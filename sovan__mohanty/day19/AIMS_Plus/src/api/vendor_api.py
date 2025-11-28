from fastapi import APIRouter, HTTPException, Depends
from src.models.vendor_model import Vendor, validate_vendor
from src.crud import vendor_crud
from src.auth.jwt_auth import User,get_current_user
router = APIRouter()

@router.post("/create", response_model=Vendor)
def create(vendor: Vendor,  current_user:User=Depends(get_current_user)):
    validate_vendor(vendor)
    new_id = vendor_crud.create_vendor(vendor)
    return {**vendor.model_dump(), "vendor_id": new_id}

@router.get("/list")
def list_vendors(status: str = None,  current_user:User=Depends(get_current_user)):
    rows = vendor_crud.list_vendors(status)
    if not rows:
        raise HTTPException(status_code=404, detail="No vendors found")
    return {"status": "success", "data": rows}
@router.get("/count")
def count_vendors( current_user:User=Depends(get_current_user)):
    row = vendor_crud.count_vendors()
    return {"status": "success", "count": row["total"]}

@router.get("/{vendor_id}", response_model=Vendor)
def get_vendor(vendor_id: int,  current_user:User=Depends(get_current_user)):
    row = vendor_crud.get_vendor(vendor_id)
    if not row:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return Vendor(**row)

@router.put("/{vendor_id}", response_model=Vendor)
def update_vendor(vendor_id: int, vendor: Vendor,  current_user:User=Depends(get_current_user)):
    validate_vendor(vendor)
    vendor_crud.update_vendor(vendor_id, vendor)
    row = vendor_crud.get_vendor(vendor_id)
    return Vendor(**row)

@router.patch("/{vendor_id}/status")
def update_status(vendor_id: int, status: str,  current_user:User=Depends(get_current_user)):
    if status not in {"Active", "Inactive"}:
        raise HTTPException(status_code=422, detail="Invalid status")
    vendor_crud.update_status(vendor_id, status)
    return {"status": "success", "message": f"Vendor {vendor_id} status updated to {status}"}

@router.delete("/{vendor_id}")
def delete_vendor(vendor_id: int,  current_user:User=Depends(get_current_user)):
    vendor_crud.delete_vendor(vendor_id)
    return {"status": "success", "message": "Vendor deleted"}

@router.get("/search")
def search_vendors(keyword: str,  current_user:User=Depends(get_current_user)):
    rows = vendor_crud.search_vendors(keyword)
    if not rows:
        raise HTTPException(status_code=404, detail="No matching vendors found")
    return {"status": "success", "data": rows}

