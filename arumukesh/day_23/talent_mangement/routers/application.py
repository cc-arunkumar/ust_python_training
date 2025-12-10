from fastapi import APIRouter, Depends, HTTPException,status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uuid
from database import collections
from models import Application, ApplicationStatus, UserRole
from utils.security import get_current_user

router = APIRouter()
@router.post("/", response_model=Application)
async def create_application(
    app_in: Application,
    current_user: dict = Depends(get_current_user)
):
    role = current_user["role"]
    
    # 1. Only TP or Non-TP employees can apply
    if role not in ["TP", "Non TP"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only employees can create applications"
        )

    # 2. CRITICAL: Validate that job_rr_id exists and is Open
    job_rr_id = app_in.job_rr_id.strip()
    job = await collections["jobs"].find_one({
        "rr_id": job_rr_id,
        "status": "Open"  # Prevent applying to closed jobs
    })

    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with RR ID '{job_rr_id}' not found or is no longer open"
        )

    # 3. Optional: Prevent duplicate applications (same employee + same job)
    existing = await collections["applications"].find_one({
        "employee_id": int(current_user["employee_id"]),
        "job_rr_id": job_rr_id,
        "status": {"$nin": [ApplicationStatus.WITHDRAWN, ApplicationStatus.REJECTED]}
    })
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You have already applied for this job"
        )

    # 4. Create the application
    application_data = app_in.dict(by_alias=True)
    application_data.update({
        "_id": str(uuid.uuid4()),
        "employee_id": int(current_user["employee_id"]),
        "status": ApplicationStatus.DRAFT,
        "submitted_at": None,
        "updated_at": datetime.utcnow()
    })

    result = await collections["applications"].insert_one(application_data)
    created_app = await collections["applications"].find_one({"_id": result.inserted_id})

    return Application(**created_app)
@router.put("/{app_id}")
async def update_draft(app_id: str, update_data: Application, current_user: dict = Depends(get_current_user)):
    app = await collections["applications"].find_one({"_id": app_id, "employee_id": int(current_user["employee_id"])})
    if not app or app["status"] != ApplicationStatus.DRAFT:
        raise HTTPException(400, "Cannot edit")
    await collections["applications"].update_one(
        {"_id": app_id},
        {"$set": {**update_data.dict(exclude_unset=True), "updated_at": datetime.utcnow()}}
    )
    return {"message": "Updated"}

@router.post("/{app_id}/submit")
async def submit_application(app_id: str, current_user: dict = Depends(get_current_user)):
    app = await collections["applications"].find_one({"_id": app_id, "employee_id": int(current_user["employee_id"])})
    if not app or app["status"] != ApplicationStatus.DRAFT:
        raise HTTPException(400)
    await collections["applications"].update_one(
        {"_id": app_id},
        {"$set": {"status": ApplicationStatus.SUBMITTED, "submitted_at": datetime.utcnow()}}
    )
    return {"message": "Submitted"}

@router.delete("/{app_id}")
async def withdraw(app_id: str, current_user: dict = Depends(get_current_user)):
    app = await collections["applications"].find_one({"_id": app_id, "employee_id": int(current_user["employee_id"])})
    if not app or app["status"] in [ApplicationStatus.SHORTLISTED, ApplicationStatus.INTERVIEW, ApplicationStatus.SELECTED, ApplicationStatus.ALLOCATED]:
        raise HTTPException(400, "Cannot withdraw")
    await collections["applications"].update_one(
        {"_id": app_id},
        {"$set": {"status": ApplicationStatus.WITHDRAWN}}
    )
    return {"message": "Withdrawn"}