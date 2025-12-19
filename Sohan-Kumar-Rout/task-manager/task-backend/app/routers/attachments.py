from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session
from app import models, schemas
from app.deps import get_current_user, get_db
from fastapi.responses import FileResponse
from pathlib import Path
import shutil
import time

router = APIRouter(prefix="/api/attachments", tags=["Attachments"])


@router.post("", response_model=schemas.AttachmentOut, status_code=status.HTTP_201_CREATED)
def create_attachment(att: schemas.AttachmentCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_att = models.TaskAttachment(**att.dict())
    db.add(db_att)
    db.commit()
    db.refresh(db_att)
    return db_att


@router.post("/upload/{task_id}", response_model=schemas.AttachmentOut, status_code=status.HTTP_201_CREATED)
def upload_attachment(task_id: int, file: UploadFile = File(...), db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """
    Accepts a multipart file, saves it to the local `uploads/` directory and creates a TaskAttachment record.
    Returns the created AttachmentOut model.
    """
    uploads_dir = Path("uploads")
    uploads_dir.mkdir(parents=True, exist_ok=True)

    timestamp = int(time.time())
    safe_name = f"{timestamp}_{file.filename}"
    dest = uploads_dir / safe_name

    try:
        with dest.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    finally:
        file.file.close()

    size = dest.stat().st_size
    file_url = f"/uploads/{safe_name}"

    db_att = models.TaskAttachment(
        task_id=task_id,
        file_name=file.filename,
        file_path=file_url,
        file_size=size,
        uploaded_by=int(current_user.get("emp_id")),
    )
    db.add(db_att)
    db.commit()
    db.refresh(db_att)
    return db_att


@router.get("", response_model=list[schemas.AttachmentOut])
def get_attachments(db: Session = Depends(get_db)):
    return db.query(models.TaskAttachment).all()


@router.get("/task/{task_id}", response_model=list[schemas.AttachmentOut])
def get_attachments_for_task(task_id: int, db: Session = Depends(get_db)):
    return db.query(models.TaskAttachment).filter(models.TaskAttachment.task_id == task_id).all()


@router.get("/{id}", response_model=schemas.AttachmentOut)
def get_attachment(id: int, db: Session = Depends(get_db)):
    att = db.query(models.TaskAttachment).filter(models.TaskAttachment.id == id).first()
    if not att:
        raise HTTPException(404, "Attachment not found")
    return att


@router.delete("/{id}")
def delete_attachment(id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    att = db.query(models.TaskAttachment).filter(models.TaskAttachment.id == id).first()
    if not att:
        raise HTTPException(404, "Attachment not found")

    # Remove file from disk if exists (best-effort)
    try:
        file_path = Path(".") / att.file_path.lstrip("/")
        if file_path.exists():
            file_path.unlink()
    except Exception:
        pass

    db.delete(att)
    db.commit()
    return {"message": "Attachment deleted successfully"}
