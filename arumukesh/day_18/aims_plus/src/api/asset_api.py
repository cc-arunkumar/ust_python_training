from fastapi import Depends,APIRouter, HTTPException
from src.model.model_asset_inventory import AssetInventory
from src.auth.jwt_authentication import get_current_user,User
from src.crud.asset_crud import (
    create_asset,
    get_all,
    get_by_id,
    update,
    delete,
    count_records,
    find
)

router = APIRouter(prefix="/assets", tags=["Assets"])


@router.post("/")
def create(data: AssetInventory,current_user:User=Depends(get_current_user)):
    return create_asset(data)


@router.get("/")
def list_all(current_user:User=Depends(get_current_user)):
    return get_all()


# @router.get("/status/{status}")
# def filter_by_status(status: str):
#     return get_by_stat(status)


@router.get("/count")
def count_data(current_user:User=Depends(get_current_user)):
    return count_records()


@router.get("/search/{column}/{value}")
def search(column: str, value: str,current_user:User=Depends(get_current_user)):
    return find(column, value)


@router.get("/{asset_id}")
def get(asset_id: str,current_user:User=Depends(get_current_user)):
    result = get_by_id(asset_id)
    if not result:
        raise HTTPException(404, "Asset not found")
    return result


@router.put("/{asset_id}")
def modify(asset_id: str, data: AssetInventory,current_user:User=Depends(get_current_user)):
    return update(asset_id, data)


@router.delete("/{asset_id}")
def remove(asset_id: str,current_user:User=Depends(get_current_user)):
    return delete(asset_id)
