from fastapi import FastAPI, HTTPException, status,APIRouter,Depends
from typing import List, Optional
from src.auth.auth_jwt_token import User, get_current_user
from src.models.vendor_model import VendorModel  # Assuming you have a Vendor model
from src.config.db_connection import get_connection
from src.crud.vendor_crud import get_all_vendors, get_vendor_by_id, insert_vendor, update_vendor_by_id, delete_vendor, search_vendor

# app = FastAPI()
vendor_router=APIRouter(prefix="/vendor")
# Endpoint to get the list of vendors with optional status filter
@vendor_router.get("/list", response_model=List[VendorModel])
def get_vendors(status_filter: Optional[str] = "",current_user: User = Depends(get_current_user)):
    try:
        rows = get_all_vendors(status_filter)
        vendor_list = []
        for row in rows:
            vendor_list.append(VendorModel(**row))
        return vendor_list
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{e}")

# Endpoint to search vendors by a specific field (e.g., vendor_name, contact_phone)
@vendor_router.get("/search")
def search_by_word(field_type: str, keyword: str,current_user: User = Depends(get_current_user)):
    try:
        data = search_vendor(field_type, keyword)
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to fetch data: {e}")

# Endpoint to count the number of vendors
@vendor_router.get("/count")
def count_data():
    try:
        data = get_all_vendors()
        if data is None:
            raise HTTPException(status_code=404, detail="No vendors found.")
        return {"count": len(data)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error counting vendors: {str(e)}")

# Endpoint to get a vendor by vendor_id
@vendor_router.get("/{vendor_id}", response_model=VendorModel)
def get_by_id(vendor_id: int,current_user: User = Depends(get_current_user)):
    try:
        rows = get_vendor_by_id(vendor_id)
        if not rows:
            raise HTTPException(status_code=404, detail="Vendor does not exist")
        return VendorModel(**rows)
    except Exception as e:
        raise HTTPException(status_code=400, detail="ID not found")

# Endpoint to create a new vendor
@vendor_router.post('/create', response_model=VendorModel)
def create_vendor(new_vendor: VendorModel,current_user: User = Depends(get_current_user)):
    try:
        insert_vendor(new_vendor)
        return new_vendor
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error: {e}")

# Endpoint to update an existing vendor by vendor_id
@vendor_router.put("/{vendor_id}", response_model=VendorModel)
def update_vendor_details(vendor_id: int, update_vendor: VendorModel,current_user: User = Depends(get_current_user)):
    try:
        update_vendor_by_id(vendor_id, update_vendor)
        return update_vendor
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Update failed: {str(e)}")

# Endpoint to delete a vendor by vendor_id
@vendor_router.delete("/{vendor_id}")
def delete_vendor_by_id(vendor_id: int,current_user: User = Depends(get_current_user)):
    try:
        if delete_vendor(vendor_id):
            return {"detail": "Vendor deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting vendor: {str(e)}")

@vendor_router.patch("/{vendor_id}/status")
def update_vendor_status(vendor_id: int, status: str,current_user: User = Depends(get_current_user)):
    try:
        # Fetch the existing vendor by vendor_id
        data = get_vendor_by_id(vendor_id)
        
        if not data:
            raise HTTPException(status_code=404, detail="Vendor not found")
        
        # Update the active_status field of the vendor
        data['active_status'] = status
        
        # Update the vendor record in the database
        update_vendor_by_id(vendor_id, VendorModel(**data))
        
        return {"message": "Vendor status updated successfully", "vendor_id": vendor_id, "new_status": status}
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating vendor status: {str(e)}")
