# main.py
from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
import pandas as pd
from io import BytesIO
from datetime import datetime
import re

from database import collections


# Import your models
from demo import Employee, ResourceRequest

app = FastAPI(title="Career Velocity & RR Report Processor")

# In-memory storage
employees_in_memory: List[Employee] = []
resource_requests_in_memory: List[ResourceRequest] = []


@app.post("/upload/employees")
async def upload_career_velocity(file: UploadFile = File(...)):
    """
    Upload Career Velocity Report (Excel)
    Validates using Employee Pydantic model
    """
    global employees_in_memory

    if not file.filename.endswith(('.xlsx', '.xls')):
        raise HTTPException(400, "Only Excel files allowed")

    content = await file.read()
    try:
        df = pd.read_excel(BytesIO(content))
    except Exception as e:
        raise HTTPException(400, f"Failed to read Excel: {e}")

    required_cols = ["Employee ID", "Employee Name", "Designation", "Band", "City", "Type"]
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise HTTPException(400, f"Missing required columns: {missing}")

    validated_employees = []
    errors = []

    for idx, row in df.iterrows():
        row_dict = row.to_dict()
        row_dict = {k: None if pd.isna(v) else v for k, v in row_dict.items()}  # Handle NaN

        try:
            employee = Employee(**row_dict)  # Full Pydantic validation
            validated_employees.append(employee)
        except Exception as e:
            errors.append({"row": idx + 2, "error": str(e), "data": row_dict})
    # print(len(validated_employees))

    if errors:
        return {
            "message": f"{len(validated_employees)} valid, {len(errors)} failed",
            "valid_count": len(validated_employees),
            "errors": errors[:10],  # Show first 10 errors
            "sample_valid": [e.dict(by_alias=True) for e in validated_employees[:3]]
        }

    # Update in-memory store
    records_to_check = [emp.model_dump(by_alias=True) for emp in validated_employees]
    await collections["employees"].insert_many(records_to_check, ordered=False)

    return {
        "message": f"Successfully processed {len(validated_employees)} employees",
        "total_employees": len(employees_in_memory),
        "sample": [e.dict(by_alias=True) for e in validated_employees[:3]],
        "timestamp": datetime.utcnow().isoformat()
    }


@app.post("/upload/rr-report")
async def upload_rr_report(file: UploadFile = File(...)):
    """
    Upload RR Report (Excel) - skips first 6 junk rows
    Uses full ResourceRequest model with all validators
    """
    global resource_requests_in_memory

    if not file.filename.endswith(('.xlsx', '.xls')):
        raise HTTPException(400, "Only Excel files allowed")

    content = await file.read()
    try:
        # Skip first 6 rows of junk header
        df = pd.read_excel(BytesIO(content), skiprows=6)
    except Exception as e:
        raise HTTPException(400, f"Failed to read Excel: {e}")

    # Check if we have the main header row
    if "Resource Request ID" not in df.columns:
        raise HTTPException(400, "Invalid RR Report format - missing 'Resource Request ID' column")

    validated_rrs = []
    errors = []
    seen_rr_ids = set()

    for idx, row in df.iterrows():
        if pd.isna(row.get("Resource Request ID")):
            continue  # Skip empty rows

        row_dict = row.to_dict()
        row_dict = {k: None if pd.isna(v) else v for k, v in row_dict.items()}

        rr_id = str(row_dict.get("Resource Request ID", "")).strip()
        if rr_id in seen_rr_ids:
            errors.append({"row": idx + 8, "error": "Duplicate RR ID", "rr_id": rr_id})
            continue
        seen_rr_ids.add(rr_id)

        try:
            rr = ResourceRequest(**row_dict)  # Full validation magic happens here
            validated_rrs.append(rr)
        except Exception as e:
            errors.append({"row": idx + 8, "error": str(e), "rr_id": rr_id})

    # Update in-memory
    resource_requests_in_memory = validated_rrs
    


    return {
        "message": f"RR Report processed",
        "valid_requests": len(validated_rrs),
        "failed_rows": len(errors),
        "total_in_memory": len(resource_requests_in_memory),
        "errors_sample": errors[:10] if errors else None,
        "sample_valid": [
            {
                "resource_request_id": rr.resource_request_id,
                "title": rr.ust_role,
                "location": f"{rr.city}, {rr.country}",
                "mandatory_skills": rr.mandatory_skills,
                "status": rr.rr_status
            }
            for rr in validated_rrs[:3]
        ],
        "timestamp": datetime.utcnow().isoformat()
    }


# Optional: View current in-memory data
@app.get("/data/employees")
async def get_employees():
    return {
        "count": len(employees_in_memory),
        "employees": [e.dict() for e in employees_in_memory[:10]]
    }


@app.get("/data/rrs")
async def get_rrs():
    return {
        "count": len(resource_requests_in_memory),
        "requests": [
            {
                "rr_id": rr.resource_request_id,
                "role": rr.ust_role,
                "location": rr.city,
                "skills": rr.mandatory_skills,
                "status": rr.rr_status
            }
            for rr in resource_requests_in_memory[:10]
        ]
    }


@app.get("/")
async def root():
    return {
        "message": "Career Velocity & RR Report Processor API",
        "endpoints": {
            "POST /upload/employees": "Upload Career Velocity Report",
            "POST /upload/rr-report": "Upload RR Report",
            "GET /data/employees": "View loaded employees",
            "GET /data/rrs": "View loaded RRs"
        },
        "total_employees": len(employees_in_memory),
        "total_rrs": len(resource_requests_in_memory)
    }