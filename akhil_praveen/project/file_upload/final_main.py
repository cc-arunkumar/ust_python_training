# main.py
from fastapi import FastAPI, File, UploadFile, HTTPException, Request
from fastapi.responses import JSONResponse
from typing import List
import pandas as pd
from io import BytesIO
from datetime import datetime, date, time, timezone
import chardet
from database import collections
from bson import ObjectId

# Import your models
from final_model import Employee, ResourceRequest, Job


# ============================================================
# 🔥 CUSTOM EXCEPTION CLASSES
# ============================================================
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


# ============================================================
# 🔥 GLOBAL EXCEPTION HANDLERS
# ============================================================
app = FastAPI(title="Career Velocity & RR Report Processor")

@app.exception_handler(FileFormatException)
async def file_format_exception_handler(request: Request, exc: FileFormatException):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})


@app.exception_handler(ValidationException)
async def validation_exception_handler(request: Request, exc: ValidationException):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})


@app.exception_handler(DatabaseException)
async def db_exception_handler(request: Request, exc: DatabaseException):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})


@app.exception_handler(ReportProcessingException)
async def report_processing_exception_handler(request: Request, exc: ReportProcessingException):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})


# ============================================================
# IN-MEMORY STORAGE
# ============================================================
employees_in_memory: List[Employee] = []
resource_requests_in_memory: List[ResourceRequest] = []


# ============================================================
# 🔥 UNIVERSAL AUDIT LOGGER
# ============================================================
async def log_upload_action(
    audit_type: str,
    filename: str,
    file_type: str,
    uploaded_by: str,
    total_rows: int,
    valid_rows: int,
    failed_rows: int,
    sample_errors
):
    audit_record = {
        "audit_type": audit_type,
        "filename": filename,
        "file_type": file_type,
        "uploaded_by": uploaded_by or "Unknown User",
        "upload_time_utc": datetime.utcnow(),
        "total_rows": total_rows,
        "valid_rows": valid_rows,
        "failed_rows": failed_rows,
        "sample_errors": sample_errors,
    }

    await collections["audit_logs"].insert_one(audit_record)
    return True


# ============================================================
# ENCODING DETECTOR
# ============================================================
def detect_encoding(byte_data: bytes) -> str:
    detection = chardet.detect(byte_data)
    encoding = detection["encoding"] or "utf-8"
    if detection["confidence"] < 0.7:
        for enc in ["utf-8", "cp1252", "latin1", "iso-8859-1"]:
            try:
                byte_data.decode(enc)
                return enc
            except:
                continue
        return "utf-8"
    return encoding


# ============================================================
# DATE FIXER FOR MONGO
# ============================================================
def convert_dates_for_mongo(data):
    for key, value in data.items():
        if isinstance(value, dict):
            data[key] = convert_dates_for_mongo(value)
        elif isinstance(value, date) and not isinstance(value, datetime):
            data[key] = datetime.combine(value, time.min).replace(tzinfo=timezone.utc)
    return data


# ============================================================
# RR SYNC FUNCTION (UNCHANGED)
# ============================================================
async def sync_rr_with_db(validated_rrs: List[ResourceRequest]):
    pass  # Your original function here


# ============================================================
# 📌 CAREER VELOCITY UPLOAD WITH AUDIT + CUSTOM EXCEPTIONS
# ============================================================
@app.post("/upload/employees")
async def upload_career_velocity(file: UploadFile = File(...)):
    global employees_in_memory

    if not file.filename.endswith((".xlsx", ".xls")):
        raise FileFormatException("Only Excel files (.xlsx/.xls) allowed")

    content = await file.read()
    try:
        df = pd.read_excel(BytesIO(content))
    except Exception as e:
        raise ReportProcessingException(f"Failed to read Excel: {e}")

    required_cols = ["Employee ID", "Employee Name", "Designation", "Band", "City", "Type"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValidationException(f"Missing required columns: {missing}")

    validated_employees = []
    errors = []

    for idx, row in df.iterrows():
        row_dict = {k: None if pd.isna(v) else v for k, v in row.to_dict().items()}

        try:
            emp = Employee(**row_dict)
            validated_employees.append(emp)
        except Exception as e:
            errors.append({"row": idx + 2, "error": str(e), "data": row_dict})

    # AUDIT LOG
    await log_upload_action(
        audit_type="employees",
        filename=file.filename,
        file_type="Excel",
        uploaded_by="System",
        total_rows=len(df),
        valid_rows=len(validated_employees),
        failed_rows=len(errors),
        sample_errors=errors[:5],
    )

    # INSERT INTO MONGO
    if validated_employees:
        records = [e.model_dump(by_alias=True) for e in validated_employees]
        try:
            await collections["employees"].insert_many(records, ordered=False)
        except Exception as e:
            raise DatabaseException(f"Failed to insert employees: {e}")

    return {
        "message": "Employee report processed successfully!",
        "valid": len(validated_employees),
        "failed": len(errors),
        "errors_sample": errors[:5],
    }


# ============================================================
# 📌 RR REPORT UPLOAD WITH AUDIT + CUSTOM EXCEPTIONS
# ============================================================
@app.post("/upload/rr-report")
async def upload_rr_report(file: UploadFile = File(...)):
    filename = file.filename.lower()
    content = await file.read()

    if not filename.endswith((".xlsx", ".xls", ".csv")):
        raise FileFormatException("Only .xlsx, .xls or .csv allowed")

    # Parse file
    try:
        if filename.endswith(".csv"):
            encoding = detect_encoding(content)
            df = pd.read_csv(
                BytesIO(content),
                skiprows=6,
                encoding=encoding,
                dtype=str,
                engine="python",
                on_bad_lines="skip",
            )
        else:
            df = pd.read_excel(BytesIO(content), skiprows=6, dtype=str)

        df = df.dropna(how="all")
    except Exception as e:
        raise ReportProcessingException(f"Failed to read file: {e}")

    if "Resource Request ID" not in df.columns:
        raise ValidationException("Missing required column 'Resource Request ID'")

    validated_rrs = []
    errors = []

    for idx, row in df.iterrows():
        rr_id = row.get("Resource Request ID")
        if not rr_id or pd.isna(rr_id):
            continue

        row_dict = {k: None if pd.isna(v) else v for k, v in row.to_dict().items()}
        row_dict["rr_status"] = True

        try:
            rr = ResourceRequest(**row_dict)
            validated_rrs.append(rr)
        except Exception as e:
            errors.append({"row": idx + 8, "rr_id": str(rr_id), "error": str(e)})

    # AUDIT
    await log_upload_action(
        audit_type="rr_report",
        filename=file.filename,
        file_type="CSV" if filename.endswith(".csv") else "Excel",
        uploaded_by="System",
        total_rows=len(df),
        valid_rows=len(validated_rrs),
        failed_rows=len(errors),
        sample_errors=errors[:5],
    )

    # Save in memory
    global resource_requests_in_memory
    resource_requests_in_memory.extend(validated_rrs)

    # Sync DB
    try:
        await sync_rr_with_db(validated_rrs)
    except Exception as e:
        raise DatabaseException(f"RR Sync failed: {e}")

    return {
        "message": "RR Report processed successfully!",
        "valid_requests": len(validated_rrs),
        "failed_rows": len(errors),
        "errors_sample": errors[:5],
    }


# ============================================================
# OTHER ENDPOINTS
# ============================================================
@app.get("/data/employees")
async def get_employees():
    return {"count": len(employees_in_memory), "employees": employees_in_memory[:10]}


@app.get("/data/rrs")
async def get_rrs():
    return {
        "total": len(resource_requests_in_memory),
        "sample": [
            {
                "rr_id": rr.resource_request_id,
                "role": rr.ust_role,
                "location": f"{rr.city}, {rr.country}",
                "priority": rr.priority,
                "skill_count": len(rr.mandatory_skills),
            }
            for rr in resource_requests_in_memory[:5]
        ],
    }


@app.get("/")
async def root():
    return {
        "message": "Career Velocity & RR Report Processor API",
        "audit_logging": "Enabled",
        "custom_exceptions": "Enabled",
    }
