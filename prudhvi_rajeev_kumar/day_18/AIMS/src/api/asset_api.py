from fastapi import HTTPException
from src.models.asset_model import AssetInventory
from src.crud.asset_crud import (
    create_asset,
    get_asset_by_id as crud_get_asset_by_id,
    get_all_assets,
    delete_asset
)

def register_asset_api(app):
    @app.post("/assets")
    def add_asset(asset: AssetInventory):
        try:
            asset_id = create_asset(asset)
            return {"message": "Asset created successfully", "asset_id": asset_id}
        except Exception as e:
            print(f"Error in create_asset: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")

    @app.get("/assets")
    def list_assets():
        return get_all_assets()

    @app.get("/assets/{asset_id}")
    def read_asset(asset_id: int):
        asset = crud_get_asset_by_id(asset_id)
        if not asset:
            raise HTTPException(status_code=404, detail="Asset not found.")
        return asset


    @app.delete("/assets/{asset_id}")
    def remove_asset(asset_id: int):
        deleted = delete_asset(asset_id)
        if deleted == 0:
            raise HTTPException(status_code=404, detail="Asset not found")
        return {"message": "Asset deleted"}
