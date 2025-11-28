from fastapi import FastAPI, HTTPException, status, APIRouter,Depends
from src.crud import asset_crud
from src.models import asset_model
from typing import List, Optional
from src.auth.auth_jwt_token import get_current_user
from src.models.login_model import User

# Create an API router with prefix "/asset"
asset_router = APIRouter(prefix="/asset")

# Search assets by a specific field and keyword
@asset_router.get('/search', response_model=List[asset_model.AssetInventory])
def search_by_word(field_type: str, keyword: str, curr_user: User = Depends(get_current_user)):

    try:
        data = asset_crud.search_assets(field_type, keyword)
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to fetch data: {e}")


# Get all assets (optionally filter by status)
@asset_router.get('/list', response_model=List[asset_model.AssetInventory])
def get_all(status_filter: Optional[str] = "", curr_user: User = Depends(get_current_user)):

    try:
        data = asset_crud.get_all_assets(status_filter)
        new_li = []
        for row in data:
            new_li.append(asset_model.AssetInventory(**row))
        return new_li
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Failed to Fetch All the Records: {e}")


# Get count of all assets
@asset_router.get("/count")
def count_all(curr_user: User = Depends(get_current_user)):

    data = asset_crud.get_all_assets()
    return {"detail": f"Count of records: {len(data)}"}


# Get asset by ID
@asset_router.get('/{id}', response_model=asset_model.AssetInventory)
def get_by_id(id: int,curr_user: User = Depends(get_current_user)):

    try:
        data = asset_crud.get_asset_by_id(id)
        if not data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not Found")
        return asset_model.AssetInventory(**data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"ID not Found or Unable to fetch the Record : {e}")


# Create a new asset
@asset_router.post('/create', response_model=asset_model.AssetInventory)
def create_asset(new_asset: asset_model.AssetInventory,curr_user: User = Depends(get_current_user)):

    try:
        data = asset_crud.create_asset(new_asset)
        return asset_model.AssetInventory(**data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error: {e}")


# Delete an asset by ID
@asset_router.delete("/{id}")
def delete_asset_id(id: int,curr_user: User = Depends(get_current_user)):

    try:
        if asset_crud.delete_asset_by_id(id):
            return {"detail": "Record deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Asset Id Doesnt Exist: {e}")


# Update an asset by ID
@asset_router.put("/{id}", response_model=asset_model.AssetInventory)
def update_by_id(id: int, new_asset: asset_model.AssetInventory,curr_user: User = Depends(get_current_user)):

    try:
        asset_crud.update_asset_by_id(id, new_asset)
        data = asset_crud.get_asset_by_id(id)
        return asset_model.AssetInventory(**data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to update asset: {e}")


# Patch asset status by ID
@asset_router.patch("/{id}/status", response_model=asset_model.AssetInventory)
def patch_by_id(id: int, status: str,curr_user: User = Depends(get_current_user)):

    data = get_by_id(id)
    try:
        if data:
            data.asset_status = status
            return update_by_id(id, data)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error: {e}")
