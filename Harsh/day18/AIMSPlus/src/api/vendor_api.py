from typing import List
from fastapi import HTTPException
from src.models.vendor_model import VendorMaster
from src.crud.vendor_crud import (
    count_vendor,
    create_vendor,
    get_all_vendor_by_status,
    get_vendor_by_id,
    get_all_vendors,
    delete_vendor,
    search_vendor,
    bulk_upload_vendor,
    update_vendor_by_id,
    update_vendor_status
)

def register_vendor_api(app):
    """
    Register all vendor-related API endpoints with the FastAPI app.
    Each endpoint interacts with the CRUD functions defined in vendor_crud.
    """

    # 1. Create a new vendor
    @app.post("/vendors/create")
    def add_vendor(vendor: VendorMaster):
        """
        Endpoint: POST /vendors/create
        Input: VendorMaster object (validated by Pydantic model)
        Action: Calls create_vendor() to insert a new vendor into DB
        Returns: Success message + vendor_id
        """
        vendor_id = create_vendor(vendor)
        return {"message": "Vendor created successfully", "vendor_id": vendor_id}

    # 2. List all vendors
    @app.get("/vendors/list")
    def list_vendors():
        """
        Endpoint: GET /vendors/list
        Action: Fetch all vendors
        Returns: List of vendors
        """
        return get_all_vendors()
    
    # 3. Search vendors by column and keyword
    @app.get("/vendors/search")   # <-- corrected path (was /assets/search)
    def search(column_name: str, keyword: str):
        """
        Endpoint: GET /vendors/search
        Query params: column_name, keyword
        Action: Search vendors based on column and keyword
        Returns: Matching vendors
        """
        return search_vendor(column_name, keyword)
    
    # 4. Count total vendors
    @app.get("/vendors/count")
    def get_count():
        """
        Endpoint: GET /vendors/count
        Action: Returns total count of vendors
        """
        return count_vendor()

    # 5. Get vendor by ID
    @app.get("/vendors/{vendor_id}")
    def read_vendor(vendor_id: int):
        """
        Endpoint: GET /vendors/{vendor_id}
        Path param: vendor_id
        Action: Fetch vendor by ID
        Returns: Vendor record or 404 if not found
        """
        vendor = get_vendor_by_id(vendor_id)
        if not vendor:
            raise HTTPException(status_code=404, detail="Vendor not found")
        return vendor

    # 6. List vendors by status (Active/Inactive)
    @app.get("/vendors/list/status")
    def read_vendor_by_status(active_status: str | None = None):
        """
        Endpoint: GET /vendors/list/status
        Query param: active_status (optional)
        Action: Fetch vendors filtered by active status
        Returns: List of vendors or 404 if none found
        """
        status = get_all_vendor_by_status(active_status)
        if not status:
            raise HTTPException(status_code=404, detail="Vendor not found")
        return status   
    
    # 7. Delete vendor
    @app.delete("/vendors/{vendor_id}")
    def remove_vendor(vendor_id: int):
        """
        Endpoint: DELETE /vendors/{vendor_id}
        Path param: vendor_id
        Action: Delete vendor by ID
        Returns: Success message or 404 if not found
        """
        deleted = delete_vendor(vendor_id)
        if deleted == 0:
            raise HTTPException(status_code=404, detail="Vendor not found")
        return {"message": "Vendor deleted"}
    
    # 8. Bulk upload vendors (CSV parsed into VendorMaster list)
    @app.post("/vendors/bulk-upload")
    def bulk_upload(csv_data: List[VendorMaster]):
        """
        Endpoint: POST /vendors/bulk-upload
        Body: List of VendorMaster objects (parsed from CSV)
        Action: Insert multiple vendors at once
        Returns: Bulk upload result
        """
        return bulk_upload_vendor(csv_data) 
    
    # 9. Update full vendor record
    @app.put("/vendors/{vendor_id}")
    def update_vendor_endpoint(vendor_id: int, new_vendor: VendorMaster):
        """
        Endpoint: PUT /vendors/{vendor_id}
        Path param: vendor_id
        Body: VendorMaster object
        Action: Replace vendor record with new data
        Returns: Updated vendor or 404 if not found
        """
        result = update_vendor_by_id(vendor_id, new_vendor)
        if not result:
            raise HTTPException(status_code=404, detail="Vendor not found")
        return result

    # 10. Update only vendor status
    @app.patch("/vendors/{vendor_id}/status")   
    def update_status(vendor_id: int, new_status: str):
        """
        Endpoint: PATCH /vendors/{vendor_id}/status
        Path param: vendor_id
        Body: new_status string
        Action: Update only the status field of a vendor
        Returns: Updated vendor or 404 if not found
        """
        result = update_vendor_status(vendor_id, new_status)
        if not result:
            raise HTTPException(status_code=404, detail="Vendor not found")
        return result
