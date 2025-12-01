from fastapi import HTTPException, Depends
from src.models.vendor_model import VendorMaster
from src.crud.vendor_crud import (
    create_vendor,
    get_vendor_by_id as crud_get_vendor_by_id,
    get_vendor_by_status,
    get_all_vendors,
    search as search_vendor,
    update_vendor,
    count_len_vendors,
    update_vendor_status,
    delete_vendor
)
# Import JWT auth dependency
from src.authentication.auth import get_current_user, User


def register_vendor_api(app):
    
    # POST /vendors/create
    @app.post("/vendors/create")
    def add_vendor(vendor: VendorMaster, current_user: User = Depends(get_current_user)):
        vendor_id = create_vendor(vendor)
        return {"message": "Vendor created successfully", "vendor_id": vendor_id}

    # GET /vendors/list
    @app.get("/vendors/list")
    def list_vendors(status: str | None = None, current_user: User = Depends(get_current_user)):
        if status:
            return get_vendor_by_status(status)
        return get_all_vendors()

    # GET /vendors/search
    @app.get("/vendors/search")
    def search_vendor_api(keyword: str, value: str, current_user: User = Depends(get_current_user)):
        try:
            results = search_vendor(keyword, value)
            if not results:
                raise HTTPException(status_code=404, detail="No matching vendors found")
            return results
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    # GET /vendors/{vendor_id}
    @app.get("/vendors/{vendor_id}")
    def read_vendor(vendor_id: int, current_user: User = Depends(get_current_user)):
        vendor = crud_get_vendor_by_id(vendor_id)
        if not vendor:
            raise HTTPException(status_code=404, detail="Vendor not found")
        return vendor

    # GET /vendors
    @app.get("/vendors")
    def count_vendors(current_user: User = Depends(get_current_user)):
        return count_len_vendors()

    # PUT /vendors/{vendor_id}
    @app.put("/vendors/{vendor_id}")
    def update_vendor_record(vendor_id: int, vendor: VendorMaster, current_user: User = Depends(get_current_user)):
        updated = update_vendor(vendor_id, vendor)
        if updated == 0:
            raise HTTPException(status_code=404, detail="Vendor not found")
        return {"message": "Vendor updated successfully"}

    # PATCH /vendors/{vendor_id}/status
    @app.patch("/vendors/{vendor_id}/status")
    def change_vendor_status(vendor_id: int, new_status: str, current_user: User = Depends(get_current_user)):
        updated = update_vendor_status(vendor_id, new_status)
        if updated == 0:
            raise HTTPException(status_code=404, detail="Vendor not found")
        return {"message": "Vendor status updated"}

    # DELETE /vendors/{vendor_id}
    @app.delete("/vendors/{vendor_id}")
    def remove_vendor(vendor_id: int, current_user: User = Depends(get_current_user)):
        deleted = delete_vendor(vendor_id)
        if deleted == 0:
            raise HTTPException(status_code=404, detail="Vendor not found")
        return {"message": "Vendor deleted"}
