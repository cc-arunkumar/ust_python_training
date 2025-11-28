from fastapi import HTTPException, Depends,FastAPI,APIRouter
from src.models.assert_inventory_pydentic import Asset_inventory
from src.crud.asset_inventory import get_task,create_task, get_task_by_id,update_asset,update_asset_status,delete_asset, get_assets_by_status,search_assets_by_column,count_assets
from src.auth.jwt_auth import get_current_user
from src.models.login_model import User

assets_router = APIRouter(prefix="/assets") 



@assets_router.post("/create")

def create_asset(asset: Asset_inventory, current_user: User = Depends(get_current_user)):
    return create_task(
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




@assets_router.get("")
def get_all_assets(current_user: User = Depends(get_current_user)):
    try:
        assets = get_task()
        return {"assets": assets}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching assets: {str(e)}")
    
@assets_router.get("/get{id}")
def get_assets_by_id(id: int,current_user: User = Depends(get_current_user)):
    return get_task_by_id(id)

    
@assets_router.get("/list")
def list_assets(status: str,current_user: User = Depends(get_current_user)):
    return {"assets": get_assets_by_status(status)}
@assets_router.get("/search")
def search_assets_api(column: str, value: str):
    return search_assets_by_column(column, value)


@assets_router.get("/count")
def count_assets_api(current_user: User = Depends(get_current_user)):
    return {"total_assets": count_assets()}


@assets_router.put("/{id}")
def update_asset_api(id: int, asset: Asset_inventory,current_user: User = Depends(get_current_user)):
    return update_asset(
        id,
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

@assets_router.patch("/{id}/status")
def update_asset_status_api(id: int, asset_status: str,current_user: User = Depends(get_current_user)):
    return update_asset_status(id, asset_status)

@assets_router.delete("/{id}")
def delete_asset_api(id: int,current_user: User = Depends(get_current_user)):
    return delete_asset(id)


