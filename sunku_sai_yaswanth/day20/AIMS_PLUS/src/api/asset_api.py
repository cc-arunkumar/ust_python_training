from fastapi import Depends, FastAPI, HTTPException,status,APIRouter
from typing import List, Optional
from auth.auth_jwt_token import User, get_current_user
from models.asset_model import AssetInventory
from config.db_connection import get_connection
from crud.asset_crud import read_all_assets,read_asset_by_id,insert_asset_to_db,update_asset_by_id,delete_asset,search_assets

asset_router=APIRouter(prefix="/assets")
# app = FastAPI(title="AIMS+ (AssetInventory Management System - Advanced Edition)")
@asset_router.post('/create',response_model=AssetInventory)
def create_asset(new_asset : AssetInventory,current_user: User = Depends(get_current_user)):
    try:
        data = insert_asset_to_db(new_asset)
        return new_asset
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Error: {e}")
        
@asset_router.get("/lists", response_model=List[AssetInventory])
def get_assets(current_user: User = Depends(get_current_user)):
    try:
        rows = read_all_assets()
        assest_li=[]
        for row in rows:
            assest_li.append(AssetInventory(**row))
        return assest_li
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"{e}")
@asset_router.get("/search")
def search_by_word(field_type:str,keyword : str,current_user: User = Depends(get_current_user)):
    try:
        data = search_assets(field_type,keyword)
        return data
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Unable to fetch data: {e}")
    
    
@asset_router.get("/lists", response_model=List[AssetInventory])
def get_assets(status_filter:Optional[str]="",current_user: User = Depends(get_current_user)):
    try:
        rows = read_all_assets(status_filter)
        assest_li=[]
        for row in rows:
            assest_li.append(AssetInventory(**row))
        return assest_li
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"{e}")


@asset_router.get("/count")
def count_data(current_user: User = Depends(get_current_user)):
    try:
        data = read_all_assets()
        if data is None:
            raise HTTPException(status_code=404, detail="No assets found.")
        return {"count": len(data)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error counting assets: {str(e)}")
 

@asset_router.get("/{asset_id}", response_model=AssetInventory)
def get_asset_by_id(asset_id: int,current_user: User = Depends(get_current_user)):
    try:
        rows=read_asset_by_id(asset_id)
        if not rows:
            raise HTTPException(status_code=404,detail="Asset not exists")
        return AssetInventory(**rows)
    except Exception as e:
        raise HTTPException(status_code=400,detail="ID not found")


@asset_router.put("/{id}",response_model=AssetInventory)
def update_details(id:int,update_asset:AssetInventory,current_user: User = Depends(get_current_user)):
    try:
        update_asset_by_id(id,update_asset)
        data=read_asset_by_id(id)
        return AssetInventory(**data)
    except Exception as e:
        raise HTTPException(status_code=404,detail="Update is not complete")
        

@asset_router.delete("/{asset_id}")
def delete_asset_by_id(asset_id: int,current_user: User = Depends(get_current_user)):
    try:
        
        if delete_asset(asset_id):
            return {"detail":"asset deleted successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting asset: {str(e)}")

@asset_router.patch("/{id}/status")
def update_status(id: int, status: str,current_user: User = Depends(get_current_user)):
    try:
        data = read_asset_by_id(id)
        
        if not data:
            raise HTTPException(status_code=404, detail="Asset not found")
        
        data['asset_status'] = status
        
        update_asset_by_id(id, AssetInventory(**data))
        
        return {"message": "Asset status updated successfully", "asset_id": id, "new_status": status}
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating asset status: {str(e)}")
