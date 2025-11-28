from fastapi import APIRouter, HTTPException, Depends
from src.models.asset_model import Asset, validate_asset
from src.crud import asset_crud
from src.auth.jwt_auth import User,get_current_user
router = APIRouter()

# 1. POST /assets/create
@router.post("/create", response_model=Asset)
def create(asset: Asset,current_user:User=Depends(get_current_user)):
    validate_asset(asset)
    new_id = asset_crud.create_asset(asset)
    return {**asset.model_dump(), "asset_id": new_id}

# 2 & 3. GET /assets/list (+?status=)
@router.get("/list")
def list_assets(status: str = None, current_user:User=Depends(get_current_user) ):
    rows = asset_crud.list_assets(status)
    if not rows:
        raise HTTPException(status_code=404, detail="No assets found")
    return {"status": "success", "data": rows}
@router.get("/count")
def count_assets(current_user:User=Depends(get_current_user)):
    row = asset_crud.count_assets()
    return {"status": "success", "count": row["total"]}
# 4. GET /assets/{id}
@router.get("/{asset_id}", response_model=Asset)
def get_asset(asset_id: int, current_user:User=Depends(get_current_user)):
    row = asset_crud.get_asset(asset_id)
    if not row:
        raise HTTPException(status_code=404, detail="Asset not found")
    return Asset(**row)

# 5. PUT /assets/{id}
@router.put("/{asset_id}", response_model=Asset)
def update_asset(asset_id: int, asset: Asset, current_user:User=Depends(get_current_user)):
    validate_asset(asset)
    asset_crud.update_asset(asset_id, asset)
    row = asset_crud.get_asset(asset_id)
    return Asset(**row)

# 6. PATCH /assets/{id}/status
@router.patch("/{asset_id}/status")
def update_status(asset_id: int, status: str, current_user:User=Depends(get_current_user)):
    if status not in {"Available", "Assigned", "Repair", "Retired"}:
        raise HTTPException(status_code=422, detail="Invalid status")
    asset_crud.update_status(asset_id, status)
    return {"status": "success", "message": f"Asset {asset_id} status updated to {status}"}

# 7. DELETE /assets/{id}
@router.delete("/{asset_id}")
def delete_asset(asset_id: int, current_user:User=Depends(get_current_user)):
    asset_crud.delete_asset(asset_id)
    return {"status": "success", "message": "Asset deleted"}

# 8. GET /assets/search?keyword=
@router.get("/search")
def search_assets(keyword: str, current_user:User=Depends(get_current_user)):
    rows = asset_crud.search_assets(keyword)
    if not rows:
        raise HTTPException(status_code=404, detail="No matching assets found")
    return {"status": "success", "data": rows}

