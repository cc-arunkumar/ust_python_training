from fastapi import APIRouter, HTTPException, FastAPI
from app.auth import create_access_token  # Import the JWT token creation function
from app.models import TrainingRequest, TrainingRequestCreate  # Import Pydantic models for requests and responses
from app.crud import create_training_request, read_all_training_requests, read_training_request_by_id, update_training_request_by_id, delete_training_request_by_id  # Import CRUD operations

# Initialize FastAPI app with a title for the API
app = FastAPI(title="UST Employee Training Request Management")

# Route for user login (authentication)
@app.post("/auth/login")
def login(username: str, password: str):
    """
    Authenticates a user based on username and password.
    :param username: The username provided by the user.
    :param password: The password provided by the user.
    :return: A success message if login is successful, or an error if credentials are invalid.
    """
    if username == "admin" and password == "password123":
        return {"message": "Login successful"}  # Return success message if credentials are correct
    else:
        # Raise an HTTPException if credentials are invalid
        raise HTTPException(status_code=401, detail="Invalid credentials")

# Route for creating a new training request
@app.post("/", response_model=TrainingRequest)
def create_request(request: TrainingRequestCreate):
    """
    Creates a new training request.
    :param request: The training request data to be created.
    :return: The created training request object.
    """
    return create_training_request(request)  # Calls the CRUD function to create the request

# Route for getting all training requests
@app.get("/", response_model=list[TrainingRequest])
def get_all_requests():
    """
    Fetches all training requests.
    :return: A list of all training requests.
    """
    return read_all_training_requests()  # Calls the CRUD function to fetch all requests

# Route for getting a specific training request by ID
@app.get("/{id}", response_model=TrainingRequest)
def get_request_by_id(id: int):
    """
    Fetches a training request by its ID.
    :param id: The ID of the training request to retrieve.
    :return: The training request object if found.
    :raises HTTPException: If the training request is not found, raises a 404 error.
    """
    request = read_training_request_by_id(id)  # Calls the CRUD function to get a specific request
    if request:
        return request  # Return the found request
    # Raise a 404 error if the request is not found
    raise HTTPException(status_code=404, detail="Training request not found")

# Route for updating a training request by ID (full update)
@app.put("/{id}", response_model=TrainingRequest)
def update_request(id: int, request: TrainingRequestCreate):
    """
    Updates a training request by its ID.
    :param id: The ID of the training request to update.
    :param request: The updated data for the training request.
    :return: The updated training request.
    :raises HTTPException: If the training request is not found, raises a 404 error.
    """
    updated_request = update_training_request_by_id(id, request)  # Calls the CRUD function to update the request
    if updated_request:
        return updated_request  # Return the updated request
    # Raise a 404 error if the request is not found
    raise HTTPException(status_code=404, detail="Training request not found")

# Route for partially updating a training request by ID (PATCH request)
@app.patch("/{id}", response_model=TrainingRequest)
def partial_update_request(id: int, request: TrainingRequestCreate):
    """
    Partially updates a training request by its ID.
    :param id: The ID of the training request to update.
    :param request: The updated data for the training request.
    :return: The updated training request.
    :raises HTTPException: If the training request is not found, raises a 404 error.
    """
    updated_request = update_training_request_by_id(id, request)  # Calls the CRUD function for partial update
    if updated_request:
        return updated_request  # Return the updated request
    # Raise a 404 error if the request is not found
    raise HTTPException(status_code=404, detail="Training request not found")

# Route for deleting a training request by ID
@app.delete("/{id}")
def delete_request(id: int):
    """
    Deletes a training request by its ID.
    :param id: The ID of the training request to delete.
    :return: A success message if deletion is successful.
    :raises HTTPException: If the training request is not found, raises a 404 error.
    """
    if delete_training_request_by_id(id):  # Calls the CRUD function to delete the request
        return {"message": "Training request deleted successfully."}  # Return success message
    # Raise a 404 error if the request is not found
    raise HTTPException(status_code=404, detail="Training request not found")
