from fastapi import FastAPI, HTTPException, APIRouter,Depends
from typing import Optional
from ..models.vendor_model import VendorMaster, StatusValidate
from ..crud.vendor_crud import VendorCrud
from ..models.login_model import User
from ..auth.jwt_auth import get_current_user

# Initialize the VendorCrud instance to interact with the vendor database
vendor_reader = VendorCrud()

# Create the APIRouter instance for vendor-related routes with a prefix "/vendor"
vendor_router = APIRouter(prefix="/vendor")

# Route to create a new vendor record in the database
@vendor_router.post("/create")
def create_vendor(vendor: VendorMaster,current_user: User = Depends(get_current_user)):
    try:
        # Call the create_vendor method from VendorCrud to insert the vendor record
        return vendor_reader.create_vendor(vendor)
    except Exception as e:
        # Log the error and raise a 404 HTTPException if something goes wrong
        print(e)
        raise HTTPException(status_code=404, detail="Not Found")

# Route to retrieve a list of all vendors, or filter by status
@vendor_router.get("/list")
def get_all_vendor(status: Optional[str] = "ALL",current_user: User = Depends(get_current_user)):
    try:
        # Call the get_all_vendor method from VendorCrud to fetch vendor records based on status
        return vendor_reader.get_all_vendor(status)
    except Exception:
        # If an error occurs, raise a 404 HTTPException with a message
        raise HTTPException(status_code=404, detail="Not Found")

# Route to retrieve a specific vendor record by its ID
@vendor_router.get("/{id}")
def get_vendor_by_id(id: int,current_user: User = Depends(get_current_user)):
    try:
        # Call the get_vendor_by_id method from VendorCrud to fetch the vendor record by ID
        return vendor_reader.get_vendor_by_id(id)
    except Exception:
        # If an error occurs, raise a 404 HTTPException with a message
        raise HTTPException(status_code=404, detail="Not Found")

# Route to update a vendor record by its ID
@vendor_router.put("/{id}")
def update_vendor(id: int, data: VendorMaster,current_user: User = Depends(get_current_user)):
    try:
        # Call the update_vendor method from VendorCrud to update the vendor record
        return vendor_reader.update_vendor(id, data)
    except Exception as e:
        # Log the error and raise a 404 HTTPException if something goes wrong
        print(str(e))
        raise HTTPException(status_code=404, detail="Not Found")

# Route to update the status of a vendor record by its ID
@vendor_router.patch("/{id}/status")
def update_vendor_status(id: int, status: StatusValidate,current_user: User = Depends(get_current_user)):
    try:
        # Print the status for debugging purposes
        print(status)
        # Call the update_vendor_status method from VendorCrud to update the vendor record status
        return vendor_reader.update_vendor_status(id, status.status)
    except Exception:
        # If an error occurs, raise a 404 HTTPException with a message
        raise HTTPException(status_code=404, detail="Not Found")

# Route to delete a vendor record by its ID
@vendor_router.delete("/{id}")
def delete_vendor(id: int,current_user: User = Depends(get_current_user)):
    try:
        # Call the delete_vendor method from VendorCrud to delete the vendor record by ID
        return vendor_reader.delete_vendor(id)
    except Exception:
        # If an error occurs, raise a 404 HTTPException with a message
        raise HTTPException(status_code=404, detail="Not Found")

# Route to search for a vendor record by a specific keyword (e.g., 'vendor_name') and value
@vendor_router.get("/search/keyword")
def get_vendor_by_keyword(keyword: str, value: str,current_user: User = Depends(get_current_user)):
    try:
        # Call the get_vendor_by_keyword method from VendorCrud to search vendor records
        return vendor_reader.get_vendor_by_keyword(keyword, value)
    except Exception as e:
        # Log the error and raise a 404 HTTPException if something goes wrong
        print(e)
        raise HTTPException(status_code=404, detail="Not Found")

# Route to retrieve the count of all vendor records
@vendor_router.get("/list/count")
def get_count(current_user: User = Depends(get_current_user)):
    try:
        # Call the get_all_vendor_count method from VendorCrud to get the vendor count
        return vendor_reader.get_all_vendor_count()
    except Exception as e:
        # Log the error and raise a 404 HTTPException if something goes wrong
        print(e)
        raise HTTPException(status_code=404, detail="Not Found")
