from fastapi import FastAPI, HTTPException, status, APIRouter, Depends
from typing import List, Optional
from src.models.asset_model import AssetInventory  # Importing the Asset model for asset inventory
from src.config.db_connection import get_connection  # Importing DB connection function
from src.crud.asset_crud import read_all_assets, read_asset_by_id, insert_asset_to_db, update_asset_by_id, delete_asset, search_assets  # CRUD operations for assets
from src.auth.auth_jwt_token import User, get_curr_user  # JWT auth and user authentication

# Initialize the FastAPI app and asset router
asset_router = APIRouter(prefix="/assets")

# Create Asset endpoint (No authentication needed for this one)
@asset_router.post('/create', response_model=AssetInventory)
def create_asset(new_asset: AssetInventory):
    """
    Endpoint to create a new asset. This route doesn't require authentication.
    It takes a new asset as input and inserts it into the database.
    """
    try:
        insert_asset_to_db(new_asset)  # Insert the asset into the DB
        return new_asset  # Return the newly created asset
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error: {e}")  # If error occurs, raise HTTP exception

# Get all assets endpoint (Secured with JWT)
@asset_router.get("/", response_model=List[AssetInventory])
def get_assets(current_user: User = Depends(get_curr_user)):  # Secure this route with JWT authentication
    """
    Endpoint to get a list of all assets. Only accessible by authenticated users.
    """
    try:
        rows = read_all_assets()  # Fetch all assets from the DB
        if not rows:
            return []  # Return an empty list if no assets are found
        assets_li = [AssetInventory(**row) for row in rows]  # Convert DB rows to Pydantic models
        return assets_li  # Return the list of assets
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{e}")  # Raise error if something goes wrong

# Search assets by field and keyword (Secured with JWT)
@asset_router.get("/search")
def search_by_word(field_type: str, keyword: str, current_user: User = Depends(get_curr_user)):  # Secure with JWT
    """
    Endpoint to search assets by a specific field and keyword. Only accessible by authenticated users.
    """
    try:
        data = search_assets(field_type, keyword)  # Perform search operation in DB
        return data  # Return search results
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to fetch data: {e}")  # Handle errors in search

# Get assets with optional status filter (Secured with JWT)
@asset_router.get("/lists", response_model=List[AssetInventory])
def get_assets(status_filter: Optional[str] = "", current_user: User = Depends(get_curr_user)):  # Secure with JWT
    """
    Endpoint to get a list of assets filtered by status (if provided). Only accessible by authenticated users.
    """
    try:
        rows = read_all_assets(status_filter)  # Fetch assets, filtered by status if provided
        if not rows:
            return []  # Return an empty list if no assets are found
        assets_li = [AssetInventory(**row) for row in rows]  # Convert rows to Pydantic models
        return assets_li  # Return the list of assets
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{e}")  # Handle errors during asset retrieval

# Get asset count (Secured with JWT)
@asset_router.get("/count")
def count_data(current_user: User = Depends(get_curr_user)):  # Secure with JWT
    """
    Endpoint to get the count of assets. Only accessible by authenticated users.
    """
    try:
        data = read_all_assets()  # Get all assets from DB
        count = len(data) if data else 0  # Get count of assets, return 0 if none are found
        return {"count": count}  # Return the count in a dictionary
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error counting assets: {str(e)}")  # Handle errors while counting assets

# Get asset by ID (Secured with JWT)
@asset_router.get("/{asset_id}", response_model=AssetInventory)
def get_asset_by_id(asset_id: int, current_user: User = Depends(get_curr_user)):  # Secure with JWT
    """
    Endpoint to get a single asset by its ID. Only accessible by authenticated users.
    """
    try:
        row = read_asset_by_id(asset_id)  # Fetch asset by ID from the DB
        if not row:
            raise HTTPException(status_code=404, detail="Asset not found")  # Raise error if asset is not found
        return AssetInventory(**row)  # Return the asset as a Pydantic model
    except Exception as e:
        raise HTTPException(status_code=400, detail="ID not found")  # Raise error for invalid ID

# Update asset details (Secured with JWT)
@asset_router.put("/{id}", response_model=AssetInventory)
def update_details(id: int, update_asset: AssetInventory, current_user: User = Depends(get_curr_user)):  # Secure with JWT
    """
    Endpoint to update asset details. Only accessible by authenticated users.
    """
    try:
        update_asset_by_id(id, update_asset)  # Update asset in DB
        data = read_asset_by_id(id)  # Fetch the updated asset
        return AssetInventory(**data)  # Return the updated asset
    except Exception as e:
        raise HTTPException(status_code=404, detail="Update failed")  # Handle errors during update

# Delete asset by ID (Secured with JWT)
@asset_router.delete("/{asset_id}")
def delete_asset_by_id(asset_id: int, current_user: User = Depends(get_curr_user)):  # Secure with JWT
    """
    Endpoint to delete an asset by its ID. Only accessible by authenticated users.
    """
    try:
        if delete_asset(asset_id):  # Attempt to delete the asset
            return {"detail": "Asset deleted successfully"}  # Return success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting asset: {str(e)}")  # Handle errors during deletion

# Update asset status (Secured with JWT)
@asset_router.patch("/{id}/status")
def update_status(id: int, status: str, current_user: User = Depends(get_curr_user)):  # Secure with JWT
    """
    Endpoint to update the status of an asset. Only accessible by authenticated users.
    """
    try:
        data = read_asset_by_id(id)  # Fetch asset by ID
        if not data:
            raise HTTPException(status_code=404, detail="Asset not found")  # Raise error if asset not found
        
        data['asset_status'] = status  # Update asset's status
        update_asset_by_id(id, AssetInventory(**data))  # Update asset in the DB
        
        return {"message": "Asset status updated successfully", "asset_id": id, "new_status": status}  # Return success message with updated status
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating asset status: {str(e)}")  # Handle errors during status update
