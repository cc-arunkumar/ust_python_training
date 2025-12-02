from fastapi import FastAPI, Depends, HTTPException, status
from typing import List
from auth import verify_token, router  # Assuming `verify_token` handles authentication
from models import TrainingRequest, TrainingRequestUpdate, TrainingRequestRead  # These are Pydantic models
from crud import (create_training_request, get_all_training_requests, 
                  get_training_request_by_id, update_training_request,
                  patch_training_request, delete_training_request)

# Create FastAPI instance
app = FastAPI(title="UST Employee Training Request API")

# Include the router from the 'auth' module (which may include routes for authentication, etc.)
app.include_router(router)

# Endpoint to create a new training request
@app.post("/training-requests", response_model=TrainingRequestRead)
def create_request(request: TrainingRequest):
    """
    Create a new training request.
    - request: The training request data to be created.
    - Returns the created request as a response.
    """
    return create_training_request(request)

# Endpoint to get all training requests
@app.get("/training-requests", response_model=List[TrainingRequestRead])
def get_all_requests():
    """
    Fetch all training requests.
    - Returns a list of all training requests.
    """
    return get_all_training_requests()

# Endpoint to get a specific training request by ID
@app.get("/training-requests/{request_id}", response_model=TrainingRequestRead)
def get_request(request_id: int):
    """
    Fetch a specific training request by ID.
    - request_id: The ID of the training request.
    - Returns the requested training request.
    """
    return get_training_request_by_id(request_id)

# Endpoint to update a training request by ID
@app.put("/training-requests/{request_id}", response_model=TrainingRequestRead)
def update_request(request_id: int, request: TrainingRequest):
    """
    Update an existing training request.
    - request_id: The ID of the training request to update.
    - request: The updated request data.
    - Returns the updated request.
    """
    return update_training_request(request_id, request)

# Endpoint to partially update a training request (only fields provided in the request)
@app.patch("/training-requests/{request_id}", response_model=TrainingRequestRead)
def patch_request(request_id: int, request: TrainingRequestUpdate):
    """
    Partially update a training request (using PATCH).
    - request_id: The ID of the training request to update.
    - request: The partial data to update.
    - Returns the partially updated request.
    """
    return patch_training_request(request_id, request)

# Endpoint to delete a training request by ID
@app.delete("/training-requests/{request_id}")
def delete_request(request_id: int):
    """
    Delete a specific training request by ID.
    - request_id: The ID of the training request to delete.
    - Returns a success message if the deletion is successful.
    """
    return delete_training_request(request_id)
