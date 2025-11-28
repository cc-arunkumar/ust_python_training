from fastapi import FastAPI,APIRouter,Depends
from src.crud.asset_crud import get_all_assets,get_by_id,create_asset,update_by_id,delete_by_id,update_by_status,get_by_search,get_by_count,get_assets_by_status
from src.models.asset__model import AssetInventory
from ..auth.jwt_auth import get_current_user,User

# Create router for asset-related APIs with prefix "/assets"
asset_router=APIRouter(prefix="/assets")

# Search assets by field type and keyword
@asset_router.get("/search")
def get_search(field_type:str="",keyword:str="",current_user: User = Depends(get_current_user)):
    return get_by_search(field_type,keyword)

# Get count of all assets
@asset_router.get("/count",)
def get_count(current_user: User = Depends(get_current_user)):
    return get_by_count()

# Get assets filtered by status
@asset_router.get("/list")
def get_assets_status(status:str="",current_user: User = Depends(get_current_user)):
    return get_assets_by_status(status)

# Get all assets
@asset_router.get("/list")
def get_assets(current_user: User = Depends(get_current_user)):
    return get_all_assets()

# Get asset by ID
@asset_router.get("/{id}",)
def get_id(id:int,current_user: User = Depends(get_current_user)):
    return get_by_id(id)

# Create a new asset
@asset_router.post("/create")
def create_assets(asset:AssetInventory,current_user: User = Depends(get_current_user)):
    return create_asset(asset)

# Update asset by ID
@asset_router.put("/{id}")
def update_id(id:int,asset:AssetInventory,current_user: User = Depends(get_current_user)):
    return update_by_id(id,asset)

# Update asset status by ID
@asset_router.patch("/{id}")
def update_status(id:int,status:str="",current_user: User = Depends(get_current_user)):
    return update_by_status(id,status)

# Delete asset by ID
@asset_router.delete("/{id}",)
def delete_id(id:int,current_user: User = Depends(get_current_user)):
    return delete_by_id(id)
