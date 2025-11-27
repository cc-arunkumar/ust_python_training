from fastapi import HTTPException
from src.models.vendor_model import VendorMaster
from src.crud.vendor_crud import (
    create_vendor,
    get_vendor_by_id as crud_get_vendor_by_id,
    get_all_vendors,
    delete_vendor
)

def register_vendor_api(app):
    @app.post("/vendors")
    def add_vendor(vendor: VendorMaster):
        vendor_id = create_vendor(vendor)
        return {"message": "Vendor created successfully", "vendor_id": vendor_id}

    @app.get("/vendors")
    def list_vendors():
        return get_all_vendors()

    @app.get("/vendors/{vendor_id}")
    def read_vendor(vendor_id: int):
        vendor = crud_get_vendor_by_id(vendor_id)
        if not vendor:
            raise HTTPException(status_code=404, detail="Vendor not found")
        return vendor


    @app.delete("/vendors/{vendor_id}")
    def remove_vendor(vendor_id: int):
        deleted = delete_vendor(vendor_id)
        if deleted == 0:
            raise HTTPException(status_code=404, detail="Vendor not found")
        return {"message": "Vendor deleted"}
