from fastapi import APIRouter, HTTPException, UploadFile, File
from utils.llm_services import parse_resume_with_llm
from utils.employee_services import extract_text_from_pdf, save_to_gridfs, extract_text_from_binary, fetch_employee_by_id, update_parsed_resume
from database import employees
from bson import ObjectId
import base64

resume_router = APIRouter(prefix="/resume")


def clean_text(text: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)


@resume_router.put("/upload/{employee_id}")
async def upload_resume(employee_id: int, file: UploadFile = File(...)):
    emp_col = employees()

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    file_bytes = await file.read()
    if not file_bytes:
        raise HTTPException(status_code=400, detail="Uploaded file is empty")

    try:
        file_id = save_to_gridfs(file.filename, file_bytes)  # Save file to GridFS
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving file: {str(e)}")

    try:
        raw_text = extract_text_from_pdf(file_bytes)
        extracted_text = clean_text(raw_text)  # Clean the extracted text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error extracting text: {str(e)}")

    # Await the update operation to get the result
    try:
        update_result = await emp_col.update_one(
            {"Employee ID": employee_id},
            {
                "$set": {
                    "Resume": file.filename,
                    "Resume_Extension": file.filename.split(".")[-1],
                    "Resume_File_ID": str(file_id),
                    "Resume_text": extracted_text
                }
            }
        )

        if update_result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Employee ID not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating employee data: {str(e)}")

    return {
        "message": "Resume uploaded successfully",
        "filename": file.filename,
        "text_preview": extracted_text[:200]
    }
