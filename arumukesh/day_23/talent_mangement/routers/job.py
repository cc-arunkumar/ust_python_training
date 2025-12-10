from fastapi import APIRouter, Depends, Query, HTTPException,status
from pydantic import BaseModel
from typing import List, Optional
from database import collections
from models import Job, UserRole,Application,ApplicationStatus
from utils.security import get_current_user
import uuid
from datetime import datetime

router = APIRouter()

@router.get("/", response_model=List[Job])
async def get_jobs(
    location: Optional[str] = Query(None),
    grade: Optional[str] = Query(None),
    skills: Optional[str] = Query(None),
    current_user: dict = Depends(get_current_user)
):
    query = {"status": "Open"}

    # Role-based filtering
    if current_user["role"] == UserRole.WFM:
        query["wfm_id"] = current_user["employee_id"]
    elif current_user["role"] == UserRole.HM:
        query["hm_id"] = current_user["employee_id"]
    elif current_user["role"] in [UserRole.EMPLOYEE_TP, UserRole.EMPLOYEE_NON_TP]:
        employee = await collections["employees"].find_one({"employee_id": int(current_user["employee_id"])})
        if employee["type"] == "TP":
            band_num = int(employee["band"][1:]) if employee["band"].startswith("B") else 0
            allowed = [f"B{band_num-1}", f"B{band_num}", f"B{band_num+1}"]
            query["job_grade"] = {"$in": allowed}

    if location:
        query["location"] = {"$regex": location, "$options": "i"}
    if grade:
        query["job_grade"] = grade
    if skills:
        query["required_skills"] = {"$in": [s.strip() for s in skills.split(",")]}

    jobs = await collections["jobs"].find(query).to_list(100)
    return [Job(**j) for j in jobs]


# @router.post("/", response_model=Application)
class ApplicationCreate(BaseModel):
    job_rr_id: str
    cover_letter: Optional[str] = None
    resume: Optional[str] = None

@router.post("/", response_model=dict)
async def create_application(
    data: ApplicationCreate,
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] not in ["TP", "Non TP"]:
        raise HTTPException(status_code=403, detail="Only employees can apply")

    job_rr_id = data.job_rr_id.strip()

    # THIS LINE IS THE GUARD — WILL BLOCK 100% OF FAKE RR IDs
    job = await collections["jobs"].find_one({
        "rr_id": job_rr_id,
        "status": "Open"
    })
    print(job)
    if not job:
        raise HTTPException(
            status_code=404,
            detail=f"Job RR ID '{job_rr_id}' does not exist or is closed. Application rejected."
        )

    # Prevent duplicate
    existing = await collections["applications"].find_one({
        "employee_id": int(current_user["employee_id"]),
        "job_rr_id": job_rr_id,
        "status": {"$nin": ["Withdrawn", "Rejected"]}
    })
    if existing:
        raise HTTPException(status_code=400, detail="Already applied")

    app_id = str(uuid.uuid4())
    app_doc = {
        "_id": app_id,
        "employee_id": int(current_user["employee_id"]),
        "job_rr_id": job_rr_id,
        "status": ApplicationStatus.DRAFT,
        "cover_letter": data.cover_letter,
        "resume": data.resume,
        "submitted_at": None,
        "updated_at": datetime.utcnow()
    }

    await collections["applications"].insert_one(app_doc)

    return {
        "message": "Application created (Draft)",
        "application_id": app_id,
        "job_rr_id": job_rr_id
    }
# @router.post("/")
# async def create_job(job: Job, current_user: dict = Depends(get_current_user)):
#     if current_user["role"] != UserRole.HM:
#         raise HTTPException(403, "Only Hiring Manager can create jobs")
#     job_dict = job.dict(by_alias=True)
#     await collections["jobs"].insert_one(job_dict)
#     return job_dict