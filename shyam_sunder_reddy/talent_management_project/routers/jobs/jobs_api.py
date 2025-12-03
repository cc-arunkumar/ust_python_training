from fastapi import APIRouter, Depends, HTTPException
from typing import Optional, List,Union
from models import Job, ResourceRequest
from routers.jobs import jobs_crud
from utils.security import get_current_user

jobs_router = APIRouter(prefix="/jobs")

@jobs_router.get("/", response_model=List[dict])
async def get_all_jobs(location: Optional[str] = None, current_user=Depends(get_current_user)):
    return await jobs_crud.get_jobs(location, current_user)

@jobs_router.post("/create")
async def create_new_job(new_job: ResourceRequest, current_user=Depends(get_current_user)):
    if current_user["role"] != "HM":
        raise HTTPException(status_code=403, detail="Not Authorized")
    try:
        await jobs_crud.create_job_and_resource_request(new_job, current_user)
        return {"detail": "Job Created Successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {e}")

@jobs_router.put("/modify")
async def update_job(request_id: str, updated_job: ResourceRequest, current_user=Depends(get_current_user)):
    if current_user["role"] != "HM":
        raise HTTPException(status_code=403, detail="Not Authorized")
    try:
        await jobs_crud.update_job_and_resource_request(request_id, updated_job, current_user)
        return {"detail": "Job Updated Successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {e}")
