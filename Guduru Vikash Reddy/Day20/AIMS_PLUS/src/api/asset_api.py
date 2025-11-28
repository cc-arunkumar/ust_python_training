from fastapi import Depends, HTTPException, status, APIRouter
from typing import List, Optional
from src.models.asset_model import AssetInventory
from src.crud.asset_crud import read_all_assets, read_asset_by_id, insert_asset_to_db, update_asset_by_id, delete_asset, search_assets
from src.auth.jwt_auth import User,get_curr_user

# Initialize the asset_router with a prefix "/assets"
asset_router = APIRouter(prefix="/assets")

# POST endpoint to create a new asset
@asset_router.post('/create', response_model=AssetInventory)
def create_asset(new_asset: AssetInventory,current_user: User = Depends(get_curr_user)):
    try:
        # Check if the asset already exists by its asset_id
        existing_asset = get_asset_by_id(new_asset.asset_id)
        if existing_asset:
            # If the asset already exists, raise an error
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Asset with this ID already exists.")
        
        # Insert the new asset into the database
        data = insert_asset_to_db(new_asset)
        return new_asset  # Return the created asset
    except Exception as e:
        # If there is an error, raise an HTTP exception with a 404 Not Found status
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error: {e}")

# GET endpoint to search assets based on a field (e.g., vendor_name, serial_number)
@asset_router.get("/search")
def search_by_word(field_type: str, keyword: str,current_user: User = Depends(get_curr_user)):
    try:
        # Call the search function from CRUD operations
        data = search_assets(field_type, keyword)
        return data  # Return the search results
    except Exception as e:
        # If there is an error, raise an HTTP exception with a 400 Bad Request status
        raise HTTPException(status_code=400, detail=f"Unable to fetch data: {e}")

# GET endpoint to fetch a list of assets, with an optional status filter
@asset_router.get("/lists", response_model=List[AssetInventory])
def get_assets(status_filter: Optional[str] = "",current_user: User = Depends(get_curr_user)):
    try:
        # Fetch all assets or filter by status if provided
        rows = read_all_assets(status_filter)
        asset_list = []
        for row in rows:
            # Create AssetInventory objects from the rows returned by the database
            asset_list.append(AssetInventory(**row))
        return asset_list  # Return the list of assets
    except Exception as e:
        # If there is an error, raise an HTTP exception with a 400 Bad Request status
        raise HTTPException(status_code=400, detail=f"{e}")

# GET endpoint to count the total number of assets
@asset_router.get("/count")
def count_data(current_user: User = Depends(get_curr_user)):
    try:
        # Fetch all assets to count them
        data = read_all_assets()
        if data is None:
            # Raise a 404 Not Found error if no assets are found
            raise HTTPException(status_code=404, detail="No assets found.")
        return {"count": len(data)}  # Return the count of assets
    except Exception as e:
        # Raise a 500 Internal Server Error if there is an issue
        raise HTTPException(status_code=500, detail=f"Error counting assets: {str(e)}")

# GET endpoint to fetch an asset by its ID
@asset_router.get("/{asset_id}", response_model=AssetInventory)
def get_asset_by_id(asset_id: int,current_user: User = Depends(get_curr_user)):
    try:
        # Fetch the asset by ID from the database
        rows = read_asset_by_id(asset_id)
        if not rows:
            # If no asset is found, raise a 404 Not Found error
            raise HTTPException(status_code=404, detail="Asset not exists")
        return AssetInventory(**rows)  # Return the asset data
    except Exception as e:
        # Raise a 400 Bad Request error if something goes wrong
        raise HTTPException(status_code=400, detail="ID not found")

# PUT endpoint to update an existing asset's details by asset ID
@asset_router.put("/{id}", response_model=AssetInventory)
def update_details(id: int, update_asset: AssetInventory,current_user: User = Depends(get_curr_user)):
    try:
        # Update the asset by its ID using the provided data
        update_asset_by_id(id, update_asset)
        # Fetch the updated asset to return it
        data = read_asset_by_id(id)
        return AssetInventory(**data)  # Return the updated asset
    except Exception as e:
        # If there is an error, raise a 404 Not Found error
        raise HTTPException(status_code=404, detail="Update is not complete")

# DELETE endpoint to remove an asset by its ID
@asset_router.delete("/{asset_id}")
def delete_asset_by_id(asset_id: int,current_user: User = Depends(get_curr_user)):
    try:
        # Attempt to delete the asset
        if delete_asset(asset_id):
            return {"detail": "Asset deleted successfully"}  # Return success message
    except Exception as e:
        # Raise an HTTP exception with a 400 Bad Request error if there's an issue
        raise HTTPException(status_code=400, detail=f"Error deleting asset: {str(e)}")

# PATCH endpoint to update the status of an asset by its ID
@asset_router.patch("/{id}/status")
def update_status(id: int, status: str,current_user: User = Depends(get_curr_user)):
    try:
        # Fetch the asset by ID
        data = read_asset_by_id(id)
        
        if not data:
            # If the asset is not found, raise a 404 Not Found error
            raise HTTPException(status_code=404, detail="Asset not found")
        
        # Update the asset's status
        data['asset_status'] = status
        
        # Call the update function to apply the status change
        update_asset_by_id(id, AssetInventory(**data))
        
        return {"message": "Asset status updated successfully", "asset_id": id, "new_status": status}
    except Exception as e:
        # Raise a 400 Bad Request error if there is an issue updating the status
        raise HTTPException(status_code=400, detail=f"Error updating asset status: {str(e)}")
