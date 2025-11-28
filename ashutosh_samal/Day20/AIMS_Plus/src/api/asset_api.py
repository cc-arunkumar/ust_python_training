from fastapi import APIRouter, HTTPException,Depends
from typing import List, Optional
from src.model.asset_model import AssetCreate
from ..auth.jwt_auth import jwt_router,get_current_user,User
from src.crud.asset_crud import (
    fetch_assets,
    fetch_asset_by_id,
    create_new_asset,
    modify_asset,
    modify_asset_status,
    remove_asset,
    find_assets_by_keyword,
    get_total_asset_count
)

# Create a FastAPI router for managing assets
asset_router = APIRouter(prefix="/assets")

# Endpoint to get a list of assets, optionally filtered by status
@asset_router.get("/list")
async def list_assets(status: Optional[str] = None,current_user: User = Depends(get_current_user)):
    try:
        assets = fetch_assets(status)  # Fetch assets based on status (if provided)
        return assets  # Return the list of assets
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Handle any exceptions

# Endpoint to get a single asset by its asset_id
@asset_router.get("/{asset_id}")
async def get_asset(asset_id: int,current_user: User = Depends(get_current_user)):
    try:
        asset = fetch_asset_by_id(asset_id)  # Fetch asset by ID
        if asset is None:
            raise HTTPException(status_code=404, detail="Asset not found")  # Handle asset not found
        return asset  # Return the asset details
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Handle any exceptions

# Endpoint to create a new asset
@asset_router.post("/create")
async def create_asset_endpoint(asset: AssetCreate,current_user: User = Depends(get_current_user)):
    try:
        create_new_asset(asset)  # Call the function to create a new asset in the database
        return asset  # Return the created asset data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Handle any exceptions

# Endpoint to update an existing asset
@asset_router.put("/{asset_id}")
async def update_asset_endpoint(asset_id: int, asset: AssetCreate,current_user: User = Depends(get_current_user)):
    try:
        modify_asset(asset_id, asset)  # Call function to update asset data
        return asset  # Return the updated asset data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Handle any exceptions

# Endpoint to update the status of an asset (e.g., Available, Assigned, etc.)
@asset_router.patch("/{asset_id}/status")
async def update_asset_status_endpoint(asset_id: int, asset_status: str,current_user: User = Depends(get_current_user)):
    try:
        modify_asset_status(asset_id, asset_status)  # Call function to update the asset status
        return {"message": "Asset status updated successfully"}  # Return a success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Handle any exceptions

# Endpoint to delete an asset by its ID
@asset_router.delete("/{asset_id}")
async def delete_asset_endpoint(asset_id: int,current_user: User = Depends(get_current_user)):
    try:
        remove_asset(asset_id)  # Call function to delete the asset by its ID
        return {"message": "Asset deleted successfully"}  # Return a success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Handle any exceptions

# Endpoint to search assets based on a keyword (e.g., asset tag, manufacturer, model)
@asset_router.get("/search")
async def search_assets_endpoint(keyword: str,current_user: User = Depends(get_current_user)):
    try:
        assets = find_assets_by_keyword(keyword)  # Call function to search for assets using the keyword
        return assets  # Return the matching assets
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Handle any exceptions

# Endpoint to get the total count of assets in the database
@asset_router.get("/count")
async def count_assets_endpoint(current_user: User = Depends(get_current_user)):
    try:
        count = get_total_asset_count()  # Call function to get the total asset count
        return {"total_assets": count}  # Return the total count of assets
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  # Handle any exceptions
