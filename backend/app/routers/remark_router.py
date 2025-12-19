from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, Form
from typing import List, Optional
from app.models.models import RemarkReqRes
from app.core.security import get_current_user
from app.crud.remark_crud import add_remark, get_remarks_by_task, delete_remark_by_id, update_remark
from app.crud.remark_crud import get_all_remarks_for_user
from app.database.mongodb_connection import fs
from fastapi.responses import StreamingResponse
from bson import ObjectId
from app.crud.users_crud import normalize_role_param

remark_router = APIRouter(prefix="/Remark", tags=["Remark"])


@remark_router.get("/getbytask", response_model=List[RemarkReqRes])
def list_for_task(task_id: int, role: str, user=Depends(get_current_user)):
    role_clean = normalize_role_param(role)
    if not role_clean or role_clean not in user.role:
        raise HTTPException(status_code=400,detail="you dont have the access of mentioned role")
        
    remarks = get_remarks_by_task(task_id)
    if not remarks:
        raise HTTPException(status_code=404, detail="No remarks found for task")
    return remarks


@remark_router.post("/create")
def create_remark(
    task_id: int = Form(...),
    comment: str = Form(...),
    file: Optional[UploadFile] = File(None),
    role: str = Form(...),
    user=Depends(get_current_user),
):
    role_clean = normalize_role_param(role)
    if not role_clean or role_clean not in user.role:
        raise HTTPException(status_code=400,detail="you dont have the access of mentioned role")

    r = add_remark(task_id=task_id, comment=comment, e_id=getattr(user, "e_id", None), file=file, role=role_clean, user=user)
    return {"detail": "Remark Added Successfully", "remark": r}


@remark_router.put("/update")
def update_remark_api(
    remark_id: str = Form(...),
    comment: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None),
    role: str = Form(...),
    user=Depends(get_current_user),
):
     
    role_clean = normalize_role_param(role)
    updated = update_remark(remark_id=remark_id, comment=comment, file=file, e_id=getattr(user, "e_id", None), role=role_clean)
    return {"detail": "Remark Updated Successfully", "remark": updated}


@remark_router.delete("/delete")
def delete_remark_by_id_api(id: str, role: str, user=Depends(get_current_user)):
    role_clean = normalize_role_param(role)
    if not role_clean or role_clean not in user.role:
        raise HTTPException(status_code=400,detail="you dont have the access of mentioned role")

    resp = delete_remark_by_id(id, role_clean, user)
    return resp




@remark_router.get("/file")
def get_remark_file(file_id: str, user=Depends(get_current_user)):
    """Stream a file stored in GridFS by its id. Requires auth (token).

    Returns the file with correct Content-Type so browsers can preview images inline.
    """
    try:
        grid_out = fs.get(ObjectId(file_id))
    except Exception:
        raise HTTPException(status_code=404, detail="File not found")

    return StreamingResponse(grid_out, media_type=grid_out.content_type, headers={"Content-Disposition": f'inline; filename="{grid_out.filename}"'})



@remark_router.get("/list")
def list_all_remarks(user=Depends(get_current_user)):
    """List remarks visible to the requesting user.

    Admins and Managers see all remarks. Developers see remarks they created and remarks on tasks assigned to them.
    """
    remarks = get_all_remarks_for_user(user)
    return remarks