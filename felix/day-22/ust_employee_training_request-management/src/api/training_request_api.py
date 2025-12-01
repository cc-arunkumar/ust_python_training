from fastapi import APIRouter, HTTPException, status, Depends
from ..crud.training_request_crud import TrainingRequestCrud
from ..models.training_request_model import TrainingRequest, RequestModel
from ..auth.jwt_auth import get_current_user
from ..models.user_model import User

# Create a router instance for training request-related endpoints
training_request_router = APIRouter(prefix="/training_request")

# Initialize CRUD operations handler for training requests
training_request = TrainingRequestCrud()

@training_request_router.get("")
def get_all_requests(user: User = Depends(get_current_user)):
    """
    Endpoint: GET /training_request
    - Retrieves all training requests.
    - Requires authentication via JWT.
    """
    try:
        return training_request.get_all_requests()
    except Exception as e:
        # Return HTTP 400 if any error occurs
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@training_request_router.get("/{emp_id}")
def get_request_by_id(emp_id, user: User = Depends(get_current_user)):
    """
    Endpoint: GET /training_request/{emp_id}
    - Retrieves a specific training request by employee ID.
    - Requires authentication via JWT.
    """
    try:
        return training_request.get_request_by_id(emp_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@training_request_router.post("")
def create_request(request: TrainingRequest, user: User = Depends(get_current_user)):
    """
    Endpoint: POST /training_request
    - Creates a new training request.
    - Accepts a TrainingRequest model in the request body.
    - Requires authentication via JWT.
    """
    try:
        return training_request.creaate_request(request)  # Note: Possible typo in 'creaate_request'
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@training_request_router.put("/{emp_id}")
def update_reuest(emp_id, request: TrainingRequest, user: User = Depends(get_current_user)):
    """
    Endpoint: PUT /training_request/{emp_id}
    - Updates an existing training request by employee ID.
    - Accepts a full TrainingRequest model in the request body.
    - Requires authentication via JWT.
    """
    try:
        return training_request.update_request(emp_id, request)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@training_request_router.patch("/{emp_id}")
def patch_reuest(emp_id, request: RequestModel, user: User = Depends(get_current_user)):
    """
    Endpoint: PATCH /training_request/{emp_id}
    - Partially updates a training request by employee ID.
    - Accepts a RequestModel with fields to update.
    - Requires authentication via JWT.
    """
    try:
        return training_request.patch_request(emp_id, request)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@training_request_router.delete("/{emp_id}")
def delete_request(emp_id, user: User = Depends(get_current_user)):
    """
    Endpoint: DELETE /training_request/{emp_id}
    - Deletes a training request by employee ID.
    - Requires authentication via JWT.
    """
    try:
        return training_request.delete_request(emp_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))