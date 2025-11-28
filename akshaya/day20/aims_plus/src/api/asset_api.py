from fastapi import FastAPI, HTTPException, UploadFile, File, Query, APIRouter, Depends
from typing import Optional
import csv, io
from src.crud.asset_crud import list_assets_by_status_db
from ..auth.jwt_auth import get_current_user
from ..models.asset_model import AssetModel
from ..models.user_model import User
from ..crud.asset_crud import (
    create_asset_db, get_all_assets_db, get_asset_by_id_db,
    update_asset_db, update_asset_status_db, delete_asset_db,
    search_assets_db, count_assets_db
)

# Create an instance of APIRouter for asset-related routes
asset_router = APIRouter()

# 1. Create asset endpoint
@asset_router.post("/assets/create")
def create_asset(asset: AssetModel, current_user: User = Depends(get_current_user)):
    """
    Creates a new asset in the database. 
    The asset data is provided in the request body.
    The user must be authenticated via JWT (Depends on `get_current_user`).
    """
    # Attempt to create the asset in the database
    if not create_asset_db(asset):
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "message": "Asset created successfully"}

# 2. List assets endpoint
@asset_router.get("/assets/list")
def list_assets(status: Optional[str] = None, current_user: User = Depends(get_current_user)):
    """
    Returns a list of assets. Optionally filters by asset status if 'status' is provided.
    The user must be authenticated via JWT.
    """
    # If status is provided, filter assets by status
    if status:
        result = list_assets_by_status_db(status)
    else:
        # Otherwise, fetch all assets
        result = get_all_assets_db()

    # Handle case where database query fails
    if result is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "data": result}

# 3. Search assets endpoint
@asset_router.get("/assets/search")
def search_assets(keyword: str = Query(...), value: str = Query(...), current_user: User = Depends(get_current_user)):
    """
    Searches assets based on a provided keyword and value.
    The user must be authenticated via JWT.
    """
    # Perform the search based on provided keyword and value
    result = search_assets_db(keyword, value)

    # Handle case where database query fails
    if result is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "data": result}

# 4. Count total assets endpoint
@asset_router.get("/assets/count")
def count_assets(current_user: User = Depends(get_current_user)):
    """
    Returns the total count of assets in the database.
    The user must be authenticated via JWT.
    """
    # Fetch the total count of assets from the database
    total = count_assets_db()

    # Handle case where the database query fails
    if total is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "count": total}

# 5. Get asset by asset_id endpoint
@asset_router.get("/assets/{id}")
def get_asset(id: int, current_user: User = Depends(get_current_user)):
    """
    Fetches a specific asset by its ID.
    Returns asset data if found, otherwise raises a 404 error.
    The user must be authenticated via JWT.
    """
    # Fetch the asset by ID from the database
    asset = get_asset_by_id_db(id)

    # If no asset is found, raise a 404 HTTP exception
    if asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return {"status": "success", "data": asset}

# 6. Update full asset record endpoint
@asset_router.put("/assets/{id}")
def update_asset(id: int, asset: AssetModel, current_user: User = Depends(get_current_user)):
    """
    Updates an existing asset with the provided new data.
    The user must be authenticated via JWT.
    """
    # Attempt to update the asset in the database
    if not update_asset_db(id, asset):
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "message": "Asset updated successfully"}

# 7. Update only asset status endpoint
@asset_router.patch("/assets/{id}/status")
def update_asset_status(id: int, status: str, current_user: User = Depends(get_current_user)):
    """
    Updates only the status of an existing asset.
    The user must be authenticated via JWT.
    """
    # Attempt to update the asset status in the database
    if not update_asset_status_db(id, status):
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "message": "Asset status updated"}

# 8. Delete asset endpoint
@asset_router.delete("/assets/{id}")
def delete_asset(id: int, current_user: User = Depends(get_current_user)):
    """
    Deletes an asset by its ID.
    The user must be authenticated via JWT.
    """
    # Attempt to delete the asset from the database
    if not delete_asset_db(id):
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "message": f"Asset {id} deleted"}
