from fastapi import APIRouter, Query, Depends, HTTPException, status
from src.models.asset_model import AssetCreate, AssetUpdate
from src.crud.asset_crud import (
    create_asset, get_all_assets, get_asset_by_id,
    update_asset, update_status_only, delete_asset,
    search_assets, count_assets
)
from src.auth.auth import get_curr_user
from src.models.login_model import User

# Create an API router for assets
asset_router = APIRouter(prefix="/assets", tags=["Assets"])

# CREATE: Only accessible by authenticated users
@asset_router.post("/create")
def create(asset: AssetCreate, current_user: User = Depends(get_curr_user)):
    # `get_curr_user` ensures that only authenticated users can create assets
    return create_asset(
        asset.asset_tag, asset.asset_type, asset.serial_number,
        asset.manufacturer, asset.model, asset.purchase_date,
        asset.warranty_years, asset.condition_status,
        asset.assigned_to or "", asset.location, asset.asset_status
    )

# LIST ALL + FILTER BY STATUS: Accessible only by authenticated users
@asset_router.get("/list")
def list_all(status: str = None, current_user: User = Depends(get_curr_user)):
    # `get_curr_user` ensures that only authenticated users can access the list
    if status:
        return get_all_assets(status)
    else:
        return get_all_assets()

# COUNT: Accessible only by authenticated users
@asset_router.get("/count")
def count(current_user: User = Depends(get_curr_user)):
    # `get_curr_user` ensures that only authenticated users can access the count
    return count_assets()

# SEARCH: Accessible only by authenticated users
@asset_router.get("/search")
def search(keyword: str = Query(..., description="Search in tag, model, manufacturer, serial"), current_user: User = Depends(get_curr_user)):
    # `get_curr_user` ensures that only authenticated users can search assets
    return search_assets(keyword)

# UPDATE STATUS ONLY: Accessible only by authenticated users
@asset_router.patch("/{id}/status")
def patch_status(id: int, status: str = Query(..., description="New status: Available/Assigned/Repair/Retired"), current_user: User = Depends(get_curr_user)):
    # `get_curr_user` ensures that only authenticated users can update the asset status
    return update_status_only(id, status)

# GET SINGLE: Accessible only by authenticated users
@asset_router.get("/{id}")
def get_one(id: int, current_user: User = Depends(get_curr_user)):
    # `get_curr_user` ensures that only authenticated users can access asset details
    return get_asset_by_id(id)

# UPDATE FULL: Accessible only by authenticated users
@asset_router.put("/{id}")
def update(id: int, asset: AssetUpdate, current_user: User = Depends(get_curr_user)):
    # `get_curr_user` ensures that only authenticated users can update asset details
    return update_asset(
        id,
        asset.asset_tag, asset.asset_type, asset.serial_number,
        asset.manufacturer, asset.model, asset.purchase_date,
        asset.warranty_years, asset.condition_status,
        asset.assigned_to or "", asset.location, asset.asset_status
    )

# DELETE: Accessible only by authenticated users
@asset_router.delete("/{id}")
def delete(id: int, current_user: User = Depends(get_curr_user)):
    # `get_curr_user` ensures that only authenticated users can delete assets
    return delete_asset(id)
