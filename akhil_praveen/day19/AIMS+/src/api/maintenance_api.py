from fastapi import FastAPI, HTTPException, APIRouter,Depends
from typing import Optional
from ..models.maintenance_model import MaintenanceLog, StatusValidate
from ..crud.maintenance_crud import MaintenanceCrud
from ..models.login_model import User
from ..auth.jwt_auth import get_current_user

# Initialize the MaintenanceCrud instance to interact with the maintenance database
maintenance_reader = MaintenanceCrud()

# Create the APIRouter instance for maintenance-related routes with a prefix "/maintenance"
maintenance_router = APIRouter(prefix="/maintenance")

# Route to create a new maintenance record in the database
@maintenance_router.post("/create")
def create_maintenance(maintenance: MaintenanceLog,current_user: User = Depends(get_current_user)):
    try:
        # Call the create_maintenance method from MaintenanceCrud to insert the maintenance record
        return maintenance_reader.create_maintenance(maintenance)
    except Exception as e:
        # Log the error and raise a 404 HTTPException if something goes wrong
        print(e)
        raise HTTPException(status_code=404, detail="Not Found")

# Route to retrieve a list of all maintenance records, or filter by status
@maintenance_router.get("/list")
def get_all_maintenance(status: Optional[str] = "ALL",current_user: User = Depends(get_current_user)):
    try:
        # Call the get_all_maintenance method from MaintenanceCrud to fetch maintenance records based on status
        return maintenance_reader.get_all_maintenance(status)
    except Exception:
        # If an error occurs, raise a 404 HTTPException with a message
        raise HTTPException(status_code=404, detail="Not Found")

# Route to retrieve a specific maintenance record by its ID
@maintenance_router.get("/{id}")
def get_maintenance_by_id(id: int,current_user: User = Depends(get_current_user)):
    try:
        # Call the get_maintenance_by_id method from MaintenanceCrud to fetch the maintenance record by ID
        return maintenance_reader.get_maintenance_by_id(id)
    except Exception:
        # If an error occurs, raise a 404 HTTPException with a message
        raise HTTPException(status_code=404, detail="Not Found")

# Route to update a maintenance record by its ID
@maintenance_router.put("/{id}")
def update_maintenance(id: int, data: MaintenanceLog,current_user: User = Depends(get_current_user)):
    try:
        # Call the update_maintenance method from MaintenanceCrud to update the maintenance record
        return maintenance_reader.update_maintenance(id, data)
    except Exception as e:
        # Log the error and raise a 404 HTTPException if something goes wrong
        print(str(e))
        raise HTTPException(status_code=404, detail="Not Found")

# Route to update the status of a maintenance record by its ID
@maintenance_router.patch("/{id}/status")
def update_maintenance_status(id: int, status: StatusValidate,current_user: User = Depends(get_current_user)):
    try:
        # Print the status for debugging purposes
        print(status)
        # Call the update_maintenance_status method from MaintenanceCrud to update the maintenance record status
        return maintenance_reader.update_maintenance_status(id, status.status)
    except Exception:
        # If an error occurs, raise a 404 HTTPException with a message
        raise HTTPException(status_code=404, detail="Not Found")

# Route to delete a maintenance record by its ID
@maintenance_router.delete("/{id}")
def delete_maintenance(id: int,current_user: User = Depends(get_current_user)):
    try:
        # Call the delete_maintenance method from MaintenanceCrud to delete the maintenance record by ID
        return maintenance_reader.delete_maintenance(id)
    except Exception:
        # If an error occurs, raise a 404 HTTPException with a message
        raise HTTPException(status_code=404, detail="Not Found")

# Route to search for a maintenance record by a specific keyword (e.g., 'asset_tag') and value
@maintenance_router.get("/search/keyword")
def get_maintenance_by_keyword(keyword: str, value: str,current_user: User = Depends(get_current_user)):
    try:
        # Call the get_maintenance_by_keyword method from MaintenanceCrud to search maintenance records
        return maintenance_reader.get_maintenance_by_keyword(keyword, value)
    except Exception as e:
        # Log the error and raise a 404 HTTPException if something goes wrong
        print(e)
        raise HTTPException(status_code=404, detail="Not Found")

# Route to retrieve the count of all maintenance records
@maintenance_router.get("/list/count")
def get_count(current_user: User = Depends(get_current_user)):
    try:
        # Call the get_all_maintenance_count method from MaintenanceCrud to get the maintenance count
        return maintenance_reader.get_all_maintenance_count()
    except Exception as e:
        # Log the error and raise a 404 HTTPException if something goes wrong
        print(e)
        raise HTTPException(status_code=404, detail="Not Found")
