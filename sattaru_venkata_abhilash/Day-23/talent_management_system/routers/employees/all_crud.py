from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from database import jobs, applications, employees

# Defining routers
hm_router = APIRouter(prefix="/hm")
wfm_router = APIRouter(prefix="/wfm")
tp_router = APIRouter(prefix="/tp")

# Directly refer to MongoDB collections (no need for function wrappers)
job_col = jobs  # Now it's directly referring to the MongoDB collection
app_col = applications
emp_col = employees

# Endpoint for HM (Hiring Manager)
@hm_router.get("/{hm_id}")
async def get_hm_employees(hm_id: str):
    # 1. Get the job record
    job_rr = await job_col.find_one({"hm_id": hm_id})
    print("Job record:", job_rr)

    if not job_rr:
        return []

    job_rr_id = str(job_rr["rr_id"])
    print("Job RR ID:", job_rr_id)

    # 2. Get allocated applications
    allocated_apps = await app_col.find({
        "job_rr_id": job_rr_id,
        "status": "Allocated"
    }).to_list(length=100)
    print("Allocated Apps:", allocated_apps)

    if not allocated_apps:
        return []

    # 3. Convert employee IDs from apps into INT (because Employee ID in DB is INT)
    employee_ids = [int(app["employee_id"]) for app in allocated_apps]
    print("Converted Employee IDs:", employee_ids)

    # 4. Fetch employees
    employees_data = await emp_col.find({
        "Employee ID": {"$in": employee_ids}
    }).to_list(length=100)
    
    for emp in employees_data:
        emp["id"] = str(emp["_id"])
        emp.pop("_id", None)

    return employees_data


# Endpoint for WFM (Workforce Manager)
@wfm_router.get("/{wfm_id}")
async def wfm_view(wfm_id: str):
    # 1. Get the jobs for the given WFM ID
    wfm_jobs = await job_col.find({"wfm_id": wfm_id}, {"rr_id": 1}).to_list(length=100)
    print("WFM Jobs:", wfm_jobs)

    if not wfm_jobs:
        return []

    job_rr_ids = [str(j["rr_id"]) for j in wfm_jobs]
    print("RR IDs:", job_rr_ids)

    # 2. Get applications for the job RR IDs
    apps = await app_col.find({
        "job_rr_id": {"$in": job_rr_ids}
    }, {"employee_id": 1}).to_list(length=100)
    print("Apps:", apps)

    if not apps:
        return []

    emp_ids = list({int(a["employee_id"]) for a in apps})
    print("Employee IDs:", emp_ids)

    if not emp_ids:
        return []

    # 3. Get employee data for the found employee IDs
    result = await emp_col.find({
        "Employee ID": {"$in": emp_ids}
    }).to_list(length=100)

    for r in result:
        r["id"] = str(r["_id"])
        r.pop("_id", None)

    return result


# Endpoint for TP (Third-Party)
@tp_router.get("/application_employees")
async def get_employees_from_applications():
    # 1. Get all applications and their employee IDs
    apps = await app_col.find({}, {"employee_id": 1, "_id": 0}).to_list(length=100)
    if not apps:
        return []

    # 2. Extract unique employee IDs
    employee_ids = list({int(app["employee_id"]) for app in apps})

    # 3. Fetch employees with the extracted IDs and the "Type" set to "TP"
    employees_data = await emp_col.find({
        "Employee ID": {"$in": employee_ids},
        "Type": "TP"
    }).to_list(length=100)

    for emp in employees_data:
        emp["id"] = str(emp["_id"])
        emp.pop("_id", None)

    return employees_data
