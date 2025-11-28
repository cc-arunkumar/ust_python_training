from fastapi import FastAPI, HTTPException, APIRouter,Depends
from src.auth.jwt_auth import get_current_user,User
from src.models import asset_model
from src.crud import asset_crud
from typing import List, Optional


# Router for asset-related endpoints, all prefixed with "/asset"
asset_router = APIRouter(prefix="/asset")

# -------------------------------
# Endpoint: Search assets by field
# -------------------------------
@asset_router.get("/", response_model=List[asset_model.Asset])
def search(field: str, val: str,current_user: User = Depends(get_current_user)):
    """
    Search assets by a given field and value.
    Example: /asset?field=name&val=server1
    """
    x = asset_crud.search_by_tag(field, val)
    if x:
        return x
    raise HTTPException(status_code=404, detail="Not found")


# -------------------------------
# Endpoint: Create a new asset
# -------------------------------
@asset_router.post("/create", response_model=asset_model.Asset)
def create_asset(new_asset: asset_model.Asset,current_user: User = Depends(get_current_user)):
    """
    Create a new asset record.
    Validates the asset before inserting into DB.
    """
    print(asset_model.validate_asset(new_asset))  # Debug validation output
    if not asset_crud.create_asset(new_asset):
        raise HTTPException(status_code=400, detail="Failed to create the asset")
    return new_asset


# -------------------------------
# Endpoint: List all assets / List all By Status
# -------------------------------
@asset_router.get("/list", response_model=List[asset_model.Asset])
def get_all(status: Optional[str] = "",current_user: User = Depends(get_current_user)):
    """
    Retrieve all assets, optionally filtered by status.
    Example: /asset/list?status=active
    """
    data = asset_crud.get_all_assets(status)
    new_li = []
    for row in list(data):
        x = asset_model.Asset(**row)  # Convert dict to Asset model
        new_li.append(x)
    return new_li


# -------------------------------
# Endpoint: Count all assets
# -------------------------------
@asset_router.get("/count")
def count_all(current_user: User = Depends(get_current_user)):
    """
    Return the total count of assets in the system.
    """
    data = asset_crud.get_all_assets()
    return {"detail": f"Count of records: {len(data)}"}


# -------------------------------
# Endpoint: Get asset by ID
# -------------------------------
@asset_router.get("/{id}", response_model=asset_model.Asset)
def get_by_id(id: int,current_user: User = Depends(get_current_user)):
    """
    Retrieve a single asset by its ID.
    """
    data = asset_crud.get_asset_by_id(id)
    if data:
        return asset_model.Asset(**data)
    raise HTTPException(status_code=404, detail="Asset id not found")


# -------------------------------
# Endpoint: Update asset by ID
# -------------------------------
@asset_router.put("/{id}", response_model=asset_model.Asset)
def update_by_id(id: int, new_asset: asset_model.Asset,current_user: User = Depends(get_current_user)):
    """
    Update an existing asset by ID.
    """
    if asset_crud.update_asset_by_id(id, new_asset):
        return new_asset
    raise HTTPException(status_code=400, detail="Unable to update asset")


# -------------------------------
# Endpoint: Patch asset status
# -------------------------------
@asset_router.patch("/{id}/status", response_model=asset_model.Asset)
def patch_by_id(id: int, status: str,current_user: User = Depends(get_current_user)):
    """
    Update only the status field of an asset by ID.
    """
    data = get_by_id(id)
    if data:
        data.asset_status = status
        return update_by_id(id, data)
    raise HTTPException(status_code=404, detail="ID not found")


# -------------------------------
# Endpoint: Delete asset by ID
# -------------------------------
@asset_router.delete("/{id}")
def delete_asset_id(id: int,current_user: User = Depends(get_current_user)):
    """
    Delete an asset by its ID.
    """
    if asset_crud.delete_asset_by_id(id):
        return {"detail": "Record deleted successfully"}
    raise HTTPException(status_code=404, detail="Asset Id Doesnt Exist")
