# main.py → FINAL VERSION – NO MORE ENCODING ERRORS
from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
import pandas as pd
from io import BytesIO
from datetime import datetime
import chardet  # pip install chardet
from model import ResourceRequest

from database import collections

app = FastAPI(title="RR Report Processor – Excel & CSV (Any Encoding)")

resource_requests_in_memory: List[ResourceRequest] = []


def detect_encoding(byte_data: bytes) -> str:
    """Detect file encoding using chardet"""
    detection = chardet.detect(byte_data)
    encoding = detection['encoding'] or 'utf-8'
    confidence = detection['confidence']
    if confidence < 0.7:
        # Fallback chain for common Excel/CSV exports
        for enc in ['utf-8', 'cp1252', 'latin1', 'iso-8859-1']:
            try:
                byte_data.decode(enc)
                return enc
            except:
                continue
        return 'utf-8'
    return encoding


@app.post("/upload/rr-report")
async def upload_rr_report(file: UploadFile = File(...)):
    filename = file.filename.lower()
    content = await file.read()

    if not filename.endswith(('.xlsx', '.xls', '.csv')):
        raise HTTPException(400, "Only .xlsx, .xls, or .csv files allowed")

    try:
        if filename.endswith('.csv'):
            # Detect encoding automatically
            encoding = detect_encoding(content)
            df = pd.read_csv(
                BytesIO(content),
                skiprows=6,
                encoding=encoding,
                dtype=str,           # Prevent type guessing
                engine='python',     # More forgiving
                on_bad_lines='skip'  # Skip malformed lines
            )
        else:
            # Excel files are always safe
            df = pd.read_excel(BytesIO(content), skiprows=6, dtype=str)

        df = df.dropna(how='all')  # Remove completely blank rows

    except Exception as e:
        raise HTTPException(400, f"Failed to read file: {str(e)}")

    if "Resource Request ID" not in df.columns:
        raise HTTPException(400, "Invalid RR Report – missing 'Resource Request ID' column")

    validated_rrs = []
    errors = []

    for idx, row in df.iterrows():
        rr_id = row.get("Resource Request ID")
        if pd.isna(rr_id) or str(rr_id).strip() == "":
            continue

        row_dict = {k: None if pd.isna(v) else str(v) for k, v in row.to_dict().items()}

        try:
            rr = ResourceRequest(**row_dict)
            validated_rrs.append(rr)
        except Exception as e:
            errors.append({
                "row": idx + 8,
                "rr_id": str(rr_id),
                "error": str(e)[:200]  # Truncate long errors
            })

    global resource_requests_in_memory
    resource_requests_in_memory = validated_rrs

    return {
        "message": "RR Report processed successfully!",
        "file_type": "CSV" if filename.endswith('.csv') else "Excel",
        "detected_encoding": encoding if filename.endswith('.csv') else "N/A (Excel)",
        "valid_requests": len(validated_rrs),
        "failed_rows": len(errors),
        "total_loaded": len(resource_requests_in_memory),
        "errors_sample": errors[:5] if errors else None,
        "sample": [
            {
                "rr_id": rr.resource_request_id,
                "role": rr.ust_role,
                "city": rr.city,
                "priority": rr.priority,
                "skills": rr.mandatory_skills[:6]
            }
            for rr in validated_rrs[:3]
        ],
        "timestamp": datetime.utcnow().isoformat()
    }


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
                "skill_count": len(rr.mandatory_skills)
            }
            for rr in resource_requests_in_memory[:5]
        ]
    }


@app.get("/")
async def root():
    return {
        "message": "RR Report API – Fully Ready!",
        "supported_formats": [".xlsx", ".xls", ".csv (any encoding)"],
        "total_rrs_loaded": len(resource_requests_in_memory),
        "endpoints": {
            "POST /upload/rr-report": "Upload RR Report",
            "GET /data/rrs": "View loaded RRs"
        }
    }