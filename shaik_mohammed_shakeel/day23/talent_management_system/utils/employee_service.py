# ...existing code...
import os
from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, status
import base64
from database import employees, resource_request, fs,applications
import tempfile
import docx2txt
import fitz  # PyMuPDF
from pdfminer.high_level import extract_text as extract_pdf
 
# -----------------------------------------
# Import necessary components
from typing import List, Dict, Any
from motor.motor_asyncio import AsyncIOMotorCursor
resource_request_col=resource_request 
app_col = applications
emp_col = employees
# Your existing _serialize function (no changes needed)
def _serialize(doc: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if not doc:
        return {}
    out = dict(doc)
 
    # Convert ObjectId → string
    if "_id" in out:
        out["id"] = str(out.pop("_id"))
 
    return out
 
#---------------------- FETCH ALL EMPLOYEES ----------------------
async def fetch_all_employees() -> List[Dict[str, Any]]:
    col = emp_col
 
    query = {}
 
    try:
        # Use 'await' to get the cursor and then convert it to a list
        cursor = col.find(query)
        results = await cursor.to_list(length=None)  # Await the cursor to list
    except Exception as e:
        raise RuntimeError(f"Failed to query collection employees: {e}")
 
    # Serialize the results
    return [_serialize(d) for d in results]
 
 
# Fetch employee by ID
async def fetch_employee_by_id(emp_id: int) -> Optional[Dict[str, Any]]:
    col = emp_col
    doc = await col.find_one({"employee_id": emp_id})   # <-- FIXED
    if not doc:
        return None
    doc["id"] = str(doc["_id"])  # <-- you used employee_id before, correct is _id
    del doc["_id"]
    return doc
 
# Get jobs by Hiring Manager
async def get_jobs_by_hm(hm_id: str) -> List[Dict[str, Any]]:
    col = resource_request_col
    cursor = col.find({"hm_id": hm_id})
    jobs_list = await cursor.to_list(length=None)
    return [_serialize(doc) for doc in jobs_list]
 
# Get TP employees
async def get_tp_employees() -> List[Dict[str, Any]]:
    col = emp_col
    cursor = col.find({"type": "TP"})
    tp_employees = await cursor.to_list(length=None)
    return [_serialize(doc) for doc in tp_employees]
 
# Update parsed resume
async def update_parsed_resume(emp_id: int, parsed_text: str):
    col = emp_col
    result = await col.update_one(
        {"employee_id": emp_id},
        {"$set": {"ExtractedText": parsed_text}}
    )
    return result.modified_count > 0
 
# Save to GridFS
def save_to_gridfs(filename: str, file_bytes: bytes) -> str:
    file_id = fs.put(file_bytes, filename=filename)
    return str(file_id)
 
# Extract text from PDF
def extract_text_from_pdf(file_bytes: bytes) -> str:
    text = ""
    pdf = fitz.open("pdf", file_bytes)
    for page in pdf:
        text += page.get_text()
    return text
 
# Decode base64 to file
def decode_base64_to_file(base64_data: str, filename: str) -> str:
    path = os.path.join(tempfile.gettempdir(), filename)
    with open(path, "wb") as f:
        f.write(base64.b64decode(base64_data))
    return path
 
# Extract text from binary (PDF or DOCX)
def extract_text_from_binary(base64_data: str, filename: str) -> str:
    ext = filename.split(".")[-1].lower()
    temp_path = decode_base64_to_file(base64_data, filename)
    if ext == "pdf":
        return extract_pdf(temp_path)
    return docx2txt.process(temp_path)
 