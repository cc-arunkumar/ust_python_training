# Importing necessary modules for the FastAPI app
from fastapi import Depends, FastAPI, HTTPException, status, APIRouter
from typing import List, Optional
from src.auth.auth_jwt_token import User, get_current_user  # JWT authentication utilities
from src.models.asset_model import AssetInventory  # Asset model for validation
from src.config.db_connection import get_connection  # DB connection helper
from src.crud.asset_crud import read_all_assets, read_asset_by_id, insert_asset_to_db, update_asset_by_id, delete_asset, search_assets  # CRUD operations for assets

# Create an APIRouter instance for asset-related endpoints with a common prefix "/assets"
asset_router = APIRouter(prefix="/assets")

# Endpoint to create a new asset, only accessible to authenticated users
@asset_router.post('/create', response_model=AssetInventory)
def create_asset(new_asset: AssetInventory, current_user: User = Depends(get_current_user)):
    try:
        # Insert the new asset into the database
        data = insert_asset_to_db(new_asset)
        return new_asset  # Return the created asset as the response
    except Exception as e:
        # In case of an error, raise an HTTP 404 error with the exception message
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error: {e}")

# Endpoint to get a list of all assets
@asset_router.get("/lists", response_model=List[AssetInventory])
def get_assets(current_user: User = Depends(get_current_user)):
    try:
        # Read all assets from the database
        rows = read_all_assets()
        asset_li = []
        for row in rows:
            # Convert each row to AssetInventory model
            asset_li.append(AssetInventory(**row))
        return asset_li  # Return the list of assets
    except Exception as e:
        # In case of an error, raise an HTTP 400 error with the exception message
        raise HTTPException(status_code=400, detail=f"{e}")

# Endpoint to search assets by field and keyword (e.g., asset_tag or asset_type)
@asset_router.get("/search")
def search_by_word(field_type: str, keyword: str, current_user: User = Depends(get_current_user)):
    try:
        # Perform the search based on the field type and keyword
        data = search_assets(field_type, keyword)
        return data  # Return the search result
    except Exception as e:
        # In case of an error, raise an HTTP 400 error
        raise HTTPException(status_code=400, detail=f"Unable to fetch data: {e}")

# Endpoint to get a list of assets with an optional status filter
@asset_router.get("/lists", response_model=List[AssetInventory])
def get_assets(status_filter: Optional[str] = "", current_user: User = Depends(get_current_user)):
    try:
        # Read all assets, applying the optional status filter if provided
        rows = read_all_assets(status_filter)
        asset_li = []
        for row in rows:
            # Convert each row to AssetInventory model
            asset_li.append(AssetInventory(**row))
        return asset_li  # Return the list of filtered assets
    except Exception as e:
        # In case of an error, raise an HTTP 400 error
        raise HTTPException(status_code=400, detail=f"{e}")

# Endpoint to count the total number of assets in the system
@asset_router.get("/count")
def count_data(current_user: User = Depends(get_current_user)):
    try:
        # Retrieve all assets to count them
        data = read_all_assets()
        if data is None:
            # If no assets are found, raise a 404 error
            raise HTTPException(status_code=404, detail="No assets found.")
        return {"count": len(data)}  # Return the asset count
    except Exception as e:
        # In case of an error, raise a 500 error
        raise HTTPException(status_code=500, detail=f"Error counting assets: {str(e)}")

# Endpoint to get a specific asset by its ID
@asset_router.get("/{asset_id}", response_model=AssetInventory)
def get_asset_by_id(asset_id: int, current_user: User = Depends(get_current_user)):
    try:
        # Fetch the asset from the database by its ID
        rows = read_asset_by_id(asset_id)
        if not rows:
            # If no asset is found, raise a 404 error
            raise HTTPException(status_code=404, detail="Asset not exists")
        return AssetInventory(**rows)  # Return the asset details
    except Exception as e:
        # In case of an error, raise a 400 error
        raise HTTPException(status_code=400, detail="ID not found")

# Endpoint to update an asset's details by its ID
@asset_router.put("/{id}", response_model=AssetInventory)
def update_details(id: int, update_asset: AssetInventory, current_user: User = Depends(get_current_user)):
    try:
        # Update the asset details in the database
        update_asset_by_id(id, update_asset)
        # Fetch the updated asset from the database
        data = read_asset_by_id(id)
        return AssetInventory(**data)  # Return the updated asset details
    except Exception as e:
        # In case of an error, raise a 404 error
        raise HTTPException(status_code=404, detail="Update is not complete")

# Endpoint to delete an asset by its ID
@asset_router.delete("/{asset_id}")
def delete_asset_by_id(asset_id: int, current_user: User = Depends(get_current_user)):
    try:
        # Attempt to delete the asset from the database
        if delete_asset(asset_id):
            return {"detail": "Asset deleted successfully"}  # Return success message
    except Exception as e:
        # In case of an error, raise a 400 error with the exception message
        raise HTTPException(status_code=400, detail=f"Error deleting asset: {str(e)}")

# Endpoint to update an asset's status by its ID
@asset_router.patch("/{id}/status")
def update_status(id: int, status: str, current_user: User = Depends(get_current_user)):
    try:
        # Fetch the asset by its ID
        data = read_asset_by_id(id)
        
        if not data:
            # If no asset is found, raise a 404 error
            raise HTTPException(status_code=404, detail="Asset not found")
        
        # Update the asset's status
        data['asset_status'] = status
        
        # Save the updated asset back to the database
        update_asset_by_id(id, AssetInventory(**data))
        
        # Return success message with updated asset details
        return {"message": "Asset status updated successfully", "asset_id": id, "new_status": status}
        
    except Exception as e:
        # In case of an error, raise a 400 error with the exception message
        raise HTTPException(status_code=400, detail=f"Error updating asset status: {str(e)}")
