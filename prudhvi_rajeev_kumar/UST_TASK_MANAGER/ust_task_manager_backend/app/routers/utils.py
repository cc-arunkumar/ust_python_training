import os
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from app.core.config import settings
from app.core.dependencies import get_current_user, AuthUser

router = APIRouter(prefix="/api/utils", tags=["utils"])

@router.post("/upload")
def upload_file(file: UploadFile = File(...), user: AuthUser = Depends(get_current_user)):
    os.makedirs(settings.file_upload_dir, exist_ok=True)
    ext = os.path.splitext(file.filename)[1]
    name = f"{uuid.uuid4().hex}{ext}"
    path = os.path.join(settings.file_upload_dir, name)
    try:
        with open(path, "wb") as f:
            f.write(file.file.read())
    except Exception:
        raise HTTPException(status_code=500, detail="File upload failed")
    return {"filename": name, "path": path}
