import sys
import os
from src.models.login_model import User
# Add the 'src' directory to the Python path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'src'))

# Now, you can import the crud module
from crud.asset_crud import (get_asset_data,get_asset_data_by_id,delete_asset_by_id,assets_count_api,get_assets_list,create_asset,update_asset_by_id,update_asset_status_by_id,search_assets)
from models.asset_model import AssetInventory,UpdateStatusRequest
from fastapi import FastAPI,HTTPException,APIRouter,Depends
from src.auth.login_function import get_current_user

# Initialize the FastAPI router for asset-related endpoints with a prefix "/assets"
asset_router =APIRouter(prefix="/assets")

# 1. Get all assets
@asset_router.get("/assets/list")
def get_all_assets(current_user: User = Depends(get_current_user)):
    # Fetches the list of all assets from the database
    result = get_asset_data()
    return result

# 2. Get asset by ID
@asset_router.get("/assets/{id}")
def get_all_assets(id: int,current_user: User = Depends(get_current_user)):
    # Fetches the asset by ID from the database
    return get_asset_data_by_id(id)

# 3. DELETE /assets/{id} - Delete asset by ID
@asset_router.delete("/assets/{id}")
def delete_asset_by_id_api(id: int,current_user: User = Depends(get_current_user)):
    # Deletes an asset by its ID
    delete_asset_by_id(id)

# 4. GET /assets/count - Get total count of assets
@asset_router.get("/assets")
def get_assets_count_api(current_user: User = Depends(get_current_user)):
    # Retrieves the total count of assets
    result = assets_count_api()
    return {result}

# 5. GET /assets/list?status= - Filter assets by status
@asset_router.get("/assets/list/status")
def get_assets_list_api(status: str,current_user: User = Depends(get_current_user)):
    # Filters assets based on their status
    result = get_assets_list(status)
    return {"assets": result}

# 6. POST /assets - Create a new asset
@asset_router.post("/assets")
def create_asset_api(asset_detail: AssetInventory,current_user: User = Depends(get_current_user)):
    # Creates a new asset in the database
    result = create_asset(asset_detail)
    
    if Exception in result:
        # If an error occurs, raise an HTTPException with status code 500
        raise HTTPException(status_code=500, detail=result["error"])
    
    return result  

# 7. PUT /assets/{id} - Update asset by ID
@asset_router.put("/assets/{id}")
def update_asset_api(id: int, asset_detail: AssetInventory,current_user: User = Depends(get_current_user)):
    # Updates an asset by its ID
    result = update_asset_by_id(id, asset_detail)
    
    if "message" in result and result["message"] == "Asset not found for update":
        # If asset not found, return 404 error
        raise HTTPException(status_code=404, detail=result["message"])
    if "message" in result and result["message"] == "Duplicate serial number found":
        # If duplicate serial number is found, return 400 error
        raise HTTPException(status_code=400, detail=result["message"])  # Bad Request
    if "error" in result:
        # If there's an error, return 500 error
        raise HTTPException(status_code=500, detail=result["error"])
    return result

# 8. PATCH /assets/{id}/status - Update asset status only
@asset_router.patch("/assets/{id}/status")
def update_asset_status(asset_id: int, status_update: UpdateStatusRequest,current_user: User = Depends(get_current_user)):
    # Updates the status of an asset by ID
    result = update_asset_status_by_id(asset_id, status_update.asset_status)
    
    if "message" in result and result["message"] == "Asset not found for update":
        # If asset not found, return 404 error
        raise HTTPException(status_code=404, detail=result["message"])
    
    if "message" in result and "Invalid asset status" in result["message"]:
        # If invalid status provided, return 400 error
        raise HTTPException(status_code=400, detail=result["message"])  # Bad Request
    
    if "error" in result:
        # If there's an error, return 500 error
        raise HTTPException(status_code=500, detail=result["error"])  # Internal Server Error
    
    return result

# 9. GET /assets/search - Search for assets by keyword
@asset_router.get("/assets/search")
def search_assets_api(keyword: str,current_user: User = Depends(get_current_user)):
    # Search for assets matching the provided keyword
    result = search_assets(keyword)
    
    if "message" in result and result["message"] == "No assets found matching the keyword":
        # If no assets are found, return 404 error
        raise HTTPException(status_code=404, detail=result["message"])
    
    if "error" in result:
        # If there's an error, return 500 error
        raise HTTPException(status_code=500, detail=result["error"])
    
    return result
