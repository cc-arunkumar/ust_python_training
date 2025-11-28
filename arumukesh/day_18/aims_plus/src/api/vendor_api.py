from fastapi import Depends, APIRouter, HTTPException
from src.model.model_vendor_master import VendorMaster
from src.auth.jwt_authentication import get_current_user, User
from src.crud.vendor_crud import (
    create_vendor,
    get_all,
    get_by_id,
    update,
    delete,
    get_by_stat,
    get_count,
    find
)

# Router configuration for Vendor module
router = APIRouter(prefix="/vendors", tags=["Vendors"])


@router.post("/")
def create(data: VendorMaster, current_user: User = Depends(get_current_user)):
    """
    Create a new vendor record.
    Requires JWT authentication.
    """
    return create_vendor(data)


@router.get("/")
def list_all(current_user: User = Depends(get_current_user)):
    """
    Retrieve all vendor records.
    """
    return get_all()


@router.get("/status/{status}")
def filter_by_status(status: str, current_user: User = Depends(get_current_user)):
    """
    Filter vendors based on active status.
    Example: /vendors/status/Active
    """
    return get_by_stat(status)


@router.get("/count")
def count_data(current_user: User = Depends(get_current_user)):
    """
    Get the total vendor count.
    Useful for UI dashboards and analytics.
    """
    return get_count()


@router.get("/search/{column}/{value}")
def search(column: str, value: str, current_user: User = Depends(get_current_user)):
    """
    Search vendors using a column and value.
    Example: /vendors/search/vendor_name/Lenovo
    """
    return find(column, value)


@router.get("/{vendor_id}")
def get(vendor_id: int, current_user: User = Depends(get_current_user)):
    """
    Retrieve a vendor by ID.
    Raises a 404 error if vendor does not exist.
    """
    result = get_by_id(vendor_id)
    if not result:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return result


@router.put("/{vendor_id}")
def modify(vendor_id: int, data: VendorMaster, current_user: User = Depends(get_current_user)):
    """
    Update vendor details using PUT (full update).
    """
    return update(vendor_id, data)


@router.delete("/{vendor_id}")
def remove(vendor_id: int, current_user: User = Depends(get_current_user)):
    """
    Delete vendor record by vendor ID.
    """
    return delete(vendor_id)
