from fastapi import FastAPI, HTTPException, Query, APIRouter, Depends
from ..auth.auth_jwt_token import get_current_user   # Dependency to get the currently logged-in user
from ..models.user_model import User                 # User model for authentication
from typing import Optional
from src.crud.asset_crud import list_assets_by_status_db  # CRUD function for filtering assets by status

from ..models.asset_model import AssetInventory      # Asset model definition
from ..crud.asset_crud import (
    create_asset_db, get_all_assets_db, get_asset_by_id_db,
    update_asset_db, update_asset_status_db, delete_asset_db,
    search_assets_db, count_assets_db
)

# Create a router for asset-related endpoints with a common prefix
asset_router = APIRouter(prefix="/assets")


# ------------------- CREATE -------------------
@asset_router.post("/assets/create")
def create_asset(asset: AssetInventory, current_user: User = Depends(get_current_user)):
    """
    Create a new asset in the inventory.
    - Requires authentication (current_user).
    - Accepts AssetInventory object as input.
    - Returns success message if created, else raises HTTP 500.
    """
    if not create_asset_db(asset):
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "message": "Asset created successfully"}


# ------------------- LIST -------------------
@asset_router.get("/assets/list")
def list_assets(status: Optional[str] = None, current_user: User = Depends(get_current_user)):
    """
    List all assets.
    - Optional query parameter 'status' to filter assets by status.
    - Returns all assets if no status is provided.
    - Raises HTTP 500 if database connection fails.
    """
    if status:
        result = list_assets_by_status_db(status)
    else:
        result = get_all_assets_db()
    if result is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "data": result}


# ------------------- SEARCH -------------------
@asset_router.get("/assets/search")
def search_assets(keyword: str = Query(...), value: str = Query(...), current_user: User = Depends(get_current_user)):
    """
    Search assets by keyword and value.
    - Example: /assets/search?keyword=name&value=laptop
    - Returns matching assets.
    - Raises HTTP 500 if database connection fails.
    """
    result = search_assets_db(keyword, value)
    if result is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "data": result}


# ------------------- COUNT -------------------
@asset_router.get("/assets/count")
def count_assets(current_user: User = Depends(get_current_user)):
    """
    Count total number of assets in the inventory.
    - Returns integer count.
    - Raises HTTP 500 if database connection fails.
    """
    total = count_assets_db()
    if total is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "count": total}


# ------------------- GET BY ID -------------------
@asset_router.get("/assets/{id}")
def get_asset(id: int, current_user: User = Depends(get_current_user)):
    """
    Retrieve a single asset by its ID.
    - Returns asset details if found.
    - Raises HTTP 404 if asset not found.
    """
    asset = get_asset_by_id_db(id)
    if asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return {"status": "success", "data": asset}


# ------------------- UPDATE -------------------
@asset_router.put("/assets/{id}")
def update_asset(id: int, asset: AssetInventory, current_user: User = Depends(get_current_user)):
    """
    Update an existing asset by ID.
    - Accepts AssetInventory object with updated fields.
    - Returns success message if updated.
    - Raises HTTP 500 if database connection fails.
    """
    if not update_asset_db(id, asset):
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "message": "Asset updated successfully"}


# ------------------- UPDATE STATUS -------------------
@asset_router.patch("/assets/{id}/status")
def update_asset_status(id: int, status: str, current_user: User = Depends(get_current_user)):
    """
    Update only the status of an asset.
    - Example: PATCH /assets/1/status?status=inactive
    - Returns success message if updated.
    - Raises HTTP 500 if database connection fails.
    """
    if not update_asset_status_db(id, status):
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "message": "Asset status updated"}


# ------------------- DELETE -------------------
@asset_router.delete("/assets/{id}")
def delete_asset(id: int, current_user: User = Depends(get_current_user)):
    """
    Delete an asset by ID.
    - Returns success message if deleted.
    - Raises HTTP 500 if database connection fails.
    """
    if not delete_asset_db(id):
        raise HTTPException(status_code=500, detail="Database connection failed")
    return {"status": "success", "message": f"Asset {id} deleted"}
