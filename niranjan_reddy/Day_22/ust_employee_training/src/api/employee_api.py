from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from src.models.training_request_model import TrainingRequest
from src.crud.employee_crud import get_data, get_data_by_id, update_db, insert_to_db, delete_row
from src.auth.jwt_auth import User,get_curr_user

# Initialize APIRouter with prefix for the routes
employee_router = APIRouter(prefix="/api/v1/training-requests")

# Endpoint to fetch all training request records
@employee_router.get("/", response_model=List[TrainingRequest])
def get_all_data(current_user: User = Depends(get_curr_user)):
    try:
        # Retrieve all records from the database
        rows = get_data()
        emp_li = []
        for row in rows:
            emp_li.append(TrainingRequest(**row))  # Convert each row to TrainingRequest model
        return emp_li
    except Exception as e:
        # If there is an error, raise an HTTP exception with a 400 Bad Request status
        raise HTTPException(status_code=400, detail=f"{e}")
    
# Endpoint to fetch a training request by its ID
@employee_router.get("/{id}", response_model=TrainingRequest)
def get_by_id(id: int,current_user: User = Depends(get_curr_user)):
    try:
        # Retrieve the record by ID
        row = get_data_by_id(id)
        if not row:
            # If no record is found, raise a 404 Not Found error
            raise HTTPException(status_code=404, detail="Asset not exists")
        return TrainingRequest(**row)  # Convert to TrainingRequest model and return
    except Exception as e:
        # Raise a 400 Bad Request error if something goes wrong
        raise HTTPException(status_code=400, detail="ID not found")
    
# Endpoint to insert a new training request record
@employee_router.post("/", response_model=TrainingRequest)
def insert_data(add_data: TrainingRequest,current_user: User = Depends(get_curr_user)):
    try:
        # Insert the new training request into the database
        insert_to_db(add_data)
        return add_data  # Return the inserted data
    except Exception as e:
        # If there is an error, raise a 404 Not Found error
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error: {e}")

# Endpoint to update a training request record by ID
@employee_router.put("/{id}")
def update_data(id: int, request_data: TrainingRequest,current_user: User = Depends(get_curr_user)):
    try:
        # Perform the update in the database
        update_db(id, request_data)
        return {"message": "Employee updated successfully"}  # Return success message
    except Exception as e:
        # If any other error occurs, raise a 400 Bad Request error
        raise HTTPException(status_code=400, detail=f"Update failed: {str(e)}")

# Endpoint to perform a partial update (PATCH) on a training request by ID
@employee_router.patch("/{id}", response_model=TrainingRequest)
def update_row(id: int, patch_data: TrainingRequest,current_user: User = Depends(get_curr_user)):
    try:
        # Get the existing record first
        existing_data = get_data_by_id(id)
        
        if not existing_data:
            # If no record is found for partial update, raise 404 error
            raise HTTPException(status_code=404, detail="Training request not found for partial update")
        
        # Update only the fields that are provided in patch_data (non-None values)
        if patch_data.employee_id is not None:
            existing_data["employee_id"] = patch_data.employee_id
        if patch_data.employee_name is not None:
            existing_data["employee_name"] = patch_data.employee_name
        if patch_data.training_title is not None:
            existing_data["training_title"] = patch_data.training_title
        if patch_data.training_description is not None:
            existing_data["training_description"] = patch_data.training_description
        if patch_data.requested_date is not None:
            existing_data["requested_date"] = patch_data.requested_date
        if patch_data.status is not None:
            existing_data["status"] = patch_data.status
        if patch_data.manager_id is not None:
            existing_data["manager_id"] = patch_data.manager_id
        
        # Perform the update in the database
        updated_row = update_db(id, existing_data)
        return TrainingRequest(**updated_row)  # Return updated data as TrainingRequest model
    
    except Exception as e:
        # If any error occurs, raise a 400 Bad Request error
        raise HTTPException(status_code=400, detail=f"Partial update failed: {str(e)}")

# Endpoint to delete a training request by ID
@employee_router.delete("/{id}")
def deleted_data(id: int,current_user: User = Depends(get_curr_user)):
    try:
        # Attempt to delete the record by its ID
        if delete_row(id):
            return {"detail": "Employee deleted successfully"}  # Return success message
    except Exception as e:
        # If there is an error, raise an HTTP exception with a 400 Bad Request status
        raise HTTPException(status_code=400, detail=f"Error deleting asset: {str(e)}")
