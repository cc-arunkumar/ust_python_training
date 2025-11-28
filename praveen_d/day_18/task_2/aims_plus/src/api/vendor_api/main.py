import sys
import os

# Add the 'src' directory to sys.path dynamically
# Adjusting the path to point one level higher
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

from fastapi import FastAPI, HTTPException,APIRouter,Depends
from typing import List 
from src.crud.vendor_crud import (create_vendor, get_all_vendors,get_vendors_by_status,get_vendor_by_id,update_vendor, update_vendor_status,delete_vendor,search_vendors_by_keyword,get_vendor_count) 
from models.vendor_model import Vendor  # Import the Vendor Pydantic model
from src.auth.login_function import get_current_user,User

vendor_router =  APIRouter(prefix="/vendor")

# 1. POST /vendors/create - Create a new vendor
@vendor_router.post("/vendors/create", response_model=Vendor)
def create_vendor_api(vendor: Vendor,current_user: User = Depends(get_current_user)):
    result = create_vendor(vendor)
    return result

# 2. GET /vendors/list - Get all vendors
@vendor_router.get("/vendors/list", response_model=List[Vendor])
def get_vendors_api(current_user: User = Depends(get_current_user)):
    vendors = get_all_vendors()
    return vendors

# 3. GET /vendors/list?status= - Get vendors by status
@vendor_router.get("/vendors/list", response_model=List[Vendor])
def get_vendors_by_status_api(status: str,current_user: User = Depends(get_current_user)):
    vendors = get_vendors_by_status(status)
    return vendors

# 4. GET /vendors/{id} - Get vendor by ID
@vendor_router.get("/vendors/{id}", response_model=Vendor)
def get_vendor_by_id_api(id: int,current_user: User = Depends(get_current_user)):
    vendor = get_vendor_by_id(id)
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return vendor

# 5. PUT /vendors/{id} - Update vendor by ID
@vendor_router.put("/vendors/{id}", response_model=Vendor)
def update_vendor_api(id: int, vendor: Vendor,current_user: User = Depends(get_current_user)):
    vendor_data = vendor
    result = update_vendor(id, vendor_data)
    return result

# 6. PATCH /vendors/{id}/status - Update vendor status by ID
@vendor_router.patch("/vendors/{id}/status")
def update_vendor_status_api(id: int, status: str,current_user: User = Depends(get_current_user)):
    result = update_vendor_status(id, status)
    return result

# 7. DELETE /vendors/{id} - Delete vendor by ID
@vendor_router.delete("/vendors/{id}")
def delete_vendor_api(id: int,current_user: User = Depends(get_current_user)):
    result = delete_vendor(id)
    return result

# 8. GET /vendors/search?keyword= - Search vendors by keyword
@vendor_router.get("/vendors/search", response_model=List[Vendor])
def search_vendors_api(keyword: str,current_user: User = Depends(get_current_user)):
    vendors = search_vendors_by_keyword(keyword)
    return vendors

# 9. GET /vendors/count - Get the count of vendors
@vendor_router.get("/vendors/count")
def count_vendors_api(current_user: User = Depends(get_current_user)):
    count = get_vendor_count()
    return {"count": count}
