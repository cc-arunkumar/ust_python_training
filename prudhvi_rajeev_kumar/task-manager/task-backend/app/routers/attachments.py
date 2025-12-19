from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app import models, schemas
from app.deps import get_current_user, get_db
from pathlib import Path
import shutil
import time

router = APIRouter(prefix="/api/attachments", tags=["Attachments"])

UPLOAD_DIR = Path(__file__).resolve().parent.parent.parent / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("", response_model=schemas.AttachmentOut, status_code=status.HTTP_201_CREATED)
def create_attachment(att: schemas.AttachmentCreate, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    """Create attachment metadata only (used for non-file scenarios)."""
    db_att = models.TaskAttachment(**att.dict())
    db.add(db_att)
    db.commit()
    db.refresh(db_att)
    return db_att


@router.post("/upload", response_model=schemas.AttachmentOut, status_code=status.HTTP_201_CREATED)
def upload_attachment(task_id: int = Form(...), uploaded_by: int = Form(...), file: UploadFile = File(...), current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    """Accept multipart file upload, save file to disk and create metadata record.
    Returns the created attachment metadata.
    """
    # sanitize and create a unique filename
    timestamp = int(time.time() * 1000)
    safe_name = f"{timestamp}_{Path(file.filename).name}"
    dest = UPLOAD_DIR / safe_name
    try:
        with dest.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    finally:
        file.file.close()

    # store metadata with a path that frontend can use to download from the backend
    file_path = f"/uploads/{safe_name}"
    db_att = models.TaskAttachment(task_id=task_id, file_name=file.filename, file_path=file_path, file_size=dest.stat().st_size, uploaded_by=uploaded_by)
    db.add(db_att)
    db.commit()
    db.refresh(db_att)
    return db_att


@router.get("", response_model=list[schemas.AttachmentOut])
def get_attachments(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(models.TaskAttachment).all()


@router.get("/{id}", response_model=schemas.AttachmentOut)
def get_attachment(id: int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    att = db.query(models.TaskAttachment).filter(models.TaskAttachment.id == id).first()
    if not att:
        raise HTTPException(404, "Attachment not found")
    return att


@router.get("/{id}/download")
def download_attachment(id: int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    att = db.query(models.TaskAttachment).filter(models.TaskAttachment.id == id).first()
    if not att:
        raise HTTPException(404, "Attachment not found")
    # resolve filesystem path
    fs_path = Path(__file__).resolve().parent.parent.parent / att.file_path.lstrip('/')
    if not fs_path.exists():
        raise HTTPException(404, "File not found on server")
    return FileResponse(path=str(fs_path), filename=att.file_name, media_type='application/octet-stream')


@router.delete("/{id}")
def delete_attachment(id: int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    att = db.query(models.TaskAttachment).filter(models.TaskAttachment.id == id).first()
    if not att:
        raise HTTPException(404, "Attachment not found")

    # delete file from disk if exists
    try:
        fs_path = Path(__file__).resolve().parent.parent.parent / att.file_path.lstrip('/')
        if fs_path.exists():
            fs_path.unlink()
    except Exception:
        # ignore filesystem errors but proceed to remove metadata
        pass

    db.delete(att)
    db.commit()
    return {"message": "Attachment deleted successfully"}
