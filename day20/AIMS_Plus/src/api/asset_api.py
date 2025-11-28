from fastapi import APIRouter, HTTPException,Depends
from ..models.asset_model import AssetInventory
from ..models.user_model import User
from ..crud.asset_crud import Asset
from typing import List, Optional
from ..auth.jwt_auth import get_current_user


asset_service = Asset()  # Service instance for asset CRUD
asset_router = APIRouter(prefix="/assets")  # Router with /assets prefix


@asset_router.get("/list")
def get_all(status: Optional[str] = "all",current_user : User =Depends(get_current_user)):  # Get all assets (optionally filter by status)
    try:
        return asset_service.get_all_asset(status)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@asset_router.get("/{asset_id}")
def get_by_id(asset_id: int,current_user : User =Depends(get_current_user)):  # Get asset by ID
    try:
        return asset_service.get_asset_by_id(asset_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@asset_router.put("/{asset_id}")
def update_asset(asset_id: int, asset: AssetInventory,current_user : User =Depends(get_current_user)):  # Update full asset record
    try:
        if asset_service.update_asset(asset_id, asset):
            return {"message": "Update Successful"}
        else:
            return {"message": "Asset Not Found"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@asset_router.patch("/{asset_id}/")
def update_asset(asset_id: int, status: str,current_user : User =Depends(get_current_user)):  # Update only asset status
    try:
        if asset_service.update_asset_status(asset_id, status):
            return {"message": "Update Successful"}
        else:
            return {"message": "Asset Not Found"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@asset_router.post("/create")
def create_asset(asset: AssetInventory,current_user : User =Depends(get_current_user)):  # Create new asset
    try:
        if asset_service.create_asset(asset):
            return {"message": "Added Successful"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@asset_router.delete("/{asset_id}")
def delete_asset(asset_id: int,current_user : User =Depends(get_current_user)):  # Delete asset by ID
    try:
        if asset_service.delete_asset(asset_id):
            return {"message": "Deleted Successful"}
        else:
            return {"message": "Asset Not Found"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@asset_router.get("/search/keyword/")
def get_by_keyword(keyword: str, value: str,current_user : User =Depends(get_current_user)):  # Search asset by keyword/value
    try:
        return asset_service.get_asset_keyword(keyword, value)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@asset_router.get("/all/count/")
def get_count(current_user : User =Depends(get_current_user)):  # Get total asset count
    try:
        return asset_service.get_asset_count()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))