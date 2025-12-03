from fastapi import FastAPI,HTTPException,APIRouter
from ..models.asset_model import Asset
from typing import Optional
from ..crud.inventory_asset_crud import AssetCrud

# app=FastAPI()
# def get_connection():
#     return pymysql.connect(
#         host="localhost",
#         user="root",
#         password="pass@word1",
#         database="ust_assets"
#     )

asset_reader=AssetCrud()
asset_router=APIRouter(prefix="/asset")
@asset_router.get("/list")
def get_all_assets(status: Optional[str] = "ALL"):
    try:
        return asset_reader.get_all_assets(status)
    except Exception:
        raise HTTPException(status_code=404,detail="Not Found")