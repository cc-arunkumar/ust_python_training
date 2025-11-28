from fastapi import HTTPException
from typing import List
from src.models.asset_model import AssetInventory
from src.crud.asset_crud import (
    create_asset,
    get_asset_by_id as crud_get_asset_by_id,
    get_all_assets,
    delete_asset,
    update_asset_by_id,
    update_asset_status,
    search_assets,
    count_assets,
    bulk_upload_assets,
)

def register_asset_api(app):
    # 1. Create asset
    @app.post("/assets/create")
    def add_asset(asset: AssetInventory):
        try:
            result = create_asset(asset)
            return result
        except Exception as e:
            print(f"Error in create_asset: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")

    @app.get("/assets/list")
    def list_assets(status: str | None = None):
        return get_all_assets(status)

    @app.get("/assets/search")
    def search(column_name:str,keyword: str):
        return search_assets(column_name,keyword)
    
    @app.get("/assets/count")
    def count():
        return count_assets()
    
    # 3. Get asset by ID
    @app.get("/assets/{asset_id}")
    def read_asset(asset_id: int):
        asset = crud_get_asset_by_id(asset_id)
        if not asset:
            raise HTTPException(status_code=404, detail="Asset not found.")
        return asset

    # 4. Update full record
    @app.put("/assets/{asset_id}")
    def update_asset_endpoint(asset_id: int, new_asset: AssetInventory):
        result = update_asset_by_id(asset_id, new_asset)
        if not result:
            raise HTTPException(status_code=404, detail="Asset not found")
        return result

    # 5. Update only status
    @app.patch("/assets/{asset_id}/status")
    def update_status(asset_id: int, new_status: str):
        result = update_asset_status(asset_id, new_status)
        if not result:
            raise HTTPException(status_code=404, detail="Asset not found")
        return result

    # 6. Delete asset
    @app.delete("/assets/{asset_id}")
    def remove_asset(asset_id: int):
        result = delete_asset(asset_id)
        if not result:
            raise HTTPException(status_code=404, detail="Asset not found")
        return result


    # 9. Bulk upload assets (CSV parsed into AssetInventory list)
    @app.post("/assets/bulk-upload")
    def bulk_upload(csv_data: List[AssetInventory]):
        return bulk_upload_assets(csv_data)
