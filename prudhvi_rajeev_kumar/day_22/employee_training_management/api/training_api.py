from fastapi import APIRouter, HTTPException, Depends
from models.training_model import TrainingRequest
from crud.training_crud import(
    create_request,
    get_all_requests,
    get_req_by_id,
    update_requests,
    delete_request
)
from authentication.jwt import get_current_user, User
router = APIRouter(prefix="/requests", tags=["TrainingRequests"])

@router.post("/create")
def create_new_request(req : TrainingRequest, current_user: User = Depends(get_current_user)):
    id = create_request(req)
    return {"message" : "Request created successfully with ", "id" : id}

@router.get("/list")
def list_requests(current_user: User = Depends(get_current_user)):
    return get_all_requests()

@router.get("/{id}")
def get_request_by_id(id: int, current_user: User = Depends(get_current_user)):
    request = get_req_by_id(id)
    if not request:
        raise HTTPException(status_code=404, detail="Request not found.")
    return request

@router.put("/{id}")
def update_record(id: int, new_req: TrainingRequest, current_user: User = Depends(get_current_user)):
    updated = update_requests(id, new_req)
    if updated == 0:
        raise HTTPException(status_code=404, detail="Request not found")
    return {"message": "Request updated successfully"}

@router.delete("/{id}")
def delete_record(id : int, current_user: User = Depends(get_current_user)):
    deleted = delete_request(id)
    if deleted == 0:
        raise HTTPException(status_code=404, detail="request not found")
    return {"message" : "Request deleted successfully."}

