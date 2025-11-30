from fastapi import APIRouter, Query,Depends
from typing import Optional
from models.asset_models import AssetCreate, AssetUpdate, AssetStatusUpdate
from auth.auth_jwt_token import get_current_user

from crud.asset_crud import (
    create_asset,
    list_assets,
    get_asset_by_id,
    update_asset,
    update_asset_status,
    delete_asset,
    search_asset,
    count_assets,
    bulk_upload_assets_from_csv,
)

router = APIRouter(prefix="/assets", tags=["Assets"])   


def success(message, data=None):
    return {"status": "success", "message": message, "data": data}


@router.post("/create")
def create_asset_api(payload: AssetCreate,current_user: dict = Depends(get_current_user)):
    return success("Asset created", create_asset(payload))


@router.get("/list")
def list_assets_api(status: Optional[str] = Query(default=None),current_user: dict = Depends(get_current_user)):
    return success("Assets fetched", list_assets(status))


@router.get("/{asset_id}")
def get_asset_api(asset_id: int,current_user: dict = Depends(get_current_user)):
    return success("Asset fetched", get_asset_by_id(asset_id))


@router.put("/{asset_id}")
def update_asset_api(asset_id: int, payload: AssetUpdate,current_user: dict = Depends(get_current_user)):
    return success("Asset updated", update_asset(asset_id, payload))


@router.patch("/{asset_id}/status")
def update_status_api(asset_id: int, payload: AssetStatusUpdate,current_user: dict = Depends(get_current_user)):
    return success("Asset status updated", update_asset_status(asset_id, payload.asset_status))


@router.delete("/{asset_id}")
def delete_asset_api(asset_id: int,current_user: dict = Depends(get_current_user)):
    delete_asset(asset_id)
    return success("Asset deleted", None)


@router.get("/search/")
def search_asset_api(keyword: str = Query(...),current_user: dict = Depends(get_current_user)):
    return success("Search results", search_asset(keyword))


@router.get("/count")
def count_assets_api(current_user: dict = Depends(get_current_user)):
    return success("Asset count", {"count": count_assets()})


@router.post("/bulk-upload")
def bulk_upload_api(current_user: dict = Depends(get_current_user)):
    bulk_upload_assets_from_csv()
    return success("Bulk upload completed")
