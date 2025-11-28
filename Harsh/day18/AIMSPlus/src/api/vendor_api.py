from typing import List
from fastapi import HTTPException
from src.models.vendor_model import VendorMaster
from src.crud.vendor_crud import (
    count_vendor,
    create_vendor,
    get_all_vendor_by_status,
    get_vendor_by_id ,
    get_all_vendors,
    delete_vendor,
    search_vendor,
    bulk_upload_vendor,
    update_vendor_by_id,
    update_vendor_status
)

def register_vendor_api(app):
    @app.post("/vendors/create")
    def add_vendor(vendor: VendorMaster):
        vendor_id = create_vendor(vendor)
        return {"message": "Vendor created successfully", "vendor_id": vendor_id}

    @app.get("/vendors/list")
    def list_vendors():
        return get_all_vendors()
    
    @app.get("/assets/search")
    def search(column_name:str,keyword: str):
        return search_vendor(column_name,keyword)
    
    @app.get("/vendors/count")
    def get_count():
        return count_vendor()

    @app.get("/vendors/{vendor_id}")
    def read_vendor(vendor_id: int):
        vendor = get_vendor_by_id(vendor_id)
        if not vendor:
            raise HTTPException(status_code=404, detail="Vendor not found")
        return vendor

    @app.get("/vendors/list/status")
    def read_vendor_by_status(active_status:str | None = None):
        status=get_all_vendor_by_status(active_status)
        if not status:
            raise HTTPException(status_code=404,detail="Vendor not found")
        return status   
    
    @app.delete("/vendors/{vendor_id}")
    def remove_vendor(vendor_id: int):
        deleted = delete_vendor(vendor_id)
        if deleted == 0:
            raise HTTPException(status_code=404, detail="Vendor not found")
        return {"message": "Vendor deleted"}
    
    @app.post("/vendors/bulk-upload")
    def bulk_upload(csv_data: List[VendorMaster]):
        return bulk_upload_vendor(csv_data) 
    
    @app.put("/vendors/{vendor_id}")
    def update_asset_endpoint(vendor_id: int, new_asset: VendorMaster):
        result = update_vendor_by_id(vendor_id, new_asset)
        if not result:
            raise HTTPException(status_code=404, detail="Asset not found")
        return result

    @app.patch("/vendor/{vendor}/status")
    def update_status(vendor_id: int, new_status: str):
        result = update_vendor_status(vendor_id, new_status)
        if not result:
            raise HTTPException(status_code=404, detail="Asset not found")
        return result