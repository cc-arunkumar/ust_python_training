from fastapi import APIRouter, HTTPException ,Depends,Query # Import FastAPI components
from typing import List, Optional  # Import typing components for type hinting
from ..models.asset_model import AssetCreate  # Import AssetCreate model from asset_model
from ..auth.auth_jwt_token import get_current_user

from ..crud.asset_crud import (
    get_assets,  # Import CRUD operations for assets
    get_asset_by_id,
    create_asset,
    update_asset,
    update_asset_status,
    delete_asset,
    search_assets,
    count_assets
)

asset_router = APIRouter(prefix="/assets",tags=["Asset_Inventory"])  # Create a new router for asset-related endpoints


# Endpoint to list assets, optionally filtered by status
@asset_router.get("/list")
def list_assets(current_user: dict = Depends(get_current_user),status: Optional[str] = None,):
    try:
        assets = get_assets(status)  # Fetch assets based on status
        return assets
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure




@asset_router.get("/count")
async def count_assets_endpoint(current_user: dict = Depends(get_current_user)):
    try:
        count = count_assets()  # Get total asset count
        return {"total_assets": count}  # Return asset count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))




@asset_router.get("/search")
def search(keyword: str = Query(..., description="Search in tag, model, manufacturer, serial"),current_user: dict = Depends(get_current_user)):
    return search_assets(keyword)
 

# Endpoint to fetch a specific asset by ID
@asset_router.get("/{asset_id}")
def get_asset(asset_id: int,current_user: dict = Depends(get_current_user)):
    try:
        asset = get_asset_by_id(asset_id)  # Fetch asset by ID
        if asset is None:
            raise HTTPException(status_code=404, detail="Asset not found")  # Return error if not found
        return asset
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure



# Endpoint to create a new asset
@asset_router.post("/create")
def create_asset_endpoint(asset: AssetCreate,current_user: dict = Depends(get_current_user)):
    try:
        create_asset(asset)  # Call CRUD function to create asset
        return asset  # Return created asset
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure



# Endpoint to update an existing asset by ID
@asset_router.put("/{asset_id}")
def update_asset_endpoint(asset_id: int, asset: AssetCreate,current_user: dict = Depends(get_current_user)):
    try:
        update_asset(asset_id, asset)  # Update asset using the provided ID and data
        return asset  # Return updated asset
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure



# Endpoint to update the status of an asset
@asset_router.patch("/{asset_id}/status")
def update_asset_status_endpoint(asset_id: int, asset_status: str,current_user: dict = Depends(get_current_user)):
    try:
        update_asset_status(asset_id, asset_status)  # Update asset status
        return {"message": "Asset status updated successfully"}  # Return success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure


# Endpoint to delete an asset by ID
@asset_router.delete("/{asset_id}")
def delete_asset_endpoint(asset_id: int,current_user: dict = Depends(get_current_user)):
    try:
        delete_asset(asset_id)  # Delete asset using the provided ID
        return {"message": "Asset deleted successfully"}  # Return success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTP error on failure


