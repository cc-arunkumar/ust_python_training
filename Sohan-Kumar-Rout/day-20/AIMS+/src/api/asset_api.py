# asset_api.py
from fastapi import APIRouter, Depends, HTTPException
from auth.jwt_auth import User, get_curr_user
from crud.asset_crud import (
    get_task, asset_by_id, assets_by_status, asset_searching,
    count_assets, delete_asset, creating_task, update_asset, update_asset_status
)
from models.asset_model import Asset_inventory

router = APIRouter(prefix="/assets", tags=["Assets"])

@router.get("/count")
def count_assets_api(current_user: User = Depends(get_curr_user)):
    return count_assets()

@router.get("/")
def get_all_assets(current_user: User = Depends(get_curr_user)):
    try:
        return get_task()
    except Exception:
        raise HTTPException(status_code=500, detail="fetching issue")

@router.get("/{id}")
def get_assets_by_id(id: int, current_user: User = Depends(get_curr_user)):
    return asset_by_id(id)

@router.get("/list")
def list_assets(status: str, current_user: User = Depends(get_curr_user)):
    return assets_by_status(status)

@router.get("/search")
def search_assets(keyword: str, current_user: User = Depends(get_curr_user)):
    return {"assets": asset_searching(keyword)}



@router.delete("/{id}")
def delete_asset_api(id: int, current_user: User = Depends(get_curr_user)):
    return delete_asset(id)

@router.post("/create")
def create_asset(asset: Asset_inventory, current_user: User = Depends(get_curr_user)):
    return creating_task(
        asset.asset_id,
        asset.asset_tag,
        asset.asset_type,
        asset.serial_number,
        asset.manufacturer,
        asset.model,
        asset.purchase_date,
        asset.warranty_years,
        asset.condition_status,
        asset.assigned_to,
        asset.location,
        asset.asset_status,
    )

@router.put("/{asset_id}")
def update_asset_details(asset_id: int, asset: Asset_inventory, current_user: User = Depends(get_curr_user)):
    return update_asset(
        asset_id,
        asset.asset_tag,
        asset.asset_type,
        asset.serial_number,
        asset.manufacturer,
        asset.model,
        asset.purchase_date,
        asset.warranty_years,
        asset.condition_status,
        asset.assigned_to,
        asset.location,
        asset.asset_status,
    )

@router.patch("/{asset_id}/status")
def change_asset_status(asset_id: int, asset_status: str, current_user: User = Depends(get_curr_user)):
    return update_asset_status(asset_id, asset_status)
