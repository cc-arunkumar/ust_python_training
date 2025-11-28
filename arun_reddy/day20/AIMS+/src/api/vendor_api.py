from fastapi import FastAPI,APIRouter,Depends
from src.crud.vendor_crud import get_all,get_by_id,create_asset,update_by_id,delete_by_id,update_by_status,get_by_search,get_by_count,get_assets_by_status
from src.models.vendor_model import Vendor
from ..auth.jwt_auth import get_current_user,User

# Create router for vendor-related APIs with prefix "/vendors"
vendor_router=APIRouter(prefix="/vendors")

# Search vendors by field type and keyword
@vendor_router.get("/search")
def get_search(field_type:str="",keyword:str="",current_user: User = Depends(get_current_user)):
    return get_by_search(field_type,keyword)

# Get count of all vendors
@vendor_router.get("/count")
def get_count(current_user: User = Depends(get_current_user)):
    return get_by_count()

# Get vendors filtered by status
@vendor_router.get("/list")
def get_assets_status(status:str="",current_user: User = Depends(get_current_user)):
    return get_assets_by_status(status)

# Get all vendors
@vendor_router.get("/list")
def get_assets(current_user: User = Depends(get_current_user)):
    return get_all()

# Get vendor by ID
@vendor_router.get("/{id}")
def get_id(id:int,current_user: User = Depends(get_current_user)):
    return get_by_id(id)

# Create a new vendor record
@vendor_router.post("/create")
def create_assets(asset:Vendor,current_user: User = Depends(get_current_user)):
    return create_asset(asset)

# Update vendor record by ID
@vendor_router.put("/{id}")
def update_id(id:int,asset:Vendor,current_user: User = Depends(get_current_user)):
    return update_by_id(id,asset)

# Update vendor status by ID
@vendor_router.patch("/{id}")
def update_status(id:int,status:str="",current_user: User = Depends(get_current_user)):
    return update_by_status(id,status)

# Delete vendor record by ID
@vendor_router.delete("/{id}")
def delete_id(id:int,current_user: User = Depends(get_current_user)):
    return delete_by_id(id)
