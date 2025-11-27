from fastapi import HTTPException
from src.models.asset_model import AssetInventory
from src.crud.asset_crud import (
    create_asset,
    get_asset_by_id as crud_get_asset_by_id,
    get_all_assets,
    get_assets_by_status,
    update_asset,
    update_asset_status,
    delete_asset,
    search_assets,
    get_all_assets
)

def register_asset_api(app):
    # 1. POST /assets/create
    @app.post("/assets/create")
    def add_asset(asset: AssetInventory):
        asset_id = create_asset(asset)
        return {"message": "Asset created successfully", "asset_id": asset_id}

    # 2 & 3. GET /assets/list (with optional status filter)
    @app.get("/assets/list")
    def list_assets(status: str | None = None):
        if status:
            return get_assets_by_status(status)
        return get_all_assets()

    @app.get("/assets/search_keyword")
    def search_by_column(column_name: str, value: str):
        try:
            results = search_assets(column_name, value)
            if not results:
                raise HTTPException(status_code=404, detail="No matching assets found")
            return results
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
    
    @app.get("/assets/count")
    def get_count():
        return len(get_all_assets())
    
    # 4. GET /assets/{id}
    @app.get("/assets/{asset_id}")
    def read_asset(asset_id: int):
        asset = crud_get_asset_by_id(asset_id)
        if not asset:
            raise HTTPException(status_code=404, detail="Asset not found")
        return asset

    @app.get("/assets")
    def get_all():
        return get_all_assets()
    
    @app.put("/assets/{asset_id}")
    def update_asset_record(asset_id: int, asset: AssetInventory):
        updated = update_asset(asset_id, asset)
        if updated == 0:
            raise HTTPException(status_code=404, detail="Asset not found")
        return {"message": "Asset updated successfully"}

    
    @app.patch("/assets/{asset_id}/status")
    def change_asset_status(asset_id: int, new_status: str):
        updated = update_asset_status(asset_id, new_status)
        if updated == 0:
            raise HTTPException(status_code=404, detail="Asset not found")
        return {"message": "Asset status updated"}

    
    @app.delete("/assets/{asset_id}")
    def remove_asset(asset_id: int):
        deleted = delete_asset(asset_id)
        if deleted == 0:
            raise HTTPException(status_code=404, detail="Asset not found")
        return {"message": "Asset deleted"}

