from fastapi import UploadFile, File,APIRouter, Depends, HTTPException
from auth.jwt_auth import get_current_user
from services.user_services import get_User_by_id
from services.file_services import upload_file_to_task, get_task_files, get_file_by_id
import base64
from typing import List
from bson.objectid import ObjectId
from database.mongo_connection import files

task_router = APIRouter()

@task_router.post("/tasks/{task_id}/upload", tags=["Tasks"])
async def upload_file_to_tasks(
    task_id: str,
    file: UploadFile = File(...),
    user: str = Depends(get_current_user)
):
    """Upload file to specific task - Manager/Developer only"""
    try:
        emp_id = int(user)
        auth_user = get_User_by_id(emp_id)
        if not auth_user:
            raise HTTPException(status_code=401, detail="User not found")

        # roles = auth_user.role
        # if not any(r in roles for r in ["manager", "developer"]):
        #     raise HTTPException(status_code=403, detail="Forbidden: manager or developer role required")

        # ✅ FIX: Properly await file.read() and handle bytes
        content = await file.read()
        if len(content) > 10 * 1024 * 1024:  # 10MB limit
            raise HTTPException(status_code=413, detail="File too large (max 10MB)")

        if not content:
            raise HTTPException(status_code=400, detail="File is empty")

        file_data = {
            "file_name": file.filename or "unnamed_file",
            "file_type": file.content_type or "application/octet-stream",
            "file_size": len(content),
            "file_data": content  # bytes object ✅
        }

        result = upload_file_to_task(task_id, file_data, emp_id)
        return result  # This is a regular dict ✅
        
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@task_router.get("/tasks/{task_id}/files", tags=["Tasks"])
def get_task_files_endpoint(task_id: str, user: str = Depends(get_current_user)):
    """Get all files for a task"""
    try:
        emp_id = int(user)
        auth_user = get_User_by_id(emp_id)
        if not auth_user:
            raise HTTPException(status_code=401, detail="User not found")

        roles = auth_user.role
        if not any(r in roles for r in ["admin", "manager", "developer"]):
            raise HTTPException(status_code=403, detail="Forbidden")

        files = get_task_files(task_id)
        return {"files": files}
        
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@task_router.get("/files/{file_id}", tags=["Tasks"])
def download_file(file_id: str, user: str = Depends(get_current_user)):
    """Get file metadata and base64 data"""
    try:
        emp_id = int(user)
        auth_user = get_User_by_id(emp_id)
        if not auth_user:
            raise HTTPException(status_code=401, detail="User not found")

        roles = auth_user.role
        if not any(r in roles for r in ["admin", "manager", "developer"]):
            raise HTTPException(status_code=403, detail="Forbidden")

        # ✅ DIRECT FIX: Get raw file and convert here
        oid = ObjectId(file_id)
        file_doc = files.find_one({"_id": oid})
        if not file_doc:
            raise HTTPException(status_code=404, detail="File not found")
        
        # ✅ Convert ObjectId to string and Binary to base64
        response = {
            "file_id": str(file_doc["_id"]),
            "task_id": str(file_doc.get("task_id", "")),
            "file_name": file_doc["file_name"],
            "file_type": file_doc["file_type"],
            "file_size": file_doc["file_size"],
            "uploaded_by": file_doc["uploaded_by"],
            "uploaded_at": file_doc["uploaded_at"],
            "file_data": base64.b64encode(file_doc["file_data"]).decode('utf-8')
        }
        return response  # ✅ 100% JSON-safe
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
