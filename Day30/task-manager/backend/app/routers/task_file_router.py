"""from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
import io

from app.database.connection import get_db
from app.schemas.task_file import TaskFileResponse
from app.services.task_file_service import upload_task_file, get_task_file
from app.utils.auth_dependency import get_current_user

router = APIRouter(
    prefix="/api/tasks",
    tags=["Task Files"]
)


# -----------------------------
# UPLOAD FILE TO TASK
# -----------------------------
@router.post("/{task_id}/files", response_model=TaskFileResponse)
def upload_file(
    task_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return upload_task_file(db, task_id, file)


@router.get("/files/{file_id}")
def download_file(
    file_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    file = get_task_file(db, file_id)

    # ---- Decide rendering behavior ----
    inline_types = [
        "image/png",
        "image/jpeg",
        "image/jpg",
        "application/pdf"
    ]

    disposition = "inline" if file.content_type in inline_types else "attachment"

    return StreamingResponse(
        io.BytesIO(file.file_data),
        media_type=file.content_type,
        headers={
            "Content-Disposition": f"{disposition}; filename={file.filename}"
        }
    )
"""

from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
import io
from app.database.connection import get_db
from app.schemas.task_file import TaskFileResponse
from app.services.task_file_service import upload_task_file, get_task_file
from app.utils.auth import get_current_user

router = APIRouter(prefix="/api/tasks", tags=["Task Files"])

@router.post("/{task_id}/files", response_model=TaskFileResponse)
def upload_file(task_id: int, file: UploadFile = File(...), db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return upload_task_file(db, task_id, file)

@router.get("/files/{file_id}")
def download_file(file_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    file = get_task_file(db, file_id)
    # ---- Decide rendering behavior ----
    inline_types = [
        "image/png",
        "image/jpeg",
        "image/jpg",
        "application/pdf"
    ]
    disposition = "inline" if file.content_type in inline_types else "attachment"
    return StreamingResponse(
        io.BytesIO(file.file_data),
        media_type=file.content_type,
        headers={
            "Content-Disposition": f"{disposition}; filename={file.filename}"
        }
    )