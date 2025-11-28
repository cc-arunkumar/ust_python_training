from fastapi import FastAPI, HTTPException, status, APIRouter, Depends
from typing import List, Optional
from src.models.maintenance_model import MaintenanceLogModel  # Importing MaintenanceLog model for validation
from src.crud.maintenance_crud import get_all, get_by_id, insert_maintenance_log, update_maintenance_log_by_id, delete_maintenance_log, search_maintenance_log  # Importing CRUD operations for maintenance logs
from src.auth.auth_jwt_token import User, get_curr_user  # Importing JWT authentication logic

# Initialize the FastAPI app and create an APIRouter for maintenance-related routes
maintenance_router = APIRouter(prefix="/maintenance")

# Get all maintenance logs with an optional status filter (Secured with JWT)
@maintenance_router.get("/lists", response_model=List[MaintenanceLogModel])
def get_logs(status_filter: Optional[str] = "", current_user: User = Depends(get_curr_user)):  # Secure with JWT
    """
    Endpoint to fetch all maintenance logs, with an optional status filter. 
    This route requires the user to be authenticated via JWT.
    """
    try:
        rows = get_all(status_filter)  # Fetch all maintenance logs from the database, optionally filtered by status
        log_list = [MaintenanceLogModel(**row) for row in rows]  # Convert database rows into Pydantic models
        return log_list  # Return the list of maintenance logs
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching maintenance logs: {e}")  # Handle errors during log retrieval

# Search maintenance logs by a specific field type and keyword (Secured with JWT)
@maintenance_router.get("/search")
def search_logs(field_type: str, keyword: str, current_user: User = Depends(get_curr_user)):  # Secure with JWT
    """
    Endpoint to search maintenance logs based on a specific field (e.g., 'vendor_name', 'technician_name') and keyword.
    This route requires the user to be authenticated via JWT.
    """
    try:
        data = search_maintenance_log(field_type, keyword)  # Perform a search operation in the database
        return data  # Return the search results
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to search maintenance logs: {e}")  # Handle search errors

# Get count of all maintenance logs (Secured with JWT)
@maintenance_router.get("/count")
def count_logs(current_user: User = Depends(get_curr_user)):  # Secure with JWT
    """
    Endpoint to get the total count of maintenance logs.
    This route requires the user to be authenticated via JWT.
    """
    try:
        data = get_all()  # Fetch all maintenance logs from the database
        return {"count": len(data)} if data else {"count": 0}  # Return the count of maintenance logs, or 0 if none
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error counting maintenance logs: {str(e)}")  # Handle errors during counting

# Get a specific maintenance log by its log_id (Secured with JWT)
@maintenance_router.get("/{log_id}", response_model=MaintenanceLogModel)
def get_log_by_id(log_id: int, current_user: User = Depends(get_curr_user)):  # Secure with JWT
    """
    Endpoint to fetch a specific maintenance log by its ID.
    This route requires the user to be authenticated via JWT.
    """
    try:
        row = get_by_id(log_id)  # Fetch maintenance log by its ID
        if not row:
            raise HTTPException(status_code=404, detail="Maintenance log not found")  # Raise error if log not found
        return MaintenanceLogModel(**row)  # Convert the row to a Pydantic model and return it
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error fetching maintenance log")  # Handle errors during log retrieval

# Create a new maintenance log entry (No authentication needed for this one)
@maintenance_router.post("/create", response_model=MaintenanceLogModel)
def create_maintenance_log(new_log: MaintenanceLogModel):
    """
    Endpoint to create a new maintenance log entry.
    No authentication required for this route.
    """
    try:
        insert_maintenance_log(new_log)  # Insert the new maintenance log into the database
        return new_log  # Return the created maintenance log
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error: {e}")  # Handle errors during creation

# Update an existing maintenance log entry by log_id (Secured with JWT)
@maintenance_router.put("/{log_id}", response_model=MaintenanceLogModel)
def update_maintenance_log(log_id: int, updated_log: MaintenanceLogModel, current_user: User = Depends(get_curr_user)):  # Secure with JWT
    """
    Endpoint to update an existing maintenance log entry by its ID.
    This route requires the user to be authenticated via JWT.
    """
    try:
        update_maintenance_log_by_id(log_id, updated_log)  # Update the maintenance log in the database
        return updated_log  # Return the updated maintenance log
    except HTTPException as e:
        raise e  # Raise any HTTP exceptions that may occur
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Update failed: {str(e)}")  # Handle other errors during update

# Delete a maintenance log entry by log_id (Secured with JWT)
@maintenance_router.delete("/{log_id}")
def delete_maintenance_log_by_id(log_id: int, current_user: User = Depends(get_curr_user)):  # Secure with JWT
    """
    Endpoint to delete a maintenance log entry by its ID.
    This route requires the user to be authenticated via JWT.
    """
    try:
        if delete_maintenance_log(log_id):  # Attempt to delete the maintenance log
            return {"detail": "Maintenance log deleted successfully"}  # Return success message if deleted
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting maintenance log: {str(e)}")  # Handle errors during deletion

# Update the status of a maintenance log (Secured with JWT)
@maintenance_router.patch("/{log_id}/status")
def update_status(log_id: int, status: str, current_user: User = Depends(get_curr_user)):  # Secure with JWT
    """
    Endpoint to update the status of a maintenance log by its ID.
    This route requires the user to be authenticated via JWT.
    """
    try:
        data = get_by_id(log_id)  # Fetch the maintenance log by ID
        if not data:
            raise HTTPException(status_code=404, detail="Maintenance log not found")  # Raise error if log not found
        
        data['status'] = status  # Update the status field of the maintenance log
        update_maintenance_log_by_id(log_id, MaintenanceLogModel(**data))  # Save the updated log in the database
        
        return {"message": "Maintenance log status updated successfully", "log_id": log_id, "new_status": status}  # Return success message
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating maintenance log status: {str(e)}")  # Handle errors during status update
