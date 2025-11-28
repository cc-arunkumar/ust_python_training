from fastapi import FastAPI,APIRouter,Depends
from src.crud.maintainence_crud import get_all,get_by_id,create_asset,update_by_id,delete_by_id,update_by_status,get_by_search,get_by_count,get_assets_by_status
from ..models.maintainence_model import Maintenence
from ..auth.jwt_auth import get_current_user,User

# Create router for maintenance-related APIs with prefix "/maintenance"
maintainence_router=APIRouter(prefix="/maintenance")

# Search maintenance records by field type and keyword
@maintainence_router.get("/search")
def get_search(field_type:str="",keyword:str="",current_user: User = Depends(get_current_user)):
    return get_by_search(field_type,keyword)

# Get count of all maintenance records
@maintainence_router.get("/count")
def get_count(current_user: User = Depends(get_current_user)):
    return get_by_count()

# Get maintenance records filtered by status
@maintainence_router.get("/list")
def get_assets_status(status:str="",current_user: User = Depends(get_current_user)):
    return get_assets_by_status(status)

# Get all maintenance records
@maintainence_router.get("/list")
def get_assets(current_user: User = Depends(get_current_user)):
    return get_all()

# Get maintenance record by ID
@maintainence_router.get("/{id}")
def get_id(id:int,current_user: User = Depends(get_current_user)):
    return get_by_id(id)

# Create a new maintenance record
@maintainence_router.post("/create")
def create_assets(asset:Maintenence,current_user: User = Depends(get_current_user)):
    return create_asset(asset)

# Update maintenance record by ID
@maintainence_router.put("/{id}")
def update_id(id:int,asset:Maintenence,current_user: User = Depends(get_current_user)):
    return update_by_id(id,asset)

# Update maintenance status by ID
@maintainence_router.patch("/{id}")
def update_status(id:int,status:str="",current_user: User = Depends(get_current_user)):
    return update_by_status(id,status)

# Delete maintenance record by ID
@maintainence_router.delete("/{id}")
def delete_id(id:int,current_user: User = Depends(get_current_user)):
    return delete_by_id(id)
