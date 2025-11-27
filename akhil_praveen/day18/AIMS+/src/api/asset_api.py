from fastapi import FastAPI,HTTPException,APIRouter
from typing import Optional
from ..models.assetsinventory import AssetInventory,StatusValidate
from ..crud.asset_crud import AssetCrud

asset_reader = AssetCrud()
asset_router = APIRouter(prefix="/asset")

@asset_router.post("/create")
def create_asset(asset:AssetInventory):
    try:
        return asset_reader.create_asset(asset)
    except Exception:
        raise HTTPException(status_code=404,detail="Not Found")

@asset_router.get("/list")
def get_all_asset(status:Optional[str] = "ALL"):
    try:
        return asset_reader.get_all_asset(status)
    except Exception:
        raise HTTPException(status_code=404,detail="Not Found")

@asset_router.get("/{id}")
def get_asset_by_id(id:int):
    try:
        return asset_reader.get_asset_by_id(id)
    except Exception:
        raise HTTPException(status_code=404,detail="Not Found")

@asset_router.put("/{id}")
def update_asset(id:int,data:AssetInventory):
    try:
        return asset_reader.update_asset(id,data)
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404,detail="Not Found")

@asset_router.patch("/{id}/status")
def update_asset_status(id:int,status:StatusValidate):
    try:
        print(status)
        return asset_reader.update_asset_status(id,status.asset_status)
    except Exception:
        raise HTTPException(status_code=404,detail="Not Found")

@asset_router.delete("/{id}")
def update_asset_status(id:int):
    try:
        return asset_reader.delete_asset(id)
    except Exception:
        raise HTTPException(status_code=404,detail="Not Found")

@asset_router.get("/search/keyword")
def get_asset_by_keyword(keyword:str,value:str):
    try:
        return asset_reader.get_asset_by_keyword(keyword,value)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404,detail="Not Found")

@asset_router.get("/list/count")
def get_asset_by_keyword():
    try:
        return asset_reader.get_all_asset_count()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404,detail="Not Found")
