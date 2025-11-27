from fastapi import APIRouter,HTTPException
from ..models.asset_model import AssetInventory
from ..crud.asset_crud import Asset
from typing import List

asset_service = Asset

asset_router = APIRouter(prefix="/asset")


@asset_router.get("/list")
def get_all():
    try:
        return asset_service.get_all_asset()
    except Exception:
        raise HTTPException(status_code=404,detail="Not found")