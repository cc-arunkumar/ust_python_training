from fastapi import Depends, HTTPException
from typing import List
from src.models.asset_model import AssetInventory
from src.crud.asset_crud import (
    create_asset,
    get_asset_by_id,
    get_all_assets,
    delete_asset,
    update_asset_by_id,
    update_asset_status,
    search_assets,
    count_assets,
)
from src.auth.jwt_auth import get_current_user, User
def register_asset_api(app):
    """
    Register all asset-related API endpoints with the FastAPI app.
    Each endpoint interacts with the CRUD functions defined in asset_crud.
    """

    # 1. Create a new asset
    @app.post("/assets/create")
    def add_asset(asset: AssetInventory,current_user: User = Depends(get_current_user)):
        """
        Endpoint: POST /assets/create
        Input: AssetInventory object (validated by Pydantic model)
        Action: Calls create_asset() to insert a new asset into DB
        Returns: Created asset record
        """
        try:
            result = create_asset(asset)
            return result
        except Exception as e:
            print(f"Error in create_asset: {e}")
            # Return HTTP 500 if something goes wrong
            raise HTTPException(status_code=500, detail="Internal Server Error")

    # 2. List all assets (optionally filter by status)
    @app.get("/assets/list")
    def list_assets(status: str | None = None,current_user: User = Depends(get_current_user)):
        """
        Endpoint: GET /assets/list
        Query param: status (optional)
        Action: Fetch all assets, optionally filtered by status
        Returns: List of assets
        """
        return get_all_assets(status)

    # 3. Search assets by column and keyword
    @app.get("/assets/search")
    def search(column_name: str, keyword: str,current_user: User = Depends(get_current_user)):
        """
        Endpoint: GET /assets/search
        Query params: column_name, keyword
        Action: Search assets based on column and keyword
        Returns: Matching assets
        """
        return search_assets(column_name, keyword)
    
    # 4. Count total assets
    @app.get("/assets/count")
    def count(current_user: User = Depends(get_current_user)):
        """
        Endpoint: GET /assets/count
        Action: Returns total count of assets
        """
        return count_assets()
    
    # 5. Get asset by ID
    @app.get("/assets/{asset_id}")
    def read_asset(asset_id: int,current_user: User = Depends(get_current_user)):
        """
        Endpoint: GET /assets/{asset_id}
        Path param: asset_id
        Action: Fetch asset by its ID
        Returns: Asset record or 404 if not found
        """
        asset = get_asset_by_id(asset_id)
        if not asset:
            raise HTTPException(status_code=404, detail="Asset not found.")
        return asset

    # 6. Update full asset record
    @app.put("/assets/{asset_id}")
    def update_asset_endpoint(asset_id: int, new_asset: AssetInventory,current_user: User = Depends(get_current_user)):
        """
        Endpoint: PUT /assets/{asset_id}
        Path param: asset_id
        Body: AssetInventory object
        Action: Replace asset record with new data
        Returns: Updated asset or 404 if not found
        """
        result = update_asset_by_id(asset_id, new_asset,)
        if not result:
            raise HTTPException(status_code=404, detail="Asset not found")
        return result

    # 7. Update only asset status
    @app.patch("/assets/{asset_id}/status")
    def update_status(asset_id: int, new_status: str,current_user: User = Depends(get_current_user)):
        """
        Endpoint: PATCH /assets/{asset_id}/status
        Path param: asset_id
        Body: new_status string
        Action: Update only the status field of an asset
        Returns: Updated asset or 404 if not found
        """
        result = update_asset_status(asset_id, new_status)
        if not result:
            raise HTTPException(status_code=404, detail="Asset not found")
        return result

    # 8. Delete asset
    @app.delete("/assets/{asset_id}")
    def remove_asset(asset_id: int,current_user: User = Depends(get_current_user)):
        """
        Endpoint: DELETE /assets/{asset_id}
        Path param: asset_id
        Action: Delete asset by ID
        Returns: Deleted asset or 404 if not found
        """
        result = delete_asset(asset_id)
        if not result:
            raise HTTPException(status_code=404, detail="Asset not found")
        return result

