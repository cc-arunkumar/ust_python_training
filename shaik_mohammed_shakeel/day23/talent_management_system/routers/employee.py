from fastapi import APIRouter, HTTPException,Depends
from typing import List, Dict, Any
from database import resource_request, applications, employees,files
from utils.security import get_current_user
from typing import List, Dict, Any, Optional
from fastapi import APIRouter, HTTPException, status, Query
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, UploadFile, File
from utils.llm_service import parse_resume_with_llm
from utils.employee_service import extract_text_from_pdf, save_to_gridfs, extract_text_from_binary, fetch_employee_by_id, update_parsed_resume
from database import employees
from bson import ObjectId
import base64
from utils.employee_service import (
    fetch_all_employees,
    fetch_employee_by_id,
    _serialize,              
)
from database import employees  
 
resume_router = APIRouter(prefix="/resume")
router = APIRouter(prefix="/employees")
# Defining routers
hm_router = APIRouter(prefix="/hm")
wfm_router = APIRouter(prefix="/wfm")
tp_router = APIRouter(prefix="/tp")


 
# Directly refer to MongoDB collections (no need for function wrappers)
files_col=files
resouce_request_col=resource_request 
app_col = applications
emp_col = employees
 
# --- Simple inline role guard factory (no new files) ---
def role_guard(required_role: str):
    """
    Dependency factory to enforce that current_user.role == required_role.
    Usage: Depends(role_guard("HM"))
    """
    async def _guard(current_user: Dict[str, Any] = Depends(get_current_user)):
        role = current_user.get("role")
        if role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"User role '{role}' not authorized. Required role: '{required_role}'"
            )
        return current_user
    return _guard
 
# ---------------- HM endpoint (only HM role allowed) ----------------
@hm_router.get("/{hm_id}")
async def get_hm_employees(
    hm_id: str,
    current_user: Dict[str, Any] = Depends(role_guard("HM"))
):
    # 1. Get the job record
    job_rr = await resouce_request_col.find_one({"hm_id": hm_id})
    # If no job found, return empty list (consistent with original behavior)
    if not job_rr:
        return []
 
    job_rr_id = str(job_rr.get("resource_request_id"))
    # 2. Get allocated applications
    allocated_apps = await app_col.find(
        {"job_rr_id": job_rr_id, "status": "Allocated"}
    ).to_list(length=100)
 
    if not allocated_apps:
        return []
 
    # 3. Convert employee IDs from apps into INT (because Employee ID in DB is INT)
    try:
        employee_ids = [int(app["employee_id"]) for app in allocated_apps]
    except Exception:
        # If conversion fails for any record, filter safely
        employee_ids = []
        for app in allocated_apps:
            try:
                employee_ids.append(int(app["employee_id"]))
            except Exception:
                continue
 
    if not employee_ids:
        return []
 
    # 4. Fetch employees
    employees_data = await emp_col.find({"Employee ID": {"$in": employee_ids}}).to_list(length=100)
 
    for emp in employees_data:
        emp["id"] = str(emp.get("_id"))
        emp.pop("_id", None)
 
    return employees_data
 
# ---------------- WFM endpoint (only WFM role allowed) ----------------
@wfm_router.get("/{wfm_id}")
async def wfm_view(
    wfm_id: str,
    current_user: Dict[str, Any] = Depends(role_guard("WFM"))
):
    # 1. Get the jobs for the given WFM ID
    wfm_jobs = await resouce_request_col.find({"wfm_id": wfm_id}, {"resource_request_id": 1}).to_list(length=100)
    if not wfm_jobs:
        return []
 
    job_rr_ids = [str(j["rr_id"]) for j in wfm_jobs if j.get("resource_request_id") is not None]
    if not job_rr_ids:
        return []
 
    # 2. Get applications for the job RR IDs
    apps = await app_col.find({"job_rr_id": {"$in": job_rr_ids}}, {"employee_id": 1}).to_list(length=100)
    if not apps:
        return []
 
    # 3. Convert and dedupe employee IDs (int)
    emp_ids = []
    for a in apps:
        try:
            emp_ids.append(int(a["employee_id"]))
        except Exception:
            continue
    emp_ids = list(set(emp_ids))
    if not emp_ids:
        return []
 
    # 4. Get employee data for the found employee IDs
    result = await emp_col.find({"Employee ID": {"$in": emp_ids}}).to_list(length=100)
 
    for r in result:
        r["id"] = str(r.get("_id"))
        r.pop("_id", None)
 
    return result
 
# ---------------- TP endpoint (only TP Manager role allowed) ----------------
@tp_router.get("/application_employees")
async def get_employees_from_applications(
    current_user: Dict[str, Any] = Depends(role_guard("TP Manager"))
):
    # 1. Get all applications and their employee IDs
    apps = await app_col.find({}, {"employee_id": 1, "_id": 0}).to_list(length=100)
    if not apps:
        return []
 
    # 2. Extract unique employee IDs (int)
    employee_ids = []
    for app in apps:
        try:
            employee_ids.append(int(app["employee_id"]))
        except Exception:
            continue
    employee_ids = list(set(employee_ids))
    if not employee_ids:
        return []
 
    # 3. Fetch employees with the extracted IDs and the "Type" set to "TP"
    employees_data = await emp_col.find({
        "Employee ID": {"$in": employee_ids},
        "Type": "TP"
    }).to_list(length=100)
 
    for emp in employees_data:
        emp["id"] = str(emp.get("_id"))
        emp.pop("_id", None)
 
    return employees_data
 
# --- Simple inline role guard factory (no new files) ---
def role_guard(required_role: str):
    """
    Dependency factory to enforce that current_user.role == required_role.
    Usage: Depends(role_guard("HM"))
    """
    async def _guard(current_user: Dict[str, Any] = Depends(get_current_user)):
        role = current_user.get("role")
        if role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"User role '{role}' not authorized. Required role: '{required_role}'"
            )
        return current_user
    return _guard
 
# ---------------- HM endpoint (only HM role allowed) ----------------
@hm_router.get("/{hm_id}")
async def get_hm_employees(
    hm_id: str,
    current_user: Dict[str, Any] = Depends(role_guard("HM"))
):
    # 1. Get the job record
    job_rr = await resouce_request_col.find_one({"hm_id": hm_id})
    # If no job found, return empty list (consistent with original behavior)
    if not job_rr:
        return []
 
    job_rr_id = str(job_rr.get("rr_id"))
    # 2. Get allocated applications
    allocated_apps = await app_col.find(
        {"job_rr_id": job_rr_id, "status": "Allocated"}
    ).to_list(length=100)
 
    if not allocated_apps:
        return []
 
    # 3. Convert employee IDs from apps into INT (because Employee ID in DB is INT)
    try:
        employee_ids = [int(app["employee_id"]) for app in allocated_apps]
    except Exception:
        # If conversion fails for any record, filter safely
        employee_ids = []
        for app in allocated_apps:
            try:
                employee_ids.append(int(app["employee_id"]))
            except Exception:
                continue
 
    if not employee_ids:
        return []
 
    # 4. Fetch employees
    employees_data = await emp_col.find({"Employee ID": {"$in": employee_ids}}).to_list(length=100)
 
    for emp in employees_data:
        emp["id"] = str(emp.get("_id"))
        emp.pop("_id", None)
 
    return employees_data
 
# ---------------- WFM endpoint (only WFM role allowed) ----------------
@wfm_router.get("/{wfm_id}")
async def wfm_view(
    wfm_id: str,
    current_user: Dict[str, Any] = Depends(role_guard("WFM"))
):
    # 1. Get the jobs for the given WFM ID
    wfm_jobs = await resouce_request_col.find({"wfm_id": wfm_id}, {"rr_id": 1}).to_list(length=100)
    if not wfm_jobs:
        return []
 
    job_rr_ids = [str(j["rr_id"]) for j in wfm_jobs if j.get("rr_id") is not None]
    if not job_rr_ids:
        return []
 
    # 2. Get applications for the job RR IDs
    apps = await app_col.find({"job_rr_id": {"$in": job_rr_ids}}, {"employee_id": 1}).to_list(length=100)
    if not apps:
        return []
 
    # 3. Convert and dedupe employee IDs (int)
    emp_ids = []
    for a in apps:
        try:
            emp_ids.append(int(a["employee_id"]))
        except Exception:
            continue
    emp_ids = list(set(emp_ids))
    if not emp_ids:
        return []
 
    # 4. Get employee data for the found employee IDs
    result = await emp_col.find({"Employee ID": {"$in": emp_ids}}).to_list(length=100)
 
    for r in result:
        r["id"] = str(r.get("_id"))
        r.pop("_id", None)
 
    return result
 
# ---------------- TP endpoint (only TP Manager role allowed) ----------------
@tp_router.get("/application_employees")
async def get_employees_from_applications(
    current_user: Dict[str, Any] = Depends(role_guard("TP Manager"))
):
    # 1. Get all applications and their employee IDs
    apps = await app_col.find({}, {"employee_id": 1, "_id": 0}).to_list(length=100)
    if not apps:
        return []
 
    # 2. Extract unique employee IDs (int)
    employee_ids = []
    for app in apps:
        try:
            employee_ids.append(int(app["employee_id"]))
        except Exception:
            continue
    employee_ids = list(set(employee_ids))
    if not employee_ids:
        return []
 
    # 3. Fetch employees with the extracted IDs and the "Type" set to "TP"
    employees_data = await emp_col.find({
        "Employee ID": {"$in": employee_ids},
        "Type": "TP"
    }).to_list(length=100)
 
    for emp in employees_data:
        emp["id"] = str(emp.get("_id"))
        emp.pop("_id", None)
 
    return employees_data
 
 
 
# ====================== SEARCH (FINAL - WITH EMPLOYEE TYPE) ======================
@router.get("/search")
async def search_employees(search: str = Query(..., min_length=1)):
    """
    Global search across:
    - Employee Name
    - Designation
    - Primary & Secondary Technology
    - Employee ID
    - Type (TP / Non TP)
    - Employment Type (Employee)
    - City
    - Band
    """
    query = {
        "$or": [
            {"Employee Name": {"$regex": search, "$options": "i"}},
            {"Designation": {"$regex": search, "$options": "i"}},
            {"Primary Technology": {"$regex": search, "$options": "i"}},
            {"Secondary Technology": {"$regex": search, "$options": "i"}},
 
            # Employee identifiers
            {"Employee ID": {"$regex": search, "$options": "i"}},
           
            # Employee Type fields (both exist in your data)
            {"Type": {"$regex": search, "$options": "i"}},           # e.g. "TP", "Non TP"
            {"Employment Type": {"$regex": search, "$options": "i"}}, # e.g. "Employee"
 
            # Location & Grade
            {"City": {"$regex": search, "$options": "i"}},
            {"Band": {"$regex": search, "$options": "i"}},
        ]
    }
 
    # Bonus: If search is a full number → also try exact Employee ID match (faster & accurate)
    if search.strip().isdigit():
        query["$or"].append({"Employee ID": int(search)})
 
    cursor = employees.find(query)
    docs = await cursor.to_list(length=None)
    result = [_serialize(doc) for doc in docs]
 
    return {"count": len(result), "data": result}
 
 # ====================== FILTER ======================
@router.get("/filter")
async def filter_employees(
    employee_type: Optional[str] = Query(None, description="TP, Non TP"),
    employment_type: Optional[str] = Query(None, description="Employee, Contractor"),
    city: Optional[str] = Query(None, description="e.g. Bangalore, Chennai"),
    band: Optional[str] = Query(None, description="e.g. A3, B1"),
    designation: Optional[str] = Query(None, description="e.g. Tester III"),
    primary_tech: Optional[str] = Query(None, alias="primary", description="e.g. Java"),
    secondary_tech: Optional[str] = Query(None, alias="secondary", description="e.g. Angular"),
):
    """
    Multiple filters at once - perfect for UI with many dropdowns
    Example:
    /employees/filter?employee_type=TP&city=Bangalore&band=A3&skills=Java,Angular
    """
    query: Dict[str, Any] = {}
 
    if employee_type:
        query["Type"] = {"$regex": f"^{employee_type}$", "$options": "i"}
    if employment_type:
        query["Employment Type"] = {"$regex": f"^{employment_type}$", "$options": "i"}
    if city:
        query["City"] = {"$regex": city, "$options": "i"}
    if band:
        query["Band"] = {"$regex": band, "$options": "i"}
    if designation:
        query["Designation"] = {"$regex": designation, "$options": "i"}
    if primary_tech:
        query["Primary Technology"] = {"$regex": primary_tech, "$options": "i"}
    if secondary_tech:
        query["Secondary Technology"] = {"$regex": secondary_tech, "$options": "i"}
   
    cursor = employees.find(query)
    docs = await cursor.to_list(length=None)
    result = [_serialize(doc) for doc in docs]
 
    return {
        "count": len(result),
        "data": result,
        "applied_filters": {
            "employee_type": employee_type,
            "employment_type": employment_type,
            "city": city,
            "band": band,
            "designation": designation,
            "primary_tech": primary_tech,
            "secondary_tech": secondary_tech,
        }
    }
 
# ====================== SORT ======================
 
@router.get("/sort")
async def sort_employees(
    sort_by: str = Query(
        "Employee Name",
        description="Field to sort by (case-insensitive)",
        regex="^(?i)(Employee Name|Employee ID|Designation|Band|City|Type)$"  # ← Magic here
    ),
    order: str = Query(
        "asc",
        description="asc or desc",
        regex="^(?i)(asc|desc)$"  # also accepts ASC, Desc, etc.
    )
):
    """
    Sort by:
    - Employee Name
    - Employee ID
    - Designation
    - Band
    - City      ← works with city / City / CITY
    - Type      ← works with type / TYPE
    """
    sort_order = 1 if order.lower() == "asc" else -1
 
    # Normalize the field name to exact DB field
    field_map = {
        "employee name": "Employee Name",
        "employee id": "Employee ID",
        "designation": "Designation",
        "band": "Band",
        "city": "City",
        "type": "Type",
    }
 
    normalized = sort_by.strip().lower()
    db_field = field_map.get(normalized, "Employee Name")  # safe fallback
 
    cursor = employees.find().sort(db_field, sort_order)
    docs = await cursor.to_list(length=None)
    result = [_serialize(doc) for doc in docs]
 
    return {
        "count": len(result),
        "data": result,
        "sorted_by": db_field,
        "order": order.lower()
    }
 
 
 
# ====================== LIST ALL EMPLOYEES ======================
@router.get("/employees", response_model=List[Dict[str, Any]])
async def get_employees():
    try:
        employees_list = await fetch_all_employees()
        return employees_list
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching employees: {str(e)}"
        )
 
 
# ====================== GET SINGLE EMPLOYEE ======================
@router.get("/{employee_id}", response_model=Dict[str, Any])
async def get_employee(employee_id: int):
    try:
        emp = await fetch_employee_by_id(employee_id)
        if not emp:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found"
            )
        return emp
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching employee: {str(e)}"
        )
        

# ====================== RESUME UPLOAD & PARSING ======================    

def clean_text(text: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)
 
#  #API endpoint to upload resume
# @resume_router.put("/upload/{employee_id}")
# async def upload_resume(employee_id: int, file: UploadFile = File(...)):
#     emp_col = employees
 
#     if file.content_type != "application/pdf":
#         raise HTTPException(status_code=400, detail="Only PDF files are allowed")
 
#     file_bytes = await file.read()
#     if not file_bytes:
#         raise HTTPException(status_code=400, detail="Uploaded file is empty")
 
#     try:
#         # Save file to GridFS
#         file_id = save_to_gridfs(file.filename, file_bytes)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error saving file: {str(e)}")
 
#     # 1. Extract raw text from PDF
#     try:
#         raw_text = extract_text_from_pdf(file_bytes)
#         extracted_text = clean_text(raw_text)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error extracting text: {str(e)}")
 
#     # 2. Send to LLM and get parsed clean resume
#     try:
#         parsed_resume = await parse_resume_with_llm(extracted_text)
#     except Exception as e:
#         parsed_resume = None  # Continue even if LLM fails
 
#     # 3. Update employee record
#     update_body = {
#         "resume": file_id,
#         "resume_text": extracted_text,
#     }
 
#     # True parsed resume available → store inside DB
#     if parsed_resume:
#         update_body["resume_text"] = parsed_resume
 
#     try:
#         result = await emp_col.update_one(
#             {"employee_id": employee_id},
#             {"$set": update_body}
#         )
#         if result.matched_count == 0:
#             raise HTTPException(status_code=404, detail="Employee ID not found")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error updating employee data: {str(e)}")
 
#     return {
#         "message": "Resume uploaded successfully",
#         "filename": file.filename,
#         "raw_text_preview": extracted_text[:200],
#         "llm_resume_preview": parsed_resume[:200] if parsed_resume else "LLM not available"
#     }
 
 
from fastapi import UploadFile, File, HTTPException
from fastapi import HTTPException
from database import fs,sync_db

from fastapi import HTTPException
from bson import ObjectId
import gridfs

# Assuming `fs` is the synchronous GridFS object initialized with pymongo
fs = gridfs.GridFS(sync_db, collection="files")
from fastapi import HTTPException
from bson import ObjectId
from fastapi.responses import JSONResponse, StreamingResponse
import gridfs

# Assuming `fs` is the synchronous GridFS object initialized with pymongo
fs = gridfs.GridFS(sync_db, collection="files")

@resume_router.get("/employee/{employee_id}/resume")
async def fetch_employee_resume(employee_id: int):
    try:
        # Step 1: Fetch the employee from the employees collection
        employee = await emp_col.find_one({"employee_id": employee_id})
        
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        
        # Step 2: Get the resume file's _id from the employee's resume field
        file_id = employee.get("resume")  # This should be the ObjectId of the file in GridFS
        
        if not file_id:
            raise HTTPException(status_code=404, detail="Resume file not found for this employee")
        
        # Step 3: Convert the file_id to ObjectId
        file_object_id = ObjectId(file_id)
        
        # Step 4: Fetch the file metadata using the file_id (which is the ObjectId)
        file_metadata = fs.find_one({"_id": file_object_id})
        
        if not file_metadata:
            raise HTTPException(status_code=404, detail="File not found in GridFS")
        
        # Step 5: Return file metadata (file name, file size, upload date, and custom metadata)
        return {
            "file_id": str(file_metadata._id),
            "filename": file_metadata.filename,
            "content_type": file_metadata.content_type,
            "length": file_metadata.length,
            "upload_date": file_metadata.uploadDate.isoformat(),
            "metadata": file_metadata.metadata  # Include the custom metadata if present
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching employee's resume: {str(e)}")

@resume_router.get("/employee/{employee_id}/resume/download")
async def download_employee_resume(employee_id: int):
    try:
        # Step 1: Fetch the employee from the employees collection
        employee = await emp_col.find_one({"employee_id": employee_id})
        
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        
        # Step 2: Get the resume file's _id from the employee's resume field
        file_id = employee.get("resume")
        
        if not file_id:
            raise HTTPException(status_code=404, detail="Resume file not found for this employee")
        
        # Step 3: Convert the file_id to ObjectId
        file_object_id = ObjectId(file_id)
        
        # Step 4: Fetch the file metadata from GridFS (this is a synchronous operation)
        file_metadata = fs.find_one({"_id": file_object_id})
        
        if not file_metadata:
            raise HTTPException(status_code=404, detail="File not found in GridFS")
        
        # Step 5: Fetch the file content from GridFS synchronously (GridOut is not async)
        file_data = fs.get(file_metadata._id)  # Sync operation, no await
        
        # Step 6: Return the file as a StreamingResponse (binary data)
        return StreamingResponse(file_data, media_type=file_metadata.content_type)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error downloading employee's resume: {str(e)}")


@resume_router.put("/upload/{employee_id}")
async def upload_resume(employee_id: int, file: UploadFile = File(...)):
    emp_col = employees

    # Check if the file is a PDF
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    # Read the file contents
    file_bytes = await file.read()
    if not file_bytes:
        raise HTTPException(status_code=400, detail="Uploaded file is empty")

    try:
        # Save the file to GridFS and get the file_id (this will be the ObjectId)
        file_id = save_to_gridfs(file.filename, file_bytes)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving file: {str(e)}")

    # 1. Extract raw text from PDF
    try:
        raw_text = extract_text_from_pdf(file_bytes)
        extracted_text = clean_text(raw_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error extracting text: {str(e)}")

    # 2. Send to LLM and get parsed clean resume
    try:
        parsed_resume = await parse_resume_with_llm(extracted_text)
    except Exception as e:
        parsed_resume = None  # Continue even if LLM fails

    # 3. Update employee record with the file_id and extracted/parsed resume
    update_body = {
        "resume": file_id,
        "resume_text": extracted_text,

    }

    # If parsed resume is available, store it inside DB
    if parsed_resume:
        update_body["resume_text"] = parsed_resume

    try:
        result = await emp_col.update_one(
            {"employee_id": employee_id},
            {"$set": update_body}
        )
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Employee ID not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating employee data: {str(e)}")

    return {
        "message": "Resume uploaded successfully",
        "filename": file.filename,
        "raw_text_preview": extracted_text[:200],
        "llm_resume_preview": parsed_resume[:200] if parsed_resume else "LLM not available",
        "file_id": str(file_id)  # Return the file_id (ObjectId) to the user
    }
