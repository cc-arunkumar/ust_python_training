from fastapi import FastAPI, HTTPException, APIRouter,Depends
from typing import Optional
from ..models.assetsinventory import AssetInventory, StatusValidate
from ..curd.asset_crud import AssetCrud
from ..auth.jwt_auth import get_current_user,User

# Initialize CRUD handler for asset operations
asset_reader = AssetCrud()

# Create a router instance with a prefix for all asset-related endpoints
asset_router = APIRouter(prefix="/asset")


@asset_router.post("/create")
def create_asset(asset: AssetInventory,current_user: User = Depends(get_current_user)):
    """
    Endpoint to create a new asset.
    Accepts an AssetInventory model as input.
    """
    try:
        return asset_reader.create_asset(asset)
    except Exception:
        # Raise HTTP 404 if asset creation fails
        raise HTTPException(status_code=404, detail="Not Found")


@asset_router.get("/list")
def get_all_asset(status: Optional[str] = "ALL",current_user: User = Depends(get_current_user)):
    """
    Endpoint to retrieve all assets.
    Optional query parameter 'status' can filter assets by status.
    Defaults to 'ALL' to return every asset.
    """
    try:
        return asset_reader.get_all_asset(status)
    except Exception:
        raise HTTPException(status_code=404, detail="Not Found")


@asset_router.get("/{id}")
def get_asset_by_id(id: int,current_user: User = Depends(get_current_user)):
    """
    Endpoint to fetch a single asset by its unique ID.
    """
    try:
        return asset_reader.get_asset_by_id(id)
    except Exception:
        raise HTTPException(status_code=404, detail="Not Found")


@asset_router.put("/{id}")
def update_asset(id: int, data: AssetInventory,current_user: User = Depends(get_current_user)):
    """
    Endpoint to update an existing asset by ID.
    Accepts an AssetInventory model with updated data.
    """
    try:
        return asset_reader.update_asset(id, data)
    except Exception as e:
        # Log the error for debugging purposes
        print(str(e))
        raise HTTPException(status_code=404, detail="Not Found")


@asset_router.patch("/{id}/status")
def update_asset_status(id: int, status: StatusValidate,current_user: User = Depends(get_current_user)):
    """
    Endpoint to update only the status of an asset.
    Accepts a StatusValidate model containing the new status.
    """
    try:
        print(status)  # Debug print, can be replaced with proper logging
        return asset_reader.update_asset_status(id, status.asset_status)
    except Exception:
        raise HTTPException(status_code=404, detail="Not Found")


@asset_router.delete("/{id}")
def delete_asset(id: int,current_user: User = Depends(get_current_user)):
    """
    Endpoint to delete an asset by ID.
    """
    try:
        return asset_reader.delete_asset(id)
    except Exception:
        raise HTTPException(status_code=404, detail="Not Found")


@asset_router.get("/search/keyword")
def get_asset_by_keyword(keyword: str, value: str,current_user: User = Depends(get_current_user)):
    """
    Endpoint to search assets dynamically by a given keyword and value.
    Example: /asset/search/keyword?keyword=name&value=Laptop
    """
    try:
        return asset_reader.get_asset_by_keyword(keyword, value)
    except Exception as e:
        print(e)  # Debug print, can be replaced with proper logging
        raise HTTPException(status_code=404, detail="Not Found")


@asset_router.get("/list/count")
def get_count(current_user: User = Depends(get_current_user)):
    """
    Endpoint to return the total count of assets.
    Useful for dashboards or summary views.
    """
    try:
        return asset_reader.get_all_asset_count()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail="Not Found")