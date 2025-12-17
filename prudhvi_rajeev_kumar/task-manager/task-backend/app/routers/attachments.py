from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.deps import get_current_user

router = APIRouter(prefix="/api/attachments", tags=["Attachments"])


@router.post("", response_model=schemas.AttachmentOut, status_code=status.HTTP_201_CREATED)
def create_attachment(att: schemas.AttachmentCreate, db: Session = Depends(get_current_user)):
    db_att = models.TaskAttachment(**att.dict())
    db.add(db_att)
    db.commit()
    db.refresh(db_att)
    return db_att


@router.get("", response_model=list[schemas.AttachmentOut])
def get_attachments(db: Session = Depends(get_current_user)):
    return db.query(models.TaskAttachment).all()


@router.get("/{id}", response_model=schemas.AttachmentOut)
def get_attachment(id: int, db: Session = Depends(get_current_user)):
    att = db.query(models.TaskAttachment).filter(models.TaskAttachment.id == id).first()
    if not att:
        raise HTTPException(404, "Attachment not found")
    return att


@router.delete("/{id}")
def delete_attachment(id: int, db: Session = Depends(get_current_user)):
    att = db.query(models.TaskAttachment).filter(models.TaskAttachment.id == id).first()
    if not att:
        raise HTTPException(404, "Attachment not found")
    
    db.delete(att)
    db.commit()
    return {"message": "Attachment deleted successfully"}
