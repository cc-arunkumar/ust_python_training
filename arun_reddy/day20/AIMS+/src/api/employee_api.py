from fastapi import FastAPI,APIRouter,Depends
from src.crud.employee_crud import get_all,get_by_id,create_asset,update_by_id,delete_by_id,update_by_status,get_by_search,get_by_count,get_assets_by_status
from src.models.employee_model import Employee
from ..auth.jwt_auth import get_current_user,User


# Create router for employee-related APIs with prefix "/employee"
employee_router=APIRouter(prefix="/employee")

# Search employees by field type and keyword
@employee_router.get("/search")
def get_search(field_type:str="",keyword:str="",current_user: User = Depends(get_current_user)):
    return get_by_search(field_type,keyword)

# Get count of all employees
@employee_router.get("/count")
def get_count(current_user: User = Depends(get_current_user)):
    return get_by_count()

# Get employees filtered by status
@employee_router.get("/list")
def get_assets_status(status:str="",current_user: User = Depends(get_current_user)):
    return get_assets_by_status(status)

# Get all employees
@employee_router.get("/list")
def get_assets(current_user: User = Depends(get_current_user)):
    return get_all()

# Get employee by ID
@employee_router.get("/{id}")
def get_id(id:int,current_user: User = Depends(get_current_user)):
    return get_by_id(id)

# Create a new employee record
@employee_router.post("/create")
def create_assets(asset:Employee,current_user: User = Depends(get_current_user)):
    return create_asset(asset)

# Update employee record by ID
@employee_router.put("/{id}")
def update_id(id:int,asset:Employee,current_user: User = Depends(get_current_user)):
    return update_by_id(id,asset)

# Update employee status by ID
@employee_router.patch("/{id}")
def update_status(id:int,status:str="",current_user: User = Depends(get_current_user)):
    return update_by_status(id,status)

# Delete employee record by ID
@employee_router.delete("/{id}")
def delete_id(id:int,current_user: User = Depends(get_current_user)):
    return delete_by_id(id)
