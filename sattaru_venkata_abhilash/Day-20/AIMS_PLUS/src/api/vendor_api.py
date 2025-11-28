from fastapi import FastAPI, HTTPException, status, APIRouter, Depends
from typing import List, Optional
from src.models.vendor_model import VendorModel  # Importing VendorModel for vendor data validation
from src.crud.vendor_crud import get_all_vendors, get_vendor_by_id, insert_vendor, update_vendor_by_id, delete_vendor, search_vendor  # Importing CRUD functions for vendor operations
from src.auth.auth_jwt_token import User, get_curr_user  # Importing JWT authentication logic

# Initialize the FastAPI app and create an APIRouter for vendor-related routes
vendor_router = APIRouter(prefix="/vendors")

# Get the list of vendors with an optional status filter (Secured with JWT)
@vendor_router.get("/list", response_model=List[VendorModel])
def get_vendors(status_filter: Optional[str] = "", current_user: User = Depends(get_curr_user)):  # Secure with JWT
    """
    Endpoint to fetch a list of all vendors, with an optional status filter (active/inactive).
    This route requires the user to be authenticated via JWT.
    """
    try:
        rows = get_all_vendors(status_filter)  # Fetch vendors from DB, filtered by status if provided
        vendor_list = [VendorModel(**row) for row in rows]  # Convert database rows to Pydantic VendorModel instances
        return vendor_list  # Return the list of vendors
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching vendors: {e}")  # Handle any errors

# Search vendors by a specific field (e.g., vendor_name, contact_phone) (Secured with JWT)
@vendor_router.get("/search")
def search_by_word(field_type: str, keyword: str, current_user: User = Depends(get_curr_user)):  # Secure with JWT
    """
    Endpoint to search vendors based on a field (e.g., vendor_name, contact_phone) and a keyword.
    This route requires the user to be authenticated via JWT.
    """
    try:
        data = search_vendor(field_type, keyword)  # Perform search operation in DB
        return data  # Return the search results
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to search vendors: {e}")  # Handle search errors

# Get count of all vendors (Secured with JWT)
@vendor_router.get("/count")
def count_vendors(current_user: User = Depends(get_curr_user)):  # Secure with JWT
    """
    Endpoint to get the total count of vendors. Only accessible by authenticated users.
    """
    try:
        data = get_all_vendors()  # Get all vendors from DB
        return {"count": len(data)} if data else {"count": 0}  # Return the vendor count, or 0 if none are found
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error counting vendors: {str(e)}")  # Handle errors

# Get a vendor by vendor_id (Secured with JWT)
@vendor_router.get("/{vendor_id}", response_model=VendorModel)
def get_vendor_by_id_route(vendor_id: int, current_user: User = Depends(get_curr_user)):  # Secure with JWT
    """
    Endpoint to fetch a specific vendor by its ID. Only accessible by authenticated users.
    """
    try:
        row = get_vendor_by_id(vendor_id)  # Fetch vendor by ID from the DB
        if not row:
            raise HTTPException(status_code=404, detail="Vendor not found")  # Raise error if vendor not found
        return VendorModel(**row)  # Convert database row to Pydantic model and return it
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error fetching vendor")  # Handle errors during fetching

# Create a new vendor (No authentication needed for this one, can be adjusted)
@vendor_router.post("/create", response_model=VendorModel)
def create_vendor(new_vendor: VendorModel):
    """
    Endpoint to create a new vendor. This route doesn't require authentication, but can be adjusted if needed.
    """
    try:
        insert_vendor(new_vendor)  # Insert the new vendor into the database
        return new_vendor  # Return the created vendor
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error: {e}")  # Handle creation errors

# Update an existing vendor by vendor_id (Secured with JWT)
@vendor_router.put("/{vendor_id}", response_model=VendorModel)
def update_vendor(vendor_id: int, update_vendor: VendorModel, current_user: User = Depends(get_curr_user)):  # Secure with JWT
    """
    Endpoint to update an existing vendor by its ID. Only accessible by authenticated users.
    """
    try:
        update_vendor_by_id(vendor_id, update_vendor)  # Update the vendor in the database
        return update_vendor  # Return the updated vendor
    except HTTPException as e:
        raise e  # Raise any HTTP exceptions directly
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Update failed: {str(e)}")  # Handle errors during update

# Delete a vendor by vendor_id (Secured with JWT)
@vendor_router.delete("/{vendor_id}")
def delete_vendor_by_id(vendor_id: int, current_user: User = Depends(get_curr_user)):  # Secure with JWT
    """
    Endpoint to delete a vendor by its ID. Only accessible by authenticated users.
    """
    try:
        if delete_vendor(vendor_id):  # Try deleting the vendor from the database
            return {"detail": "Vendor deleted successfully"}  # Return success message if vendor is deleted
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting vendor: {str(e)}")  # Handle deletion errors

# Update vendor status (Secured with JWT)
@vendor_router.patch("/{vendor_id}/status")
def update_vendor_status(vendor_id: int, status: str, current_user: User = Depends(get_curr_user)):  # Secure with JWT
    """
    Endpoint to update the status of a vendor (e.g., active/inactive) by its ID.
    This route requires the user to be authenticated via JWT.
    """
    try:
        data = get_vendor_by_id(vendor_id)  # Fetch the vendor by ID
        if not data:
            raise HTTPException(status_code=404, detail="Vendor not found")  # Raise error if vendor not found
        
        data['active_status'] = status  # Update the vendor's status field
        update_vendor_by_id(vendor_id, VendorModel(**data))  # Save the updated vendor in the database
        
        return {"message": "Vendor status updated successfully", "vendor_id": vendor_id, "new_status": status}  # Return success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating vendor status: {str(e)}")  # Handle errors during status update
