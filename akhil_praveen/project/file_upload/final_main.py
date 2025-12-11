# main.py
import os
import logging
from datetime import datetime, timezone
from typing import List

import pandas as pd
import chardet
from io import BytesIO

from fastapi import FastAPI, File, UploadFile, HTTPException, Request
from fastapi.responses import JSONResponse

from database import collections
from final_model import Employee, ResourceRequest, Job, User
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# -------------------------------------------------------------------
# Logging
# -------------------------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("RRProcessor")

# -------------------------------------------------------------------
# Custom Exceptions
# -------------------------------------------------------------------
class FileFormatException(HTTPException):
    def __init__(self, detail="Invalid file format"):
        super().__init__(status_code=400, detail=detail)

class ValidationException(HTTPException):
    def __init__(self, detail):
        super().__init__(status_code=422, detail={"validation_error": detail})

class DatabaseException(HTTPException):
    def __init__(self, detail="Database operation failed"):
        super().__init__(status_code=500, detail=detail)

class ReportProcessingException(HTTPException):
    def __init__(self, detail):
        super().__init__(status_code=400, detail=detail)

app = FastAPI(title="Career Velocity & RR Report Processor")

# -------------------------------------------------------------------
# Global Exception Handlers
# -------------------------------------------------------------------
@app.exception_handler(FileFormatException)
async def file_format_handler(_: Request, exc: FileFormatException):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})

@app.exception_handler(ValidationException)
async def validation_handler(_: Request, exc: ValidationException):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})

@app.exception_handler(DatabaseException)
async def db_handler(_: Request, exc: DatabaseException):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})

@app.exception_handler(ReportProcessingException)
async def processing_handler(_: Request, exc: ReportProcessingException):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})

# -------------------------------------------------------------------
# Audit Logging
# -------------------------------------------------------------------
async def log_upload_action(audit_type: str, filename: str, file_type: str,
                           uploaded_by: str, total_rows: int, valid_rows: int,
                           failed_rows: int, sample_errors):
    await collections["audit_logs"].insert_one({
        "audit_type": audit_type,
        "filename": filename,
        "file_type": file_type,
        "uploaded_by": uploaded_by or "System",
        "upload_time_utc": datetime.now(timezone.utc),
        "total_rows": total_rows,
        "valid_rows": valid_rows,
        "failed_rows": failed_rows,
        "sample_errors": sample_errors,
    })

# -------------------------------------------------------------------
# Utilities
# -------------------------------------------------------------------
def detect_encoding(data: bytes) -> str:
    result = chardet.detect(data)
    encoding = result["encoding"] or "utf-8"
    if result["confidence"] < 0.7:
        for enc in ["utf-8", "cp1252", "latin1", "iso-8859-1"]:
            try:
                data.decode(enc)
                return enc
            except:
                continue
    return encoding

def convert_dates_for_mongo(data: dict):
    """Convert date objects to UTC datetime for MongoDB storage."""
    from datetime import date, time
    for k, v in data.items():
        if isinstance(v, dict):
            data[k] = convert_dates_for_mongo(v)
        elif isinstance(v, date) and not isinstance(v, datetime):
            data[k] = datetime.combine(v, time.min).replace(tzinfo=timezone.utc)
    return data

# -------------------------------------------------------------------
# Database Sync Functions
# -------------------------------------------------------------------
async def sync_rr_with_db(validated_rrs: List[ResourceRequest]):
    uploaded_ids = {rr.resource_request_id for rr in validated_rrs}

    # Fetch current state
    existing_rrs = await collections["resource_request"].find(
        {}, {"Resource Request ID": 1, "rr_status": 1}
    ).to_list(None)
    rr_map = {r["Resource Request ID"]: r for r in existing_rrs}

    existing_jobs = await collections["jobs"].find(
        {}, {"rr_id": 1, "status": 1}
    ).to_list(None)
    job_map = {j["rr_id"]: j for j in existing_jobs}

    rr_insert, rr_reactivate = [], []
    job_insert, job_reactivate = [], []

    for rr in validated_rrs:
        rr_id = rr.resource_request_id
        rr_data = convert_dates_for_mongo(rr.model_dump(by_alias=True))

        if rr_id not in rr_map:
            rr_insert.append(rr_data)
        elif not rr_map[rr_id].get("rr_status"):
            rr_reactivate.append({"filter": {"Resource Request ID": rr_id},
                                  "update": {"$set": {"rr_status": True}}})

        job_data = convert_dates_for_mongo(Job(
            rr_id=rr_id, title=rr.ust_role, city=rr.city, state=rr.state,
            country=rr.country, required_skills=rr.mandatory_skills,
            description=rr.job_description, rr_start_date=rr.rr_start_date,
            rr_end_date=rr.rr_end_date, wfm_id=rr.wfm_id, hm_id=rr.hm_id,
            status=rr.flag, job_grade=rr.job_grade, account_name=rr.account_name,
            project_id=rr.project_id
        ).__dict__)

        if rr_id not in job_map:
            job_insert.append(job_data)
        elif not job_map[rr_id].get("status"):
            job_reactivate.append({"filter": {"rr_id": rr_id},
                                   "update": {"$set": {"status": True}}})

    # Deactivate removed RRs/Jobs
    deactivate_rr = [{"filter": {"Resource Request ID": rid}, "update": {"$set": {"rr_status": False}}}
                     for rid in rr_map if rid not in uploaded_ids and rr_map[rid].get("rr_status")]
    deactivate_job = [{"filter": {"rr_id": rid}, "update": {"$set": {"status": False}}}
                      for rid in job_map if rid not in uploaded_ids and job_map[rid].get("status")]

    # Bulk operations
    if rr_insert:   await collections["resource_request"].insert_many(rr_insert, ordered=False)
    if job_insert:  await collections["jobs"].insert_many(job_insert, ordered=False)

    for op in rr_reactivate + deactivate_rr:
        await collections["resource_request"].update_one(op["filter"], op["update"])
    for op in job_reactivate + deactivate_job:
        await collections["jobs"].update_one(op["filter"], op["update"])

    return {
        "rr_inserted": len(rr_insert),
        "rr_reactivated+deactivated": len(rr_reactivate) + len(deactivate_rr),
        "jobs_inserted": len(job_insert),
        "jobs_reactivated+deactivated": len(job_reactivate) + len(deactivate_job),
    }

async def sync_employees_with_db(employees: List[Employee], users: List[User]):

    existing = await collections["employees"].find({}, {"Employee ID": 1, "status": 1}).to_list(None)
    emp_map = {e["Employee ID"]: e for e in existing}

    existing_users = await collections["users"].find({}, {"employee_id": 1}).to_list(None)
    user_set = {u["employee_id"] for u in existing_users}

    inserts_emp, inserts_user, updates = [], [], []

    for emp, user in zip(employees, users):
        eid = emp.employee_id
        emp_data = convert_dates_for_mongo(emp.model_dump(by_alias=True))
        user_data = user.model_dump(by_alias=True)

        if eid not in emp_map:
            emp_data["status"] = True
            inserts_emp.append(emp_data)
            inserts_user.append(user_data)
        else:
            if not emp_map[eid].get("status"):
                updates.append({"filter": {"Employee ID": eid}, "update": {"$set": {"status": True}}})
            updates.append({"filter": {"Employee ID": eid}, "update": {"$set": emp_data}})
            if str(eid) not in user_set:
                inserts_user.append(user_data)

    if inserts_emp:  await collections["employees"].insert_many(inserts_emp, ordered=False)
    if inserts_user: await collections["users"].insert_many(inserts_user, ordered=False)
    for op in updates:
        await collections["employees"].update_one(op["filter"], op["update"])

    return {
        "employees_inserted": len(inserts_emp),
        "employees_updated": len(updates),
        "users_inserted": len(inserts_user),
    }

# -------------------------------------------------------------------
# API Endpoints
# -------------------------------------------------------------------
@app.post("/upload/employees")
async def upload_career_velocity(file: UploadFile = File(...)):
    content = await file.read()
    if not file.filename.lower().endswith((".xlsx", ".xls", ".csv")):
        raise FileFormatException("Only .xlsx, .xls, or .csv files allowed")

    # Load file
    try:
        df = (pd.read_csv(BytesIO(content), encoding=detect_encoding(content), dtype=str, engine="python", on_bad_lines="skip")
              if file.filename.endswith(".csv") else pd.read_excel(BytesIO(content)))
        df = df.dropna(how="all")
    except Exception as e:
        raise ReportProcessingException(f"Failed to read file: {e}")

    required = ["Employee ID", "Employee Name", "Designation", "Band", "City", "Type"]
    if missing := [c for c in required if c not in df.columns]:
        raise ValidationException(f"Missing columns: {missing}")

    valid_emps, valid_users, errors = [], [], []
    for idx, row in df.iterrows():
        row_dict = {k: None if pd.isna(v) else str(v).strip() for k, v in row.to_dict().items()}
        try:
            emp = Employee(**row_dict)
            user = User(employee_id=str(emp.employee_id), role=emp.type)
            valid_emps.append(emp)
            valid_users.append(user)
        except Exception as e:
            errors.append({"row": idx + 2, "error": str(e)})

    await log_upload_action("employees", file.filename,
                            "CSV" if file.filename.endswith(".csv") else "Excel",
                            "API User", len(df), len(valid_emps), len(errors), errors[:5])

    if not valid_emps:
        return {"message": "No valid employees found", "errors_sample": errors[:5]}

    result = await sync_employees_with_db(valid_emps, valid_users)
    return {
        "message": "Career Velocity processed successfully",
        "processed": len(valid_emps),
        "failed": len(errors),
        "errors_sample": errors[:5],
        "sync": result
    }

@app.post("/upload/rr-report")
async def upload_rr_report(file: UploadFile = File(...)):
    content = await file.read()
    if not file.filename.lower().endswith((".xlsx", ".xls", ".csv")):
        raise FileFormatException("Only Excel/CSV files allowed")

    try:
        df = (pd.read_csv(BytesIO(content), skiprows=6, encoding=detect_encoding(content),
                          dtype=str, engine="python", on_bad_lines="skip")
              if file.filename.endswith(".csv") else pd.read_excel(BytesIO(content), skiprows=6, dtype=str))
        df = df.dropna(how="all")
    except Exception as e:
        raise ReportProcessingException(f"Failed to read RR report: {e}")

    if "Resource Request ID" not in df.columns:
        raise ValidationException("Column 'Resource Request ID' is required")

    valid_rrs, errors = [], []
    for idx, row in df.iterrows():
        rr_id = row.get("Resource Request ID")
        if not rr_id or pd.isna(rr_id):
            continue
        row_dict = {k: None if pd.isna(v) else v for k, v in row.to_dict().items()}
        row_dict["rr_status"] = True
        try:
            # row_dict["Mandatory Skills"] = 
            valid_rrs.append(ResourceRequest(**row_dict))
        except Exception as e:
            errors.append({"row": idx + 8, "rr_id": str(rr_id), "error": str(e)})

    await log_upload_action("rr_report", file.filename,
                            "CSV" if file.filename.endswith(".csv") else "Excel",
                            "API User", len(df), len(valid_rrs), len(errors), errors[:5])

    if not valid_rrs:
        return {"message": "No valid RRs found", "errors_sample": errors[:5]}

    await sync_rr_with_db(valid_rrs)
    return {
        "message": "RR Report processed successfully",
        "valid_requests": len(valid_rrs),
        "failed": len(errors),
        "errors_sample": errors[:5]
    }

# -------------------------------------------------------------------
# Auto-processing (watch folder)
# -------------------------------------------------------------------
UPLOAD_FOLDER = "updated"
PROCESSED_FOLDER = "processed"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

async def auto_rr_job():
    files = [f for f in os.listdir(UPLOAD_FOLDER)
             if f.lower().endswith((".xlsx", ".xls", ".csv"))]
    if not files:
        return

    latest = sorted(files)[-1]
    src = os.path.join(UPLOAD_FOLDER, latest)
    dst = os.path.join(PROCESSED_FOLDER, f"{datetime.now():%Y%m%d_%H%M%S}_{latest}")

    try:
        print(src)
        with open(src, "rb") as f:
            fake_file = UploadFile(filename=latest, file=BytesIO(f.read()))
        await upload_rr_report(fake_file)
        os.rename(src, dst)
        logger.info(f"Auto-processed RR: {latest} → processed/")
    except Exception as e:
        logger.error(f"Auto RR job failed for {latest}: {e}")

# scheduler = AsyncIOScheduler()
# scheduler.add_job(auto_rr_job, "cron", minute="*", id="rr_watcher")
# scheduler.start()

# -------------------------------------------------------------------
# Health check
# -------------------------------------------------------------------
@app.get("/")
async def root():
    return {
        "service": "Career Velocity & RR Report Processor",
        "status": "running",
        "auto_processing": "every minute from ./updated/",
        "processed_folder": "./processed/"
    }